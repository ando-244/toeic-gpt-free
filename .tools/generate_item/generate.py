#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#TOEIC風リスニングアイテムを自動生成するスクリプト（SSML非依存版）
#Piper + ffmpeg を使用し、stdin入力方式で音声を生成します。
#"""

import argparse, datetime as dt, json, os, pathlib, subprocess, sys, textwrap
import time
import requests
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()  # .env があれば読み込む（環境変数が優先）
except Exception:
    pass

# === 設定値 ===
REPO_ROOT_DEFAULT = Path(__file__).resolve().parents[2]
BASE_URL   = os.environ.get("BASE_URL", "https://ando-244.github.io/toeic-gpt-free")
VOICE      = os.environ.get("PIPER_VOICE", r"D:\TOOLS\piper\models\en_US-ryan-medium.onnx")
PIPER_EXE  = os.environ.get("PIPER_EXE",  r"D:\TOOLS\piper\piper.exe")
FFMPEG_EXE = os.environ.get("FFMPEG_EXE", r"D:\TOOLS\ffmpeg\bin\ffmpeg.exe")

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")
VOICE_M = os.environ.get("PIPER_VOICE_M")
VOICE_W = os.environ.get("PIPER_VOICE_W")

PCM_RATE, PCM_CH, PCM_FMT = 22050, 1, "s16le"
TIMEOUT_SEC = int(os.environ.get("PIPER_TIMEOUT", "300"))

OWNER  = "ando-244"
REPO   = "toeic-gpt-free"
BRANCH = "main"

# GitHub Pages（Webサイト用）と raw（生ファイル用）の両方を用意
BASE_URL_PAGES = f"https://{OWNER}.github.io/{REPO}"
BASE_URL_RAW   = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}"

# 既定は raw にする（環境変数で切替可: USE_PAGES=1 でPagesに）
USE_PAGES = os.getenv("USE_PAGES", "0") == "1"
ASSET_BASE_URL = BASE_URL_PAGES if USE_PAGES else BASE_URL_RAW

def asset_url(rel_path: pathlib.Path) -> str:
    # rel_path は "media/audio/..." のような repo ルート相対
    p = rel_path.as_posix()
    if USE_PAGES:
        return f"{ASSET_BASE_URL}/{p}"
    else:
        return f"{ASSET_BASE_URL}/{p}"

# === ユーティリティ ===
def run(cmd, *, cwd=None, timeout=None, env=None, input_text=None):
    print("+", " ".join([f'"{c}"' if " " in str(c) else str(c) for c in cmd]))
    subprocess.run(cmd, cwd=cwd, timeout=timeout, env=env,
                   input=input_text.encode("utf-8") if input_text else None,
                   check=True)

def ensure_path(p: pathlib.Path):
    p.parent.mkdir(parents=True, exist_ok=True)

def http_get(url, *, tries=3, sleep=2):
    #"""Unsplashなど不安定API向け: リトライ＋待機つきHTTP GET"""
    for k in range(tries):
        try:
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                return r
            # 一時的なエラーコードなら待って再試行
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(sleep * (k + 1))
                continue
            # それ以外は致命的なので即raise
            r.raise_for_status()
        except requests.RequestException as e:
            if k < tries - 1:
                time.sleep(sleep * (k + 1))
                continue
            raise RuntimeError(f"GET failed after {tries} tries: {url}\n{e}")
    raise RuntimeError(f"GET failed after {tries} retries: {url}")


#VOICE_M = os.environ.get("PIPER_VOICE_M", VOICE)  # 既定は VOICE
#VOICE_W = os.environ.get("PIPER_VOICE_W", VOICE)

# === Piper音声生成 ===
def piper_text_to_pcm(text: str, pcm_path: pathlib.Path, voice: str | None = None):
    # 標準入力から Piper にテキストを渡して PCM 出力。voice でモデルを上書き可。
    ensure_path(pcm_path)
    env = os.environ.copy()
    piper_cwd = os.path.dirname(PIPER_EXE)
    v = voice or VOICE
    cmd = [PIPER_EXE, "--model", v, "--output_file", str(pcm_path)]
    print("+ echo text |", " ".join(cmd))
    run(cmd, cwd=piper_cwd, timeout=TIMEOUT_SEC, env=env, input_text=text)

