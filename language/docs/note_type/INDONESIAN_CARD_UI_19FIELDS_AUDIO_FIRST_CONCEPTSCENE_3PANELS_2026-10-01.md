# MEMORIOPOLIS インドネシア語 Anki UI 完全版

更新日：2026-10-01  
言語識別子：`id`  
対象デッキ：`MEMORIOPOLIS::Indonesian`  
設計：`音 → Concept想起 → 図 → 単語 → 例文音声`

## 正式19フィールド

```text
1. ID
2. Indonesian
3. Pronunciation
4. Japanese
5. PartOfSpeech
6. UsageNote
7. ExampleIndonesian
8. ExampleJapanese
9. Root
10. Affixes
11. PerceptualSegmentation
12. MorphologicalBreakdown
13. ExampleBreakdown
14. ExampleExplanation
15. MeaningBridge
16. SoundBridge
17. Source
18. CourseTags
19. ConceptScene
```

## 表面テンプレート

```html
<div class="card-shell">
  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">INDONESIA</span>
  </div>

  <div class="sound-gate">
    <div class="sound-kicker">DENGARKAN DULU</div>
    <div class="sound-instruction">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-audio word-audio">
      {{tts id_ID:Indonesian}}
    </div>
  </div>

  {{#ConceptScene}}
  <div class="concept-scene">{{ConceptScene}}</div>
  {{/ConceptScene}}

  <div class="word-panel">
    <div class="target-word id-text">{{Indonesian}}</div>
    {{#Pronunciation}}
    <div class="pronunciation">{{Pronunciation}}</div>
    {{/Pronunciation}}
  </div>
</div>
```

## 裏面テンプレート

```html
{{FrontSide}}

<div id="answer" class="answer-divider">
  <span>CONCEPT BRIDGE</span>
</div>

<div class="answer-shell">
  <section class="core-answer">
    <div class="info-kicker">日本語Concept</div>
    <div class="japanese-answer">{{Japanese}}</div>
    {{#PartOfSpeech}}
    <div class="pos-badge">{{PartOfSpeech}}</div>
    {{/PartOfSpeech}}
  </section>

  {{#ExampleIndonesian}}
  <section class="example-card">
    <div class="section-kicker">DENGARKAN KALIMATNYA</div>
    <div class="sound-instruction example-prompt">例文の音から、見出し語と文意を探す</div>
    <div class="tts-audio example-audio">
      {{tts id_ID:ExampleIndonesian}}
    </div>
    <div class="example-target id-text">{{ExampleIndonesian}}</div>
    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleIndonesian}}

  <details class="detail-block structure-block">
    <summary><span class="summary-icon">◆</span><span>語の構造</span></summary>
    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">見出し語</div>
        <div class="detail-text structure-word id-text">{{Indonesian}}</div>
      </div>
      {{#Pronunciation}}
      <div class="detail-group">
        <div class="detail-label">発音</div>
        <div class="detail-text pronunciation-detail">{{Pronunciation}}</div>
      </div>
      {{/Pronunciation}}
      {{#Root}}
      <div class="detail-group">
        <div class="detail-label">語根</div>
        <div class="detail-text root-word id-text">{{Root}}</div>
      </div>
      {{/Root}}
      {{#Affixes}}
      <div class="detail-group">
        <div class="detail-label">接辞</div>
        <div class="detail-text japanese-text">{{Affixes}}</div>
      </div>
      {{/Affixes}}
      {{#PerceptualSegmentation}}
      <div class="detail-group segmentation-group">
        <div class="detail-label">音としての切れ目</div>
        <div class="detail-text segmentation-text">{{PerceptualSegmentation}}</div>
      </div>
      {{/PerceptualSegmentation}}
      {{#MorphologicalBreakdown}}
      <div class="detail-group">
        <div class="detail-label">形態素分解</div>
        <div class="detail-text japanese-text breakdown-text">{{MorphologicalBreakdown}}</div>
      </div>
      {{/MorphologicalBreakdown}}
    </div>
  </details>

  {{#ExampleBreakdown}}
  <details class="detail-block explanation-block">
    <summary><span class="summary-icon">◆</span><span>例文解説</span></summary>
    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">文の組み立て</div>
        <div class="detail-text japanese-text breakdown-text">{{ExampleBreakdown}}</div>
      </div>
      {{#ExampleExplanation}}
      <div class="detail-group">
        <div class="detail-label">なぜこの意味になる？</div>
        <div class="detail-text japanese-text">{{ExampleExplanation}}</div>
      </div>
      {{/ExampleExplanation}}
    </div>
  </details>
  {{/ExampleBreakdown}}

  <details class="detail-block bridge-block">
    <summary><span class="summary-icon">◆</span><span>言語間ブリッジ</span></summary>
    <div class="detail-content">
      {{#MeaningBridge}}
      <div class="detail-group">
        <div class="detail-label">意味の橋</div>
        <div class="detail-text japanese-text">{{MeaningBridge}}</div>
      </div>
      {{/MeaningBridge}}
      {{#SoundBridge}}
      <div class="detail-group">
        <div class="detail-label">音の橋</div>
        <div class="detail-text japanese-text">{{SoundBridge}}</div>
      </div>
      {{/SoundBridge}}
      {{#UsageNote}}
      <div class="detail-group">
        <div class="detail-label">用法とConcept境界</div>
        <div class="detail-text japanese-text">{{UsageNote}}</div>
      </div>
      {{/UsageNote}}
      <div class="detail-group">
        <div class="detail-label">記憶都市の住所</div>
        <div class="detail-text japanese-text bridge-note">音、ConceptScene、日本語Concept、語根、接辞、例文を同じConcept IDへ接続して観測する。</div>
      </div>
    </div>
  </details>

  {{#Source}}
  <div class="source-line"><span class="source-label">SOURCE</span><span>{{Source}}</span></div>
  {{/Source}}
</div>
```

