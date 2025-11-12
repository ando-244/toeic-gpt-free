#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#items/**/**/*.json を走査して public/manifest.json を生成。
#- 必須: id, part, level, assets.audio_url
#- 任意: assets.image_url, page_url, topic, license などはあれば反映
#- page_url が JSON に無い場合は --base-url を使って <base>/items/.../<id>.html を推測生成
#使い方:
#  python tools/build_manifest.py [--items-dir items] [--out public/manifest.json] [--base-url https://ando-244.github.io/toeic-gpt-free]
#"""

from __future__ import annotations
import argparse, json, sys, os, pathlib, datetime
from typing import Any, Dict, List

def load_json(p: pathlib.Path) -> Dict[str, Any]:
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[WARN] JSON読み込み失敗: {p} :: {e}", file=sys.stderr)
        return {}

def required(d: Dict[str, Any], ks: List[str]) -> bool:
    cur = d
    for k in ks:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return False
    return True

def guess_page_url(base_url: str, json_path: pathlib.Path, item_id: str) -> str | None:
    # items/partX/YYYY/MM/<id>.json → <base>/items/partX/YYYY/MM/<id>.html
    try:
        parts = json_path.parts
        # .../<repo>/items/partX/YYYY/MM/<file>
        idx = parts.index("items")
        rel = pathlib.Path(*parts[idx:])              # items/partX/YYYY/MM/<file>
        html = rel.with_suffix(".html")               # items/partX/YYYY/MM/<id>.html
        return f"{base_url.rstrip('/')}/{html.as_posix()}"
    except Exception:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items-dir", default="items", help="アイテムJSONのルートディレクトリ")
    ap.add_argument("--out", default="public/manifest.json", help="出力パス")
    ap.add_argument("--base-url", default=os.environ.get("PUBLIC_BASE_URL", ""), help="page_url 推測用の公開ベースURL")
    args = ap.parse_args()

    repo_root = pathlib.Path(__file__).resolve().parents[1]
    items_dir = (repo_root / args.items_dir).resolve()
    out_path  = (repo_root / args.out).resolve()

    if not items_dir.exists():
        print(f"[ERR] items ディレクトリが見つかりません: {items_dir}", file=sys.stderr)
        sys.exit(1)

    json_files = list(items_dir.rglob("*.json"))
    if not json_files:
        print(f"[WARN] JSONが見つかりません: {items_dir}", file=sys.stderr)

    items_out: List[Dict[str, Any]] = []
    seen_ids = set()

    for jp in sorted(json_files):
        data = load_json(jp)
        if not data:
            continue

        # 必須チェック
        if not all(k in data for k in ("id", "part", "level", "assets")):
            print(f"[SKIP] フィールド不足: {jp}", file=sys.stderr)
            continue
        if not required(data, ["assets", "audio_url"]):
            print(f"[SKIP] assets.audio_url 不足: {jp}", file=sys.stderr)
            continue

        item_id = data["id"]
        if item_id in seen_ids:
            print(f"[WARN] 重複 id: {item_id} ({jp})", file=sys.stderr)
            # 重複は後勝ちにして採用
        seen_ids.add(item_id)

        # page_url
        page_url = data.get("page_url")
        if not page_url and args.base_url:
            # JSONに無ければ推測で付与
            page_url = guess_page_url(args.base_url, jp, item_id)

        # 軽量なレコードを構築（必要そうなものだけ）
        rec = {
            "id": item_id,
            "part": data.get("part"),
            "level": data.get("level"),
            "topic": data.get("topic") or data.get("topics") or [],
            "page_url": page_url,
            "audio_url": data["assets"]["audio_url"],
            "image_url": data.get("assets", {}).get("image_url"),
            # 便利メタ
            "json_path": str(jp.relative_to(repo_root).as_posix()),
        }

        # ソート用キー（更新日やIDでお好み）
        rec["_sort"] = (data.get("part"), data.get("level"), item_id)
        items_out.append(rec)

    items_out.sort(key=lambda r: r["_sort"])
    for r in items_out:
        r.pop("_sort", None)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "generated_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "base_url_hint": args.base_url,
        "count": len(items_out),
        "items": items_out,
    }
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"[OK] manifest: {out_path} ({len(items_out)} items)")

if __name__ == "__main__":
    main()
