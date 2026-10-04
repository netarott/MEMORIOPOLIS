# MEMORIOPOLIS フランス語 Anki UI 完全版

更新日：2026-10-04  
正式フィールド：19  
設計：`音 → Concept想起 → ConceptScene → 綴り → 例文音声`

## 表面テンプレート

```html
<div class="card-shell">
  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">FRANÇAIS</span>
  </div>

  <div class="sound-gate">
    <div class="sound-kicker">ÉCOUTEZ D’ABORD</div>
    <div class="sound-instruction">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-audio word-audio">
      {{tts fr_FR:French}}
    </div>
  </div>

  {{#ConceptScene}}
  <div class="concept-scene">{{ConceptScene}}</div>
  {{/ConceptScene}}

  <div class="word-panel">
    <div class="target-word fr-text">{{French}}</div>
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

  {{#ExampleFrench}}
  <section class="example-card">
    <div class="section-kicker">ÉCOUTEZ LA PHRASE</div>
    <div class="sound-instruction example-prompt">例文の音から、見出し語と文意を探す</div>
    <div class="tts-audio example-audio">
      {{tts fr_FR:ExampleFrench}}
    </div>
    <div class="example-target fr-text">{{ExampleFrench}}</div>
    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleFrench}}

  <details class="detail-block structure-block">
    <summary><span class="summary-icon">◆</span><span>語の構造</span></summary>
    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">見出し語</div>
        <div class="detail-text structure-word fr-text">{{French}}</div>
      </div>
      {{#Pronunciation}}
      <div class="detail-group">
        <div class="detail-label">発音</div>
        <div class="detail-text pronunciation-detail">{{Pronunciation}}</div>
      </div>
      {{/Pronunciation}}
      {{#Root}}
      <div class="detail-group">
        <div class="detail-label">語根・構成要素</div>
        <div class="detail-text root-word fr-text">{{Root}}</div>
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
        <div class="detail-text segmentation-text fr-text">{{PerceptualSegmentation}}</div>
      </div>
      {{/PerceptualSegmentation}}
      {{#MorphologicalBreakdown}}
      <div class="detail-group">
        <div class="detail-label">語構成</div>
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
        <div class="detail-text japanese-text bridge-note">音、リエゾン、アンシェヌマン、ConceptScene、日本語Concept、語構成、例文を同じConcept IDへ接続して観測する。</div>
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
  --page:#eef1f5; --paper:#fbfaf7; --ink:#172033; --soft:#5b6678;
  --line:#d7dee7; --deep:#102a43; --blue:#235789; --blue-light:#e7f0f8;
  --gold:#b58632; --red:#b9433d; --red-light:#f8e8e5;
  --violet:#553e6b; --violet-light:#f0ebf7; --green:#355b42;
  --green-light:#eaf3ec; --shadow:0 10px 28px rgba(27,43,65,.12);
}
html,body,.card{width:100%;margin:0;text-align:center}
.card{box-sizing:border-box;padding:18px 12px 28px;color:var(--ink);background:radial-gradient(circle at 50% -10%,rgba(35,87,137,.15),transparent 34%),linear-gradient(180deg,#eff4f8 0%,var(--page) 100%);font-family:"Noto Sans","Segoe UI",Arial,sans-serif;font-size:18px;line-height:1.65;overflow-wrap:anywhere}
.card-shell,.answer-shell{box-sizing:border-box;width:100%;max-width:720px;margin:0 auto}
.card-shell{padding:18px;background:var(--paper);border:1px solid rgba(35,87,137,.18);border-radius:18px;box-shadow:var(--shadow)}
.topline{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}
.concept-id{color:var(--gold);font-size:.84rem;font-weight:800;letter-spacing:.14em}
.language-chip{padding:4px 11px;color:#fff;background:linear-gradient(90deg,#235789 0%,#235789 34%,#fbfaf7 34%,#fbfaf7 66%,#b9433d 66%);border:1px solid rgba(23,32,51,.12);border-radius:999px;font-size:.72rem;font-weight:800;letter-spacing:.08em;text-shadow:0 1px 2px rgba(0,0,0,.45)}
.sound-gate{margin-bottom:14px;padding:13px 14px;background:linear-gradient(145deg,var(--blue-light),#f8fbfd);border:1px solid rgba(35,87,137,.25);border-radius:13px}
.sound-kicker,.section-kicker,.info-kicker{color:var(--gold);font-size:.67rem;font-weight:800;letter-spacing:.14em}
.sound-instruction{margin-top:3px;color:var(--soft);font-size:.78rem}
.tts-audio{margin:10px auto 0}.replay-button svg{width:34px;height:34px}
.concept-scene{width:100%;margin:10px auto 16px}.concept-scene img{display:block;width:auto;max-width:100%;max-height:420px;height:auto;object-fit:contain;margin:0 auto;border:1px solid rgba(181,134,50,.26);border-radius:12px;box-shadow:0 8px 22px rgba(15,35,55,.16)}
.word-panel{padding:16px 14px 12px;background:linear-gradient(145deg,#fff,#f3f7fb);border:1px solid var(--line);border-radius:14px}
.target-word,.structure-word,.root-word{color:var(--deep);font-family:"Noto Serif","Georgia",serif;font-weight:700}
.target-word{font-size:clamp(2.2rem,10vw,3.6rem);line-height:1.22}.structure-word{font-size:1.7rem;text-align:center}.root-word{font-size:1.25rem;text-align:center}
.pronunciation{margin-top:8px;color:var(--blue);font-size:.96rem;letter-spacing:.02em}
.answer-divider{display:flex;align-items:center;gap:12px;max-width:720px;margin:20px auto 14px;color:var(--gold);font-size:.67rem;font-weight:800;letter-spacing:.17em}.answer-divider:before,.answer-divider:after{content:"";flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.core-answer,.example-card{padding:17px;background:var(--paper);border:1px solid var(--line);border-radius:15px;box-shadow:0 6px 18px rgba(27,43,65,.08)}.core-answer{margin-bottom:13px}.japanese-answer{margin-top:4px;font-size:1.62rem;font-weight:800}.pos-badge{display:inline-block;margin-top:8px;padding:3px 10px;color:#96382f;background:var(--red-light);border-radius:999px;font-size:.78rem;font-weight:700}
.example-card{margin-bottom:13px;border-left:4px solid var(--gold)}.example-target{margin-top:12px;color:var(--deep);font-family:"Noto Serif",Georgia,serif;font-size:1.3rem;font-weight:650;line-height:1.8}.example-japanese{margin-top:12px;padding-top:11px;border-top:1px dashed var(--line);font-size:.94rem}
.detail-block{margin:10px 0 0;background:var(--paper);border:1px solid var(--line);border-radius:13px;overflow:hidden;text-align:left;box-shadow:0 4px 14px rgba(27,43,65,.06)}.detail-block summary{display:flex;align-items:center;justify-content:center;gap:9px;padding:13px 15px;cursor:pointer;font-weight:800;list-style:none}.detail-block summary::-webkit-details-marker{display:none}.summary-icon{font-size:.66rem;transition:transform .2s}.detail-block[open] .summary-icon{transform:rotate(45deg)}
.structure-block summary{color:var(--violet);background:var(--violet-light)}.explanation-block summary{color:var(--blue);background:var(--blue-light)}.bridge-block summary{color:var(--green);background:var(--green-light)}
.detail-content{padding:4px 16px 16px}.detail-group{margin-top:13px;padding:12px 13px;background:rgba(255,255,255,.66);border:1px solid rgba(215,222,231,.8);border-radius:10px}.segmentation-group{text-align:center;background:var(--red-light)}.detail-label{margin-bottom:5px;color:var(--soft);font-size:.72rem;font-weight:800;letter-spacing:.08em}.pronunciation-detail,.segmentation-text{color:var(--blue);font-size:1.02rem;font-weight:700}.breakdown-text{line-height:1.9;white-space:pre-line}.bridge-note{padding-left:10px;border-left:3px solid #6a9b74}.source-line{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;margin-top:15px;color:#7a8290;font-size:.72rem}.source-label{color:var(--gold);font-weight:800;letter-spacing:.1em}
.nightMode.card,.night_mode.card{--page:#111820;--paper:#1a232d;--ink:#f1f5f9;--soft:#b8c5d4;--line:#3c4958;--deep:#e2f1ff;--blue:#8abce8;--blue-light:#263e52;--gold:#e4bd68;--red:#f09b92;--red-light:#4b302f;--violet:#eee3ff;--violet-light:#40354d;--green:#ddf5e4;--green-light:#294236;--shadow:0 12px 30px rgba(0,0,0,.34);color:var(--ink);background:radial-gradient(circle at 50% -10%,rgba(138,188,232,.12),transparent 34%),linear-gradient(180deg,#151e27,var(--page))}
.nightMode .card-shell,.night_mode .card-shell,.nightMode .core-answer,.night_mode .core-answer,.nightMode .example-card,.night_mode .example-card,.nightMode .detail-block,.night_mode .detail-block{background:var(--paper);border-color:var(--line)}.nightMode .sound-gate,.night_mode .sound-gate{background:linear-gradient(145deg,#263e52,#1d2932);border-color:#496a86}.nightMode .word-panel,.night_mode .word-panel{background:linear-gradient(145deg,#202b36,#202a35);border-color:var(--line)}.nightMode .target-word,.night_mode .target-word,.nightMode .structure-word,.night_mode .structure-word,.nightMode .root-word,.night_mode .root-word,.nightMode .example-target,.night_mode .example-target,.nightMode .japanese-answer,.night_mode .japanese-answer,.nightMode .example-japanese,.night_mode .example-japanese,.nightMode .detail-text,.night_mode .detail-text{color:var(--ink)}.nightMode .sound-instruction,.night_mode .sound-instruction,.nightMode .detail-label,.night_mode .detail-label{color:var(--soft)}.nightMode .language-chip,.night_mode .language-chip{border-color:#748190}.nightMode .detail-group,.night_mode .detail-group{background:rgba(255,255,255,.035);border-color:var(--line)}.nightMode .segmentation-group,.night_mode .segmentation-group{background:#452f2d}.nightMode .source-line,.night_mode .source-line{color:#aab5c2}
@media(max-width:600px){.card{padding:10px 7px 22px;font-size:16px}.card-shell{padding:12px;border-radius:14px}.concept-scene img{max-height:320px}.target-word{font-size:clamp(2.05rem,12vw,3rem)}.example-target{font-size:1.15rem}.detail-content{padding:3px 10px 12px}.detail-group{padding:10px}}
```

## TTS

```html
{{tts fr_FR:French}}
{{tts fr_FR:ExampleFrench}}
```

AnkiDroidで音声が出ない場合は、推測でvoice IDを変更せず、一時的に`{{tts-voices:}}`を表示して端末が返した値をそのまま使う。

## 確認順

1. 表面・裏面・CSSを全置換する。
2. C0001で単語音声、ConceptScene、見出し語、発音を確認する。
3. 裏面で例文音声、例文、日本語訳を確認する。
4. 3段プルダウンを確認する。
5. `id="answer"`によるAnkiDroidの自動スクロールを確認する。
6. ライト・ダーク両モードを確認する。
7. フランス語では、語単独の発音だけでなく、例文内のリエゾン、アンシェヌマン、語末子音の有無を音として観測する。