## CSS

```css
:root {
  --bg-page:#edf1f5; --bg-card:#fbfaf7; --ink-main:#172033; --ink-soft:#566176;
  --line-soft:#d8dee8; --navy:#173b5f; --navy-deep:#102a43; --blue-light:#e8f1f8;
  --gold:#b88a3b; --violet-light:#f0ebf7; --violet-ink:#553e6b;
  --green-light:#eaf3ec; --green-ink:#355b42; --red:#b7463b; --red-light:#f8e8e5;
  --teal:#277986; --teal-light:#e3f1f3; --shadow:0 10px 28px rgba(27,43,65,.12);
}
html,body,.card{width:100%;margin:0;text-align:center}
.card{box-sizing:border-box;padding:18px 12px 28px;color:var(--ink-main);background:radial-gradient(circle at 50% -10%,rgba(183,70,59,.13),transparent 34%),linear-gradient(180deg,#eef3f5 0%,var(--bg-page) 100%);font-family:"Noto Sans","Segoe UI",Arial,sans-serif;font-size:18px;line-height:1.65;overflow-wrap:anywhere}
.card-shell,.answer-shell{box-sizing:border-box;display:block;width:100%;max-width:720px;margin:0 auto}
.card-shell{padding:18px;background:var(--bg-card);border:1px solid rgba(39,121,134,.14);border-radius:18px;box-shadow:var(--shadow)}
.topline{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;margin-bottom:12px}
.concept-id{color:var(--gold);font-size:.84rem;font-weight:800;letter-spacing:.14em}
.language-chip{padding:4px 11px;color:#fff;background:var(--red);border-radius:999px;font-size:.72rem;font-weight:800;letter-spacing:.08em}
.sound-gate{margin-bottom:14px;padding:13px 14px;background:linear-gradient(145deg,var(--teal-light) 0%,#f8fbfc 100%);border:1px solid rgba(39,121,134,.24);border-radius:13px}
.sound-kicker,.section-kicker,.info-kicker{color:var(--gold);font-size:.67rem;font-weight:800;letter-spacing:.14em}
.sound-instruction{margin-top:3px;color:var(--ink-soft);font-size:.78rem}
.tts-audio{margin:10px auto 0;text-align:center}.replay-button svg{width:34px;height:34px}
.concept-scene{display:block;width:100%;margin:10px auto 16px;text-align:center}
.concept-scene img{display:block;width:auto;max-width:100%;max-height:420px;height:auto;object-fit:contain;margin:0 auto;border:1px solid rgba(184,138,59,.26);border-radius:12px;box-shadow:0 8px 22px rgba(15,35,55,.16)}
.word-panel{padding:16px 14px 12px;text-align:center;background:linear-gradient(145deg,#fff 0%,#fff5f2 100%);border:1px solid var(--line-soft);border-radius:14px}
.target-word,.structure-word,.root-word{color:var(--navy-deep);font-family:"Noto Serif",Georgia,serif;font-weight:700}
.target-word{font-size:clamp(2.2rem,10vw,3.6rem);line-height:1.18;letter-spacing:.025em}.structure-word{font-size:1.7rem;text-align:center}.root-word{font-size:1.25rem;text-align:center}
.pronunciation{margin-top:8px;color:var(--teal);font-size:.96rem;letter-spacing:.035em}
.answer-divider{display:flex;align-items:center;gap:12px;width:100%;max-width:720px;margin:20px auto 14px;color:var(--gold);font-size:.67rem;font-weight:800;letter-spacing:.17em}
.answer-divider:before,.answer-divider:after{content:"";flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.answer-shell{padding-bottom:8px}.core-answer,.example-card{padding:17px;background:var(--bg-card);border:1px solid var(--line-soft);border-radius:15px;box-shadow:0 6px 18px rgba(27,43,65,.08)}
.core-answer{margin-bottom:13px}.japanese-answer{margin-top:4px;color:var(--ink-main);font-size:1.62rem;font-weight:800}
.pos-badge{display:inline-block;margin-top:8px;padding:3px 10px;color:#96382f;background:var(--red-light);border-radius:999px;font-size:.78rem;font-weight:700}
.example-card{margin-bottom:13px;border-left:4px solid var(--gold)}.example-prompt{margin-bottom:2px}.example-target{margin-top:12px;color:var(--navy-deep);font-family:"Noto Serif",Georgia,serif;font-size:1.3rem;font-weight:650;line-height:1.75}
.example-japanese{margin-top:12px;padding-top:11px;color:var(--ink-main);border-top:1px dashed var(--line-soft);font-size:.94rem}
.detail-block{margin:10px 0 0;background:var(--bg-card);border:1px solid var(--line-soft);border-radius:13px;overflow:hidden;text-align:left;box-shadow:0 4px 14px rgba(27,43,65,.06)}
.detail-block summary{display:flex;align-items:center;justify-content:center;gap:9px;padding:13px 15px;cursor:pointer;font-weight:800;list-style:none;user-select:none}.detail-block summary::-webkit-details-marker{display:none}
.summary-icon{display:inline-block;font-size:.66rem;transition:transform .2s ease}.detail-block[open] .summary-icon{transform:rotate(45deg)}
.structure-block summary{color:var(--violet-ink);background:var(--violet-light)}.explanation-block summary{color:var(--navy);background:var(--blue-light)}.bridge-block summary{color:var(--green-ink);background:var(--green-light)}
.detail-content{padding:4px 16px 16px}.detail-group{margin-top:13px;padding:12px 13px;background:rgba(255,255,255,.66);border:1px solid rgba(216,222,232,.8);border-radius:10px}.segmentation-group{text-align:center;background:var(--red-light)}
.detail-label{margin-bottom:5px;color:var(--ink-soft);font-size:.72rem;font-weight:800;letter-spacing:.08em}.detail-text{color:var(--ink-main)}
.pronunciation-detail,.segmentation-text{color:var(--teal);font-size:1.02rem;font-weight:700;letter-spacing:.035em}.breakdown-text{line-height:1.9;white-space:pre-line}.bridge-note{padding-left:10px;border-left:3px solid #6a9b74}
.source-line{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;margin-top:15px;color:#7a8290;font-size:.72rem}.source-label{color:var(--gold);font-weight:800;letter-spacing:.1em}
.nightMode.card,.night_mode.card{--bg-page:#111820;--bg-card:#1a232d;--ink-main:#f1f5f9;--ink-soft:#b8c5d4;--line-soft:#3c4958;--navy:#87c7ff;--navy-deep:#e2f1ff;--blue-light:#263e52;--gold:#e4bd68;--violet-light:#40354d;--violet-ink:#eee3ff;--green-light:#294236;--green-ink:#ddf5e4;--red:#f09b92;--red-light:#4b302f;--teal:#8bd5df;--teal-light:#213b40;--shadow:0 12px 30px rgba(0,0,0,.34);color:var(--ink-main);background:radial-gradient(circle at 50% -10%,rgba(228,189,104,.12),transparent 34%),linear-gradient(180deg,#151e27 0%,var(--bg-page) 100%)}
.nightMode .card-shell,.night_mode .card-shell,.nightMode .core-answer,.night_mode .core-answer,.nightMode .example-card,.night_mode .example-card,.nightMode .detail-block,.night_mode .detail-block{color:var(--ink-main);background:var(--bg-card);border-color:var(--line-soft)}
.nightMode .sound-gate,.night_mode .sound-gate{background:linear-gradient(145deg,#213a40 0%,#1d2932 100%);border-color:#365a62}.nightMode .word-panel,.night_mode .word-panel{background:linear-gradient(145deg,#202b36 0%,#2b2221 100%);border-color:var(--line-soft)}
.nightMode .target-word,.night_mode .target-word,.nightMode .structure-word,.night_mode .structure-word,.nightMode .root-word,.night_mode .root-word,.nightMode .example-target,.night_mode .example-target,.nightMode .japanese-answer,.night_mode .japanese-answer,.nightMode .example-japanese,.night_mode .example-japanese,.nightMode .detail-text,.night_mode .detail-text{color:var(--ink-main)}
.nightMode .sound-instruction,.night_mode .sound-instruction,.nightMode .detail-label,.night_mode .detail-label{color:var(--ink-soft)}.nightMode .language-chip,.night_mode .language-chip{color:#321a17;background:#f09b92}.nightMode .pos-badge,.night_mode .pos-badge{color:#ffeae7;background:#56332f}.nightMode .detail-group,.night_mode .detail-group{background:rgba(255,255,255,.035);border-color:var(--line-soft)}.nightMode .segmentation-group,.night_mode .segmentation-group{background:#452f2d}.nightMode .structure-block summary,.night_mode .structure-block summary{color:var(--violet-ink);background:var(--violet-light)}.nightMode .explanation-block summary,.night_mode .explanation-block summary{color:#e4f3ff;background:var(--blue-light)}.nightMode .bridge-block summary,.night_mode .bridge-block summary{color:var(--green-ink);background:var(--green-light)}.nightMode .source-line,.night_mode .source-line{color:#aab5c2}
@media(max-width:600px){.card{padding:10px 7px 22px;font-size:16px}.card-shell{padding:12px;border-radius:14px}.concept-scene img{max-height:320px}.target-word{font-size:clamp(2.05rem,12vw,3rem)}.example-target{font-size:1.15rem}.detail-content{padding:3px 10px 12px}.detail-group{padding:10px}}

```

## 適用手順

1. 表面テンプレートを全置換する。
2. 裏面テンプレートを全置換する。
3. CSSを全置換する。
4. C0001とC0010をプレビューする。
5. 表面で`id_ID`の単語音声を聞き、Conceptを想起する。
6. ConceptScene、見出し語、発音を確認する。
7. 裏面で例文音声、例文、日本語訳を確認する。
8. 3段プルダウンと`id="answer"`の自動スクロールを確認する。
9. AnkiDroidへ同期し、ライト・ダーク両モードで確認する。

## TTS

```html
{{tts id_ID:Indonesian}}
{{tts id_ID:ExampleIndonesian}}
```

## 重点確認

- C0001 `catatan`：`ca-ta-tan /tʃaˈtatan/`、語根`catat`、接辞`-an`。
- C0010：長い見出し語、接辞、形態素分解、折り返し。
- 裏面の`id="answer"`は削除しない。
- `CourseTags`は管理用で、カード画面には表示しない。
