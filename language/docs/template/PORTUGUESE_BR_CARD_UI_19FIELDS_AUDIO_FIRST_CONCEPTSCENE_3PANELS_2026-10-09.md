# MEMORIOPOLIS ブラジル・ポルトガル語 Anki UI 完全版

**更新日:** 2026-10-09  
**言語識別子:** `pt-BR`  
**TTSロケール:** `pt_BR`  
**対象デッキ:** `MEMORIOPOLIS::PortugueseBR`  
**設計テーマ:** `音 → Concept候補 → ConceptScene → 語 → 例文`

## 正式19フィールド

```text
01 ID
02 Portuguese
03 Pronunciation
04 Japanese
05 PartOfSpeech
06 UsageNote
07 ExamplePortuguese
08 ExampleJapanese
09 Root
10 Affixes
11 PerceptualSegmentation
12 MorphologicalBreakdown
13 ExampleBreakdown
14 ExampleExplanation
15 MeaningBridge
16 SoundBridge
17 Source
18 CourseTags
19 ConceptScene
```

`CourseTags`は管理用であり、カード画面には表示しない。

---

## 表面テンプレート

```html
<div class="card-shell">
  <div class="flag-line" aria-hidden="true">
    <span class="flag-green"></span>
    <span class="flag-gold"></span>
    <span class="flag-blue"></span>
  </div>

  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">PORTUGUÊS · BRASIL</span>
  </div>

  <section class="sound-gate">
    <div class="sound-kicker">OUÇA PRIMEIRO</div>
    <div class="sound-instruction">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-audio word-audio">
      {{tts pt_BR:Portuguese}}
    </div>
  </section>

  {{#ConceptScene}}
  <div class="concept-scene">
    {{ConceptScene}}
  </div>
  {{/ConceptScene}}

  <section class="word-panel">
    <div class="target-word pt-text">{{Portuguese}}</div>

    {{#Pronunciation}}
    <div class="pronunciation">{{Pronunciation}}</div>
    {{/Pronunciation}}

    {{#PerceptualSegmentation}}
    <div class="sound-pattern">
      <span class="sound-pattern-label">RITMO</span>
      <span class="sound-pattern-text">{{PerceptualSegmentation}}</span>
    </div>
    {{/PerceptualSegmentation}}
  </section>
</div>
```

