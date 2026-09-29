# MEMORIOPOLIS ロシア語 Anki UI 完全版

更新日：2026-09-29  
言語識別子：`ru`  
対象デッキ：`MEMORIOPOLIS::Russian`  
共通画像フィールド：`ConceptScene`

## 正式17フィールド

このテンプレートは、ロシア語Core10フィールドマスターで確認済みの16フィールドと、追加済みの`ConceptScene`だけを使用する。

```text
1. ID
2. Russian
3. Stress
4. Transliteration
5. Japanese
6. PartOfSpeech
7. RussianGrammar
8. ExampleRussian
9. ExampleStress
10. ExampleTransliteration
11. ExampleJapanese
12. Source
13. Tags
14. ExampleBreakdown
15. ExampleExplanation
16. ExamplePronunciationHint
17. ConceptScene
```

---

## 表面テンプレート

```html
<div class="card-shell">
  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">РУССКИЙ</span>
  </div>

  {{#ConceptScene}}
  <div class="concept-scene">
    {{ConceptScene}}
  </div>
  {{/ConceptScene}}

  <div class="word-panel">
    <div class="target-word ru-text">{{Russian}}</div>

    {{#Stress}}
    <div class="stress-line">{{Stress}}</div>
    {{/Stress}}

    {{#Transliteration}}
    <div class="transliteration">{{Transliteration}}</div>
    {{/Transliteration}}

    <div class="tts-audio word-audio">
      {{tts ru_RU:Russian}}
    </div>
  </div>
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

  {{#ExampleRussian}}
  <section class="example-card">
    <div class="section-kicker">ПРИМЕР</div>
    <div class="example-target ru-text">{{ExampleRussian}}</div>

    {{#ExampleStress}}
    <div class="example-stress">{{ExampleStress}}</div>
    {{/ExampleStress}}

    <div class="tts-audio example-audio">
      {{tts ru_RU:ExampleRussian}}
    </div>

    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleRussian}}

  <details class="detail-block structure-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>語の構造</span>
    </summary>

    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">キリル文字</div>
        <div class="detail-text structure-word ru-text">{{Russian}}</div>
      </div>

      {{#Stress}}
      <div class="detail-group">
        <div class="detail-label">強勢付き表記</div>
        <div class="detail-text stress-detail">{{Stress}}</div>
      </div>
      {{/Stress}}

      {{#Transliteration}}
      <div class="detail-group">
        <div class="detail-label">ラテン文字転写</div>
        <div class="detail-text transliteration-detail">{{Transliteration}}</div>
      </div>
      {{/Transliteration}}

      {{#RussianGrammar}}
      <div class="detail-group">
        <div class="detail-label">文法・語形変化</div>
        <div class="detail-text japanese-text">{{RussianGrammar}}</div>
      </div>
      {{/RussianGrammar}}
    </div>
  </details>

  {{#ExampleBreakdown}}
  <details class="detail-block explanation-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>例文解説</span>
    </summary>

    <div class="detail-content">
      {{#ExampleTransliteration}}
      <div class="detail-group">
        <div class="detail-label">例文転写</div>
        <div class="detail-text example-transliteration">{{ExampleTransliteration}}</div>
      </div>
      {{/ExampleTransliteration}}

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

  {{#ExamplePronunciationHint}}
  <details class="detail-block bridge-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>言語間ブリッジ</span>
    </summary>

    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">音の橋</div>
        <div class="detail-text japanese-text">{{ExamplePronunciationHint}}</div>
      </div>

      <div class="detail-group">
        <div class="detail-label">文字とConceptの橋</div>
        <div class="detail-text japanese-text bridge-note">
          キリル文字、強勢、ラテン文字転写、日本語Concept、Concept画像を同じConcept IDへ接続して観測する。
        </div>
      </div>
    </div>
  </details>
  {{/ExamplePronunciationHint}}

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
  --bg-page: #edf1f5;
  --bg-card: #fbfaf7;
  --ink-main: #172033;
  --ink-soft: #566176;
  --line-soft: #d8dee8;
  --navy: #173b5f;
  --navy-deep: #102a43;
  --blue-light: #e8f1f8;
  --gold: #b88a3b;
  --violet-light: #f0ebf7;
  --violet-ink: #553e6b;
  --green-light: #eaf3ec;
  --green-ink: #355b42;
  --ruby: #9d3f55;
  --ruby-light: #f5e7eb;
  --shadow: 0 10px 28px rgba(27, 43, 65, 0.12);
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
  padding: 18px 12px 28px;
  color: var(--ink-main);
  background:
    radial-gradient(circle at 50% -10%, rgba(184, 138, 59, 0.14), transparent 34%),
    linear-gradient(180deg, #eef2f6 0%, var(--bg-page) 100%);
  font-family: "Noto Sans", "Noto Sans Cyrillic", "Segoe UI", Arial, sans-serif;
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
  padding: 18px;
  background: var(--bg-card);
  border: 1px solid rgba(23, 59, 95, 0.12);
  border-radius: 18px;
  box-shadow: var(--shadow);
}

.topline {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  width: 100%;
  margin-bottom: 12px;
}

.concept-id {
  color: var(--gold);
  font-size: 0.84rem;
  font-weight: 800;
  letter-spacing: 0.14em;
}

.language-chip {
  padding: 4px 11px;
  color: #fff;
  background: var(--ruby);
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.concept-scene {
  display: block;
  width: 100%;
  margin: 10px auto 16px;
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
  border: 1px solid rgba(184, 138, 59, 0.26);
  border-radius: 12px;
  box-shadow: 0 8px 22px rgba(15, 35, 55, 0.16);
}

.word-panel {
  padding: 16px 14px 11px;
  text-align: center;
  background: linear-gradient(145deg, #fff 0%, #faf3f5 100%);
  border: 1px solid var(--line-soft);
  border-radius: 14px;
}

.target-word,
.structure-word {
  color: var(--navy-deep);
  font-family: "Noto Serif", "Noto Serif Cyrillic", Georgia, serif;
  font-weight: 700;
}

.target-word {
  font-size: clamp(2.2rem, 10vw, 3.6rem);
  line-height: 1.2;
  letter-spacing: 0.035em;
}

.structure-word {
  font-size: 1.7rem;
  text-align: center;
}

.stress-line {
  margin-top: 8px;
  color: var(--ruby);
  font-family: "Noto Serif", "Noto Serif Cyrillic", Georgia, serif;
  font-size: 1.18rem;
  font-weight: 650;
  letter-spacing: 0.035em;
}

.transliteration {
  margin-top: 4px;
  color: var(--ink-soft);
  font-size: 0.94rem;
  letter-spacing: 0.04em;
}

.tts-audio {
  margin: 10px auto 0;
  text-align: center;
}

.replay-button svg {
  width: 32px;
  height: 32px;
}

.answer-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  max-width: 720px;
  margin: 20px auto 14px;
  color: var(--gold);
  font-size: 0.67rem;
  font-weight: 800;
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
  box-shadow: 0 6px 18px rgba(27, 43, 65, 0.08);
}

.core-answer {
  margin-bottom: 13px;
}

.info-kicker,
.section-kicker {
  color: var(--gold);
  font-size: 0.67rem;
  font-weight: 800;
  letter-spacing: 0.14em;
}

.japanese-answer {
  margin-top: 4px;
  color: var(--ink-main);
  font-size: 1.62rem;
  font-weight: 800;
}

.pos-badge {
  display: inline-block;
  margin-top: 8px;
  padding: 3px 10px;
  color: var(--ruby);
  background: var(--ruby-light);
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 700;
}

.example-card {
  margin-bottom: 13px;
  border-left: 4px solid var(--gold);
}

.example-target {
  margin-top: 6px;
  color: var(--navy-deep);
  font-family: "Noto Serif", "Noto Serif Cyrillic", Georgia, serif;
  font-size: 1.32rem;
  font-weight: 650;
  line-height: 1.75;
  letter-spacing: 0.01em;
}

.example-stress {
  margin-top: 8px;
  color: var(--ruby);
  font-family: "Noto Serif", "Noto Serif Cyrillic", Georgia, serif;
  font-size: 1.02rem;
  line-height: 1.7;
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
  border-radius: 13px;
  overflow: hidden;
  text-align: left;
  box-shadow: 0 4px 14px rgba(27, 43, 65, 0.06);
}

.detail-block summary {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  padding: 13px 15px;
  cursor: pointer;
  font-weight: 800;
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
  color: var(--navy);
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
  background: rgba(255, 255, 255, 0.66);
  border: 1px solid rgba(216, 222, 232, 0.8);
  border-radius: 10px;
}

.detail-label {
  margin-bottom: 5px;
  color: var(--ink-soft);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.detail-text {
  color: var(--ink-main);
}

.stress-detail {
  color: var(--ruby);
  font-family: "Noto Serif", "Noto Serif Cyrillic", Georgia, serif;
  font-size: 1.18rem;
  text-align: center;
}

.transliteration-detail,
.example-transliteration {
  color: var(--navy);
  font-size: 0.94rem;
  letter-spacing: 0.025em;
}

.breakdown-text {
  line-height: 1.9;
  white-space: pre-line;
}

.bridge-note {
  padding-left: 10px;
  border-left: 3px solid #6a9b74;
}

.source-line {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 7px;
  margin-top: 15px;
  color: #7a8290;
  font-size: 0.72rem;
}

.source-label {
  color: var(--gold);
  font-weight: 800;
  letter-spacing: 0.1em;
}

/* Anki / AnkiDroid dark mode */
.nightMode.card,
.night_mode.card {
  --bg-page: #111820;
  --bg-card: #1a232d;
  --ink-main: #f1f5f9;
  --ink-soft: #b8c5d4;
  --line-soft: #3c4958;
  --navy: #87c7ff;
  --navy-deep: #e2f1ff;
  --blue-light: #263e52;
  --gold: #e4bd68;
  --violet-light: #40354d;
  --violet-ink: #eee3ff;
  --green-light: #294236;
  --green-ink: #ddf5e4;
  --ruby: #f0a3b6;
  --ruby-light: #4d3039;
  --shadow: 0 12px 30px rgba(0, 0, 0, 0.34);
  color: var(--ink-main);
  background:
    radial-gradient(circle at 50% -10%, rgba(228, 189, 104, 0.12), transparent 34%),
    linear-gradient(180deg, #151e27 0%, var(--bg-page) 100%);
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

.nightMode .word-panel,
.night_mode .word-panel {
  background: linear-gradient(145deg, #202b36 0%, #271f23 100%);
  border-color: var(--line-soft);
}

.nightMode .target-word,
.night_mode .target-word,
.nightMode .structure-word,
.night_mode .structure-word,
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

.nightMode .transliteration,
.night_mode .transliteration,
.nightMode .detail-label,
.night_mode .detail-label {
  color: var(--ink-soft);
}

.nightMode .language-chip,
.night_mode .language-chip {
  color: #321a22;
  background: #f0a3b6;
}

.nightMode .pos-badge,
.night_mode .pos-badge {
  color: #ffeaf0;
  background: #59343f;
}

.nightMode .detail-group,
.night_mode .detail-group {
  background: rgba(255, 255, 255, 0.035);
  border-color: var(--line-soft);
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
  color: #aab5c2;
}

@media (max-width: 600px) {
  .card {
    padding: 10px 7px 22px;
    font-size: 16px;
  }

  .card-shell {
    padding: 12px;
    border-radius: 14px;
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

1. ロシア語ノートタイプの17番目に`ConceptScene`があることを確認する。
2. 表面テンプレートを本書の表面へ置き換える。
3. 裏面テンプレートを本書の裏面へ置き換える。
4. CSSは追記ではなく、原則として全置換する。
5. Core10のC0001とC0010をPC版でプレビューする。
6. 強勢記号が文字化けせず表示されることを確認する。
7. `Show answer`で`CONCEPT BRIDGE`へ自動スクロールすることを確認する。
8. 3段プルダウンが開閉することを確認する。
9. `ru_RU`の単語・例文TTSを確認する。
10. AnkiDroidへ同期し、画像、ダークモード、長文折り返しを確認する。

## 重要事項

裏面の次の行は削除しない。

```html
<div id="answer" class="answer-divider">
```

`id="answer"`がAnkiDroidの解答開始位置となる。

## フィールド整合性確認

このテンプレートが参照するフィールドは次の17個のうち、カード表示に必要なフィールドだけである。

```text
ID
Russian
Stress
Transliteration
Japanese
PartOfSpeech
RussianGrammar
ExampleRussian
ExampleStress
ExampleTransliteration
ExampleJapanese
Source
Tags
ExampleBreakdown
ExampleExplanation
ExamplePronunciationHint
ConceptScene
```

`Tags`はノート管理用であり、カード画面には表示しない。未存在フィールドは参照していない。
