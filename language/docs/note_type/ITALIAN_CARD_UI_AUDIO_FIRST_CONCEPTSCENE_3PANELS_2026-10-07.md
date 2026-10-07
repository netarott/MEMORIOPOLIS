# MEMORIOPOLIS Italian Vocabulary

## 正式仕様

- 対象ノートタイプ: `MEMORIOPOLIS Italian Vocabulary`
- フィールドマスター準拠
- 学習経路: **音 → Concept候補 → ConceptScene → 綴り → 例文 → 構造**
- TTSロケール: `it_IT`
- 識別色: イタリア国旗の緑・白・赤、補助色に金
- UI: 音優先、ConceptScene、3段プルダウン
- 対応: Anki Desktop / AnkiDroid / ライトモード / ダークモード

> 注意: `ItalianAudio` フィールドは使用しない。音声は既存の `Italian` と `ExampleItalian` フィールドをAnki TTSで読む。

---

# 表面テンプレート

```html
<div class="mp-card mp-front">
  <div class="mp-header">
    <div class="mp-brand">MEMORIOPOLIS</div>
    <div class="mp-language">ITALIANO</div>
  </div>

  <section class="audio-gate">
    <div class="audio-kicker">ASCOLTA PRIMA</div>
    <div class="audio-guide">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-primary">{{tts it_IT:Italian}}</div>
  </section>

  {{#ConceptScene}}
  <section class="concept-section">
    <div class="section-label">CONCEPT SCENE</div>
    <div class="concept-frame">
      <div class="concept-image">{{ConceptScene}}</div>
    </div>
    <div class="concept-guide">画像から意味の住所を確認する</div>
  </section>
  {{/ConceptScene}}

  <section class="word-section">
    <div class="word-label">ITALIANO</div>
    <div class="headword">{{Italian}}</div>

    {{#Pronunciation}}
    <div class="pronunciation">{{Pronunciation}}</div>
    {{/Pronunciation}}

    {{#PerceptualSegmentation}}
    <div class="sound-segmentation">
      <span class="mini-label">FORMA SONORA</span>
      <span>{{PerceptualSegmentation}}</span>
    </div>
    {{/PerceptualSegmentation}}
  </section>

  <div class="mp-footer">
    <span>{{ID}}</span>
    <span>音からConceptへ</span>
  </div>
</div>
```

---

# 裏面テンプレート

