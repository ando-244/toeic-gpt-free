#!/usr/bin/env python3
from __future__ import annotations
import pathlib
import datetime
import re
import sys

# === 設定 ===
KEEP_DAYS = 16
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]

ITEMS_DIR = REPO_ROOT / "items"
MEDIA_DIR = REPO_ROOT / "media"

ID_DATE_RE = re.compile(r"p\d-(\d{8})-\d{4}")

def extract_date_from_id(item_id: str) -> datetime.date | None:
    m = ID_DATE_RE.match(item_id)
    if not m:
        return None
    return datetime.datetime.strptime(m.group(1), "%Y%m%d").date()

def main():
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=KEEP_DAYS)

    print(f"[INFO] Cleanup cutoff date: {cutoff}")

    deleted_items = 0
    deleted_media = 0

    for json_path in ITEMS_DIR.rglob("*.json"):
        try:
            item_id = json_path.stem
            item_date = extract_date_from_id(item_id)
            if not item_date:
                continue

            if item_date >= cutoff:
                continue  # keep

            print(f"[DELETE] {item_id}")

            # --- delete item json ---
            json_path.unlink(missing_ok=True)
            deleted_items += 1

            # --- delete related media ---
            part = json_path.parts[json_path.parts.index("items") + 1]
            yyyy = item_date.strftime("%Y")
            mm   = item_date.strftime("%m")

            audio_dir = MEDIA_DIR / "audio" / part / yyyy / mm
            image_dir = MEDIA_DIR / "images" / part / yyyy / mm

            for ext in ("mp3", "wav", "pcm"):
                p = audio_dir / f"{item_id}.{ext}"
                if p.exists():
                    p.unlink()
                    deleted_media += 1

            img = image_dir / f"{item_id}.jpg"
            if img.exists():
                img.unlink()
                deleted_media += 1

        except Exception as e:
            print(f"[WARN] Failed to process {json_path}: {e}", file=sys.stderr)

    print(f"[OK] Deleted items: {deleted_items}, media files: {deleted_media}")

if __name__ == "__main__":
    main()
