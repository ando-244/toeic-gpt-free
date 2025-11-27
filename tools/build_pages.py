#!/usr/bin/env python
import json
import html
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
ITEMS_ROOT = REPO_ROOT / "items"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      margin: 1.5rem;
      line-height: 1.6;
    }}
    .audio-block {{
      margin: 1rem 0;
    }}
    img {{
      max-width: 100%;
      height: auto;
      display: block;
      margin: 1rem 0;
    }}
    .choices li {{
      margin-bottom: 0.4rem;
    }}
    .answer {{
      margin-top: 1rem;
      padding: 0.75rem;
      background: #f3f4f6;
      border-radius: 0.5rem;
    }}
  </style>
</head>
<body>
  <h1>{title}</h1>

  <div class="audio-block">
    <p>Audio:</p>
    <audio controls src="{audio_url}">
      Your browser does not support the audio element.
    </audio>
  </div>

  {image_block}

  <h2>Question</h2>
  <p>{stem}</p>

  <h3>Choices</h3>
  <ol class="choices" type="A">
    {choices_html}
  </ol>

  <div class="answer">
    <strong>Correct answer:</strong> {answer}<br>
    <strong>Explanation:</strong> {rationale}
  </div>
</body>
</html>
"""

def render_item_html(item: dict) -> str:
    content = item.get("content", {})
    assets  = item.get("assets", {})

    title = f"TOEIC Part {item.get('part')} - {item.get('id')}"
    audio_url = assets.get("audio_url", "")

    # 画像（Part1など）
    image_url = assets.get("image_url")
    if image_url:
        image_block = f'<img src="{html.escape(image_url)}" alt="Part {item.get("part")} image">'
    else:
        image_block = ""

    stem = html.escape(content.get("stem", ""))

    # choices は dict の想定
    choices = content.get("choices", {})
    # A, B, C, D の順で並べる
    choices_html = ""
    for key in sorted(choices.keys()):
        choices_html += f"<li>({key}) {html.escape(choices[key])}</li>\n"

    rationale = html.escape(content.get("rationale", ""))
    answer    = item.get("format", {}).get("answer", "")

    return HTML_TEMPLATE.format(
        title=html.escape(title),
        audio_url=html.escape(audio_url or ""),
        image_block=image_block,
        stem=stem,
        choices_html=choices_html,
        answer=html.escape(answer),
        rationale=rationale,
    )

def main():
    for json_path in ITEMS_ROOT.rglob("*.json"):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        html_text = render_item_html(data)

        html_path = json_path.with_suffix(".html")
        html_path.write_text(html_text, encoding="utf-8")
        print(f"[page] {json_path} -> {html_path}")

if __name__ == "__main__":
    main()
