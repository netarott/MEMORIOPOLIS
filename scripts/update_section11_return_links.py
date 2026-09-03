#!/usr/bin/env python3
from __future__ import annotations
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / "experience" / "chapter04" / "section11"

def update(path: Path, pattern: str, replacement: str) -> None:
    text = path.read_text(encoding="utf-8")
    if replacement in text:
        print(f"[SKIP] already updated: {path}")
        return
    match = re.search(pattern, text, flags=re.S)
    if not match:
        raise SystemExit(f"Target navigation not found: {path}")
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(path, path.with_name(path.name + f".{stamp}.bak"))
    text = text[:match.start()] + replacement + text[match.end():]
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"[OK] {path}")

def main() -> None:
    act5 = SECTION / "act5.html"
    story = SECTION / "story.html"
    if not act5.exists() or not story.exists():
        raise SystemExit("Generate act5.html and story.html before updating links.")
    act5_nav = '''<nav class="act-navigation" aria-label="第五幕の関連ページ">
<a class="primary-link" href="return04.html">第四回Returnの完全記録を読む</a>
<a href="story.html">小説本編を読み返す</a>
<a href="index.html">デジタル絵巻を読み返す</a>
<a href="trailer.html">20秒の予告編を見る</a>
<a href="../../">中央駅へ戻る</a>
</nav>'''
    story_nav = '''<nav class="story-navigation" aria-label="本編の関連ページ">
    <a class="primary-link" href="act5.html">第五幕「継ぎ目は空白ではない」を読む</a>
    <a href="return04.html">第四回Returnを読む</a>
    <a href="index.html">デジタル絵巻を体験する</a>
    <a href="trailer.html">20秒の予告編を見る</a>
    <a href="../../">中央駅へ戻る</a>
  </nav>'''
    update(act5, r'<nav class="act-navigation".*?</nav>', act5_nav)
    update(story, r'<nav class="story-navigation".*?</nav>', story_nav)

if __name__ == "__main__":
    main()
