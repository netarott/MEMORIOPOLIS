#!/usr/bin/env python3
"""Build the GitHub Pages experience for MEMORIOPOLIS chapter 4, section 10.

Usage from the repository root:

    py scripts/build_section10.py --check
    py scripts/build_section10.py

Input:
    novel/chapter04/section10/

Output:
    experience/chapter04/section10/

The builder validates all five localized Markdown sources, the fifth-act
production notes, LOCALIZATION_READY, and the final trailer MP4. It then
creates deterministic static HTML, CSS, JavaScript, and copies the trailer.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import markdown
except ImportError as exc:
    raise SystemExit(
        "Python Markdown is not installed. Run:\n"
        "  py -m pip install markdown\n"
        "or on GitHub Actions:\n"
        "  python -m pip install markdown"
    ) from exc


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = REPOSITORY_ROOT / "novel" / "chapter04" / "section10"
OUTPUT_DIR = REPOSITORY_ROOT / "experience" / "chapter04" / "section10"
MEDIA_DIR = OUTPUT_DIR / "media"

READY_FILE = SOURCE_DIR / "LOCALIZATION_READY"
NOTES_FILE = SOURCE_DIR / "section10_production_notes.md"
TRAILER_FILE = SOURCE_DIR / "trailer" / "output" / "section10_trailer_final.mp4"

MEASUREMENT_ID = "G-L51VXQ23B6"
CONSENT_STORAGE_KEY = "memoriopolis_analytics_consent"


@dataclass(frozen=True)
class Locale:
    code: str
    label: str
    file_name: str
    page_title: str


LOCALES = (
    Locale("ja", "日本語", "section10_ja.md", "第十節「二つの信頼」"),
    Locale("en", "English", "section10_en.md", "Section Ten: Two Kinds of Trust"),
    Locale("zh-TW", "臺灣繁體中文", "section10_zh-TW.md", "第十節〈兩種信任〉"),
    Locale("ko", "한국어", "section10_ko.md", "제10절 「두 가지 신뢰」"),
    Locale("ru", "Русский", "section10_ru.md", "Раздел десятый. «Два вида доверия»"),
)

MARKDOWN_EXTENSIONS = ("extra", "sane_lists")
REQUIRED_OUTPUTS = (
    "index.html",
    "notes.html",
    "trailer.html",
    "script.js",
    "styles.css",
    "media/section10_trailer_final.mp4",
)


class BuildError(RuntimeError):
    """Raised when source or output validation fails."""


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise BuildError(f"File is not valid UTF-8: {path}") from exc


def validate_markdown_source(path: Path, locale: Locale) -> str:
    if not path.is_file():
        raise BuildError(f"Missing localized source: {path}")

    text = read_utf8(path)

    if len(text.strip()) < 500:
        raise BuildError(f"Localized source appears too short: {path}")

    heading_levels = set()

    for raw_line in text.splitlines():
        line = raw_line.lstrip("\ufeff").lstrip()

        if not line.startswith("#"):
            continue

        level = len(line) - len(line.lstrip("#"))

        if not 1 <= level <= 6:
            continue

        remainder = line[level:]

        if remainder and remainder[0].isspace() and remainder.strip():
            heading_levels.add(level)

    valid_heading_sets = (
        {3, 4, 5},
        {4, 5, 6},
    )

    if not any(required <= heading_levels for required in valid_heading_sets):
        found = ", ".join(str(level) for level in sorted(heading_levels))

        raise BuildError(
            f"Expected consecutive work/chapter/section headings "
            f"at levels 3/4/5 or 4/5/6: {path} "
            f"(found: {found or 'none'})"
        )

    if "\x00" in text:
        raise BuildError(f"NUL byte found in source: {path}")

    return text


def validate_sources() -> dict[str, str]:
    errors: list[str] = []
    sources: dict[str, str] = {}

    if not READY_FILE.is_file():
        errors.append(f"Missing readiness marker: {READY_FILE}")

    for locale in LOCALES:
        path = SOURCE_DIR / locale.file_name
        try:
            sources[locale.code] = validate_markdown_source(path, locale)
        except BuildError as exc:
            errors.append(str(exc))

    if not NOTES_FILE.is_file():
        errors.append(f"Missing production notes: {NOTES_FILE}")
    else:
        notes = read_utf8(NOTES_FILE)
        if len(notes.strip()) < 1000:
            errors.append(f"Production notes appear too short: {NOTES_FILE}")
        if "第五幕" not in notes or "私たち" not in notes:
            errors.append("Production notes do not contain the fifth-act anchor.")
        sources["notes"] = notes

    if not TRAILER_FILE.is_file():
        errors.append(f"Missing final trailer: {TRAILER_FILE}")
    elif TRAILER_FILE.stat().st_size == 0:
        errors.append(f"Final trailer is empty: {TRAILER_FILE}")
    elif TRAILER_FILE.suffix.lower() != ".mp4":
        errors.append(f"Final trailer must be MP4: {TRAILER_FILE}")

    if errors:
        raise BuildError("Source validation failed:\n- " + "\n- ".join(errors))
    return sources


def markdown_to_html(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=list(MARKDOWN_EXTENSIONS),
        output_format="html5",
    )


def strip_leading_headings(rendered: str, count: int = 3) -> str:
    result = rendered
    for _ in range(count):
        result = re.sub(r"^\s*<h[1-6][^>]*>.*?</h[1-6]>\s*", "", result, count=1, flags=re.DOTALL)
    return result.strip()


def document_head(title: str, description: str) -> str:
    return f'''<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(description, quote=True)}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{html.escape(title, quote=True)}">
  <meta property="og:description" content="{html.escape(description, quote=True)}">
  <meta property="og:url" content="https://netarott.github.io/MEMORIOPOLIS/chapter04/section10/">
  <meta name="twitter:card" content="summary">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="styles.css?v=20260829-1">
  <link rel="stylesheet" href="../../assets/css/analytics-consent.css?v=20260829-1">
  <script defer src="../../assets/js/analytics-consent.js?v=20260829-1"></script>
  <script defer src="script.js?v=20260829-1"></script>
</head>'''


def site_header(kicker: str, title: str, subtitle: str = "") -> str:
    subtitle_html = f'\n      <p class="page-subtitle">{html.escape(subtitle)}</p>' if subtitle else ""
    return f'''<header class="site-header">
  <div class="site-header__inner">
    <a class="home-link" href="../../">中央駅へ戻る</a>
    <p class="kicker">{html.escape(kicker)}</p>
    <h1>{html.escape(title)}</h1>{subtitle_html}
  </div>
</header>'''


def footer_html() -> str:
    return '''<footer class="site-footer">
  <p>GitHub上のMarkdownを正本とし、このページはBuildによって生成されています。</p>
  <nav aria-label="サイト情報">
    <a href="../../privacy.html">アクセス解析について</a>
    <button type="button" class="text-button" data-analytics-consent-open>解析設定を変更</button>
  </nav>
</footer>'''


def render_index(sources: dict[str, str]) -> str:
    buttons = []
    articles = []
    for index, locale in enumerate(LOCALES):
        pressed = "true" if index == 0 else "false"
        hidden = "" if index == 0 else " hidden"
        buttons.append(
            f'<button type="button" data-language-button="{locale.code}" '
            f'aria-pressed="{pressed}">{html.escape(locale.label)}</button>'
        )
        rendered = strip_leading_headings(markdown_to_html(sources[locale.code]))
        articles.append(
            f'<article class="story" lang="{locale.code}" data-language="{locale.code}"{hidden}>'
            f'<h2>{html.escape(locale.page_title)}</h2>\n{rendered}\n</article>'
        )

    title = "記憶都市（メモリオポリス）｜第四章 第十節「二つの信頼」"
    description = "疑うことと、確かめること。その間に生まれた、まだ名前のない空間を描く第十節。"
    return f'''<!doctype html>
<html lang="ja">
{document_head(title, description)}
<body data-page-kind="story">
{site_header("MEMORIOPOLIS / CHAPTER 04", "第十節「二つの信頼」", "Fourth Chapter / Section Ten")}
<main id="main-content" class="page-shell">
  <nav class="language-switcher" aria-label="表示言語">
    {' '.join(buttons)}
  </nav>
  <div id="story-start" class="story-stack">
    {''.join(articles)}
  </div>
  <nav class="section-navigation" aria-label="第十節の関連ページ">
    <a class="primary-link" href="notes.html" data-open-production-notes data-source="story">第五幕「私たち」と書かなかった場所へ</a>
    <a href="trailer.html">21秒の予告編を見る</a>
    <a href="../../">中央駅へ戻る</a>
  </nav>
</main>
{footer_html()}
<noscript><p class="noscript-note">JavaScriptが無効なため、日本語版を表示しています。アクセス解析は行われません。</p></noscript>
</body>
</html>
'''


def annotate_notes_languages(rendered: str) -> str:
    markers = {
        "To suspect. To verify.": "en",
        "那塊空間": "zh-TW",
        "확인할 수 있는지를 묻는 거예요": "ko",
        "В том, как мы доверяем": "ru",
    }
    for marker, language in markers.items():
        escaped = html.escape(marker)
        pattern = rf"(<blockquote)(?![^>]*\blang=)([^>]*>.*?{re.escape(escaped)}.*?</blockquote>)"
        rendered = re.sub(pattern, rf'\1 lang="{language}"\2', rendered, count=1, flags=re.DOTALL)
    return rendered


def render_notes(sources: dict[str, str]) -> str:
    notes = markdown_to_html(sources["notes"])
    notes = strip_leading_headings(notes, count=2)
    notes = annotate_notes_languages(notes)
    title = "第五幕「私たち」と書かなかった場所」｜記憶都市"
    description = "四つの言語の反射と、日本語正本を変更しなかった第四回Returnを記録する第五幕。"
    return f'''<!doctype html>
<html lang="ja">
{document_head(title, description)}
<body data-page-kind="notes">
{site_header("MEMORIOPOLIS / FIFTH ACT", "「私たち」と書かなかった場所", "第四章 第十節 制作ノート")}
<main id="main-content" class="page-shell notes-page">
  <article class="notes-body">
{notes}
  </article>
  <nav class="section-navigation" aria-label="第十節の関連ページ">
    <a class="primary-link" href="./">第十節「二つの信頼」へ戻る</a>
    <a href="trailer.html">21秒の予告編を見る</a>
    <a href="../../">中央駅へ戻る</a>
  </nav>
</main>
{footer_html()}
</body>
</html>
'''


def render_trailer() -> str:
    title = "第十節「二つの信頼」予告編｜記憶都市"
    description = "五つの言語の反射を21秒の縦型映像にした、第十節「二つの信頼」の予告編。"
    transcript = '''<p>いつもの名前。<br>いつもの言葉。<br>いつもの朝。</p>
<p>これが本人のメッセージだという根拠は？</p>
<p>疑うこと。<br>確かめること。</p>
<p>二つの答えのあいだに、<br>まだ名前のない空間ができた。</p>
<p lang="en">To verify.</p>
<p lang="zh-TW">不急著決定。</p>
<p lang="ko">확인할 수 있는지</p>
<p lang="ru">как мы доверяем</p>
<p>記憶都市（メモリオポリス）<br>第四章 第十節<br>「二つの信頼」</p>'''
    return f'''<!doctype html>
<html lang="ja">
{document_head(title, description)}
<body data-page-kind="trailer">
{site_header("MEMORIOPOLIS / TRAILER", "第十節「二つの信頼」", "21-second vertical trailer")}
<main id="main-content" class="page-shell trailer-page">
  <div class="video-frame">
    <video id="section10-trailer" class="trailer-video" controls playsinline preload="metadata">
      <source src="media/section10_trailer_final.mp4" type="video/mp4">
      お使いのブラウザは動画再生に対応していません。
    </video>
  </div>
  <p class="trailer-description">五つの言語の反射を、21秒の縦型映像にしました。再生は読者の操作で始まります。</p>
  <details class="transcript">
    <summary>予告編の字幕を読む</summary>
    <div class="transcript__body">{transcript}</div>
  </details>
  <nav class="section-navigation" aria-label="第十節の関連ページ">
    <a class="primary-link" href="./">第十節「二つの信頼」を読む</a>
    <a href="notes.html" data-open-production-notes data-source="trailer">第五幕へ</a>
    <a href="../../">中央駅へ戻る</a>
  </nav>
</main>
{footer_html()}
</body>
</html>
'''


STYLES_CSS = r''':root {
  color-scheme: dark;
  --page: #03080d;
  --panel: rgba(7, 19, 27, .82);
  --paper: #e8eef0;
  --muted: #aebbc0;
  --cyan: #9fe8ee;
  --line: rgba(159, 232, 238, .28);
  --shadow: rgba(0, 0, 0, .45);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  min-height: 100vh;
  margin: 0;
  color: var(--paper);
  background:
    radial-gradient(circle at 72% 8%, rgba(30, 91, 104, .18), transparent 30rem),
    radial-gradient(circle at 18% 72%, rgba(22, 60, 79, .15), transparent 36rem),
    var(--page);
  font-family: system-ui, -apple-system, "Segoe UI", "Noto Sans JP", sans-serif;
}
a { color: #c9f1f3; text-underline-offset: .2em; }
a:hover, a:focus-visible { color: #fff; }
button { font: inherit; }

.site-header, .site-footer, .page-shell { width: min(68rem, 88vw); margin-inline: auto; }
.site-header { padding: 9vh 0 3rem; border-bottom: 1px solid var(--line); }
.site-header__inner { position: relative; }
.home-link { display: inline-block; margin-bottom: 2.4rem; color: var(--muted); }
.kicker { margin: 0 0 .75rem; color: var(--cyan); font-size: .72rem; letter-spacing: .19em; }
h1 { margin: 0; font-family: "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif JP", serif; font-size: clamp(2rem, 6vw, 4.2rem); font-weight: 500; line-height: 1.35; }
.page-subtitle { margin: 1rem 0 0; color: var(--muted); letter-spacing: .06em; }
.page-shell { padding: 3rem 0 7rem; }

.language-switcher { display: flex; flex-wrap: wrap; gap: .6rem; margin-bottom: 3rem; }
.language-switcher button {
  border: 1px solid var(--line); border-radius: 999px; padding: .65rem .9rem;
  color: var(--paper); background: rgba(5, 18, 25, .74); cursor: pointer;
}
.language-switcher button[aria-pressed="true"] { color: #031015; background: var(--cyan); border-color: var(--cyan); }
.language-switcher button:focus-visible { outline: 2px solid #fff; outline-offset: 2px; }

.story-stack { max-width: 54rem; margin-inline: auto; }
.story[hidden] { display: none; }
.story h2 { margin: 0 0 3rem; color: var(--cyan); font-size: clamp(1.45rem, 3vw, 2.1rem); font-weight: 500; }
.story p, .notes-body p, .notes-body li { font-family: "Yu Mincho", "Hiragino Mincho ProN", "Noto Serif JP", serif; font-size: clamp(1rem, 1.6vw, 1.16rem); line-height: 2.08; }
.story p { margin: 0 0 1.1rem; }
.story[lang="en"] p, .story[lang="ru"] p { font-family: Georgia, "Times New Roman", serif; line-height: 1.9; }
.story[lang="ko"] p { font-family: "Malgun Gothic", "Noto Sans KR", sans-serif; line-height: 2; }
.story[lang="zh-TW"] p { font-family: "Noto Serif TC", "Microsoft JhengHei", serif; line-height: 2; }

.notes-page { max-width: 58rem; }
.notes-body h1 { margin-top: 0; font-size: clamp(1.8rem, 4vw, 2.8rem); }
.notes-body h2 { margin: 4rem 0 1.4rem; color: var(--cyan); font-size: clamp(1.35rem, 3vw, 1.9rem); }
.notes-body h3 { margin-top: 2.5rem; }
.notes-body blockquote { margin: 2rem 0; padding: 1rem 1.3rem; border-left: 2px solid var(--cyan); background: var(--panel); }
.notes-body pre { overflow-x: auto; padding: 1rem; border: 1px solid var(--line); background: rgba(0, 0, 0, .35); }
.notes-body code { color: #c9f1f3; }
.notes-body hr { margin: 4rem 0; border: 0; border-top: 1px solid var(--line); }

.trailer-page { text-align: center; }
.video-frame { display: grid; place-items: center; }
.trailer-video { display: block; width: min(100%, 27rem); max-height: 78vh; aspect-ratio: 9 / 16; background: #000; box-shadow: 0 1.2rem 4rem var(--shadow); }
.trailer-description { max-width: 38rem; margin: 1.5rem auto; color: var(--muted); line-height: 1.8; }
.transcript { width: min(42rem, 100%); margin: 2rem auto; text-align: left; border: 1px solid var(--line); border-radius: 1rem; background: var(--panel); }
.transcript summary { padding: 1rem 1.2rem; cursor: pointer; color: #dff9fa; }
.transcript__body { padding: 0 1.2rem 1.2rem; line-height: 1.8; }

.section-navigation { display: flex; flex-wrap: wrap; gap: .8rem; justify-content: center; margin-top: 5rem; padding-top: 2rem; border-top: 1px solid var(--line); }
.section-navigation a { padding: .75rem 1rem; border: 1px solid var(--line); border-radius: 999px; text-decoration: none; background: rgba(5, 18, 25, .72); }
.section-navigation .primary-link { color: #031015; background: var(--cyan); border-color: var(--cyan); }
.site-footer { padding: 2rem 0 4rem; border-top: 1px solid var(--line); color: var(--muted); font-size: .82rem; line-height: 1.8; }
.site-footer nav { display: flex; flex-wrap: wrap; gap: .7rem 1rem; }
.text-button { border: 0; padding: 0; color: #c9f1f3; background: none; cursor: pointer; text-decoration: underline; text-underline-offset: .2em; }
.noscript-note { margin: 1rem; padding: 1rem; border: 1px solid var(--line); background: var(--panel); }

@media (max-width: 640px) {
  .site-header, .site-footer, .page-shell { width: min(92vw, 68rem); }
  .site-header { padding-top: 5rem; }
  .language-switcher { gap: .45rem; }
  .language-switcher button { flex: 1 1 auto; padding: .6rem .7rem; }
  .section-navigation { display: grid; }
  .section-navigation a { text-align: center; }
  .story p, .notes-body p, .notes-body li { line-height: 1.95; }
}
'''


SCRIPT_JS = rf'''(() => {{
  'use strict';

  const VALID_LANGUAGES = ['ja', 'en', 'zh-TW', 'ko', 'ru'];
  const CONSENT_KEY = '{CONSENT_STORAGE_KEY}';
  let currentLanguage = 'ja';
  let trailerPlaySent = false;

  function analyticsReady() {{
    try {{
      return localStorage.getItem(CONSENT_KEY) === 'granted' && typeof window.gtag === 'function';
    }} catch (error) {{
      return false;
    }}
  }}

  function sendEvent(name, parameters) {{
    if (!analyticsReady()) return;
    window.gtag('event', name, parameters);
  }}

  function languageFromHash() {{
    const value = decodeURIComponent(location.hash.replace(/^#/, ''));
    return VALID_LANGUAGES.includes(value) ? value : 'ja';
  }}

  function showLanguage(language, userInitiated = false) {{
    if (!VALID_LANGUAGES.includes(language)) return;
    const previous = currentLanguage;
    document.querySelectorAll('[data-language]').forEach((article) => {{
      article.hidden = article.dataset.language !== language;
    }});
    document.querySelectorAll('[data-language-button]').forEach((button) => {{
      button.setAttribute('aria-pressed', String(button.dataset.languageButton === language));
    }});
    document.documentElement.lang = language;
    currentLanguage = language;

    if (location.hash !== `#${{language}}`) history.replaceState(null, '', `#${{language}}`);
    if (userInitiated && previous !== language) {{
      sendEvent('language_switch', {{
        section_id: 'section10',
        from_language: previous,
        to_language: language
      }});
      document.getElementById('story-start')?.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
  }}

  function initializeLanguageSwitcher() {{
    if (!document.querySelector('[data-language-button]')) return;
    currentLanguage = languageFromHash();
    showLanguage(currentLanguage, false);
    document.querySelectorAll('[data-language-button]').forEach((button) => {{
      button.addEventListener('click', () => showLanguage(button.dataset.languageButton, true));
    }});
    window.addEventListener('hashchange', () => showLanguage(languageFromHash(), false));
  }}

  function initializeNotesLinks() {{
    document.querySelectorAll('[data-open-production-notes]').forEach((link) => {{
      link.addEventListener('click', () => {{
        sendEvent('open_production_notes', {{
          section_id: 'section10',
          source: link.dataset.source || 'unknown'
        }});
      }});
    }});
  }}

  function initializeTrailer() {{
    const video = document.getElementById('section10-trailer');
    if (!video) return;
    video.addEventListener('play', () => {{
      if (trailerPlaySent) return;
      trailerPlaySent = true;
      sendEvent('trailer_play', {{
        section_id: 'section10',
        trailer_id: 'section10_trailer_final'
      }});
    }});
  }}

  function initialize() {{
    initializeLanguageSwitcher();
    initializeNotesLinks();
    initializeTrailer();
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', initialize, {{ once: true }});
  }} else {{
    initialize();
  }}
}})();
'''


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build(sources: dict[str, str]) -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)

    write_text(OUTPUT_DIR / "index.html", render_index(sources))
    write_text(OUTPUT_DIR / "notes.html", render_notes(sources))
    write_text(OUTPUT_DIR / "trailer.html", render_trailer())
    write_text(OUTPUT_DIR / "styles.css", STYLES_CSS)
    write_text(OUTPUT_DIR / "script.js", SCRIPT_JS)
    shutil.copy2(TRAILER_FILE, MEDIA_DIR / TRAILER_FILE.name)


def validate_outputs() -> None:
    errors: list[str] = []
    for relative in REQUIRED_OUTPUTS:
        path = OUTPUT_DIR / relative
        if not path.is_file():
            errors.append(f"Missing output: {path}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty output: {path}")

    if errors:
        raise BuildError("Output validation failed:\n- " + "\n- ".join(errors))

    index = read_utf8(OUTPUT_DIR / "index.html")
    notes = read_utf8(OUTPUT_DIR / "notes.html")
    trailer = read_utf8(OUTPUT_DIR / "trailer.html")
    script = read_utf8(OUTPUT_DIR / "script.js")

    assertions = {
        "five localized articles": all(f'data-language="{locale.code}"' in index for locale in LOCALES),
        "five language buttons": all(f'data-language-button="{locale.code}"' in index for locale in LOCALES),
        "notes navigation": 'href="notes.html"' in index,
        "trailer navigation": 'href="trailer.html"' in index,
        "fifth act": "私たち" in notes and "第五幕" in notes,
        "video source": 'media/section10_trailer_final.mp4' in trailer,
        "no autoplay": "autoplay" not in trailer,
        "inline playback": "playsinline" in trailer,
        "transcript languages": all(f'lang="{code}"' in trailer for code in ("en", "zh-TW", "ko", "ru")),
        "consent key": CONSENT_STORAGE_KEY in script,
        "analytics events": all(name in script for name in ("language_switch", "open_production_notes", "trailer_play")),
        "measurement not duplicated": MEASUREMENT_ID not in script,
    }
    failed = [name for name, passed in assertions.items() if not passed]
    if failed:
        raise BuildError("Generated output consistency checks failed:\n- " + "\n- ".join(failed))


def print_summary(check_only: bool) -> None:
    mode = "CHECK" if check_only else "BUILD"
    print(f"[{mode}] Section 10")
    print(f"Repository: {REPOSITORY_ROOT}")
    print(f"Source:     {SOURCE_DIR}")
    if not check_only:
        print(f"Output:     {OUTPUT_DIR}")
        for relative in REQUIRED_OUTPUTS:
            path = OUTPUT_DIR / relative
            print(f"  {relative:<48} {path.stat().st_size:>10,} bytes")
    print(f"Checked languages: {len(LOCALES)}; errors: 0")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build MEMORIOPOLIS chapter 4, section 10.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate source files only; do not modify experience outputs.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        sources = validate_sources()
        if not args.check:
            build(sources)
            validate_outputs()
        print_summary(args.check)
    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
