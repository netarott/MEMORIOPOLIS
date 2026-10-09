# MEMORIOPOLIS 韓国語 Anki UI 完全版

更新日：2026-10-09  
対象：Core10 / Core20 / Core30  
フィールド数：14  
設計：音優先、ConceptScene、3段パネル、AnkiDroid対応

## 正式14フィールド

```text
1. ID
2. Korean
3. Romanization
4. Japanese
5. PartOfSpeech
6. ExampleKorean
7. ExampleRomanization
8. ExampleJapanese
9. Source
10. Tags
11. ExampleBreakdown
12. ExampleExplanation
13. ExamplePronunciationHint
14. ConceptScene
```

## 表面テンプレート

```html
<div class="card-shell korean-shell">
  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">한국어 · KOREAN</span>
  </div>

  <section class="sound-gate">
    <div class="sound-kicker">먼저 들어 보세요</div>
    <div class="sound-instruction">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-audio word-audio">{{tts ko_KR:Korean}}</div>
  </section>

  {{#ConceptScene}}<div class="concept-scene">{{ConceptScene}}</div>{{/ConceptScene}}

  <section class="word-panel">
    <div class="target-word ko-text">{{Korean}}</div>
    {{#Romanization}}<div class="romanization">{{Romanization}}</div>{{/Romanization}}
  </section>
</div>
```

## 裏面テンプレート

```html
{{FrontSide}}

<div id="answer" class="answer-divider"><span>CONCEPT BRIDGE</span></div>

<div class="answer-shell">
  <section class="core-answer">
    <div class="info-kicker">日本語Concept</div>
    <div class="japanese-answer">{{Japanese}}</div>
    {{#PartOfSpeech}}<div class="pos-badge">{{PartOfSpeech}}</div>{{/PartOfSpeech}}
  </section>

  {{#ExampleKorean}}
  <section class="example-card">
    <div class="section-kicker">예문을 들어 보세요</div>
    <div class="sound-instruction">例文の音から、見出し語と文意を探す</div>
    <div class="tts-audio example-audio">{{tts ko_KR:ExampleKorean}}</div>
    <div class="example-target ko-text">{{ExampleKorean}}</div>
    {{#ExampleJapanese}}<div class="example-japanese">{{ExampleJapanese}}</div>{{/ExampleJapanese}}
  </section>
  {{/ExampleKorean}}

  <details class="detail-block structure-block">
    <summary><span class="summary-icon">◆</span><span>낱말의 구조 · 語の構造</span></summary>
    <div class="detail-content">
      <div class="detail-group"><div class="detail-label">見出し語</div><div class="detail-text structure-word ko-text">{{Korean}}</div></div>
      {{#Romanization}}<div class="detail-group"><div class="detail-label">ローマ字</div><div class="detail-text romanization-detail">{{Romanization}}</div></div>{{/Romanization}}
      {{#ExamplePronunciationHint}}<div class="detail-group pronunciation-group"><div class="detail-label">実際の聞こえ方・音韻変化</div><div class="detail-text japanese-text">{{ExamplePronunciationHint}}</div></div>{{/ExamplePronunciationHint}}
    </div>
  </details>

  <details class="detail-block explanation-block">
    <summary><span class="summary-icon">◆</span><span>예문 해설 · 例文解説</span></summary>
    <div class="detail-content">
      {{#ExampleRomanization}}<div class="detail-group"><div class="detail-label">例文ローマ字</div><div class="detail-text example-romanization">{{ExampleRomanization}}</div></div>{{/ExampleRomanization}}
      {{#ExampleBreakdown}}<div class="detail-group"><div class="detail-label">文の組み立て</div><div class="detail-text japanese-text breakdown-text">{{ExampleBreakdown}}</div></div>{{/ExampleBreakdown}}
      {{#ExampleExplanation}}<div class="detail-group"><div class="detail-label">なぜこの意味になる？</div><div class="detail-text japanese-text">{{ExampleExplanation}}</div></div>{{/ExampleExplanation}}
    </div>
  </details>

  <details class="detail-block bridge-block">
    <summary><span class="summary-icon">◆</span><span>언어의 다리 · 言語間ブリッジ</span></summary>
    <div class="detail-content">
      {{#ExamplePronunciationHint}}<div class="detail-group sound-bridge"><div class="detail-label">音の橋</div><div class="detail-text japanese-text">{{ExamplePronunciationHint}}</div></div>{{/ExamplePronunciationHint}}
      <div class="detail-group"><div class="detail-label">記憶都市の住所</div><div class="detail-text japanese-text bridge-note">音、ConceptScene、日本語Concept、ハングル、語形、例文を同じConcept IDへ接続して観測する。</div></div>
    </div>
  </details>

  {{#Source}}<div class="source-line"><span class="source-label">SOURCE</span><span>{{Source}}</span></div>{{/Source}}
</div>
```

