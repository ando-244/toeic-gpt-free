#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import datetime
import re
import sys

# =========================
# 設定
# =========================
KEEP_DAYS = 0  # 本番は 90 に変更
IMAGE_EXTS = ("jpg", "jpeg", "webp", "png")
AUDIO_EXTS = ("mp3", "wav", "pcm")

# p1-20251205-0001
# p3-20251210-0001-1 も許可
ID_DATE_RE = re.compile(r"^p\d-(\d{8})-\d{4}(?:-\d+)?$")
TRAILING_QIDX_RE = re.compile(r"-(\d+)$")


# =========================
# Repo root 検出（壊れにくい）
# =========================
def find_repo_root(start: pathlib.Path) -> pathlib.Path:
    cur = start
    for _ in range(8):
        if (cur / "items").exists() and (cur / "media").exists():
            return cur
        cur = cur.parent
    raise RuntimeError("Repo root not found (items/media not found)")


REPO_ROOT = find_repo_root(pathlib.Path(__file__).resolve())
ITEMS_DIR = REPO_ROOT / "items"
MEDIA_DIR = REPO_ROOT / "media"


# =========================
# Utility
# =========================
def extract_date_from_id(item_id: str) -> datetime.date | None:
    m = ID_DATE_RE.match(item_id)
    if not m:
        return None
    return datetime.datetime.strptime(m.group(1), "%Y%m%d").date()


def base_audio_id(item_id: str) -> str:
    # p3-YYYYMMDD-0001-1 -> p3-YYYYMMDD-0001
    return TRAILING_QIDX_RE.sub("", item_id)


def safe_rmdir_upwards(start: pathlib.Path, stop: pathlib.Path, max_levels: int = 6):
    """
    start から上方向に「空ディレクトリなら削除」を繰り返す。
    stop まで到達したら止まる（stop 自体は削除しない）。
    """
    cur = start
    for _ in range(max_levels):
        if not cur.exists():
            return
        if cur == stop:
            return
        try:
            cur.rmdir()
        except OSError:
            return
        cur = cur.parent


def is_expired(d: datetime.date, cutoff: datetime.date) -> bool:
    return d < cutoff


def part_dir_from_items_path(p: pathlib.Path) -> pathlib.Path | None:
    """
    items/partX/YYYY/MM/<file> から items/partX を返す
    """
    try:
        idx = p.parts.index("items")
        return pathlib.Path(*p.parts[: idx + 2])  # .../items/partX
    except Exception:
        return None


# =========================
# Cleanup logic
# =========================
def cleanup_by_json(cutoff: datetime.date):
    deleted = {"json": 0, "html": 0, "media": 0, "skipped": 0}

    for json_path in ITEMS_DIR.rglob("*.json"):
        item_id = json_path.stem
        item_date = extract_date_from_id(item_id)
        if not item_date:
            deleted["skipped"] += 1
            continue
        if not is_expired(item_date, cutoff):
            continue

        print(f"[DELETE json] {json_path}")
        json_path.unlink(missing_ok=True)
        deleted["json"] += 1

        # ---- delete HTML (same name) ----
        html_path = json_path.with_suffix(".html")
        if html_path.exists():
            html_path.unlink()
            deleted["html"] += 1

        # ---- delete related media ----
        try:
            part = json_path.parts[json_path.parts.index("items") + 1]  # part1/part2/...
        except Exception:
            part = None

        yyyy = item_date.strftime("%Y")
        mm = item_date.strftime("%m")

        if part:
            # audio: media/audio/partX/YYYY/MM/
            audio_dir = MEDIA_DIR / "audio" / part / yyyy / mm
            audio_part_dir = MEDIA_DIR / "audio" / part  # ← partX は残すため stop をここにする
            if audio_dir.exists():
                for cid in {item_id, base_audio_id(item_id)}:
                    for ext in AUDIO_EXTS:
                        fp = audio_dir / f"{cid}.{ext}"
                        if fp.exists():
                            fp.unlink()
                            deleted["media"] += 1
                # mm → yyyy までは消してOK、partX は残す
                safe_rmdir_upwards(audio_dir, audio_part_dir)

            # image: media/images/partX/YYYY/MM/
            image_dir = MEDIA_DIR / "images" / part / yyyy / mm
            image_part_dir = MEDIA_DIR / "images" / part  # ← partX は残す
            if image_dir.exists():
                for ext in IMAGE_EXTS:
                    fp = image_dir / f"{item_id}.{ext}"
                    if fp.exists():
                        fp.unlink()
                        deleted["media"] += 1
                safe_rmdir_upwards(image_dir, image_part_dir)

        # ---- items 側の空ディレクトリ掃除（partX は残す）----
        part_dir = part_dir_from_items_path(json_path)
        if part_dir:
            safe_rmdir_upwards(json_path.parent, part_dir)

    return deleted


