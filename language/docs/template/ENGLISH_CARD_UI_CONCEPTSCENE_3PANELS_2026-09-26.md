# MEMORIOPOLIS English Vocabulary UI

更新日：2026-09-26  
対象ノートタイプ：`MEMORIOPOLIS English Vocabulary`  
前提：既存16フィールドの末尾に `ConceptScene` を追加済み

## フィールド順

1. ID
2. English
3. IPA
4. Japanese
5. PartOfSpeech
6. EnglishGrammar
7. ExampleEnglish
8. ExampleIPA
9. ExampleJapanese
10. Source
11. CourseTags
12. ExampleBreakdown
13. ExampleExplanation
14. ExamplePronunciationHint
15. UsageNote
16. ConceptContrast
17. ConceptScene

---

## Front Template

```html
<div class="card-shell">
  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">ENGLISH</span>
  </div>

  {{#ConceptScene}}
  <div class="concept-scene">
    {{ConceptScene}}
  </div>
  {{/ConceptScene}}

  <div class="word-panel">
    <div class="target-word">{{English}}</div>

    {{#IPA}}
    <div class="pronunciation">{{IPA}}</div>
    {{/IPA}}

    <div class="tts-audio word-audio">
      {{tts en_US:English}}
    </div>
  </div>
</div>
```

---

## Back Template

```html
{{FrontSide}}

<div class="answer-divider">
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

  {{#ExampleEnglish}}
  <section class="example-card">
    <div class="section-kicker">EXAMPLE</div>
    <div class="example-target">{{ExampleEnglish}}</div>

    <div class="tts-audio example-audio">
      {{tts en_US:ExampleEnglish}}
    </div>

    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleEnglish}}

  {{#EnglishGrammar}}
  <details class="detail-block structure-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>語の構造</span>
    </summary>
    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">文法・語法</div>
        <div class="detail-text japanese-text">{{EnglishGrammar}}</div>
      </div>

      {{#UsageNote}}
      <div class="detail-group">
        <div class="detail-label">使い方</div>
        <div class="detail-text japanese-text">{{UsageNote}}</div>
      </div>
      {{/UsageNote}}

      {{#IPA}}
      <div class="detail-group compact-group">
        <div class="detail-label">語の発音</div>
        <div class="detail-text ipa-detail">{{IPA}}</div>
      </div>
      {{/IPA}}
    </div>
  </details>
  {{/EnglishGrammar}}

  {{#ExampleBreakdown}}
  <details class="detail-block explanation-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>例文解説</span>
    </summary>
    <div class="detail-content">
      {{#ExampleIPA}}
      <div class="detail-group">
        <div class="detail-label">例文IPA</div>
        <div class="detail-text example-ipa">{{ExampleIPA}}</div>
      </div>
      {{/ExampleIPA}}

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

  {{#ConceptContrast}}
  <details class="detail-block bridge-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>言語間ブリッジ</span>
    </summary>
    <div class="detail-content">
      {{#ExamplePronunciationHint}}
      <div class="detail-group">
        <div class="detail-label">音の橋</div>
        <div class="detail-text japanese-text">{{ExamplePronunciationHint}}</div>
      </div>
      {{/ExamplePronunciationHint}}

      {{#UsageNote}}
      <div class="detail-group">
        <div class="detail-label">意味と用法の橋</div>
        <div class="detail-text japanese-text">{{UsageNote}}</div>
      </div>
      {{/UsageNote}}

      <div class="detail-group">
        <div class="detail-label">Conceptの境界</div>
        <div class="detail-text japanese-text contrast-text">{{ConceptContrast}}</div>
      </div>
    </div>
  </details>
  {{/ConceptContrast}}

  {{#Source}}
  <div class="source-line">
    <span class="source-label">SOURCE</span>
    <span>{{Source}}</span>
  </div>
  {{/Source}}
</div>
```

---

## Styling