# === PCM → WAV / MP3変換 ===
def pcm_to_wav_mp3(pcm_path, wav_path, mp3_path):
    ensure_path(wav_path); ensure_path(mp3_path)
    run([FFMPEG_EXE, "-y", "-f", PCM_FMT, "-ar", str(PCM_RATE), "-ac", str(PCM_CH),
         "-i", str(pcm_path), str(wav_path)])
    run([FFMPEG_EXE, "-y", "-i", str(wav_path), "-ar", "44100", "-b:a", "112k", str(mp3_path)])

# === JSON生成 ===
def make_part1_item_json(part, level, audio_url, image_url, idx, statements, answer_key):
    #"""
    #Part1（写真描写）用のJSONを生成
    #- statements: 長さ4の配列 [A, B, C, D]
    #- answer_key: "A" | "B" | "C" | "D"
    #"""
    now = dt.datetime.now(dt.UTC)
    item_id = f"p{part}-{now.strftime('%Y%m%d')}-{idx:04d}"
    choices = {
        "A": statements[0],
        "B": statements[1],
        "C": statements[2],
        "D": statements[3],
    }
    data = {
        "id": item_id,
        "part": part,
        "level": level,
        "topic": ["photo", "description"],
        "assets": {"audio_url": audio_url, "image_url": image_url},
        "format": {
            "choices": ["A", "B", "C", "D"],
            "answer": answer_key,
            "question_type": "single",
            "toeic_part_rule": "P1-Photo"
        },
        "content": {
            "stem": "(photo) Choose the statement that best describes the picture.",
            "choices": choices,
            "transcript": [
                {"speaker": "N", "text": f"Statement A. {statements[0]}"},
                {"speaker": "N", "text": f"Statement B. {statements[1]}"},
                {"speaker": "N", "text": f"Statement C. {statements[2]}"},
                {"speaker": "N", "text": f"Statement D. {statements[3]}"},
            ],
            "rationale": f"{answer_key} best matches the picture. Others are plausible distractors."
        },
        "license": {
            "type": "CC-BY-4.0",
            "origin": "original"
        }
    }
    return data

def make_part2_item_json(part, level, audio_url, idx,
                         question: str, responses: list[str], correct: str = "C"):
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
            "answer": correct,
            "question_type": "single",
            "toeic_part_rule": "P2-Response"
        },
        "content": {
            "stem": "(audio) Question-Response",
            "question": question,
            "choices": {
                "A": responses[0],
                "B": responses[1],
                "C": responses[2]
            },
            "transcript": [
                {"speaker": "W", "text": question},
                {"speaker": "R", "text": responses[0]},
                {"speaker": "R", "text": responses[1]},
                {"speaker": "R", "text": responses[2]},
            ],
            "rationale": "依頼への適切な承諾はC。Aは文脈違い、Bは場所回答で不適切。"
        },
        "license": {"type": "CC-BY-4.0", "origin": "original"}
    }


def make_part3_items_json(part, level, audio_url, idx, dialog):
    now = dt.datetime.now(dt.UTC)
    base_id = f"p{part}-{now.strftime('%Y%m%d')}-{idx:04d}"
    transcript = [{"speaker": spk, "text": text} for spk, text in dialog]

    # === 設問を定義 ===
    questions = [
        {
            "stem": "(audio) What are the speakers mainly discussing?",
            "choices": {
                "A": "A change in travel plans.",
                "B": "A change in meeting time.",
                "C": "A new employee policy.",
                "D": "A customer complaint."
            },
            "answer": "B",
            "rationale": "They talk about a schedule change, so B is correct."
        },
        {
            "stem": "(audio) When will the meeting start?",
            "choices": {
                "A": "At nine o’clock.",
                "B": "At ten o’clock.",
                "C": "At eleven o’clock.",
                "D": "At noon."
            },
            "answer": "B",
            "rationale": "The woman says it starts at ten instead of nine."
        },
        {
            "stem": "(audio) Where will they meet?",
            "choices": {
                "A": "In room A.",
                "B": "In room B.",
                "C": "In the cafeteria.",
                "D": "In the lobby."
            },
            "answer": "B",
            "rationale": "The man says they’ll meet in room B."
        }
    ]

    # === JSONリストを構築 ===
    items = []
    for q_idx, q in enumerate(questions, start=1):
        item_id = f"{base_id}-{q_idx}"
        items.append({
            "id": item_id,
            "part": part,
            "level": level,
            "topic": ["office", "schedule"],
            "assets": {"audio_url": audio_url},
            "format": {
                "choices": ["A", "B", "C", "D"],
                "answer": q["answer"],
                "question_type": "single",
                "toeic_part_rule": "P3-Conversation"
            },
            "content": {
                "stem": q["stem"],
                "choices": q["choices"],
                "transcript": transcript,
                "rationale": q["rationale"]
            },
            "license": {"type": "CC-BY-4.0", "origin": "original"}
        })
    return items


