#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / "experience" / "chapter04" / "section11"
OUTPUT = SECTION / "story.html"

LANGUAGES = (
    ("ja", "日本語", "section11_ja.md"),
    ("en", "English", "section11_en.md"),
    ("zh-TW", "臺灣繁體中文", "section11_zh-TW.md"),
    ("ko", "한국어", "section11_ko.md"),
    ("ru", "Русский", "section11_ru.md"),
)


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def render_markdown(text: str) -> str:
    lines = text.replace("\r\n", "\n").split("\n")
    output: list[str] = []
    paragraph: list[str] = []

    def flush() -> None:
        nonlocal paragraph
        if paragraph:
            output.append("<p>" + "<br>\n".join(inline(line) for line in paragraph) + "</p>")
            paragraph = []

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        heading = re.match(r"^(#{1,7})\s+(.+)$", line)
        if heading:
            flush()
            level = len(heading.group(1))
            title = heading.group(2).strip()
            html_level = 1 if level <= 5 else min(3, level - 4)
            output.append(f"<h{html_level}>{inline(title)}</h{html_level}>")
        elif line.startswith("- "):
            flush()
            output.append(f'<p class="list-line">{inline(line[2:].strip())}</p>')
        else:
            paragraph.append(line)
    flush()
    return "\n".join(output)


def main() -> None:
    missing = [name for _, _, name in LANGUAGES if not (SECTION / name).exists()]
    if missing:
        raise SystemExit("Missing canonical files:\n  " + "\n  ".join(missing))

    panels = []
    buttons = []
    for index, (code, label, filename) in enumerate(LANGUAGES):
        body = render_markdown((SECTION / filename).read_text(encoding="utf-8-sig"))
        active = " is-active" if index == 0 else ""
        hidden = "" if index == 0 else " hidden"
        buttons.append(
            f'<button type="button" data-language-button="{code}" '
            f'aria-pressed="{str(index == 0).lower()}">{label}</button>'
        )
        panels.append(
            f'<article class="story-panel{active}" data-language-panel="{code}" '
            f'lang="{code}"{hidden}>{body}</article>'
        )

    page = f'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="『記憶都市（メモリオポリス）』第四章第十一節「説明の継ぎ目」の五言語本編。">
  <title>第四章 第十一節「説明の継ぎ目」本編｜記憶都市（メモリオポリス）</title>
  <link rel="stylesheet" href="story.css?v=20260903-1">
  <link rel="stylesheet" href="../../assets/css/analytics-consent.css?v=20260829-1">
  <script defer src="../../assets/js/analytics-consent.js?v=20260829-1"></script>
  <script defer src="story.js?v=20260903-1"></script>
</head>
<body>
  <a class="skip-link" href="#story-content">本編へ移動</a>
  <header class="story-header">
    <a class="home-link" href="../../">中央駅へ戻る</a>
    <p class="kicker">MEMORIOPOLIS / CHAPTER 04 / SECTION 11</p>
    <h1>第十一節「説明の継ぎ目」</h1>
    <p class="subtitle">五言語正本</p>
  </header>
  <nav class="language-switcher" aria-label="本編の表示言語">
    {''.join(buttons)}
  </nav>
  <main id="story-content">
    {''.join(panels)}
  </main>
  <nav class="story-navigation" aria-label="本編の関連ページ">
    <a class="primary-link" href="act5.html">第五幕「継ぎ目は空白ではない」を読む</a>
    <a href="index.html">デジタル絵巻を体験する</a>
    <a href="trailer.html">20秒の予告編を見る</a>
    <a href="../../">中央駅へ戻る</a>
  </nav>
  <footer>
    <p>五言語のMarkdownを正本とし、このページはBuilderによって生成されています。</p>
  </footer>
  <noscript><p class="noscript-note">JavaScriptが無効な場合は、日本語正本を表示します。</p></noscript>
</body>
</html>'''
    OUTPUT.write_text(page, encoding="utf-8", newline="\n")
    print(f"[OK] {OUTPUT}")


if __name__ == "__main__":
    main()
