#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TOEIC風リスニングアイテムを自動生成するスクリプト（SSML非依存版）
Piper + ffmpeg を使用し、stdin入力方式で音声を生成します。
"""

import argparse, datetime as dt, json, os, pathlib, subprocess, sys, textwrap
from pathlib import Path

# === 設定値 ===
REPO_ROOT_DEFAULT = Path(__file__).resolve().parents[2]
BASE_URL   = os.environ.get("BASE_URL", "https://ando-244.github.io/toeic-gpt-free")
VOICE      = os.environ.get("PIPER_VOICE", r"D:\TOOLS\piper\models\en_US-ryan-medium.onnx")
PIPER_EXE  = os.environ.get("PIPER_EXE",  r"D:\TOOLS\piper\piper.exe")
FFMPEG_EXE = os.environ.get("FFMPEG_EXE", r"D:\TOOLS\ffmpeg\bin\ffmpeg.exe")
PCM_RATE, PCM_CH, PCM_FMT = 22050, 1, "s16le"
TIMEOUT_SEC = int(os.environ.get("PIPER_TIMEOUT", "300"))

# === ユーティリティ ===
def run(cmd, *, cwd=None, timeout=None, env=None, input_text=None):
    print("+", " ".join([f'"{c}"' if " " in str(c) else str(c) for c in cmd]))
    subprocess.run(cmd, cwd=cwd, timeout=timeout, env=env,
                   input=input_text.encode("utf-8") if input_text else None,
                   check=True)

def ensure_path(p: pathlib.Path):
    p.parent.mkdir(parents=True, exist_ok=True)

# === Piper音声生成 ===
def piper_text_to_pcm(text: str, pcm_path: pathlib.Path):
    """標準入力経由でテキストからPCMを生成"""
    ensure_path(pcm_path)
    env = os.environ.copy()
    piper_cwd = os.path.dirname(PIPER_EXE)
    cmd = [PIPER_EXE, "--model", VOICE, "--output_file", str(pcm_path)]
    print("+ echo text |", " ".join(cmd))
    run(cmd, cwd=piper_cwd, timeout=TIMEOUT_SEC, env=env, input_text=text)

# === PCM → WAV / MP3変換 ===
def pcm_to_wav_mp3(pcm_path, wav_path, mp3_path):
    ensure_path(wav_path); ensure_path(mp3_path)
    run([FFMPEG_EXE, "-y", "-f", PCM_FMT, "-ar", str(PCM_RATE), "-ac", str(PCM_CH),
         "-i", str(pcm_path), str(wav_path)])
    run([FFMPEG_EXE, "-y", "-i", str(wav_path), "-ar", "44100", "-b:a", "112k", str(mp3_path)])

# === JSON生成 ===
def make_item_json(part, level, audio_url, idx):
    now = dt.datetime.now(dt.UTC)
    item_id = f"p{part}-{now.strftime('%Y%m%d')}-{idx:04d}"
    return {
        "id": item_id,
        "part": part,
        "level": level,
        "topic": ["email", "deadline"],
        "assets": {"audio_url": audio_url},
        "format": {
            "choices": ["A", "B", "C"],
            "answer": "C",
            "question_type": "single",
            "toeic_part_rule": "P2-Response"
        },
        "content": {
            "stem": "(audio) Could you send me the draft by noon?",
            "choices": {
                "A": "No, it's not a graph.",
                "B": "At the cafeteria, I think.",
                "C": "Sure, I'll email it before twelve."
            },
            "transcript": [{"speaker": "W", "text": "Could you send me the draft by noon?"}],
            "rationale": "依頼への適切な承諾はC。Aは音の連想、Bは文脈外。"
        },
        "license": {"type": "CC-BY-4.0", "origin": "original"}
    }

# === メイン処理 ===
def main():
    ap = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                 description=textwrap.dedent("Piperで音声＋JSONを生成（SSML非依存版）"))
    ap.add_argument("--part", type=int, default=2, choices=[1, 2, 3, 4])
    ap.add_argument("--level", type=str, default="A2", choices=["A2", "B1", "B2"])
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--outdir", type=str, default=str(REPO_ROOT_DEFAULT))
    args = ap.parse_args()

    out = pathlib.Path(args.outdir)
    now = dt.datetime.now(dt.UTC)
    yyyy, mm, ymd = now.strftime("%Y"), now.strftime("%m"), now.strftime("%Y%m%d")

    for i in range(1, args.count + 1):
        audio_rel = pathlib.Path(f"media/audio/part{args.part}/{yyyy}/{mm}/p{args.part}-{i:04d}.mp3")
        wav_rel   = audio_rel.with_suffix(".wav")
        pcm_rel   = audio_rel.with_suffix(".pcm")
        json_rel  = pathlib.Path(f"items/part{args.part}/{yyyy}/{mm}/p{args.part}-{ymd}-{i:04d}.json")

        audio_url = f"{BASE_URL}/{audio_rel.as_posix()}"
        pcm_path, wav_path, mp3_path, json_path = out / pcm_rel, out / wav_rel, out / audio_rel, out / json_rel

        text = "Could you send me the draft by noon?"
        piper_text_to_pcm(text, pcm_path)
        pcm_to_wav_mp3(pcm_path, wav_path, mp3_path)

        item = make_item_json(args.part, args.level, audio_url, i)
        ensure_path(json_path)
        json_path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")

        print(f"[OK] {mp3_path} and {json_path}")

# === 実行エントリ ===
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
