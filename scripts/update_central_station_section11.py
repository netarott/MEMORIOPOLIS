#!/usr/bin/env python3
from __future__ import annotations
import re, shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/'experience'/'index.html'
SECTION=ROOT/'experience'/'chapter04'/'section11'
REQUIRED=['index.html','story.html','trailer.html','act5.html','return04.html']
SECTION11='''<section class="station station-featured" aria-labelledby="section11-title">
      <p class="eyebrow">NEW PLATFORM / DIGITAL EMAKI</p>
      <h2 id="section11-title">第四章 第十一節</h2>
      <p>「説明の継ぎ目」<span class="format-label">横スクロール式デジタル絵巻</span></p>
      <div class="station-actions">
        <a class="enter enter-primary" href="chapter04/section11/">絵巻をひらく</a>
        <a class="enter" href="chapter04/section11/story.html">本編を読む</a>
        <a class="enter enter-secondary" href="chapter04/section11/trailer.html">20秒の予告編</a>
      </div>
    </section>'''
ACT5='''<section class="station station-act5" aria-labelledby="act5-title">
      <p class="eyebrow">ACT V / MULTILINGUAL RETURN</p>
      <h2 id="act5-title">第五幕</h2>
      <p class="act5-name">「継ぎ目は空白ではない」</p>
      <p class="act5-english" lang="en">The Seam Is Not Empty</p>
      <p class="act5-description">五つの言語が、同じ物語の中に何を残し、何をずらしたのかを読む。</p>
      <div class="station-actions"><a class="enter enter-act5" href="chapter04/section11/act5.html">第五幕をひらく</a></div>
      <p class="record-link">制作記録：<a href="chapter04/section11/return04.html">第四回Returnを読む</a></p>
    </section>'''
CSS='''    /* ACT V PLATFORM START */
    .station-act5{position:relative;margin-top:5.5rem;padding:2.4rem clamp(1rem,3vw,2.2rem);border:1px solid rgba(218,202,161,.30);border-left-color:rgba(145,220,227,.46);background:linear-gradient(118deg,rgba(22,19,13,.78),rgba(9,27,35,.62))}
    .station-act5::before{content:"";position:absolute;top:-2.8rem;left:10%;width:43%;height:1px;background:linear-gradient(90deg,transparent,rgba(218,202,161,.52),transparent)}
    .station-act5 .act5-name{margin-bottom:.5rem;color:#ece6d6;font-family:"BIZ UDPMincho","BIZ UDMincho","Yu Mincho","Noto Serif JP",serif;font-size:clamp(1.1rem,2.2vw,1.55rem)}
    .act5-english{margin-bottom:1.5rem!important;color:#cfc5a9!important;font-family:Georgia,"Times New Roman",serif;font-size:1rem;letter-spacing:.045em}
    .act5-description{max-width:42rem;color:#cbd5d4!important;font-family:"BIZ UDPMincho","BIZ UDMincho","Yu Mincho","Noto Serif JP",serif}
    .enter-act5{color:#16130c;background:#ddd1b0;border-color:#ddd1b0}.enter-act5:hover,.enter-act5:focus-visible{color:#16130c;outline-color:#f1e6c8}
    .record-link{margin:1.5rem 0 0!important;color:#929fa1!important;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:.82rem}.record-link a{color:#b9dcde;text-underline-offset:.2em}
    /* ACT V PLATFORM END */
'''
def validate_files():
    if not INDEX.exists(): raise SystemExit(f'Not found: {INDEX}')
    missing=[str(SECTION/n) for n in REQUIRED if not (SECTION/n).exists()]
    if missing: raise SystemExit('Missing destinations:\n  '+'\n  '.join(missing))
def replace_one(text,pattern,replacement,label):
    matches=list(re.finditer(pattern,text,re.S))
    if len(matches)!=1: raise SystemExit(f'Expected one {label} block, found {len(matches)}')
    m=matches[0]; return text[:m.start()]+replacement+text[m.end():]
def main():
    validate_files(); original=INDEX.read_text(encoding='utf-8-sig')
    text=replace_one(original,r'<section\b[^>]*aria-labelledby="section11-title"[^>]*>.*?</section>',SECTION11,'Section 11')
    act_pattern=r'<section\b[^>]*aria-labelledby="act5-title"[^>]*>.*?</section>'
    act_matches=list(re.finditer(act_pattern,text,re.S))
    if len(act_matches)>1: raise SystemExit('Act V platform is duplicated')
    if act_matches:
        m=act_matches[0]; text=text[:m.start()]+ACT5+text[m.end():]
    else:
        pos=text.find(SECTION11)+len(SECTION11)
        if pos<len(SECTION11): raise SystemExit('Updated Section 11 block not found')
        text=text[:pos]+'\n\n    '+ACT5+text[pos:]
    marked=re.compile(r'    /\* ACT V PLATFORM START \*/.*?    /\* ACT V PLATFORM END \*/\n?',re.S)
    if marked.search(text): text=marked.sub(CSS,text,count=1)
    else:
        pos=text.find('</style>')
        if pos<0: raise SystemExit('Closing style tag not found')
        text=text[:pos]+CSS+'  '+text[pos:]
    needles=['chapter04/section11/','chapter04/section11/story.html','chapter04/section11/trailer.html','chapter04/section11/act5.html','chapter04/section11/return04.html']
    missing=[x for x in needles if x not in text]
    if missing: raise SystemExit('Validation failed: '+', '.join(missing))
    if text.count('aria-labelledby="section11-title"')!=1 or text.count('aria-labelledby="act5-title"')!=1: raise SystemExit('Platform duplication detected')
    if text==original: print('[SKIP] Central Station is already current.'); return
    stamp=datetime.now().strftime('%Y%m%d-%H%M%S'); backup=INDEX.with_name(f'index.html.{stamp}.bak'); shutil.copy2(INDEX,backup)
    INDEX.write_text(text,encoding='utf-8',newline='\n')
    print(f'[OK] Updated: {INDEX}'); print(f'[OK] Backup: {backup}'); print('[OK] Verified: emaki, story, trailer, Act V, Return 04')
if __name__=='__main__': main()
