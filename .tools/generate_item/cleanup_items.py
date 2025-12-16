#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import datetime
import re
import sys

# =========================
# 設定
# =========================
KEEP_DAYS = 18  # ← 本番は 90 に戻す
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]

ITEMS_DIR = REPO_ROOT / "items"
MEDIA_DIR = REPO_ROOT / "media"

# p1-20251205-0001
# p3-20251210-0001-1   ← 末尾 -1/-2/-3 あり
ID_DATE_RE = re.compile(r"^p\d-(\d{8})-\d{4}(?:-\d+)?$")

# Part3/4 の audio 共有: p3-...-0001-1 → p3-...-0001
TRAILING_QIDX_RE = re.compile(r"-(\d+)$")

IMAGE_EXTS = ("jpg", "jpeg", "webp", "png")
AUDIO_EXTS = ("mp3", "wav", "pcm")


def extract_date_from_id(item_id: str) -> datetime.date | None:
    m = ID_DATE_RE.match(item_id)
    if not m:
        return None
    return datetime.datetime.strptime(m.group(1), "%Y%m%d").date()


def base_audio_id(item_id: str) -> str:
    # p3-YYYYMMDD-0001-1 -> p3-YYYYMMDD-0001
    # p1/p2 は変化なし
    return TRAILING_QIDX_RE.sub("", item_id)


def safe_rmdir_upwards(start_dir: pathlib.Path, stop_dir: pathlib.Path, max_levels: int = 3):
    """
    start_dir から上方向に、空ディレクトリなら削除する。
    stop_dir より上には行かない。
    """
    cur = start_dir
    for _ in range(max_levels):
        if cur == stop_dir or not cur.exists():
            return
        try:
            # 空なら消す
            cur.rmdir()
        except OSError:
            return  # 空じゃない/消せないなら終了
        cur = cur.parent


def main():
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=KEEP_DAYS)

    print(f"[INFO] REPO_ROOT: {REPO_ROOT}")
    print(f"[INFO] Cleanup cutoff date: {cutoff}  (keep last {KEEP_DAYS} days)")

    if not ITEMS_DIR.exists():
        print(f"[ERR] items dir not found: {ITEMS_DIR}", file=sys.stderr)
        sys.exit(1)

    deleted_json = 0
    deleted_html = 0
    deleted_media = 0
    skipped = 0

    for json_path in ITEMS_DIR.rglob("*.json"):
        try:
            item_id = json_path.stem

            item_date = extract_date_from_id(item_id)
            if not item_date:
                skipped += 1
                continue

            # keep
            if item_date >= cutoff:
                continue

            # ---- delete JSON ----
            print(f"[DELETE] {item_id} :: {json_path}")
            json_path.unlink(missing_ok=True)
            deleted_json += 1

            # ---- delete HTML (same name) ----
            html_path = json_path.with_suffix(".html")
            if html_path.exists():
                html_path.unlink()
                deleted_html += 1

            # ---- delete related media ----
            # items/partX/YYYY/MM/<id>.json から part を取り出す（"part1" 等）
            try:
                part = json_path.parts[json_path.parts.index("items") + 1]  # part1/part2/...
            except Exception:
                part = None

            yyyy = item_date.strftime("%Y")
            mm = item_date.strftime("%m")

            # audio
            # media/audio/partX/YYYY/MM/
            if part:
                audio_dir = MEDIA_DIR / "audio" / part / yyyy / mm
                if audio_dir.exists():
                    # item_id と base_audio_id の両方を消す（Part3/4 対策）
                    cand_ids = {item_id, base_audio_id(item_id)}
                    for cid in cand_ids:
                        for ext in AUDIO_EXTS:
                            p = audio_dir / f"{cid}.{ext}"
                            if p.exists():
                                p.unlink()
                                deleted_media += 1
                    # 空ディレクトリ掃除（mm → yyyy → part）
                    safe_rmdir_upwards(audio_dir, MEDIA_DIR / "audio", max_levels=3)

                # image
                # media/images/partX/YYYY/MM/
                image_dir = MEDIA_DIR / "images" / part / yyyy / mm
                if image_dir.exists():
                    for ext in IMAGE_EXTS:
                        img = image_dir / f"{item_id}.{ext}"
                        if img.exists():
                            img.unlink()
                            deleted_media += 1
                    safe_rmdir_upwards(image_dir, MEDIA_DIR / "images", max_levels=3)

            # items 側の空ディレクトリ掃除（mm → yyyy → part）
            safe_rmdir_upwards(json_path.parent, ITEMS_DIR, max_levels=3)

        except Exception as e:
            print(f"[WARN] Failed to process {json_path}: {e}", file=sys.stderr)

    print("[OK] Cleanup done.")
    print(f"  deleted_json : {deleted_json}")
    print(f"  deleted_html : {deleted_html}")
    print(f"  deleted_media: {deleted_media}")
    print(f"  skipped      : {skipped}  (id/date parse did not match)")

if __name__ == "__main__":
    main()

