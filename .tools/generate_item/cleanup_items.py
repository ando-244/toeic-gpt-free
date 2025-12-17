#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import datetime
import re
import sys

# =========================
# 設定
# =========================
KEEP_DAYS = 90   # ← 本番値
IMAGE_EXTS = ("jpg", "jpeg", "webp", "png")
AUDIO_EXTS = ("mp3", "wav", "pcm")

ID_DATE_RE = re.compile(r"^p\d-(\d{8})-\d{4}(?:-\d+)?$")
TRAILING_QIDX_RE = re.compile(r"-(\d+)$")

PARTS = ("part1", "part2", "part3", "part4")


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
# Phase 1: file deletion
# =========================
def cleanup_files(cutoff: datetime.date):
    stats = {"json": 0, "html": 0, "media": 0, "skipped": 0}

    # ---- JSON / HTML / media ----
    for json_path in list(ITEMS_DIR.rglob("*.json")):
        item_id = json_path.stem
        item_date = extract_date_from_id(item_id)
        if not item_date:
            stats["skipped"] += 1
            continue
        if not is_expired(item_date, cutoff):
            continue

        print(f"[DELETE json] {json_path}")
        json_path.unlink(missing_ok=True)
        stats["json"] += 1

        html_path = json_path.with_suffix(".html")
        if html_path.exists():
            html_path.unlink()
            stats["html"] += 1

        # part 
        try:
            part = json_path.parts[json_path.parts.index("items") + 1]
        except Exception:
            continue

        # audio
        audio_dir = MEDIA_DIR / "audio" / part 
        if audio_dir.exists():
            for cid in {item_id, base_audio_id(item_id)}:
                for ext in AUDIO_EXTS:
                    p = audio_dir / f"{cid}.{ext}"
                    if p.exists():
                        p.unlink()
                        stats["media"] += 1

        # image
        image_dir = MEDIA_DIR / "images" / part 
        if image_dir.exists():
            for ext in IMAGE_EXTS:
                p = image_dir / f"{item_id}.{ext}"
                if p.exists():
                    p.unlink()
                    stats["media"] += 1

    # ---- orphan html ----
    for html_path in list(ITEMS_DIR.rglob("*.html")):
        if html_path.with_suffix(".json").exists():
            continue
        d = extract_date_from_id(html_path.stem)
        if not d or not is_expired(d, cutoff):
            continue
        print(f"[DELETE orphan html] {html_path}")
        html_path.unlink(missing_ok=True)
        stats["html"] += 1

    # ---- orphan audio ----
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
            stats["media"] += 1

    # ---- orphan images ----
    image_root = MEDIA_DIR / "images"
    if image_root.exists():
        for p in list(image_root.rglob("*")):
            if not p.is_file():
                continue
            if p.suffix.lower().lstrip(".") not in IMAGE_EXTS:
                continue
            if list(ITEMS_DIR.rglob(f"{p.stem}.json")):
                continue
            d = extract_date_from_id(p.stem)
            if not d or not is_expired(d, cutoff):
                continue
            print(f"[DELETE orphan image] {p}")
            p.unlink(missing_ok=True)
            stats["media"] += 1

    return stats


# =========================
# Phase 2: empty dir cleanup (SAFE)
# =========================
def cleanup_empty_dirs(root: pathlib.Path, stop_dirs: set[pathlib.Path]):
    """
    root 配下の空ディレクトリを削除。
    stop_dirs に含まれるディレクトリ、および root 自体は絶対に削除しない。
    """
    for d in sorted(root.rglob("*"), reverse=True):
        if not d.is_dir():
            continue
        if d == root:
            continue
        if any(d == stop or d.is_relative_to(stop) for stop in stop_dirs):
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

    stats = cleanup_files(cutoff)

    # ---- empty dir cleanup (partX は残す) ----
    cleanup_empty_dirs(
        ITEMS_DIR,
        stop_dirs={ITEMS_DIR, *(ITEMS_DIR / p for p in PARTS)}
    )
    cleanup_empty_dirs(
        MEDIA_DIR / "audio",
        stop_dirs={(MEDIA_DIR / "audio"), *((MEDIA_DIR / "audio") / p for p in PARTS)}
    )
    cleanup_empty_dirs(
        MEDIA_DIR / "images",
        stop_dirs={(MEDIA_DIR / "images"), *((MEDIA_DIR / "images") / p for p in PARTS)}
    )

    print("[OK] Cleanup finished")
    print(f"  json deleted   : {stats['json']}")
    print(f"  html deleted   : {stats['html']}")
    print(f"  media deleted  : {stats['media']}")
    print(f"  skipped        : {stats['skipped']}")


if __name__ == "__main__":
    main()
