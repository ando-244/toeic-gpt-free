#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, datetime as dt, json, os, pathlib, subprocess, sys, textwrap

BASE_URL   = os.environ.get("BASE_URL", "https://ando-244.github.io/toeic-gpt-free")
VOICE      = os.environ.get("PIPER_VOICE", r"D:\\TOOLS\\piper\\models\\en_US-ryan-medium.onnx")
PIPER_EXE  = os.environ.get("PIPER_EXE",  r"D:\\TOOLS\\piper\\piper.exe")
FFMPEG_EXE = os.environ.get("FFMPEG_EXE", "ffmpeg")
PCM_RATE, PCM_CH, PCM_FMT = 22050, 1, "s16le"

def run(cmd):
  print("+", " ".join([f'"{c}"' if " " in str(c) else str(c) for c in cmd]))
  subprocess.check_call(cmd)

def ensure(p): p.parent.mkdir(parents=True, exist_ok=True)

def ssml_wrap(lines, rate=92):
  body = "".join([f'<p><prosody rate="{rate}%">{l}</prosody></p>' for l in lines])
  return f"<speak>{body}</speak>"

def make_item_json(part, level, audio_url, idx):
  now = dt.datetime.utcnow(); item_id = f"p{part}-{now.strftime('%Y%m%d')}-{idx:04d}"
  return {
    "id": item_id,
    "part": part,
    "level": level,
    "topic": ["email","deadline"],
    "assets": {"audio_url": audio_url},
    "format": {"choices":["A","B","C"], "answer":"C", "question_type":"single", "toeic_part_rule":"P2-Response"},
    "content": {
      "stem": "(audio) Could you send me the draft by noon?",
      "choices": {"A":"No, it's not a graph.","B":"At the cafeteria, I think.","C":"Sure, I'll email it before twelve."},
      "transcript": [{"speaker":"W","text":"Could you send me the draft by noon?"}],
      "ssml": ssml_wrap(["Could you send me the draft by noon?"], rate=92),
      "rationale": "依頼への適切な承諾はC。Aは音の連想、Bは文脈外。"
    },
    "license": {"type":"CC-BY-4.0","origin":"original"}
  }

def piper_ssml_to_pcm(ssml_text, pcm_path: pathlib.Path):
  ssml = pcm_path.with_suffix(".ssml"); ssml.write_text(ssml_text, encoding="utf-8"); ensure(pcm_path)
  run([PIPER_EXE, "--model", VOICE, "--ssml", str(ssml), "--output_file", str(pcm_path)])
  ssml.unlink(missing_ok=True)

def pcm_to_wav_mp3(pcm_path, wav_path, mp3_path):
  ensure(wav_path); ensure(mp3_path)
  run([FFMPEG_EXE, "-y", "-f", PCM_FMT, "-ar", str(PCM_RATE), "-ac", str(PCM_CH), "-i", str(pcm_path), str(wav_path)])
  run([FFMPEG_EXE, "-y", "-i", str(wav_path), "-ar", "44100", "-b:a", "112k", str(mp3_path)])

def main():
  ap = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
    description=textwrap.dedent("Piperで音声MP3items JSONを生成"))
  ap.add_argument("--part", type=int, default=2, choices=[1,2,3,4])
  ap.add_argument("--level", type=str, default="A2", choices=["A2","B1","B2"])
  ap.add_argument("--count", type=int, default=1)
  ap.add_argument("--outdir", type=str, default=".")
  args = ap.parse_args()

  out = pathlib.Path(args.outdir); now = dt.datetime.utcnow()
  yyyy, mm, ymd = now.strftime("%Y"), now.strftime("%m"), now.strftime("%Y%m%d")
  for i in range(1, args.count+1):
    audio_rel = pathlib.Path(f"media/audio/part{args.part}/{yyyy}/{mm}/p{args.part}-{i:04d}.mp3")
    wav_rel   = audio_rel.with_suffix(".wav"); pcm_rel = audio_rel.with_suffix(".pcm")
    json_rel  = pathlib.Path(f"items/part{args.part}/{yyyy}/{mm}/p{args.part}-{ymd}-{i:04d}.json")

    audio_url = f"{BASE_URL}/{audio_rel.as_posix()}"
    pcm_path, wav_path, mp3_path, json_path = out/pcm_rel, out/wav_rel, out/audio_rel, out/json_rel

    ssml = ssml_wrap(["Could you send me the draft by noon?"], rate=92)
    piper_ssml_to_pcm(ssml, pcm_path)
    pcm_to_wav_mp3(pcm_path, wav_path, mp3_path)

    item = make_item_json(args.part, args.level, audio_url, i); ensure(json_path)
    json_path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] {mp3_path} and {json_path}")

if __name__ == "__main__":
  try:
    main()
  except subprocess.CalledProcessError as e:
    print(f"[ERROR] {e}", file=sys.stderr); sys.exit(1)