## CSS

```css
:root {
  --page:#edf2f7; --card:#fffdf8; --ink:#10283c; --soft:#617083;
  --line:#d7e1eb; --red:#b54f55; --red-deep:#81353b; --blue:#315f93;
  --gold:#c3922d; --violet-bg:#f1ebf8; --violet:#57416e;
  --blue-bg:#e8f1fb; --green-bg:#e8f4ed; --green:#286044;
  --shadow:0 12px 30px rgba(22,43,64,.12);
}
html,body,.card{width:100%;margin:0;text-align:center}
.card{box-sizing:border-box;padding:18px 12px 30px;color:var(--ink);background:radial-gradient(circle at 50% -10%,rgba(181,79,85,.12),transparent 34%),linear-gradient(180deg,#eef3f8,var(--page));font-family:"Noto Sans KR","Malgun Gothic","Apple SD Gothic Neo","Segoe UI",sans-serif;font-size:18px;line-height:1.65;overflow-wrap:anywhere}
.card-shell,.answer-shell{box-sizing:border-box;width:100%;max-width:760px;margin:0 auto}
.card-shell{position:relative;padding:18px;background:var(--card);border:1px solid rgba(49,95,147,.15);border-radius:20px;box-shadow:var(--shadow);overflow:hidden}
.card-shell:before{content:"";position:absolute;left:0;right:0;top:0;height:8px;background:linear-gradient(90deg,var(--red) 0 42%,#f5f5f3 42% 58%,var(--blue) 58% 100%)}
.topline{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:8px 0 16px}.concept-id{color:var(--gold);font-size:.84rem;font-weight:900;letter-spacing:.15em}.language-chip{padding:5px 13px;color:#fff;background:linear-gradient(135deg,var(--red),var(--red-deep));border-radius:999px;font-size:.72rem;font-weight:900;letter-spacing:.08em;box-shadow:0 5px 14px rgba(129,53,59,.25)}
.sound-gate{padding:18px 15px;background:linear-gradient(145deg,#fff4f3,#f2f7fc);border:1px solid rgba(181,79,85,.25);border-radius:16px}.sound-kicker,.section-kicker,.info-kicker{color:var(--gold);font-size:.7rem;font-weight:900;letter-spacing:.13em;text-transform:uppercase}.sound-instruction{margin-top:5px;color:var(--soft);font-size:.9rem}.tts-audio{margin:10px auto 0}.replay-button svg{width:34px;height:34px}
.concept-scene{margin:18px auto;text-align:center}.concept-scene img{display:block;width:auto;max-width:100%;max-height:400px;height:auto;object-fit:contain;margin:0 auto;border:1px solid rgba(195,146,45,.28);border-radius:14px;box-shadow:0 9px 24px rgba(16,40,60,.16)}
.word-panel{padding:17px 14px 12px;background:linear-gradient(145deg,#fff,#fff5f4);border:1px solid var(--line);border-radius:15px}.target-word,.structure-word,.example-target{font-family:"Noto Serif KR","Batang",serif;color:var(--ink);font-weight:750}.target-word{font-size:clamp(2.4rem,10vw,4rem);line-height:1.18;letter-spacing:.03em}.romanization{margin-top:7px;color:var(--soft);font-size:.96rem;letter-spacing:.035em}
.answer-divider{display:flex;align-items:center;gap:12px;max-width:760px;margin:20px auto 14px;color:var(--gold);font-size:.68rem;font-weight:900;letter-spacing:.17em}.answer-divider:before,.answer-divider:after{content:"";flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.core-answer,.example-card{padding:18px;background:var(--card);border:1px solid var(--line);border-radius:16px;box-shadow:0 6px 18px rgba(22,43,64,.08)}.core-answer{margin-bottom:14px}.japanese-answer{margin-top:4px;font-size:1.7rem;font-weight:900}.pos-badge{display:inline-block;margin-top:8px;padding:4px 12px;color:var(--red-deep);background:#f9e8e7;border-radius:999px;font-size:.8rem;font-weight:800}
.example-card{margin-bottom:13px;border-left:5px solid var(--gold)}.example-target{margin-top:13px;font-size:1.38rem;line-height:1.8}.example-japanese{margin-top:13px;padding-top:12px;border-top:1px dashed var(--line);font-size:.96rem}
.detail-block{margin:11px 0 0;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;text-align:left;box-shadow:0 4px 14px rgba(22,43,64,.06)}.detail-block summary{display:flex;align-items:center;justify-content:center;gap:9px;padding:14px 15px;cursor:pointer;font-weight:900;list-style:none}.detail-block summary::-webkit-details-marker{display:none}.summary-icon{font-size:.66rem;transition:transform .2s}.detail-block[open] .summary-icon{transform:rotate(45deg)}.structure-block summary{color:var(--violet);background:var(--violet-bg)}.explanation-block summary{color:#1d568a;background:var(--blue-bg)}.bridge-block summary{color:var(--green);background:var(--green-bg)}
.detail-content{padding:4px 16px 16px}.detail-group{margin-top:13px;padding:12px 13px;background:rgba(255,255,255,.7);border:1px solid rgba(215,225,235,.9);border-radius:11px}.detail-label{margin-bottom:5px;color:var(--soft);font-size:.73rem;font-weight:900;letter-spacing:.07em}.structure-word{font-size:1.75rem;text-align:center}.romanization-detail,.example-romanization{color:var(--blue);font-size:.94rem}.breakdown-text{line-height:1.9;white-space:pre-line}.sound-bridge{border-left:4px solid var(--blue)}.bridge-note{padding-left:10px;border-left:3px solid var(--green)}.source-line{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;margin-top:16px;color:#818b97;font-size:.73rem}.source-label{color:var(--gold);font-weight:900;letter-spacing:.1em}
.nightMode.card,.night_mode.card{--page:#101820;--card:#1a2530;--ink:#f3f7fa;--soft:#b9c6d2;--line:#3b4b5b;--gold:#e3bd65;--violet-bg:#40364c;--violet:#f1e5ff;--blue-bg:#243e55;--green-bg:#284238;--green:#dff5e5;--shadow:0 12px 30px rgba(0,0,0,.35);background:radial-gradient(circle at 50% -10%,rgba(181,79,85,.12),transparent 34%),linear-gradient(180deg,#15212b,var(--page));color:var(--ink)}
.nightMode .card-shell,.night_mode .card-shell,.nightMode .core-answer,.night_mode .core-answer,.nightMode .example-card,.night_mode .example-card,.nightMode .detail-block,.night_mode .detail-block{background:var(--card);color:var(--ink);border-color:var(--line)}.nightMode .word-panel,.night_mode .word-panel{background:linear-gradient(145deg,#202d38,#2a2225);border-color:var(--line)}.nightMode .sound-gate,.night_mode .sound-gate{background:linear-gradient(145deg,#2b2326,#1f303f);border-color:#64434a}.nightMode .target-word,.night_mode .target-word,.nightMode .structure-word,.night_mode .structure-word,.nightMode .example-target,.night_mode .example-target,.nightMode .japanese-answer,.night_mode .japanese-answer,.nightMode .detail-text,.night_mode .detail-text{color:var(--ink)}.nightMode .detail-group,.night_mode .detail-group{background:rgba(255,255,255,.035);border-color:var(--line)}.nightMode .pos-badge,.night_mode .pos-badge{color:#ffe9e8;background:#56373a}
@media(max-width:600px){.card{padding:10px 7px 22px;font-size:16px}.card-shell{padding:13px;border-radius:16px}.sound-gate{padding:15px 10px}.concept-scene img{max-height:320px}.target-word{font-size:clamp(2.3rem,14vw,3.35rem)}.example-target{font-size:1.2rem}.detail-content{padding:3px 10px 12px}.detail-group{padding:10px}}

```

## 適用方法

1. 表面テンプレートを全置換する。
2. 裏面テンプレートを全置換する。
3. CSSを全置換する。
4. `id="answer"`を削除しない。
5. C0001、C0020、C0030をプレビューする。
6. AnkiWebで復習メニューを再構築し、AnkiDroidへ同期する。