```html
{{FrontSide}}

<div id="answer" class="answer-divider">
  <span>RISPOSTA · 回答</span>
</div>

<div class="mp-card mp-back">
  <section class="meaning-section">
    <div class="section-label gold">JAPANESE CONCEPT</div>
    <div class="japanese-meaning">{{Japanese}}</div>

    {{#PartOfSpeech}}
    <div class="part-of-speech">{{PartOfSpeech}}</div>
    {{/PartOfSpeech}}
  </section>

  {{#ExampleItalian}}
  <section class="example-audio-section">
    <div class="audio-kicker">ASCOLTA LA FRASE</div>
    <div class="audio-guide">例文の音から、見出し語と文意を探す</div>
    <div class="tts-secondary">{{tts it_IT:ExampleItalian}}</div>
  </section>

  <section class="example-section">
    <div class="section-label">ESEMPIO</div>
    <div class="example-italian">{{ExampleItalian}}</div>
    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleItalian}}

  <div class="observation-strip">
    <span>母音</span>
    <span>二重子音</span>
    <span>強勢</span>
    <span>冠詞</span>
    <span>語尾変化</span>
    <span>語順</span>
  </div>

  <div class="detail-panels">
    <details class="detail-panel panel-purple">
      <summary>
        <span class="summary-number">1</span>
        <span class="summary-title">STRUTTURA DELLA PAROLA · 語の構造</span>
        <span class="summary-arrow">⌄</span>
      </summary>
      <div class="detail-content">
        <div class="detail-grid">
          <div class="detail-item full">
            <div class="detail-label">見出し語</div>
            <div class="detail-value italian-value">{{Italian}}</div>
          </div>
          {{#Pronunciation}}
          <div class="detail-item">
            <div class="detail-label">発音</div>
            <div class="detail-value">{{Pronunciation}}</div>
          </div>
          {{/Pronunciation}}
          {{#Root}}
          <div class="detail-item">
            <div class="detail-label">語根・基本要素</div>
            <div class="detail-value">{{Root}}</div>
          </div>
          {{/Root}}
          {{#Affixes}}
          <div class="detail-item">
            <div class="detail-label">接辞・語尾</div>
            <div class="detail-value">{{Affixes}}</div>
          </div>
          {{/Affixes}}
          {{#PerceptualSegmentation}}
          <div class="detail-item">
            <div class="detail-label">音としての切れ目</div>
            <div class="detail-value">{{PerceptualSegmentation}}</div>
          </div>
          {{/PerceptualSegmentation}}
          {{#MorphologicalBreakdown}}
          <div class="detail-item full">
            <div class="detail-label">語構成</div>
            <div class="detail-value">{{MorphologicalBreakdown}}</div>
          </div>
          {{/MorphologicalBreakdown}}
        </div>
      </div>
    </details>

    <details class="detail-panel panel-blue">
      <summary>
        <span class="summary-number">2</span>
        <span class="summary-title">SPIEGAZIONE DELLA FRASE · 例文解説</span>
        <span class="summary-arrow">⌄</span>
      </summary>
      <div class="detail-content">
        {{#ExampleBreakdown}}
        <div class="detail-block">
          <div class="detail-label">文の組み立て</div>
          <div class="detail-value">{{ExampleBreakdown}}</div>
        </div>
        {{/ExampleBreakdown}}
        {{#ExampleExplanation}}
        <div class="detail-block">
          <div class="detail-label">なぜこの日本語訳になる？</div>
          <div class="detail-value">{{ExampleExplanation}}</div>
        </div>
        {{/ExampleExplanation}}
      </div>
    </details>

    <details class="detail-panel panel-green">
      <summary>
        <span class="summary-number">3</span>
        <span class="summary-title">PONTE LINGUISTICO · 言語間ブリッジ</span>
        <span class="summary-arrow">⌄</span>
      </summary>
      <div class="detail-content">
        {{#MeaningBridge}}
        <div class="detail-block">
          <div class="detail-label">意味の橋</div>
          <div class="detail-value">{{MeaningBridge}}</div>
        </div>
        {{/MeaningBridge}}
        {{#SoundBridge}}
        <div class="detail-block">
          <div class="detail-label">音の橋</div>
          <div class="detail-value">{{SoundBridge}}</div>
        </div>
        {{/SoundBridge}}
        {{#UsageNote}}
        <div class="detail-block">
          <div class="detail-label">用法とConcept境界</div>
          <div class="detail-value">{{UsageNote}}</div>
        </div>
        {{/UsageNote}}
        <div class="memory-address">
          <div class="detail-label">記憶都市の住所</div>
          <div class="address-line">
            <span class="address-id">{{ID}}</span>
            <span class="detail-value">音、語形、強勢、ConceptScene、例文を同じConceptへ接続する。</span>
          </div>
        </div>
      </div>
    </details>
  </div>

  <div class="source-footer">
    <span>{{#Source}}Source: {{Source}}{{/Source}}</span>
    <span>{{ID}}</span>
  </div>
</div>
```

---

# CSS

