# MEMORIOPOLIS ベトナム語 Anki UI 完全版

更新日：2026-10-02  
正式フィールド：19  
設計：`音・声調 → Concept想起 → ConceptScene → 綴り → 例文音声`

## 重要なフィールド確認

アップロードされた`vi_core10_master.csv`と`vi_core10_anki.csv`はいずれも現時点では18列であり、画像参照はまだCSVへ入っていない。Ankiノートタイプには19番目として`ConceptScene`を追加済み。画像参照は次工程で正式19列CSVへ追加する。

## 表面テンプレート

```html
<div class="card-shell">
  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">TIẾNG VIỆT</span>
  </div>

  <div class="sound-gate">
    <div class="sound-kicker">NGHE TRƯỚC</div>
    <div class="sound-instruction">まず音と声調を聞き、心の中でConceptを探す</div>
    <div class="tts-audio word-audio">
      {{tts vi_VN:Vietnamese}}
    </div>
  </div>

  {{#ConceptScene}}
  <div class="concept-scene">{{ConceptScene}}</div>
  {{/ConceptScene}}

  <div class="word-panel">
    <div class="target-word vi-text">{{Vietnamese}}</div>
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

  {{#ExampleVietnamese}}
  <section class="example-card">
    <div class="section-kicker">NGHE CÂU VÍ DỤ</div>
    <div class="sound-instruction example-prompt">例文の音と声調から、見出し語と文意を探す</div>
    <div class="tts-audio example-audio">
      {{tts vi_VN:ExampleVietnamese}}
    </div>
    <div class="example-target vi-text">{{ExampleVietnamese}}</div>
    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleVietnamese}}

  <details class="detail-block structure-block">
    <summary><span class="summary-icon">◆</span><span>語の構造</span></summary>
    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">見出し語</div>
        <div class="detail-text structure-word vi-text">{{Vietnamese}}</div>
      </div>
      {{#Pronunciation}}
      <div class="detail-group">
        <div class="detail-label">発音・声調</div>
        <div class="detail-text pronunciation-detail">{{Pronunciation}}</div>
      </div>
      {{/Pronunciation}}
      {{#Root}}
      <div class="detail-group">
        <div class="detail-label">語根・構成要素</div>
        <div class="detail-text root-word vi-text">{{Root}}</div>
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
        <div class="detail-text segmentation-text vi-text">{{PerceptualSegmentation}}</div>
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
        <div class="detail-text japanese-text bridge-note">音と声調、ConceptScene、日本語Concept、語構成、例文を同じConcept IDへ接続して観測する。</div>
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
:root{--page:#edf2f3;--paper:#fbfaf7;--ink:#172033;--soft:#5b6678;--line:#d7dee7;--deep:#102a43;--teal:#176f73;--teal-light:#e0f1ef;--gold:#b58632;--red:#b9433d;--red-light:#f8e8e5;--violet:#553e6b;--violet-light:#f0ebf7;--blue:#173b5f;--blue-light:#e8f1f8;--green:#355b42;--green-light:#eaf3ec;--shadow:0 10px 28px rgba(27,43,65,.12)}
html,body,.card{width:100%;margin:0;text-align:center}.card{box-sizing:border-box;padding:18px 12px 28px;color:var(--ink);background:radial-gradient(circle at 50% -10%,rgba(185,67,61,.13),transparent 34%),linear-gradient(180deg,#edf5f4 0%,var(--page) 100%);font-family:"Noto Sans","Segoe UI",Arial,sans-serif;font-size:18px;line-height:1.65;overflow-wrap:anywhere}.card-shell,.answer-shell{box-sizing:border-box;width:100%;max-width:720px;margin:0 auto}.card-shell{padding:18px;background:var(--paper);border:1px solid rgba(23,111,115,.15);border-radius:18px;box-shadow:var(--shadow)}.topline{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:12px}.concept-id{color:var(--gold);font-size:.84rem;font-weight:800;letter-spacing:.14em}.language-chip{padding:4px 11px;color:#fff;background:var(--red);border-radius:999px;font-size:.72rem;font-weight:800;letter-spacing:.08em}.sound-gate{margin-bottom:14px;padding:13px 14px;background:linear-gradient(145deg,var(--teal-light),#f8fbfb);border:1px solid rgba(23,111,115,.24);border-radius:13px}.sound-kicker,.section-kicker,.info-kicker{color:var(--gold);font-size:.67rem;font-weight:800;letter-spacing:.14em}.sound-instruction{margin-top:3px;color:var(--soft);font-size:.78rem}.tts-audio{margin:10px auto 0}.replay-button svg{width:34px;height:34px}.concept-scene{width:100%;margin:10px auto 16px}.concept-scene img{display:block;width:auto;max-width:100%;max-height:420px;height:auto;object-fit:contain;margin:0 auto;border:1px solid rgba(181,134,50,.26);border-radius:12px;box-shadow:0 8px 22px rgba(15,35,55,.16)}.word-panel{padding:16px 14px 12px;background:linear-gradient(145deg,#fff,#fff5f2);border:1px solid var(--line);border-radius:14px}.target-word,.structure-word,.root-word{color:var(--deep);font-family:"Noto Serif","Noto Serif Vietnamese",Georgia,serif;font-weight:700}.target-word{font-size:clamp(2.2rem,10vw,3.6rem);line-height:1.22}.structure-word{font-size:1.7rem;text-align:center}.root-word{font-size:1.25rem;text-align:center}.pronunciation{margin-top:8px;color:var(--teal);font-size:.96rem;letter-spacing:.02em}.answer-divider{display:flex;align-items:center;gap:12px;max-width:720px;margin:20px auto 14px;color:var(--gold);font-size:.67rem;font-weight:800;letter-spacing:.17em}.answer-divider:before,.answer-divider:after{content:"";flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}.core-answer,.example-card{padding:17px;background:var(--paper);border:1px solid var(--line);border-radius:15px;box-shadow:0 6px 18px rgba(27,43,65,.08)}.core-answer{margin-bottom:13px}.japanese-answer{margin-top:4px;font-size:1.62rem;font-weight:800}.pos-badge{display:inline-block;margin-top:8px;padding:3px 10px;color:#96382f;background:var(--red-light);border-radius:999px;font-size:.78rem;font-weight:700}.example-card{margin-bottom:13px;border-left:4px solid var(--gold)}.example-target{margin-top:12px;color:var(--deep);font-family:"Noto Serif","Noto Serif Vietnamese",Georgia,serif;font-size:1.3rem;font-weight:650;line-height:1.8}.example-japanese{margin-top:12px;padding-top:11px;border-top:1px dashed var(--line);font-size:.94rem}.detail-block{margin:10px 0 0;background:var(--paper);border:1px solid var(--line);border-radius:13px;overflow:hidden;text-align:left;box-shadow:0 4px 14px rgba(27,43,65,.06)}.detail-block summary{display:flex;align-items:center;justify-content:center;gap:9px;padding:13px 15px;cursor:pointer;font-weight:800;list-style:none}.detail-block summary::-webkit-details-marker{display:none}.summary-icon{font-size:.66rem;transition:transform .2s}.detail-block[open] .summary-icon{transform:rotate(45deg)}.structure-block summary{color:var(--violet);background:var(--violet-light)}.explanation-block summary{color:var(--blue);background:var(--blue-light)}.bridge-block summary{color:var(--green);background:var(--green-light)}.detail-content{padding:4px 16px 16px}.detail-group{margin-top:13px;padding:12px 13px;background:rgba(255,255,255,.66);border:1px solid rgba(215,222,231,.8);border-radius:10px}.segmentation-group{text-align:center;background:var(--red-light)}.detail-label{margin-bottom:5px;color:var(--soft);font-size:.72rem;font-weight:800;letter-spacing:.08em}.pronunciation-detail,.segmentation-text{color:var(--teal);font-size:1.02rem;font-weight:700}.breakdown-text{line-height:1.9;white-space:pre-line}.bridge-note{padding-left:10px;border-left:3px solid #6a9b74}.source-line{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;margin-top:15px;color:#7a8290;font-size:.72rem}.source-label{color:var(--gold);font-weight:800;letter-spacing:.1em}
.nightMode.card,.night_mode.card{--page:#111820;--paper:#1a232d;--ink:#f1f5f9;--soft:#b8c5d4;--line:#3c4958;--deep:#e2f1ff;--teal:#8bd5d1;--teal-light:#213b3b;--gold:#e4bd68;--red:#f09b92;--red-light:#4b302f;--violet:#eee3ff;--violet-light:#40354d;--blue:#e4f3ff;--blue-light:#263e52;--green:#ddf5e4;--green-light:#294236;--shadow:0 12px 30px rgba(0,0,0,.34);color:var(--ink);background:radial-gradient(circle at 50% -10%,rgba(228,189,104,.12),transparent 34%),linear-gradient(180deg,#151e27,var(--page))}.nightMode .card-shell,.night_mode .card-shell,.nightMode .core-answer,.night_mode .core-answer,.nightMode .example-card,.night_mode .example-card,.nightMode .detail-block,.night_mode .detail-block{background:var(--paper);border-color:var(--line)}.nightMode .sound-gate,.night_mode .sound-gate{background:linear-gradient(145deg,#213a3a,#1d2932);border-color:#365a5a}.nightMode .word-panel,.night_mode .word-panel{background:linear-gradient(145deg,#202b36,#2b2221);border-color:var(--line)}.nightMode .target-word,.night_mode .target-word,.nightMode .structure-word,.night_mode .structure-word,.nightMode .root-word,.night_mode .root-word,.nightMode .example-target,.night_mode .example-target,.nightMode .japanese-answer,.night_mode .japanese-answer,.nightMode .example-japanese,.night_mode .example-japanese,.nightMode .detail-text,.night_mode .detail-text{color:var(--ink)}.nightMode .sound-instruction,.night_mode .sound-instruction,.nightMode .detail-label,.night_mode .detail-label{color:var(--soft)}.nightMode .language-chip,.night_mode .language-chip{color:#321a17;background:#f09b92}.nightMode .detail-group,.night_mode .detail-group{background:rgba(255,255,255,.035);border-color:var(--line)}.nightMode .segmentation-group,.night_mode .segmentation-group{background:#452f2d}.nightMode .source-line,.night_mode .source-line{color:#aab5c2}
@media(max-width:600px){.card{padding:10px 7px 22px;font-size:16px}.card-shell{padding:12px;border-radius:14px}.concept-scene img{max-height:320px}.target-word{font-size:clamp(2.05rem,12vw,3rem)}.example-target{font-size:1.15rem}.detail-content{padding:3px 10px 12px}.detail-group{padding:10px}}
```

## TTS

過去の2026-09-19引き継ぎ書では、ベトナム語は次の標準指定。インドネシア語のような例外voice IDは記録されていない。

```html
{{tts vi_VN:Vietnamese}}
{{tts vi_VN:ExampleVietnamese}}
```

AnkiDroidで`APP_MISSING_VOICE`が出た場合は推測で変更せず、一時的に`{{tts-voices:}}`を表示し、端末が返した値をそのまま採用する。

## 確認順

1. 表面・裏面・CSSを全置換して保存する。
2. C0001で単語音声、声調、見出し語を確認する。
3. 裏面で例文音声と`id="answer"`の移動を確認する。
4. 3段プルダウンを確認する。
5. ConceptSceneは19列CSVを再インポートした後に表示確認する。
6. AnkiDroidでライト・ダーク両モードを確認する。