def make_part4_items_json(part, level, audio_url, idx, script_text: str):
    now = dt.datetime.now(dt.UTC)
    base_id = f"p{part}-{now.strftime('%Y%m%d')}-{idx:04d}"
    transcript = [{"speaker": "N", "text": script_text}]  # Narrator

    questions = [
        {
            "stem": "(audio) What is the announcement mainly about?",
            "choices": {
                "A": "A flight delay notice.",
                "B": "A hotel reservation.",
                "C": "A restaurant promotion.",
                "D": "A safety regulation."
            },
            "answer": "A",
            "rationale": "The talk explains a flight delay, so A is correct."
        },
        {
            "stem": "(audio) Who is the intended audience?",
            "choices": {
                "A": "Travel agents.",
                "B": "Passengers waiting at Gate 12.",
                "C": "Hotel guests.",
                "D": "Bus drivers."
            },
            "answer": "B",
            "rationale": "The speaker addresses passengers waiting at Gate 12."
        },
        {
            "stem": "(audio) What should listeners do next?",
            "choices": {
                "A": "Board the plane immediately.",
                "B": "Go to the information counter.",
                "C": "Wait for further updates.",
                "D": "Collect their baggage."
            },
            "answer": "C",
            "rationale": "The speaker tells them to wait for another announcement."
        }
    ]

    items = []
    for q_idx, q in enumerate(questions, start=1):
        item_id = f"{base_id}-{q_idx}"
        items.append({
            "id": item_id,
            "part": part,
            "level": level,
            "topic": ["announcement", "airport"],
            "assets": {"audio_url": audio_url},
            "format": {
                "choices": ["A", "B", "C", "D"],
                "answer": q["answer"],
                "question_type": "single",
                "toeic_part_rule": "P4-Talk"
            },
            "content": {
                "stem": q["stem"],
                "choices": q["choices"],
                "transcript": transcript,
                "rationale": q["rationale"]
            },
            "license": {"type": "CC-BY-4.0", "origin": "original"}
        })
    return items


def unsplash_random_image(prompt: str, out_path: pathlib.Path, orientation="landscape"):
    #"Unsplash API でランダム画像を取得し out_path に保存"
    ensure_path(out_path)
    url = (
        f"https://api.unsplash.com/photos/random"
        f"?query={requests.utils.quote(prompt)}"
        f"&orientation={orientation}"
        f"&client_id={UNSPLASH_ACCESS_KEY}"
    )
    #r = requests.get(url, timeout=30)
    #r.raise_for_status()
    r = http_get(url)
    data = r.json()
    img_url = data["urls"]["regular"]
    #img_resp = requests.get(img_url, timeout=30)
    img_resp = http_get(img_url)
    img_resp.raise_for_status()
    out_path.write_bytes(img_resp.content)
    time.sleep(1)
    return img_url