```css
:root {
  --bg: #f4f1e9;
  --card: #fffdf8;
  --ink: #1f211d;
  --muted: #6d7068;
  --line: #d8d5ca;
  --italian: #176b42;
  --italian-2: #2b8a58;
  --red: #c43d3d;
  --gold: #b88a32;
  --gold-soft: #f1e4c4;
  --audio-bg: #e8f2eb;
  --example-bg: #eef5f0;
  --shadow: 0 12px 34px rgba(35, 55, 42, 0.11);
  --purple: #6c4ea1;
  --blue: #34658d;
  --green: #2f7357;
}

* { box-sizing: border-box; }

.card {
  margin: 0;
  padding: 18px 12px 34px;
  background: radial-gradient(circle at top right, rgba(196, 61, 61, 0.09), transparent 32%), var(--bg);
  color: var(--ink);
  font-family: "Noto Sans JP", "Noto Sans", "Segoe UI", Arial, sans-serif;
  font-size: 17px;
  line-height: 1.72;
  text-align: left;
  -webkit-text-size-adjust: 100%;
}

.mp-card {
  width: min(100%, 760px);
  margin: 0 auto;
  padding: 22px;
  background: var(--card);
  border: 1px solid rgba(23, 107, 66, 0.14);
  border-radius: 24px;
  box-shadow: var(--shadow);
  overflow: hidden;
}

.mp-front { position: relative; }
.mp-front::before {
  content: "";
  display: block;
  position: absolute;
  inset: 0 0 auto 0;
  height: 6px;
  background: linear-gradient(90deg, #16804a 0 33.3%, #f7f4e8 33.3% 66.6%, #c73939 66.6% 100%);
}

.mp-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin: 4px 0 20px;
  padding-bottom: 13px;
  border-bottom: 1px solid var(--line);
}

.mp-brand {
  color: var(--italian);
  font-family: Georgia, "Times New Roman", serif;
  font-size: 0.92rem;
  font-weight: 800;
  letter-spacing: 0.13em;
}

.mp-language {
  padding: 5px 11px;
  color: #fff;
  background: var(--italian);
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.14em;
}

.audio-gate, .example-audio-section {
  padding: 18px 16px;
  text-align: center;
  background: var(--audio-bg);
  border: 1px solid rgba(23, 107, 66, 0.15);
  border-radius: 18px;
}

.audio-kicker { color: var(--italian); font-size: 0.78rem; font-weight: 900; letter-spacing: 0.15em; }
.audio-guide { margin-top: 4px; color: var(--muted); font-size: 0.85rem; }
.tts-primary, .tts-secondary { margin-top: 12px; min-height: 24px; }
.replay-button, .tts-button {
  color: #fff !important;
  background: var(--italian) !important;
  border: 0 !important;
  border-radius: 999px !important;
  box-shadow: 0 5px 12px rgba(23, 107, 66, 0.18);
}

.concept-section { margin-top: 20px; text-align: center; }
.section-label { margin-bottom: 9px; color: var(--italian); font-size: 0.73rem; font-weight: 900; letter-spacing: 0.15em; }
.section-label.gold { color: #8b651f; }
.concept-frame {
  overflow: hidden;
  width: min(100%, 520px);
  margin: 0 auto;
  background: #e9e6dc;
  border: 3px solid var(--gold-soft);
  border-radius: 22px;
  box-shadow: 0 9px 24px rgba(34, 45, 38, 0.13);
}
.concept-image { display: block; width: 100%; max-height: 390px; object-fit: contain; }
.concept-image img { display: block; width: 100%; max-height: 390px; object-fit: contain; }
.concept-guide { margin-top: 8px; color: var(--muted); font-size: 0.82rem; }

.word-section { margin-top: 24px; text-align: center; }
.word-label { color: var(--red); font-size: 0.72rem; font-weight: 900; letter-spacing: 0.18em; }
.headword {
  overflow-wrap: anywhere;
  margin-top: 4px;
  color: var(--italian);
  font-family: Georgia, "Noto Serif", serif;
  font-size: clamp(2.05rem, 9vw, 3.9rem);
  font-weight: 750;
  line-height: 1.12;
  hyphens: auto;
}
.pronunciation { margin-top: 9px; color: var(--muted); font-family: "Noto Sans", "Segoe UI", sans-serif; font-size: 1rem; }
.sound-segmentation {
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 7px;
  margin-top: 13px;
  padding: 7px 12px;
  color: var(--italian);
  background: #f0eee6;
  border-radius: 12px;
  font-size: 0.88rem;
}
.mini-label { color: var(--red); font-weight: 900; letter-spacing: 0.08em; }

.mp-footer, .source-footer {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-top: 24px;
  padding-top: 13px;
  color: var(--muted);
  border-top: 1px solid var(--line);
  font-size: 0.72rem;
}

.answer-divider { position: relative; width: min(100%, 760px); margin: 20px auto; text-align: center; scroll-margin-top: 10px; }
.answer-divider::before { content: ""; position: absolute; top: 50%; left: 0; right: 0; height: 1px; background: linear-gradient(90deg, transparent, var(--gold), transparent); }
.answer-divider span { position: relative; z-index: 1; display: inline-block; padding: 5px 13px; color: #7a591f; background: var(--bg); font-size: 0.71rem; font-weight: 900; letter-spacing: 0.14em; }

.meaning-section { text-align: center; }
.japanese-meaning { color: var(--ink); font-family: "Noto Serif JP", "Yu Mincho", serif; font-size: clamp(1.65rem, 6.5vw, 2.65rem); font-weight: 700; line-height: 1.35; }
.part-of-speech { display: inline-block; margin-top: 10px; padding: 4px 10px; color: #775619; background: var(--gold-soft); border-radius: 999px; font-size: 0.75rem; font-weight: 700; }
.example-audio-section { margin-top: 23px; }
.example-section { margin-top: 20px; padding: 20px 18px; background: var(--example-bg); border-left: 5px solid var(--italian-2); border-radius: 16px; }
.example-italian { color: var(--italian); font-family: Georgia, "Noto Serif", serif; font-size: clamp(1.25rem, 4.8vw, 1.85rem); font-weight: 700; line-height: 1.55; }
.example-japanese { margin-top: 13px; padding-top: 12px; color: var(--ink); border-top: 1px solid rgba(23, 107, 66, 0.15); font-size: 1rem; }

.observation-strip { display: flex; flex-wrap: wrap; justify-content: center; gap: 7px; margin: 18px 0 2px; }
.observation-strip span { padding: 4px 9px; color: var(--italian); background: #ede8d9; border-radius: 999px; font-size: 0.68rem; font-weight: 750; }
.detail-panels { margin-top: 20px; }
.detail-panel { overflow: hidden; margin: 12px 0; background: #fff; border: 1px solid var(--line); border-radius: 16px; scroll-margin-top: 10px; }
.detail-panel summary { display: flex; align-items: center; gap: 10px; padding: 15px 14px; color: #fff; cursor: pointer; list-style: none; user-select: none; }
.detail-panel summary::-webkit-details-marker { display: none; }
.panel-purple summary { background: linear-gradient(135deg, #59417f, var(--purple)); }
.panel-blue summary { background: linear-gradient(135deg, #284f70, var(--blue)); }
.panel-green summary { background: linear-gradient(135deg, #234f3e, var(--green)); }
.summary-number { display: grid; flex: 0 0 28px; height: 28px; place-items: center; background: rgba(255, 255, 255, 0.18); border-radius: 50%; font-weight: 900; }
.summary-title { flex: 1; font-size: 0.82rem; font-weight: 900; letter-spacing: 0.05em; }
.summary-arrow { font-size: 1.2rem; transition: transform 0.2s ease; }
.detail-panel[open] .summary-arrow { transform: rotate(180deg); }
.detail-content { padding: 16px; background: var(--card); }
.detail-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.detail-item, .detail-block, .memory-address { padding: 12px; background: #f5f3ec; border-radius: 12px; }
.detail-item.full { grid-column: 1 / -1; }
.detail-block + .detail-block { margin-top: 12px; }
.memory-address { margin-top: 12px; background: var(--gold-soft); }
.detail-label { margin-bottom: 5px; color: var(--muted); font-size: 0.69rem; font-weight: 900; letter-spacing: 0.05em; }
.detail-value { overflow-wrap: anywhere; color: var(--ink); font-size: 0.93rem; }
.italian-value { color: var(--italian); font-family: Georgia, "Noto Serif", serif; font-size: 1.15rem; font-weight: 700; }
.address-line { display: flex; align-items: flex-start; gap: 10px; }
.address-id { flex: 0 0 auto; padding: 3px 8px; color: #fff; background: var(--italian); border-radius: 999px; font-size: 0.73rem; font-weight: 900; }

.nightMode, .night_mode {
  --bg: #111714;
  --card: #19221d;
  --ink: #edf3ef;
  --muted: #aebbb3;
  --line: #344139;
  --italian: #8bd0a7;
  --italian-2: #69b88b;
  --red: #ef8a8a;
  --gold: #e1b761;
  --gold-soft: #3d3422;
  --audio-bg: #1c3028;
  --example-bg: #1d2c25;
  --shadow: 0 15px 38px rgba(0, 0, 0, 0.38);
}
.nightMode .detail-item, .nightMode .detail-block, .night_mode .detail-item, .night_mode .detail-block { background: #222d27; }
.nightMode .detail-panel, .night_mode .detail-panel { background: #19221d; }
.nightMode .observation-strip span, .night_mode .observation-strip span { color: #deeadf; background: #27342d; }
.nightMode .sound-segmentation, .night_mode .sound-segmentation { background: #27342d; }

@media (max-width: 520px) {
  .card { padding: 8px 5px 25px; font-size: 16px; }
  .mp-card { padding: 16px 13px; border-radius: 18px; }
  .mp-header { align-items: flex-start; }
  .mp-brand { font-size: 0.78rem; }
  .detail-grid { grid-template-columns: 1fr; }
  .detail-item.full { grid-column: auto; }
  .source-footer, .mp-footer { flex-direction: column; gap: 3px; }
}
```