```css
:root {
  --bg-page: #edf1f5;
  --bg-card: #fbfaf7;
  --bg-panel: #ffffff;
  --ink-main: #172033;
  --ink-soft: #566176;
  --line-soft: #d8dee8;
  --navy: #173b5f;
  --navy-deep: #102a43;
  --blue-light: #e8f1f8;
  --gold: #b88a3b;
  --gold-light: #f5ead4;
  --violet-light: #f0ebf7;
  --violet-ink: #553e6b;
  --green-light: #eaf3ec;
  --green-ink: #355b42;
  --shadow: 0 10px 28px rgba(27, 43, 65, 0.12);
}

.card {
  box-sizing: border-box;
  margin: 0;
  padding: 18px 12px 28px;
  color: var(--ink-main);
  background:
    radial-gradient(circle at 50% -10%, rgba(184, 138, 59, 0.14), transparent 34%),
    linear-gradient(180deg, #eef2f6 0%, var(--bg-page) 100%);
  font-family: "Noto Sans", "Segoe UI", Arial, sans-serif;
  font-size: 18px;
  line-height: 1.65;
  text-align: center;
  overflow-wrap: anywhere;
}

.card-shell,
.answer-shell {
  box-sizing: border-box;
  width: min(100%, 720px);
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
  margin-bottom: 12px;
}

.concept-id {
  color: var(--gold);
  font-size: 0.84rem;
  font-weight: 800;
  letter-spacing: 0.14em;
}

.language-chip {
  padding: 4px 10px;
  color: #ffffff;
  background: var(--navy);
  border-radius: 999px;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.14em;
}

.concept-scene {
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
  padding: 16px 14px 10px;
  background: linear-gradient(145deg, #ffffff 0%, #f5f8fb 100%);
  border: 1px solid var(--line-soft);
  border-radius: 14px;
}

.target-word {
  color: var(--navy-deep);
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(2rem, 8vw, 3.15rem);
  font-weight: 700;
  line-height: 1.14;
  letter-spacing: 0.01em;
}

.pronunciation {
  margin-top: 7px;
  color: var(--ink-soft);
  font-size: 1rem;
  letter-spacing: 0.03em;
}

.tts-audio {
  margin: 10px auto 0;
}

.replay-button svg {
  width: 32px;
  height: 32px;
}

.answer-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  width: min(100%, 720px);
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
  color: var(--navy);
  background: var(--blue-light);
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
  font-family: Georgia, "Times New Roman", serif;
  font-size: 1.22rem;
  font-weight: 650;
  line-height: 1.55;
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

.ipa-detail,
.example-ipa {
  color: var(--navy);
  font-size: 0.94rem;
}

.breakdown-text {
  line-height: 1.85;
}

.contrast-text {
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
  --bg-panel: #202b36;
  --ink-main: #f1f5f9;
  --ink-soft: #b8c5d4;
  --line-soft: #3c4958;
  --navy: #87c7ff;
  --navy-deep: #dceeff;
  --blue-light: #263e52;
  --gold: #e4bd68;
  --gold-light: #4a3b25;
  --violet-light: #40354d;
  --violet-ink: #eee3ff;
  --green-light: #294236;
  --green-ink: #ddf5e4;
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
  background: linear-gradient(145deg, #202b36 0%, #1b2530 100%);
  border-color: var(--line-soft);
}

.nightMode .target-word,
.night_mode .target-word,
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

.nightMode .pronunciation,
.night_mode .pronunciation,
.nightMode .detail-label,
.night_mode .detail-label {
  color: var(--ink-soft);
}

.nightMode .language-chip,
.night_mode .language-chip {
  color: #102130;
  background: #8fcaff;
}

.nightMode .pos-badge,
.night_mode .pos-badge {
  color: #e5f3ff;
  background: #284157;
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
    font-size: clamp(2rem, 12vw, 2.7rem);
  }

  .example-target {
    font-size: 1.12rem;
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

## 導入時の確認

1. C0001の`ConceptScene`へCore10画像を登録する。
2. 表面で `C0001 → 画像 → record → IPA → TTS` の順に表示される。
3. 裏面で日本語、品詞、例文、例文TTS、日本語訳が初期表示される。
4. 三つのプルダウンが開閉できる。
5. AnkiDroidのダークモードで見出し語、例文、プルダウン本文が読める。
6. C0002以降の画像未登録カードで空枠が出ない。
7. Source表示が `section12_en` になっている。

## 設計メモ

- `EnglishGrammar`と`UsageNote`は「語の構造」へ収納。
- `ExampleIPA`、`ExampleBreakdown`、`ExampleExplanation`は「例文解説」へ収納。
- `ExamplePronunciationHint`、`UsageNote`、`ConceptContrast`は「言語間ブリッジ」へ収納。
- `UsageNote`は「語の構造」と「言語間ブリッジ」に重複表示する。実機で重複が気になる場合は、言語間ブリッジ側の`UsageNote`ブロックだけ削除する。
- Core20追加後も同じ17フィールドを使える。