def cleanup_orphan_html(cutoff: datetime.date):
    deleted = 0
    for html_path in ITEMS_DIR.rglob("*.html"):
        json_path = html_path.with_suffix(".json")
        if json_path.exists():
            continue  # 孤児じゃない

        item_id = html_path.stem
        item_date = extract_date_from_id(item_id)
        if not item_date or not is_expired(item_date, cutoff):
            continue

        print(f"[DELETE orphan html] {html_path}")
        html_path.unlink(missing_ok=True)
        deleted += 1

        part_dir = part_dir_from_items_path(html_path)
        if part_dir:
            safe_rmdir_upwards(html_path.parent, part_dir)

    return deleted


def cleanup_orphan_audio(cutoff: datetime.date):
    deleted = 0
    audio_root = MEDIA_DIR / "audio"
    if not audio_root.exists():
        return 0

    for mp3_path in audio_root.rglob("*.mp3"):
        stem = mp3_path.stem  # p2-20251127-0001 など

        # items 側に該当 json が残っていたら孤児ではない
        if list(ITEMS_DIR.rglob(f"{stem}*.json")):
            continue

        d = extract_date_from_id(stem)
        if not d or not is_expired(d, cutoff):
            continue

        print(f"[DELETE orphan audio] {mp3_path}")
        mp3_path.unlink(missing_ok=True)
        deleted += 1

        # partX を残すため stop を media/audio/partX にする
        # mp3_path: media/audio/partX/YYYY/MM/file.mp3
        try:
            part = mp3_path.parts[mp3_path.parts.index("audio") + 1]
            audio_part_dir = MEDIA_DIR / "audio" / part
            safe_rmdir_upwards(mp3_path.parent, audio_part_dir)
        except Exception:
            pass

    return deleted


def cleanup_orphan_images(cutoff: datetime.date):
    deleted = 0
    image_root = MEDIA_DIR / "images"
    if not image_root.exists():
        return 0

    for img_path in image_root.rglob("*"):
        if not img_path.is_file():
            continue
        if img_path.suffix.lower().lstrip(".") not in IMAGE_EXTS:
            continue

        stem = img_path.stem  # p1-20251127-0001 など

        # 対応する json があれば孤児ではない
        if list(ITEMS_DIR.rglob(f"{stem}.json")):
            continue

        item_date = extract_date_from_id(stem)
        if not item_date or not is_expired(item_date, cutoff):
            continue

        print(f"[DELETE orphan image] {img_path}")
        img_path.unlink(missing_ok=True)
        deleted += 1

        # partX を残すため stop を media/images/partX にする
        try:
            part = img_path.parts[img_path.parts.index("images") + 1]
            image_part_dir = MEDIA_DIR / "images" / part
            safe_rmdir_upwards(img_path.parent, image_part_dir)
        except Exception:
            pass

    return deleted


# =========================
# Main
# =========================
def main():
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=KEEP_DAYS)

    print(f"[INFO] Repo root : {REPO_ROOT}")
    print(f"[INFO] Cutoff    : {cutoff} (keep {KEEP_DAYS} days)")

    if not ITEMS_DIR.exists():
        print(f"[ERR] items dir not found: {ITEMS_DIR}", file=sys.stderr)
        sys.exit(1)

    r1 = cleanup_by_json(cutoff)
    r2_html = cleanup_orphan_html(cutoff)
    r2_audio = cleanup_orphan_audio(cutoff)
    r2_image = cleanup_orphan_images(cutoff)

    print("[OK] Cleanup finished")
    print(f"  json deleted   : {r1['json']}")
    print(f"  html deleted   : {r1['html']} (+ orphan {r2_html})")
    print(f"  media deleted  : {r1['media']} (+ orphan audio {r2_audio}, orphan image {r2_image})")
    print(f"  skipped (id parse miss): {r1['skipped']}")


if __name__ == "__main__":
    main()