---

# 適用手順

1. Anki Desktopで `MEMORIOPOLIS Italian Vocabulary` を開く。
2. 「カード」を開く。
3. **表面テンプレートを上記コードで全置換**する。
4. **裏面テンプレートを上記コードで全置換**する。
5. **スタイルを上記CSSで全置換**する。
6. 保存する。
7. C0001とC0010をプレビューする。
8. 同期後、AnkiDroidで実機確認する。

CSSは追記ではなく、既存内容を全置換する。

---

# 今回のエラー修正点

誤って参照していた次のフィールドは存在しない。

```html
{{ItalianAudio}}
```

正式版では以下を使用する。

```html
{{tts it_IT:Italian}}
```

例文音声は以下を使用する。

```html
{{tts it_IT:ExampleItalian}}
```

---

# イタリア語での観測点

## 母音

イタリア語では母音が語の輪郭を作る。カタカナへ一括変換せず、子音の間にある母音を保って聞く。

## 二重子音

二重子音は、単なる綴りの重複ではなく、子音を保つ時間の差として観測する。前後の母音と一緒に音声で確認する。

## 強勢

強勢位置は語の聴覚的な住所になる。`Pronunciation` と `PerceptualSegmentation` を使い、強勢のある音節を中心に語全体を回収する。

## 冠詞と名詞