---

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

  {{#ExamplePortuguese}}
  <section class="example-card">
    <div class="section-kicker">OUÇA A FRASE</div>
    <div class="sound-instruction example-prompt">
      例文の音から、見出し語と文意を探す
    </div>

    <div class="tts-audio example-audio">
      {{tts pt_BR:ExamplePortuguese}}
    </div>

    <div class="example-target pt-text">{{ExamplePortuguese}}</div>

    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExamplePortuguese}}

  <details class="detail-block structure-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>ESTRUTURA DA PALAVRA · 語の構造</span>
    </summary>

    <div class="detail-content">
      <div class="detail-group hero-group">
        <div class="detail-label">見出し語</div>
        <div class="detail-text structure-word pt-text">{{Portuguese}}</div>
      </div>

      {{#Pronunciation}}
      <div class="detail-group">
        <div class="detail-label">発音</div>
        <div class="detail-text pronunciation-detail">{{Pronunciation}}</div>
      </div>
      {{/Pronunciation}}

      {{#Root}}
      <div class="detail-group">
        <div class="detail-label">語根・中心要素</div>
        <div class="detail-text root-word pt-text">{{Root}}</div>
      </div>
      {{/Root}}

      {{#Affixes}}
      <div class="detail-group">
        <div class="detail-label">接辞・活用要素</div>
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
        <div class="detail-label">語構成・形態素分解</div>
        <div class="detail-text japanese-text breakdown-text">{{MorphologicalBreakdown}}</div>
      </div>
      {{/MorphologicalBreakdown}}
    </div>
  </details>

  {{#ExampleBreakdown}}
  <details class="detail-block explanation-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>LEITURA DA FRASE · 例文解説</span>
    </summary>

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
    <summary>
      <span class="summary-icon">◆</span>
      <span>PONTE ENTRE LÍNGUAS · 言語間ブリッジ</span>
    </summary>

    <div class="detail-content">
      {{#MeaningBridge}}
      <div class="detail-group">
        <div class="detail-label">意味の橋</div>
        <div class="detail-text japanese-text">{{MeaningBridge}}</div>
      </div>
      {{/MeaningBridge}}

      {{#SoundBridge}}
      <div class="detail-group sound-bridge-group">
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

      <div class="detail-group address-group">
        <div class="detail-label">記憶都市の住所</div>
        <div class="detail-text japanese-text bridge-note">
          音、ブラジル・ポルトガル語のリズム、ConceptScene、日本語Concept、語根、例文を、同じConcept IDへ接続して観測する。
        </div>
      </div>
    </div>
  </details>

  {{#Source}}
  <div class="source-line">
    <span class="source-label">SOURCE</span>
    <span>{{Source}}</span>
  </div>
  {{/Source}}
</div>
```

---

## CSS

```css
:root {
  --bg-page: #edf2ef;
  --bg-card: #fffdf8;
  --ink-main: #17251f;
  --ink-soft: #5e6d65;
  --line-soft: #d7e0da;
  --forest: #146b3a;
  --forest-deep: #0b4827;
  --forest-light: #e6f3eb;
  --gold: #c4982f;
  --gold-light: #fff4cf;
  --blue: #1c5599;
  --blue-light: #e6effa;
  --violet-light: #f0ebf7;
  --violet-ink: #553e6b;
  --green-light: #e7f3e9;
  --green-ink: #2d5b39;
  --shadow: 0 12px 30px rgba(18, 64, 39, 0.13);
}

html,
body,
.card {
  width: 100%;
  margin: 0;
  text-align: center;
}

.card {
  box-sizing: border-box;
  padding: 18px 12px 30px;
  color: var(--ink-main);
  background:
    radial-gradient(circle at 12% -4%, rgba(20, 107, 58, 0.18), transparent 30%),
    radial-gradient(circle at 88% 0%, rgba(196, 152, 47, 0.16), transparent 29%),
    linear-gradient(180deg, #f2f6f3 0%, var(--bg-page) 100%);
  font-family: "Noto Sans", "Segoe UI", Arial, sans-serif;
  font-size: 18px;
  line-height: 1.65;
  overflow-wrap: anywhere;
}

.card-shell,
.answer-shell {
  box-sizing: border-box;
  display: block;
  width: 100%;
  max-width: 720px;
  margin: 0 auto;
}

.card-shell {
  position: relative;
  padding: 18px;
  background: var(--bg-card);
  border: 1px solid rgba(20, 107, 58, 0.16);
  border-radius: 20px;
  box-shadow: var(--shadow);
  overflow: hidden;
}

.flag-line {
  display: flex;
  height: 5px;
  margin: -18px -18px 16px;
}

.flag-line span {
  display: block;
  height: 100%;
}

.flag-green { flex: 5; background: #146b3a; }
.flag-gold { flex: 3; background: #e5b637; }
.flag-blue { flex: 2; background: #1c5599; }

.topline {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  width: 100%;
  margin-bottom: 13px;
}

.concept-id {
  color: var(--gold);
  font-size: 0.84rem;
  font-weight: 850;
  letter-spacing: 0.14em;
}

.language-chip {
  padding: 5px 12px;
  color: #fff;
  background: linear-gradient(135deg, var(--forest), var(--forest-deep));
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 999px;
  font-size: 0.7rem;
  font-weight: 850;
  letter-spacing: 0.08em;
  box-shadow: 0 4px 12px rgba(11, 72, 39, 0.2);
}

.sound-gate {
  margin-bottom: 15px;
  padding: 14px;
  background: linear-gradient(145deg, var(--forest-light) 0%, #fbfefa 100%);
  border: 1px solid rgba(20, 107, 58, 0.24);
  border-radius: 14px;
}

.sound-kicker,
.section-kicker,
.info-kicker {
  color: var(--gold);
  font-size: 0.67rem;
  font-weight: 850;
  letter-spacing: 0.15em;
}

.sound-instruction {
  margin-top: 4px;
  color: var(--ink-soft);
  font-size: 0.79rem;
}

.tts-audio {
  margin: 10px auto 0;
  text-align: center;
}

.replay-button svg {
  width: 35px;
  height: 35px;
}

.concept-scene {
  display: block;
  width: 100%;
  margin: 10px auto 17px;
  text-align: center;
}

.concept-scene img {
  display: block;
  width: auto;
  max-width: 100%;
  max-height: 420px;
  height: auto;
  object-fit: contain;
  margin: 0 auto;
  border: 1px solid rgba(196, 152, 47, 0.32);
  border-radius: 14px;
  box-shadow: 0 9px 24px rgba(12, 58, 32, 0.17);
}

.word-panel {
  padding: 17px 14px 13px;
  text-align: center;
  background:
    radial-gradient(circle at 90% 10%, rgba(229, 182, 55, 0.17), transparent 34%),
    linear-gradient(145deg, #fff 0%, #f6fbf7 100%);
  border: 1px solid var(--line-soft);
  border-radius: 15px;
}

.target-word,
.structure-word,
.root-word {
  color: var(--forest-deep);
  font-family: "Noto Serif", Georgia, serif;
  font-weight: 750;
}

.target-word {
  font-size: clamp(2.15rem, 10vw, 3.55rem);
  line-height: 1.18;
  letter-spacing: 0.018em;
}

.structure-word {
  font-size: 1.72rem;
  text-align: center;
}

.root-word {
  font-size: 1.24rem;
  text-align: center;
}

.pronunciation {
  margin-top: 8px;
  color: var(--blue);
  font-size: 0.98rem;
  letter-spacing: 0.035em;
}

.sound-pattern {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
  padding: 5px 10px;
  background: var(--gold-light);
  border: 1px solid rgba(196, 152, 47, 0.24);
  border-radius: 999px;
}

.sound-pattern-label {
  color: #8d6713;
  font-size: 0.62rem;
  font-weight: 850;
  letter-spacing: 0.1em;
}

.sound-pattern-text {
  color: var(--forest-deep);
  font-size: 0.84rem;
  font-weight: 750;
}

.answer-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  max-width: 720px;
  margin: 21px auto 14px;
  color: var(--gold);
  font-size: 0.67rem;
  font-weight: 850;
  letter-spacing: 0.17em;
}

.answer-divider::before,
.answer-divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
}

.answer-shell {
  padding-bottom: 8px;
}

.core-answer,
.example-card {
  padding: 17px;
  background: var(--bg-card);
  border: 1px solid var(--line-soft);
  border-radius: 15px;
  box-shadow: 0 6px 18px rgba(18, 64, 39, 0.08);
}

.core-answer {
  margin-bottom: 13px;
}

.japanese-answer {
  margin-top: 4px;
  color: var(--ink-main);
  font-size: 1.62rem;
  font-weight: 850;
}

.pos-badge {
  display: inline-block;
  margin-top: 8px;
  padding: 4px 11px;
  color: var(--forest-deep);
  background: var(--forest-light);
  border: 1px solid rgba(20, 107, 58, 0.17);
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 750;
}

.example-card {
  margin-bottom: 13px;
  border-left: 4px solid var(--gold);
}

.example-prompt {
  margin-bottom: 2px;
}

.example-target {
  margin-top: 12px;
  color: var(--forest-deep);
  font-family: "Noto Serif", Georgia, serif;
  font-size: 1.31rem;
  font-weight: 650;
  line-height: 1.76;
}

.example-japanese {
  margin-top: 12px;
  padding-top: 11px;
  color: var(--ink-main);
  border-top: 1px dashed var(--line-soft);
  font-size: 0.94rem;
}

.detail-block {
  margin: 10px 0 0;
  background: var(--bg-card);
  border: 1px solid var(--line-soft);
  border-radius: 14px;
  overflow: hidden;
  text-align: left;
  box-shadow: 0 5px 15px rgba(18, 64, 39, 0.065);
}

.detail-block summary {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  padding: 13px 15px;
  cursor: pointer;
  font-size: 0.93rem;
  font-weight: 850;
  list-style: none;
  user-select: none;
}

.detail-block summary::-webkit-details-marker {
  display: none;
}

.summary-icon {
  display: inline-block;
  font-size: 0.66rem;
  transition: transform 0.2s ease;
}

.detail-block[open] .summary-icon {
  transform: rotate(45deg);
}

.structure-block summary {
  color: var(--violet-ink);
  background: var(--violet-light);
}

.explanation-block summary {
  color: var(--blue);
  background: var(--blue-light);
}

.bridge-block summary {
  color: var(--green-ink);
  background: var(--green-light);
}

.detail-content {
  padding: 4px 16px 16px;
}

.detail-group {
  margin-top: 13px;
  padding: 12px 13px;
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(215, 224, 218, 0.9);
  border-radius: 11px;
}

.hero-group {
  text-align: center;
  background: linear-gradient(145deg, rgba(230, 243, 235, 0.72), #fff);
}

.segmentation-group {
  text-align: center;
  background: var(--gold-light);
}

.sound-bridge-group {
  border-left: 3px solid var(--blue);
}

.address-group {
  background: linear-gradient(145deg, var(--green-light), #fff);
}

.detail-label {
  margin-bottom: 5px;
  color: var(--ink-soft);
  font-size: 0.72rem;
  font-weight: 850;
  letter-spacing: 0.08em;
}

.detail-text {
  color: var(--ink-main);
}

.pronunciation-detail,
.segmentation-text {
  color: var(--blue);
  font-size: 1.02rem;
  font-weight: 750;
  letter-spacing: 0.035em;
}

.breakdown-text {
  line-height: 1.9;
  white-space: pre-line;
}

.bridge-note {
  padding-left: 10px;
  border-left: 3px solid var(--forest);
}

.source-line {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 7px;
  margin-top: 15px;
  color: #7a857e;
  font-size: 0.72rem;
}

.source-label {
  color: var(--gold);
  font-weight: 850;
  letter-spacing: 0.1em;
}

/* Anki / AnkiDroid dark mode */
.nightMode.card,
.night_mode.card {
  --bg-page: #101915;
  --bg-card: #19241f;
  --ink-main: #f2f7f4;
  --ink-soft: #b8c7be;
  --line-soft: #3b4c43;
  --forest: #73cf98;
  --forest-deep: #e4f8eb;
  --forest-light: #213c2d;
  --gold: #e4bd68;
  --gold-light: #493b20;
  --blue: #91bdf0;
  --blue-light: #263b52;
  --violet-light: #40354d;
  --violet-ink: #eee3ff;
  --green-light: #294236;
  --green-ink: #ddf5e4;
  --shadow: 0 12px 30px rgba(0, 0, 0, 0.36);
  color: var(--ink-main);
  background:
    radial-gradient(circle at 12% -4%, rgba(115, 207, 152, 0.12), transparent 30%),
    radial-gradient(circle at 88% 0%, rgba(228, 189, 104, 0.11), transparent 29%),
    linear-gradient(180deg, #15211b 0%, var(--bg-page) 100%);
}

.nightMode .card-shell,
.night_mode .card-shell,
.nightMode .core-answer,
.night_mode .core-answer,
.nightMode .example-card,
.night_mode .example-card,
.nightMode .detail-block,
.night_mode .detail-block {
  color: var(--ink-main);
  background: var(--bg-card);
  border-color: var(--line-soft);
}

.nightMode .sound-gate,
.night_mode .sound-gate {
  background: linear-gradient(145deg, #213c2d 0%, #1b2b23 100%);
  border-color: #355d45;
}

.nightMode .word-panel,
.night_mode .word-panel {
  background:
    radial-gradient(circle at 90% 10%, rgba(228, 189, 104, 0.09), transparent 34%),
    linear-gradient(145deg, #202c26 0%, #242a21 100%);
  border-color: var(--line-soft);
}

.nightMode .target-word,
.night_mode .target-word,
.nightMode .structure-word,
.night_mode .structure-word,
.nightMode .root-word,
.night_mode .root-word,
.nightMode .example-target,
.night_mode .example-target,
.nightMode .japanese-answer,
.night_mode .japanese-answer,
.nightMode .example-japanese,
.night_mode .example-japanese,
.nightMode .detail-text,
.night_mode .detail-text {
  color: var(--ink-main);
}

.nightMode .sound-instruction,
.night_mode .sound-instruction,
.nightMode .detail-label,
.night_mode .detail-label {
  color: var(--ink-soft);
}

.nightMode .language-chip,
.night_mode .language-chip {
  color: #0e2b1b;
  background: linear-gradient(135deg, #83dca7, #55bd7f);
}

.nightMode .pos-badge,
.night_mode .pos-badge {
  color: #e7f8ed;
  background: #284634;
  border-color: #3f6a4f;
}

.nightMode .sound-pattern,
.night_mode .sound-pattern {
  background: #493b20;
  border-color: #67552d;
}

.nightMode .sound-pattern-label,
.night_mode .sound-pattern-label,
.nightMode .sound-pattern-text,
.night_mode .sound-pattern-text {
  color: #f5d886;
}

.nightMode .detail-group,
.night_mode .detail-group {
  background: rgba(255, 255, 255, 0.035);
  border-color: var(--line-soft);
}

.nightMode .hero-group,
.night_mode .hero-group,
.nightMode .address-group,
.night_mode .address-group {
  background: rgba(115, 207, 152, 0.06);
}

.nightMode .segmentation-group,
.night_mode .segmentation-group {
  background: #44391f;
}

.nightMode .structure-block summary,
.night_mode .structure-block summary {
  color: var(--violet-ink);
  background: var(--violet-light);
}

.nightMode .explanation-block summary,
.night_mode .explanation-block summary {
  color: #e4f3ff;
  background: var(--blue-light);
}

.nightMode .bridge-block summary,
.night_mode .bridge-block summary {
  color: var(--green-ink);
  background: var(--green-light);
}

.nightMode .source-line,
.night_mode .source-line {
  color: #aab7af;
}

@media (max-width: 600px) {
  .card {
    padding: 10px 7px 22px;
    font-size: 16px;
  }

  .card-shell {
    padding: 12px;
    border-radius: 15px;
  }

  .flag-line {
    margin: -12px -12px 13px;
  }

  .language-chip {
    max-width: 62%;
    font-size: 0.62rem;
    letter-spacing: 0.045em;
  }

  .concept-scene img {
    max-height: 320px;
  }

  .target-word {
    font-size: clamp(2.05rem, 12vw, 3rem);
  }

  .example-target {
    font-size: 1.15rem;
  }

  .detail-block summary {
    padding: 12px 8px;
    font-size: 0.82rem;
  }

  .detail-content {
    padding: 3px 10px 12px;
  }

  .detail-group {
    padding: 10px;
  }
}
```

---

## 適用手順

1. ブラジル・ポルトガル語ノートタイプの19番目に`ConceptScene`があることを確認する。
2. 表面テンプレートを本書の表面へ全置換する。
3. 裏面テンプレートを本書の裏面へ全置換する。
4. CSSを追記ではなく全置換する。
5. Core10のC0001とC0010をPC版でプレビューする。
6. 表面で単語TTSが先に再生されることを確認する。
7. ConceptScene、見出し語、発音、音の切れ目を確認する。
8. `Show answer`で`CONCEPT BRIDGE`へ移動することを確認する。
9. 裏面で例文TTSが再生されることを確認する。
10. 3段パネルを開閉する。
11. AnkiWebで復習メニューを再構築する。
12. AnkiDroidへ同期し、ライト・ダーク両モードを実機確認する。

## 重点確認

```text
C0001
```

- 単語音声が最初に再生される。
- C0001のConceptSceneが表示される。
- `Portuguese`と`Pronunciation`が正しい。
- `Root`、`Affixes`、`PerceptualSegmentation`が読みやすい。

```text
C0010
```

- 長い見出し語が画面幅内で折り返す。
- 例文と形態素分解がはみ出さない。
- C0001とは異なるConceptSceneが表示される。
- ダークモードでも緑、金、青の階層が見える。

## TTS

標準指定：

```html
{{tts pt_BR:Portuguese}}
{{tts pt_BR:ExamplePortuguese}}
```

AnkiDroidで音声が出ない場合は、推測でロケールを書き換えず、カード末尾へ一時的に次を置く。

```html
{{tts-voices:}}
```

端末が返したブラジル・ポルトガル語のロケールとVoice IDを、そのまま採用する。診断後は`{{tts-voices:}}`を削除する。

## 重要事項

裏面の次の行は削除しない。

```html
<div id="answer" class="answer-divider">
```

`id="answer"`がAnkiDroidの解答開始位置になる。