def make_part1_audio(statements, pcm_path, narrator_prefix=False, label_read=False, gap_ms=350):
    #"""
    #Part1音声を生成:
    #  - narrator_prefix=False なら前置きなし
    #  - label_read=False なら 'Statement A/B/C/D' を読まない（公式寄せ）
    #  - seg/sil を s16le 22050Hz mono で作り、Pythonでバイナリ連結
    #"""
    tmp_dir = pcm_path.parent / "_p1tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    seg_paths = []  # ← ここに Path を順番通りに積む

    def add_silence(ms, idx):
        dur = f"{ms/1000:.3f}"
        sil = tmp_dir / f"sil{idx:02d}.pcm"
        run([FFMPEG_EXE, "-y",
             "-f", "lavfi", "-i", f"anullsrc=r={PCM_RATE}:cl=mono",
             "-t", dur,
             "-f", PCM_FMT, "-ar", str(PCM_RATE), "-ac", str(PCM_CH),
             str(sil)])
        seg_paths.append(sil)

    seg_idx = 1
    if narrator_prefix:
        intro = "You will hear four statements. Choose the one that best describes the picture."
        seg = tmp_dir / f"seg{seg_idx:02d}.pcm"
        piper_text_to_pcm(intro, seg)
        seg_paths.append(seg)
        seg_idx += 1
        add_silence(gap_ms, seg_idx); seg_idx += 1

    labels = ["A", "B", "C", "D"]
    for j, text in enumerate(statements):
        spoken = f"Statement {labels[j]}. {text}" if label_read else text
        seg = tmp_dir / f"seg{seg_idx:02d}.pcm"
        piper_text_to_pcm(spoken, seg)
        seg_paths.append(seg)
        seg_idx += 1
        if j < len(statements) - 1:
            add_silence(gap_ms, seg_idx); seg_idx += 1

    # ここからが超重要：Pythonで生PCMを連結（ffmpeg concatは使わない）
    ensure_path(pcm_path)
    with open(pcm_path, "wb") as w:
        total = 0
        for p in seg_paths:
            b = p.read_bytes()
            w.write(b)
            total += len(b)
    print(f"[concat] wrote {len(seg_paths)} segments -> {pcm_path} ({total} bytes)")

    # 一時を掃除（失敗しても無視）
    try:
        for f in tmp_dir.glob("seg*.pcm"): f.unlink()
        for f in tmp_dir.glob("sil*.pcm"): f.unlink()
        tmp_dir.rmdir()
    except Exception:
        pass


def make_part2_audio(question: str, responses: list[str], pcm_path: pathlib.Path,
                     gap_ms: int = 350, read_labels: bool = False):
    #"""
    #Part2 (Question-Response) 音声を生成。
    #- read_labels=False で公式寄せ（A/B/Cは読まない）
    #- 出力は s16le, 22050Hz, mono の PCM を 1本
    #"""
    if len(responses) != 3:
        raise ValueError("responses must have exactly 3 items for Part 2")

    # 無音のバイト列を生成（ffmpegなし）
    def silence_bytes(ms: int) -> bytes:
        n_samples = int(PCM_RATE * ms / 1000)
        return b"\x00" * (n_samples * PCM_CH * 2)  # s16le = 2 bytes

    tmp_dir = pcm_path.parent / "_p2tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    segs = []

    try:
        # Q
        q_seg = tmp_dir / "q01.pcm"
        piper_text_to_pcm(question, q_seg)
        if q_seg.stat().st_size == 0:
            raise RuntimeError("Empty question segment")
        segs.append(q_seg)

        # R1..R3
        labels = ["A", "B", "C"]
        for i, text in enumerate(responses, start=1):
            if i > 1:
                # Qと各応答の間、および応答同士の間に無音を挟む
                segs.append(("SIL", gap_ms))
            spoken = f"Choice {labels[i-1]}. {text}" if read_labels else text
            r_seg = tmp_dir / f"r{i:02d}.pcm"
            piper_text_to_pcm(spoken, r_seg)
            if r_seg.stat().st_size == 0:
                raise RuntimeError(f"Empty response segment r{i:02d}")
            segs.append(r_seg)

        # バイナリ連結
        ensure_path(pcm_path)
        total = 0
        with open(pcm_path, "wb") as w:
            for s in segs:
                if isinstance(s, tuple) and s[0] == "SIL":
                    w.write(silence_bytes(s[1])); total += len(silence_bytes(s[1]))
                else:
                    b = Path(s).read_bytes()
                    w.write(b); total += len(b)
        print(f"[concat P2] wrote -> {pcm_path} ({total} bytes)")

    finally:
        # 掃除（失敗は無視）
        try:
            for f in tmp_dir.glob("*.pcm"): f.unlink()
            tmp_dir.rmdir()
        except Exception:
            pass


