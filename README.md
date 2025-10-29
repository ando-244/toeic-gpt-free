# toeic-gpt-free

無料スタック（Piper + ffmpeg + GitHub Pages）で TOEIC L&R Part1〜4 の音声画像問題を生成配信する最小構成。

## 要件
- Windows 10/11
- Piper（DLL一式揃った動作版）
- ffmpeg
- Python 3.10+

## 使い方（最短）
1. .tools/generate_item/generate.py を実行して音声+JSON生成
2. コミットして push  GitHub Pages で配信

### 例
`powershell
cd .tools/generate_item
python .\generate.py --part 2 --level A2 --count 1
