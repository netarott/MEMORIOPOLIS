# MEMORIOPOLIS フィリピン語 Anki UI 完全版

更新日：2026-09-30  
言語識別子：`fil`  
対象デッキ：`MEMORIOPOLIS::Filipino`  
共通画像フィールド：`ConceptScene`  
設計テーマ：`音 → 図 → Concept → 単語 → 例文`

## 正式19フィールド

```text
1. ID
2. Filipino
3. Pronunciation
4. Japanese
5. PartOfSpeech
6. UsageNote
7. ExampleFilipino
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

このテンプレートは上記19フィールドだけを使用する。`CourseTags`は管理用であり、カード画面には表示しない。

---

## 表面テンプレート

```html
<div class="card-shell">
  <div class="topline">
    <span class="concept-id">{{ID}}</span>
    <span class="language-chip">FILIPINO</span>
  </div>

  <div class="sound-gate">
    <div class="sound-kicker">PAKINGGAN MUNA</div>
    <div class="sound-instruction">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-audio word-audio">
      {{tts fil_PH:Filipino}}
    </div>
  </div>

  {{#ConceptScene}}
  <div class="concept-scene">
    {{ConceptScene}}
  </div>
  {{/ConceptScene}}

  <div class="word-panel">
    <div class="target-word fil-text">{{Filipino}}</div>

    {{#Pronunciation}}
    <div class="pronunciation">{{Pronunciation}}</div>
    {{/Pronunciation}}
  </div>
</div>
```

### 表面の役割

```text
単語音声
  ↓
心の中で検索
  ↓
ConceptScene
  ↓
Concept ID
  ↓
フィリピン語見出し語
```

`Filipino`フィールドのTTSが先に再生され、画像がConceptの共通住所として働く。

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

  {{#ExampleFilipino}}
  <section class="example-card">
    <div class="section-kicker">PAKINGGAN ANG PANGUNGUSAP</div>
    <div class="sound-instruction example-prompt">例文の音から、見出し語と文意を探す</div>

    <div class="tts-audio example-audio">
      {{tts fil_PH:ExampleFilipino}}
    </div>

    <div class="example-target fil-text">{{ExampleFilipino}}</div>

    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleFilipino}}

  <details class="detail-block structure-block">
    <summary>
      <span class="summary-icon">◆</span>
      <span>語の構造</span>
    </summary>

    <div class="detail-content">
      <div class="detail-group">
        <div class="detail-label">見出し語</div>
        <div class="detail-text structure-word fil-text">{{Filipino}}</div>
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
        <div class="detail-text root-word fil-text">{{Root}}</div>
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
    <summary>
      <span class="summary-icon">◆</span>
      <span>例文解説</span>
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
      <span>言語間ブリッジ</span>
    </summary>

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
        <div class="detail-text japanese-text bridge-note">
          音、ConceptScene、日本語Concept、語根、接辞、例文を同じConcept IDへ接続して観測する。
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
  --sun: #c8871d;
  --sun-light: #fff1d5;
  --sea: #237a8b;
  --sea-light: #e2f2f4;
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
    radial-gradient(circle at 50% -10%, rgba(200, 135, 29, 0.16), transparent 34%),
    linear-gradient(180deg, #eef4f5 0%, var(--bg-page) 100%);
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
  padding: 18px;
  background: var(--bg-card);
  border: 1px solid rgba(35, 122, 139, 0.14);
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
  background: var(--sea);
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.sound-gate {
  margin-bottom: 14px;
  padding: 13px 14px;
  background: linear-gradient(145deg, var(--sea-light) 0%, #f7fbfc 100%);
  border: 1px solid rgba(35, 122, 139, 0.24);
  border-radius: 13px;
}

.sound-kicker,
.section-kicker,
.info-kicker {
  color: var(--gold);
  font-size: 0.67rem;
  font-weight: 800;
  letter-spacing: 0.14em;
}

.sound-instruction {
  margin-top: 3px;
  color: var(--ink-soft);
  font-size: 0.78rem;
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
  padding: 16px 14px 12px;
  text-align: center;
  background: linear-gradient(145deg, #fff 0%, #fff8e9 100%);
  border: 1px solid var(--line-soft);
  border-radius: 14px;
}

.target-word,
.structure-word,
.root-word {
  color: var(--navy-deep);
  font-family: "Noto Serif", Georgia, serif;
  font-weight: 700;
}

.target-word {
  font-size: clamp(2.2rem, 10vw, 3.6rem);
  line-height: 1.18;
  letter-spacing: 0.025em;
}

.structure-word {
  font-size: 1.7rem;
  text-align: center;
}

.root-word {
  font-size: 1.25rem;
  text-align: center;
}

.pronunciation {
  margin-top: 8px;
  color: var(--sea);
  font-size: 0.96rem;
  letter-spacing: 0.035em;
}

.tts-audio {
  margin: 10px auto 0;
  text-align: center;
}

.replay-button svg {
  width: 34px;
  height: 34px;
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
  color: #8d5c0c;
  background: var(--sun-light);
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 700;
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
  color: var(--navy-deep);
  font-family: "Noto Serif", Georgia, serif;
  font-size: 1.3rem;
  font-weight: 650;
  line-height: 1.75;
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

.segmentation-group {
  text-align: center;
  background: var(--sun-light);
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

.pronunciation-detail,
.segmentation-text {
  color: var(--sea);
  font-size: 1.02rem;
  font-weight: 700;
  letter-spacing: 0.035em;
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
  --sun: #efb44e;
  --sun-light: #493a21;
  --sea: #8bd5df;
  --sea-light: #213b40;
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

.nightMode .sound-gate,
.night_mode .sound-gate {
  background: linear-gradient(145deg, #213a40 0%, #1d2932 100%);
  border-color: #365a62;
}

.nightMode .word-panel,
.night_mode .word-panel {
  background: linear-gradient(145deg, #202b36 0%, #2a261d 100%);
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
  color: #10272b;
  background: #8bd5df;
}

.nightMode .pos-badge,
.night_mode .pos-badge {
  color: #ffecc8;
  background: #534325;
}

.nightMode .detail-group,
.night_mode .detail-group {
  background: rgba(255, 255, 255, 0.035);
  border-color: var(--line-soft);
}

.nightMode .segmentation-group,
.night_mode .segmentation-group {
  background: #42371f;
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

1. フィリピン語ノートタイプの19番目に`ConceptScene`があることを確認する。
2. 表面テンプレートを本書の表面へ全置換する。
3. 裏面テンプレートを本書の裏面へ全置換する。
4. CSSを追記ではなく全置換する。
5. Core10のC0001とC0010をPC版でプレビューする。
6. 表面で単語TTSが再生されることを確認する。
7. ConceptScene、見出し語、発音が表示されることを確認する。
8. `Show answer`で`CONCEPT BRIDGE`へ移動することを確認する。
9. 裏面で例文TTSが再生されることを確認する。
10. 3段プルダウンを確認する。
11. AnkiDroidへ同期し、ライト・ダーク両モードを確認する。

## 重点確認

```text
C0001 rekord
```

- `re-kord /reˈkord/`が表示される。
- `Root`と`PerceptualSegmentation`が読みやすい。
- 例文音声が自然に再生される。

```text
C0010
```

- 長い見出し語や接辞情報が折り返される。
- 形態素分解が画面幅からはみ出さない。
- ConceptSceneがC0001とは異なる。

## TTSについて

標準設定は次のとおり。

```html
{{tts fil_PH:Filipino}}
{{tts fil_PH:ExampleFilipino}}
```

AnkiDroid端末で`fil_PH`音声が見つからない場合は、端末のTTS音声一覧を確認する。端末側でフィリピン語が`fil-PH`または`Filipino (Philippines)`として表示される場合がある。

## 重要事項

裏面の次の行は削除しない。

```html
<div id="answer" class="answer-divider">
```

この`id="answer"`が、AnkiDroidの解答開始位置になる。