def generate_dialog_audio(
    dialog, pcm_path: pathlib.Path,
    gap_ms: int = 300,
    pre_silence_ms: int = 0,
    post_silence_ms: int = 0,
    label_speaker: bool = False
):
    if not dialog:
        raise ValueError("dialog is empty")

    def voice_for(s):
        su = str(s).upper()
        if su.startswith(("M", "MALE")):
            return VOICE_M
        if su.startswith(("W", "F", "FEMALE")):
            return VOICE_W
        return VOICE  # 予備

    def silence_bytes(ms: int) -> bytes:
        n = int(PCM_RATE * ms / 1000)
        return b"\x00" * (n * PCM_CH * 2)

    tmp_dir = pcm_path.parent / "_p3p4tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    seg_paths = []
    try:
        for idx, (spk, text) in enumerate(dialog, start=1):
            spoken = f"{'Man' if str(spk).upper().startswith('M') else 'Woman'}: {text}" if label_speaker else text
            seg = tmp_dir / f"seg{idx:02d}.pcm"
            piper_text_to_pcm(spoken, seg, voice=voice_for(spk))   # ← 話者ごとにモデル切替
            if seg.stat().st_size == 0:
                raise RuntimeError(f"Piper produced empty segment: {seg}")
            seg_paths.append(seg)

        ensure_path(pcm_path)
        with open(pcm_path, "wb") as w:
            if pre_silence_ms: w.write(silence_bytes(pre_silence_ms))
            for j, seg in enumerate(seg_paths):
                w.write(seg.read_bytes())
                if j < len(seg_paths) - 1 and gap_ms:
                    w.write(silence_bytes(gap_ms))
            if post_silence_ms: w.write(silence_bytes(post_silence_ms))

        print(f"[concat] wrote {len(seg_paths)} segments -> {pcm_path} ({os.path.getsize(pcm_path)} bytes)")
    finally:
        try:
            for f in tmp_dir.glob("seg*.pcm"): f.unlink()
            tmp_dir.rmdir()
        except Exception:
            pass

# ================================
#  各設問HTMLの自動生成（静的）
# ================================

def write_item_html(item: dict, html_path: pathlib.Path):
    #"""
    #items/.../<id>.json と同じディレクトリに <id>.html を出力して、
    #画像と音声をネイティブ再生できる最小ページを作る。
    #- APIや複雑なJSは使わない（CORSを踏まない）
    #- lang/title/label等を入れてアクセシビリティも担保
    #"""
    ensure_path(html_path)

    part     = item.get("part")
    content  = item.get("content", {})
    assets   = item.get("assets", {})
    stem     = content.get("stem", "")
    choices  = content.get("choices", {})
    answer   = item.get("format", {}).get("answer", "")
    transcript = content.get("transcript", [])
    rationale  = content.get("rationale", "")

    # 画像URL（Part1ならあるはず）
    image_url = assets.get("image_url") or assets.get("image") or ""

    # 音声URL（必須）
    audio_url = assets.get("audio_url", "")

    # タイトル
    page_title = f"TOEIC Part{part} – {item.get('id','')}"

    # 選択肢のHTML
    def render_choices(choices_dict: dict, correct_key: str) -> str:
        if not choices_dict:
            return ""
        rows = []
        for key in sorted(choices_dict.keys()):
            text = choices_dict[key]
            mark = " ✓" if key == correct_key else ""
            rows.append(f"<li><strong>{key}.</strong> {text}{mark}</li>")
        return "<ol type='A'>\n" + "\n".join(rows) + "\n</ol>"

    # 会話/スクリプトのHTML（Part3/4向け）
    def render_transcript(lines: list) -> str:
        if not lines:
            return ""
        rows = []
        for turn in lines:
            spk = turn.get("speaker","")
            txt = turn.get("text","")
            rows.append(f"<p><strong>{spk}</strong>: {txt}</p>")
        return "\n".join(rows)

    # 画像ブロック（任意）
    image_block = ""
    if image_url:
        image_block = f"""
      <figure style="margin:0 0 12px">
        <img src="{image_url}" alt="illustration for the item" style="max-width:100%;height:auto;border-radius:8px"/>
      </figure>"""

    # トランスクリプトブロック（Part3/4主に）
    transcript_block = ""
    if transcript:
        transcript_block = f"""
      <section aria-label="transcript" style="margin-top:12px">
        <h2 style="font-size:1.1rem;margin:0 0 6px">Transcript</h2>
        {render_transcript(transcript)}
      </section>"""

    # 選択肢ブロック（Part2/3/4で使う）
    choices_block = ""
    if choices:
        choices_block = f"""
      <section aria-label="choices" style="margin-top:12px">
        <h2 style="font-size:1.1rem;margin:0 0 6px">Choices</h2>
        {render_choices(choices, answer)}
      </section>"""

    # 解説ブロック（任意）
    rationale_block = ""
    if rationale:
        rationale_block = f"""
      <section aria-label="explanation" style="margin-top:12px">
        <h2 style="font-size:1.1rem;margin:0 0 6px">Explanation</h2>
        <p>{rationale}</p>
      </section>"""

    # 本文
    html = f"""<!doctype html>
        <html lang="en">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>{page_title}</title>
        <style>
          body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; line-height:1.5; margin: 0; }}
          .wrap {{ max-width: 960px; margin: 0 auto; padding: 16px; }}
          header h1 {{ font-size: 1.25rem; margin: 0 0 8px; }}
          .card {{ background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; box-shadow: 0 1px 2px rgba(0,0,0,.04); }}
          .meta {{ color: #6b7280; font-size:.875rem; margin-bottom:6px }}
          pre.json {{ background:#f6f8fa; padding:12px; border-radius:8px; overflow:auto }}
        </style>
        <body>
          <div class="wrap">
            <header>
              <h1>{page_title}</h1>
              <p class="meta">Level: {item.get('level','')} | Topic: {", ".join(item.get("topic", []))}</p>
            </header>

            <main class="card" role="main">
              {image_block}
              <section aria-label="audio">
                <p style="margin:8px 0"><strong>Question</strong>: {stem}</p>
                <audio src="{audio_url}" controls preload="metadata" style="width:100%"></audio>
                <p style="margin-top:6px"><a href="{audio_url}" target="_blank" rel="noopener">Open audio</a></p>
              </section>

              {choices_block}
              {transcript_block}
              {rationale_block}

              <details style="margin-top:12px">
                <summary>Show JSON</summary>
                <pre class="json">{_escape_html(json.dumps(item, ensure_ascii=False, indent=2))}</pre>
              </details>
            </main>
          </div>
        </body>
        </html>"""

    html_path.write_text(html, encoding="utf-8")


