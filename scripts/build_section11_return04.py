#!/usr/bin/env python3
from __future__ import annotations
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / "experience" / "chapter04" / "section11"
SOURCE = SECTION / "section11_return04_ja.md"
OUTPUT = SECTION / "return04.html"

TONES = {
    1: ("en", "#101722", "#1d2937"),
    2: ("zh", "#211e16", "#332f22"),
    3: ("ko", "#0d1b29", "#153348"),
    4: ("ru", "#13201d", "#273932"),
    5: ("ja", "#0b1921", "#17303c"),
    6: ("ja", "#091720", "#132b37"),
    7: ("ja", "#08161f", "#112833"),
    8: ("ja", "#07151d", "#102631"),
    9: ("ja", "#07141c", "#10242f"),
    10: ("final", "#06131b", "#0e222c"),
}

def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text

def render(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    para: list[str] = []
    section_open = False
    section_no = 0

    def flush() -> None:
        nonlocal para
        if para:
            out.append("<p>" + "<br>\n".join(inline(x) for x in para) + "</p>")
            para = []

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if line.startswith("### "):
            flush()
            title = line[4:].strip()
            if re.match(r"^\d+．", title):
                if section_open:
                    out.append("</section>")
                section_no += 1
                key, a, b = TONES.get(section_no, TONES[10])
                out.append(
                    f'<section class="return-section tone-{key}" '
                    f'style="--tone-a:{a};--tone-b:{b}" data-return-section="{section_no}">'
                )
                out.append(f'<h2><span class="section-index">{section_no:02d}</span>{inline(title)}</h2>')
                section_open = True
            else:
                out.append(f'<p class="document-title">{inline(title)}</p>')
        elif line.startswith("#### "):
            flush()
            out.append(f'<h3>{inline(line[5:].strip())}</h3>')
        elif line.startswith("## "):
            flush()
        elif line.startswith("- "):
            flush()
            out.append(f'<p class="list-line">{inline(line[2:].strip())}</p>')
        else:
            para.append(line)
    flush()
    if section_open:
        out.append("</section>")
    return "\n".join(out)

def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Missing canonical Return file: {SOURCE}")
    body = render(SOURCE.read_text(encoding="utf-8-sig"))
    page = f'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="五言語を通過して日本語正本へ戻った、第四章第十一節の第四回Return完全記録。">
  <title>第四回Return｜記憶都市（メモリオポリス）</title>
  <link rel="stylesheet" href="return04.css?v=20260903-1">
  <link rel="stylesheet" href="../../assets/css/analytics-consent.css?v=20260829-1">
  <script defer src="../../assets/js/analytics-consent.js?v=20260829-1"></script>
  <script defer src="return04.js?v=20260903-1"></script>
</head>
<body>
  <div class="strata strata-left" aria-hidden="true"></div>
  <div class="strata strata-right" aria-hidden="true"></div>
  <a class="skip-link" href="#return-content">Returnへ移動</a>
  <header class="return-hero">
    <a class="home-link" href="../../">中央駅へ戻る</a>
    <p class="kicker">MEMORIOPOLIS / RETURN 04</p>
    <h1>第四回Return</h1>
    <p class="return-title">五言語を通過して<br>日本語正本へ戻る</p>
    <p class="decision">日本語正本は変更しない。</p>
    <p class="lead">これは修正文の一覧ではない。五つの言語が前景化したものと、日本語が言わずに保持していたものを保存する判断記録である。</p>
  </header>
  <main id="return-content">{body}</main>
  <div class="return-rest" aria-hidden="true"></div>
  <nav class="return-navigation" aria-label="第四回Returnの関連ページ">
    <a class="primary-link" href="act5.html">第五幕「継ぎ目は空白ではない」を読む</a>
    <a href="story.html#ja">日本語正本を読み返す</a>
    <a href="story.html">五言語本編を読む</a>
    <a href="index.html">デジタル絵巻を読み返す</a>
    <a href="../../">中央駅へ戻る</a>
  </nav>
  <footer><p>正本：section11_return04_ja.md</p></footer>
  <noscript><p class="noscript-note">JavaScriptが無効でも全文を読めます。背景は日本語正本の青灰で固定されます。</p></noscript>
</body>
</html>'''
    OUTPUT.write_text(page, encoding="utf-8", newline="\n")
    print(f"[OK] {OUTPUT}")

if __name__ == "__main__":
    main()
