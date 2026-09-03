#!/usr/bin/env python3
from __future__ import annotations
import html, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / 'experience' / 'chapter04' / 'section11'
SOURCE_CANDIDATES = (
    SECTION / 'section11_multilingual_creation_notes.md',
    ROOT / 'section11_multilingual_creation_notes.md',
)
OUTPUT = SECTION / 'act5.html'

PALETTE = {
    'ja': ('#07131b', '#102632'),
    'en': ('#07111c', '#192432'),
    'zh': ('#16140f', '#2b271d'),
    'ko': ('#081521', '#102b3b'),
    'ru': ('#0d1715', '#20302b'),
    'return': ('#18140d', '#342818'),
    'final': ('#07131b', '#102632'),
}

def source_path() -> Path:
    for p in SOURCE_CANDIDATES:
        if p.exists(): return p
    raise SystemExit('section11_multilingual_creation_notes.md was not found in section11 or repository root.')

def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    return text

def lang_for(title: str, index: int) -> str:
    if index == 14: return 'return'
    if index >= 15: return 'final'
    if 'English' in title: return 'en'
    if '한국어' in title: return 'ko'
    if 'Русский' in title: return 'ru'
    if '臺灣' in title or '華語' in title: return 'zh'
    return 'ja'

def render_markdown(md: str) -> str:
    lines = md.replace('\r\n','\n').split('\n')
    out, para, section_open, section_no = [], [], False, 0
    def flush():
        nonlocal para
        if para:
            out.append('<p>' + '<br>\n'.join(inline(x) for x in para) + '</p>')
            para = []
    for raw in lines:
        line = raw.rstrip()
        if not line.strip(): flush(); continue
        if line.startswith('### '):
            flush()
            if section_open: out.append('</section>')
            section_no += 1
            title = line[4:].strip()
            key = lang_for(title, section_no)
            a,b = PALETTE[key]
            out.append(f'<section class="act-section tone-{key}" style="--tone-a:{a};--tone-b:{b}" data-act-section="{section_no}">')
            out.append(f'<h2><span class="section-index">{section_no:02d}</span>{inline(title)}</h2>')
            section_open = True
        elif line.startswith('#### '):
            flush(); out.append(f'<h3>{inline(line[5:].strip())}</h3>')
        elif line.startswith('##### '):
            flush(); out.append(f'<p class="subtitle" lang="en">{inline(line[6:].strip())}</p>')
        elif line.startswith('## '):
            flush()
        elif line.startswith('- '):
            flush(); out.append(f'<p class="list-line">{inline(line[2:].strip())}</p>')
        else:
            para.append(line)
    flush()
    if section_open: out.append('</section>')
    return '\n'.join(out)

def main():
    md = source_path().read_text(encoding='utf-8-sig')
    body = render_markdown(md)
    page = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="五つの言語が同じ物語に残した重なりとずれを読む、独立作品としての第五幕。">
<title>第五幕「継ぎ目は空白ではない」｜記憶都市（メモリオポリス）</title>
<link rel="stylesheet" href="act5.css?v=20260903-1">
<link rel="stylesheet" href="../../assets/css/analytics-consent.css?v=20260829-1">
<script defer src="../../assets/js/analytics-consent.js?v=20260829-1"></script>
<script defer src="act5.js?v=20260903-1"></script>
</head>
<body>
<a class="skip-link" href="#act5-content">第五幕へ移動</a>
<header class="act-hero">
<a class="home-link" href="../../">中央駅へ戻る</a>
<p class="kicker">MEMORIOPOLIS / ACT V / MULTILINGUAL RETURN</p>
<h1>第五幕<br><span>「継ぎ目は空白ではない」</span></h1>
<p class="english-title" lang="en">The Seam Is Not Empty</p>
<p class="descriptor">第四章第十一節 五言語混交制作ノート</p>
<p class="lead">五つの言語が，同じ物語の中に何を残し，何をずらしたのかを読む．</p>
</header>
<main id="act5-content">{body}</main>
<div class="closing-space" aria-hidden="true"></div>
<nav class="act-navigation" aria-label="第五幕の関連ページ">
<a class="primary-link" href="story.html">小説本編を読み返す</a>
<a href="index.html">デジタル絵巻を読み返す</a>
<a href="trailer.html">20秒の予告編を見る</a>
<a href="../../">中央駅へ戻る</a>
</nav>
<footer><p>GitHub上のMarkdownを正本とし，第五幕は小説と絵巻に並ぶ独立作品として公開されます．</p></footer>
<noscript><p class="noscript-note">JavaScriptが無効でも全文を読めます．背景色は固定されます．</p></noscript>
</body></html>'''
    OUTPUT.write_text(page, encoding='utf-8', newline='\n')
    print(f'[OK] {OUTPUT}')

if __name__ == '__main__': main()