def _escape_html(s: str) -> str:
    return (s.replace("&","&amp;")
             .replace("<","&lt;")
             .replace(">","&gt;")
             .replace('"',"&quot;")
             .replace("'","&#39;"))


# === メイン処理 ===
def main():
    global VOICE

    ap = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                 description=textwrap.dedent("Piperで音声＋JSONを生成（SSML非依存版）"))
    ap.add_argument("--part", type=int, default=2, choices=[1, 2, 3, 4])
    ap.add_argument("--level", type=str, default="A2", choices=["A2", "B1", "B2"])
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--outdir", type=str, default=str(REPO_ROOT_DEFAULT))
    ap.add_argument("--query", type=str, default="office desk laptop coffee")
    ap.add_argument("--voice", type=str, default=VOICE)  # 既定VOICEを上書き
    args = ap.parse_args()

    VOICE = args.voice

    out = pathlib.Path(args.outdir)
    now = dt.datetime.now(dt.UTC)
    yyyy, mm, ymd = now.strftime("%Y"), now.strftime("%m"), now.strftime("%Y%m%d")

    for i in range(1, args.count + 1):
        audio_rel = pathlib.Path(f"media/audio/part{args.part}/{yyyy}/{mm}/p{args.part}-{i:04d}.mp3")
        wav_rel   = audio_rel.with_suffix(".wav")
        pcm_rel   = audio_rel.with_suffix(".pcm")
        json_rel  = pathlib.Path(f"items/part{args.part}/{yyyy}/{mm}/p{args.part}-{ymd}-{i:04d}.json")

        #audio_url = f"{BASE_URL}/{audio_rel.as_posix()}"
        audio_url = asset_url(audio_rel)
        pcm_path, wav_path, mp3_path, json_path = out / pcm_rel, out / wav_rel, out / audio_rel, out / json_rel

        #text = "Could you send me the draft by noon?"
        #piper_text_to_pcm(text, pcm_path)
        #pcm_to_wav_mp3(pcm_path, wav_path, mp3_path)

        # === Partごとの処理分岐 ===
        if args.part == 1:
            #prompt = "office desk laptop coffee"  # 写真キーワードの例
            image_rel = pathlib.Path(f"media/images/part1/{yyyy}/{mm}/p1-{i:04d}.webp")
            image_path = out / image_rel
            #image_url = unsplash_random_image(prompt, image_path)
            #image_url = unsplash_random_image(args.query, image_path)
            #image_url = f"{BASE_URL}/{image_rel.as_posix()}"
            image_url = asset_url(image_rel)
            # statements…
            statements = [
                "A laptop is open on the desk.",       # 正解
                "Some people are standing in a line.",
                "A car is parked on the street.",
                "The room is decorated for a party."
            ]
            answer_key = "A"

            # 1) 音声（PCM）だけ作る
            #make_part1_audio(statements, pcm_path)
            make_part1_audio(statements, pcm_path, narrator_prefix=False, label_read=False, gap_ms=400)

            # 2) JSON
            item = make_part1_item_json(args.part, args.level, audio_url, image_url, i, statements, answer_key)

        elif args.part == 2:
            question = "Could you send me the draft by noon?"
            responses = [
                "I’ll send it before lunch.",     # A
                "I’m meeting her at the cafeteria.",  # B（文脈外）
                "Sure, I’ll email it by twelve."  # C 正解
            ]
            correct = "C"

            # 1) 音声（PCM）だけ作る
            make_part2_audio(question, responses, pcm_path, gap_ms=350, read_labels=False)

            # 2) JSON
            item = make_part2_item_json(args.part, args.level, audio_url, i,
                                question, responses, correct)

        elif args.part == 3:
            dialog = [
                ("M", "Good morning. Did you check the new meeting schedule?"),
                ("W", "Yes, it starts at ten instead of nine."),
                ("M", "Right, and we’ll meet in room B now.")
            ]

            # 1) 会話音声生成（二人の声で）
            generate_dialog_audio(dialog, pcm_path, gap_ms=300, label_speaker=False)

            # 2) WAV/MP3変換
            pcm_to_wav_mp3(pcm_path, wav_path, mp3_path)

            # 3) 設問3本のJSONを生成
            items = make_part3_items_json(args.part, args.level, audio_url, i, dialog)
            item_dir = out / pathlib.Path(f"items/part{args.part}/{yyyy}/{mm}")
            item_dir.mkdir(parents=True, exist_ok=True)
            
            # 4) JSON出力
            for item in items:
                out_json = item_dir / f"{item['id']}.json"
                out_json.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
                #print(f"[JSON] {out_json}")
                #print(f"[OK] {mp3_path} and {out_json}")
                out_html = item_dir / f"{item['id']}.html"
                write_item_html(item, out_html)
            
            continue

        elif args.part == 4:
            # 例：空港アナウンス
            script_text = (
                "Good afternoon, passengers. "
                "This is an announcement for all travelers waiting for Flight 102 to Seattle. "
                "Due to heavy fog, the departure will be delayed for about thirty minutes. "
                "Please remain near Gate 12 and listen for further updates. "
                "We apologize for the inconvenience and thank you for your patience."
            )

            # 1) 音声生成（話者1人、ナレーション風）
            generate_dialog_audio([("N", script_text)], pcm_path, gap_ms=0, label_speaker=False)

            # 2) WAV/MP3変換
            pcm_to_wav_mp3(pcm_path, wav_path, mp3_path)

            # 3) JSON生成（設問3つ）
            items = make_part4_items_json(args.part, args.level, audio_url, i, script_text)
            item_dir = out / pathlib.Path(f"items/part{args.part}/{yyyy}/{mm}")
            item_dir.mkdir(parents=True, exist_ok=True)

            # 4) 各設問JSONを保存
            for item in items:
                out_json = item_dir / f"{item['id']}.json"
                out_json.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
                #print(f"[JSON] {out_json}")
                #print(f"[OK] {mp3_path} and {out_json}")
                out_html = item_dir / f"{item['id']}.html"
                write_item_html(item, out_html)

            continue

        else:
            raise ValueError(f"Unsupported part: {args.part}")

        # === PCM → WAV → MP3 ===
        pcm_to_wav_mp3(pcm_path, wav_path, mp3_path)

        # === JSON保存 ===
        ensure_path(json_path)
        json_path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
        html_path = json_path.with_suffix(".html")
        write_item_html(item, html_path)

        print(f"[OK] {mp3_path} and {json_path}")

# === 実行エントリ ===
if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