見出し語が名詞の場合、例文では冠詞、性、数との結び付きを観測する。単語単体だけで固定せず、例文のまとまりでConceptへ接続する。

## 語尾変化

名詞・形容詞・動詞の語尾は、性・数・人称・時制などの情報を担う。語根と語尾を分断しすぎず、意味の変化として捉える。

## 綴りと音

`c`、`g`、`ch`、`gh`、`sc`、`gn`、`gl` などは、後続母音との組み合わせで音が変わる。文字単体ではなく、まとまりとして聞く。

---

# 最初の確認項目

## C0001

```text
単語TTS
ConceptScene
見出し語
発音
音としての切れ目
日本語Concept
例文TTS
3段パネル
```

## C0010

```text
長い語の折り返し
長い例文
ConceptScene
ダークモード
解答開始位置への自動スクロール
3段パネル
```

## TTS

```html
{{tts it_IT:Italian}}
```

```html
{{tts it_IT:ExampleItalian}}
```

AnkiDroidで音が出ない場合、ロケールやVoice IDを推測で変更しない。カードへ一時的に次を追加し、端末が返す実在音声を確認する。

```html
{{tts-voices:}}
```

確認後は `{{tts-voices:}}` を削除する。

---

# 次工程

1. C0001とC0010をAnki Desktopでプレビュー
2. AnkiDroidへ同期して実機確認
3. `E0001_it.md` を作成
4. イタリア語Core20を作成
