#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import datetime
import re
import sys

# =========================
# 設定
# =========================
KEEP_DAYS = 0   # ← 本番値
IMAGE_EXTS = ("jpg", "jpeg", "webp", "png")
AUDIO_EXTS = ("mp3", "wav", "pcm")

ID_DATE_RE = re.compile(r"^p\d-(\d{8})-\d{4}(?:-\d+)?$")
TRAILING_QIDX_RE = re.compile(r"-(\d+)$")

PART_DIR_NAMES = {"part1", "part2", "part3", "part4"}


# =========================
# Repo root 検出
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
    return TRAILING_QIDX_RE.sub("", item_id)


def is_expired(d: datetime.date, cutoff: datetime.date) -> bool:
    return d < cutoff


# =========================
# Cleanup phase 1: file delete
# =========================
def cleanup_files(cutoff: datetime.date):
    deleted = {"json": 0, "html": 0, "media": 0, "skipped": 0}

    # --- JSON / HTML / media ---
    for json_path in list(ITEMS_DIR.rglob("*.json")):
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

        html_path = json_path.with_suffix(".html")
        if html_path.exists():
            html_path.unlink()
            deleted["html"] += 1

        # media
        try:
            part = json_path.parts[json_path.parts.index("items") + 1]
        except Exception:
            continue

        yyyy = item_date.strftime("%Y")
        mm = item_date.strftime("%m")

        # audio
        audio_dir = MEDIA_DIR / "audio" / part / yyyy / mm
        if audio_dir.exists():
            for cid in {item_id, base_audio_id(item_id)}:
                for ext in AUDIO_EXTS:
                    fp = audio_dir / f"{cid}.{ext}"
                    if fp.exists():
                        fp.unlink()
                        deleted["media"] += 1

        # image
        image_dir = MEDIA_DIR / "images" / part / yyyy / mm
        if image_dir.exists():
            for ext in IMAGE_EXTS:
                fp = image_dir / f"{item_id}.{ext}"
                if fp.exists():
                    fp.unlink()
                    deleted["media"] += 1

    # --- orphan html ---
    for html_path in list(ITEMS_DIR.rglob("*.html")):
        if html_path.with_suffix(".json").exists():
            continue
        item_id = html_path.stem
        d = extract_date_from_id(item_id)
        if not d or not is_expired(d, cutoff):
            continue
        print(f"[DELETE orphan html] {html_path}")
        html_path.unlink(missing_ok=True)
        deleted["html"] += 1

    # --- orphan audio ---
    audio_root = MEDIA_DIR / "audio"
    if audio_root.exists():
        for p in list(audio_root.rglob("*.mp3")):
            stem = p.stem
            if list(ITEMS_DIR.rglob(f"{stem}*.json")):
                continue
            d = extract_date_from_id(stem)
            if not d or not is_expired(d, cutoff):
                continue
            print(f"[DELETE orphan audio] {p}")
            p.unlink(missing_ok=True)
            deleted["media"] += 1

    # --- orphan images ---
    image_root = MEDIA_DIR / "images"
    if image_root.exists():
        for p in list(image_root.rglob("*")):
            if not p.is_file():
                continue
            if p.suffix.lower().lstrip(".") not in IMAGE_EXTS:
                continue
            stem = p.stem
            if list(ITEMS_DIR.rglob(f"{stem}.json")):
                continue
            d = extract_date_from_id(stem)
            if not d or not is_expired(d, cutoff):
                continue
            print(f"[DELETE orphan image] {p}")
            p.unlink(missing_ok=True)
            deleted["media"] += 1

    return deleted


# =========================
# Cleanup phase 2: empty dir cleanup
# =========================
def cleanup_empty_dirs(root: pathlib.Path, stop_names: set[str]):
    for d in sorted(root.rglob("*"), reverse=True):
        if not d.is_dir():
            continue
        if d.name in stop_names:
            continue
        try:
            d.rmdir()
            print(f"[RMDIR] {d}")
        except OSError:
            pass


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

    r = cleanup_files(cutoff)

    # empty dir cleanup (safe)
    cleanup_empty_dirs(ITEMS_DIR, PART_DIR_NAMES)
    cleanup_empty_dirs(MEDIA_DIR / "audio", PART_DIR_NAMES)
    cleanup_empty_dirs(MEDIA_DIR / "images", PART_DIR_NAMES)

    print("[OK] Cleanup finished")
    print(f"  json deleted   : {r['json']}")
    print(f"  html deleted   : {r['html']}")
    print(f"  media deleted  : {r['media']}")
    print(f"  skipped        : {r['skipped']}")


if __name__ == "__main__":
    main()
