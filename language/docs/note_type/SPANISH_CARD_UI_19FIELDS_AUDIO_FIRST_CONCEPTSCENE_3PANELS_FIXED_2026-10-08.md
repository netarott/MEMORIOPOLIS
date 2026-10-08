# MEMORIOPOLIS Spanish Vocabulary

## 正式仕様

- 対象ノートタイプ: `MEMORIOPOLIS Spanish Vocabulary`
- フィールド数: 19
- 学習経路: **音 → Concept候補 → ConceptScene → 綴り → 例文 → 構造**
- TTSロケール: `es_ES`
- 識別色: 深紅、金、濃紺
- 対応: Anki Desktop / AnkiDroid / ライトモード / ダークモード

---

# 表面テンプレート

```html
<div class="mp-card mp-front" lang="es">
  <header class="mp-header">
    <div class="mp-brand">MEMORIOPOLIS</div>
    <div class="mp-language">ESPAÑOL</div>
  </header>

  <section class="audio-gate">
    <div class="audio-kicker">ESCUCHA PRIMERO</div>
    <div class="audio-guide">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-primary">{{tts es_ES:Spanish}}</div>
  </section>

  {{#ConceptScene}}
  <section class="concept-section">
    <div class="section-label">CONCEPT SCENE</div>
    <div class="concept-frame">
      <div class="concept-media">{{ConceptScene}}</div>
    </div>
    <div class="concept-guide">画像から意味の住所を確認する</div>
  </section>
  {{/ConceptScene}}

  <section class="word-section">
    <div class="word-label">ESPAÑOL</div>
    <div class="headword">{{Spanish}}</div>

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

  <footer class="mp-footer">
    <span>{{ID}}</span>
    <span>音からConceptへ</span>
  </footer>
</div>
```

---

# 裏面テンプレート

```html
{{FrontSide}}

<div id="answer" class="answer-divider" aria-label="Respuesta">
  <span>RESPUESTA · 回答</span>
</div>

<div class="mp-card mp-back" lang="es">
  <section class="meaning-section">
    <div class="section-label gold">JAPANESE CONCEPT</div>
    <div class="japanese-meaning">{{Japanese}}</div>

    {{#PartOfSpeech}}
    <div class="part-of-speech">{{PartOfSpeech}}</div>
    {{/PartOfSpeech}}
  </section>

  {{#ExampleSpanish}}
  <section class="example-audio-section">
    <div class="audio-kicker">ESCUCHA LA FRASE</div>
    <div class="audio-guide">例文の音から、見出し語と文意を探す</div>
    <div class="tts-secondary">{{tts es_ES:ExampleSpanish}}</div>
  </section>

  <section class="example-section">
    <div class="section-label">FRASE DE EJEMPLO</div>
    <div class="example-spanish">{{ExampleSpanish}}</div>

    {{#ExampleJapanese}}
    <div class="example-japanese">{{ExampleJapanese}}</div>
    {{/ExampleJapanese}}
  </section>
  {{/ExampleSpanish}}

  <section class="observation-strip">
    <span>語形成</span>
    <span>再帰動詞</span>
    <span>動詞活用</span>
    <span>性数一致</span>
    <span>強勢</span>
    <span>r音</span>
  </section>

  <section class="detail-panels">
    <details class="detail-panel panel-purple">
      <summary>
        <span class="summary-number">1</span>
        <span class="summary-title">ESTRUCTURA · 語の構造</span>
        <span class="summary-arrow">⌄</span>
      </summary>
      <div class="detail-content">
        <div class="detail-grid">
          <div class="detail-item full">
            <div class="detail-label">見出し語</div>
            <div class="detail-value spanish-value">{{Spanish}}</div>
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
            <div class="detail-label">接辞・分離要素</div>
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
        <span class="summary-title">GUÍA DE LA FRASE · 例文解説</span>
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

    <details class="detail-panel panel-red">
      <summary>
        <span class="summary-number">3</span>
        <span class="summary-title">PUENTE CONCEPTUAL · 言語間ブリッジ</span>
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
            <span>音、綴り、語形成、ConceptScene、例文を同じConceptへ接続する。</span>
          </div>
        </div>
      </div>
    </details>
  </section>

  <footer class="source-footer">
    {{#Source}}<span>Source: {{Source}}</span>{{/Source}}
    {{#CourseTags}}<span>{{CourseTags}}</span>{{/CourseTags}}
    <span>{{ID}}</span>
  </footer>
</div>

<script>
(function () {
  var answer = document.getElementById('answer');
  if (!answer) return;

  window.setTimeout(function () {
    try {
      answer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch (e) {
      answer.scrollIntoView(true);
    }
  }, 180);

  var panels = document.querySelectorAll('.detail-panel');
  panels.forEach(function (panel) {
    panel.addEventListener('toggle', function () {
      if (!panel.open) return;
      window.setTimeout(function () {
        try {
          panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } catch (e) {
          panel.scrollIntoView(true);
        }
      }, 120);
    });
  });
})();
</script>
```

---

# CSS

```css
:root {
  --bg: #f4f1e9;
  --card: #fffdf8;
  --ink: #17211b;
  --muted: #667067;
  --line: #d8d5ca;
  --spanish: #8b1e2d;
  --german-2: #28634f;
  --gold: #b88a32;
  --gold-soft: #f1e4c4;
  --audio-bg: #e4f0eb;
  --example-bg: #edf3f0;
  --shadow: 0 12px 34px rgba(24, 40, 31, 0.11);
  --purple: #6c4ea1;
  --blue: #34658d;
  --red: #a32936;
}

* {
  box-sizing: border-box;
}

.card {
  margin: 0;
  padding: 18px 12px 34px;
  background:
    radial-gradient(circle at top right, rgba(184, 138, 50, 0.10), transparent 32%),
    var(--bg);
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
  border: 1px solid rgba(23, 63, 50, 0.14);
  border-radius: 24px;
  box-shadow: var(--shadow);
  overflow: hidden;
}

.mp-front {
  position: relative;
}

.mp-front::before {
  content: "";
  display: block;
  position: absolute;
  inset: 0 0 auto 0;
  height: 6px;
  background: linear-gradient(90deg, #aa151b 0 25%, #f1bf00 25% 75%, #aa151b 75% 100%);
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
  color: var(--spanish);
  font-family: Georgia, "Times New Roman", serif;
  font-size: 0.92rem;
  font-weight: 800;
  letter-spacing: 0.13em;
}

.mp-language {
  padding: 5px 11px;
  color: #fff;
  background: var(--spanish);
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.14em;
}

.audio-gate,
.example-audio-section {
  padding: 18px 16px;
  text-align: center;
  background: var(--audio-bg);
  border: 1px solid rgba(23, 63, 50, 0.15);
  border-radius: 18px;
}

.audio-kicker {
  color: var(--spanish);
  font-size: 0.78rem;
  font-weight: 900;
  letter-spacing: 0.15em;
}

.audio-guide {
  margin-top: 4px;
  color: var(--muted);
  font-size: 0.85rem;
}

.tts-primary,
.tts-secondary {
  margin-top: 12px;
  min-height: 24px;
}

.replay-button,
.tts-button {
  color: #fff !important;
  background: var(--spanish) !important;
  border: 0 !important;
  border-radius: 999px !important;
  box-shadow: 0 5px 12px rgba(23, 63, 50, 0.18);
}

.concept-section {
  margin-top: 20px;
  text-align: center;
}

.section-label {
  margin-bottom: 9px;
  color: var(--spanish);
  font-size: 0.73rem;
  font-weight: 900;
  letter-spacing: 0.15em;
}

.section-label.gold {
  color: #8b651f;
}

.concept-frame {
  overflow: hidden;
  width: min(100%, 520px);
  margin: 0 auto;
  background: #e9e6dc;
  border: 3px solid var(--gold-soft);
  border-radius: 22px;
  box-shadow: 0 9px 24px rgba(34, 45, 38, 0.13);
}

.concept-media {
  width: 100%;
  line-height: 0;
}

.concept-media img {
  display: block;
  width: 100%;
  max-width: 100%;
  height: auto;
  margin: 0 auto;
  border: 0;
  border-radius: 15px;
  object-fit: contain;
}


.concept-image {
  display: block;
  width: 100%;
  max-height: 390px;
  object-fit: contain;
}

.concept-guide {
  margin-top: 8px;
  color: var(--muted);
  font-size: 0.82rem;
}

.word-section {
  margin-top: 24px;
  text-align: center;
}

.word-label {
  color: var(--gold);
  font-size: 0.72rem;
  font-weight: 900;
  letter-spacing: 0.18em;
}

.headword {
  overflow-wrap: anywhere;
  margin-top: 4px;
  color: var(--spanish);
  font-family: Georgia, "Noto Serif", serif;
  font-size: clamp(2.05rem, 9vw, 3.9rem);
  font-weight: 750;
  line-height: 1.12;
  hyphens: auto;
}

.pronunciation {
  margin-top: 9px;
  color: var(--muted);
  font-family: "Noto Sans", "Segoe UI", sans-serif;
  font-size: 1rem;
}

.sound-segmentation {
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 7px;
  margin-top: 13px;
  padding: 7px 12px;
  color: var(--spanish);
  background: #f0eee6;
  border-radius: 12px;
  font-size: 0.88rem;
}

.mini-label {
  color: var(--gold);
  font-weight: 900;
  letter-spacing: 0.08em;
}

.mp-footer,
.source-footer {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-top: 24px;
  padding-top: 13px;
  color: var(--muted);
  border-top: 1px solid var(--line);
  font-size: 0.72rem;
}

.answer-divider {
  position: relative;
  width: min(100%, 760px);
  margin: 20px auto;
  text-align: center;
  scroll-margin-top: 10px;
}

.answer-divider::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
}

.answer-divider span {
  position: relative;
  z-index: 1;
  display: inline-block;
  padding: 5px 13px;
  color: #7a591f;
  background: var(--bg);
  font-size: 0.71rem;
  font-weight: 900;
  letter-spacing: 0.14em;
}

.meaning-section {
  text-align: center;
}

.japanese-meaning {
  color: var(--ink);
  font-family: "Noto Serif JP", "Yu Mincho", serif;
  font-size: clamp(1.65rem, 6.5vw, 2.65rem);
  font-weight: 700;
  line-height: 1.35;
}

.part-of-speech {
  display: inline-block;
  margin-top: 10px;
  padding: 4px 10px;
  color: #775619;
  background: var(--gold-soft);
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 700;
}

.example-audio-section {
  margin-top: 23px;
}

.example-section {
  margin-top: 20px;
  padding: 20px 18px;
  background: var(--example-bg);
  border-left: 5px solid var(--german-2);
  border-radius: 16px;
}

.example-spanish {
  color: var(--spanish);
  font-family: Georgia, "Noto Serif", serif;
  font-size: clamp(1.25rem, 4.8vw, 1.85rem);
  font-weight: 700;
  line-height: 1.55;
}

.example-japanese {
  margin-top: 13px;
  padding-top: 12px;
  color: var(--ink);
  border-top: 1px solid rgba(23, 63, 50, 0.15);
  font-size: 1rem;
}

.observation-strip {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 7px;
  margin: 18px 0 2px;
}

.observation-strip span {
  padding: 4px 9px;
  color: var(--spanish);
  background: #ede8d9;
  border-radius: 999px;
  font-size: 0.68rem;
  font-weight: 750;
}

.detail-panels {
  margin-top: 20px;
}

.detail-panel {
  overflow: hidden;
  margin: 12px 0;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 16px;
  scroll-margin-top: 10px;
}

.detail-panel summary {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 15px 14px;
  color: #fff;
  cursor: pointer;
  list-style: none;
  user-select: none;
}

.detail-panel summary::-webkit-details-marker {
  display: none;
}

.panel-purple summary {
  background: linear-gradient(135deg, #59417f, var(--purple));
}

.panel-blue summary {
  background: linear-gradient(135deg, #284f70, var(--blue));
}

.panel-red summary {
  background: linear-gradient(135deg, #234f3e, var(--red));
}

.summary-number {
  display: grid;
  flex: 0 0 28px;
  height: 28px;
  place-items: center;
  background: rgba(255, 255, 255, 0.18);
  border-radius: 50%;
  font-weight: 900;
}

.summary-title {
  flex: 1;
  font-size: 0.82rem;
  font-weight: 900;
  letter-spacing: 0.05em;
}

.summary-arrow {
  font-size: 1.2rem;
  transition: transform 0.2s ease;
}

.detail-panel[open] .summary-arrow {
  transform: rotate(180deg);
}

.detail-content {
  padding: 16px;
  background: var(--card);
}

.detail-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.detail-item,
.detail-block,
.memory-address {
  padding: 12px;
  background: #f5f3ec;
  border-radius: 12px;
}

.detail-item.full {
  grid-column: 1 / -1;
}

.detail-block + .detail-block {
  margin-top: 12px;
}

.memory-address {
  margin-top: 12px;
  background: var(--gold-soft);
}

.detail-label {
  margin-bottom: 5px;
  color: var(--muted);
  font-size: 0.69rem;
  font-weight: 900;
  letter-spacing: 0.05em;
}

.detail-value {
  overflow-wrap: anywhere;
  color: var(--ink);
  font-size: 0.93rem;
}

.spanish-value {
  color: var(--spanish);
  font-family: Georgia, "Noto Serif", serif;
  font-size: 1.15rem;
  font-weight: 700;
}

.address-line {
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.address-id {
  flex: 0 0 auto;
  padding: 3px 8px;
  color: #fff;
  background: var(--spanish);
  border-radius: 999px;
  font-size: 0.73rem;
  font-weight: 900;
}

.nightMode,
.night_mode {
  --bg: #11131a;
  --card: #191c26;
  --ink: #edf3ef;
  --muted: #aebbb3;
  --line: #344139;
  --german: #88c6ab;
  --german-2: #6ab08f;
  --gold: #e1b761;
  --gold-soft: #3d3422;
  --audio-bg: #2a1d25;
  --example-bg: #24202a;
  --shadow: 0 15px 38px rgba(0, 0, 0, 0.38);
}

.nightMode .detail-item,
.nightMode .detail-block,
.night_mode .detail-item,
.night_mode .detail-block {
  background: #222d27;
}

.nightMode .detail-panel,
.night_mode .detail-panel {
  background: #191c26;
}

.nightMode .observation-strip span,
.night_mode .observation-strip span {
  color: #deeadf;
  background: #27342d;
}

.nightMode .sound-segmentation,
.night_mode .sound-segmentation {
  background: #27342d;
}

@media (max-width: 520px) {
  .card {
    padding: 8px 5px 25px;
    font-size: 16px;
  }

  .mp-card {
    padding: 16px 13px;
    border-radius: 18px;
  }

  .mp-header {
    align-items: flex-start;
  }

  .mp-brand {
    font-size: 0.78rem;
  }

  .detail-grid {
    grid-template-columns: 1fr;
  }

  .detail-item.full {
    grid-column: auto;
  }

  .source-footer,
  .mp-footer {
    flex-direction: column;
    gap: 3px;
  }
}
```

---

# 適用手順

1. <Product>Anki Desktop</Product>でスペイン語ノートタイプを開く。
2. 「カード」を開く。
3. 表面テンプレートを上記の表面コードで全置換する。
4. 裏面テンプレートを上記の裏面コードで全置換する。
5. CSSを上記CSSで全置換する。
6. 保存する。
7. C0001とC0010をプレビューする。
8. 同期後、<Product>AnkiDroid</Product>で実機確認する。

CSSは追記ではなく、既存内容を全置換する。

---

# スペイン語での観測点

## 語形成

スペイン語は、複数の語が一語へ結合しやすい。綴りを左から機械的に追うだけでなく、意味のある構成要素を探す。

```text
Grundwort
＝ 最後の要素。語全体の中心カテゴリを決めやすい。

Bestimmungswort
＝ 前の要素。中心語を限定する。
```

## 再帰動詞

辞書形では一語でも、定形文では接頭辞が文末へ移る場合がある。

```text
見出し語
＝ 一つの語

例文
＝ 動詞本体と分離接頭辞の間に文の他要素が入る
```

例文音声では、離れた二部分を一つの動詞Conceptとして回収する。

## 動詞活用

スペイン語では、文の種類や節によって定形動詞の位置が重要になる。

```text
主文
＝ 定形動詞が第2位置になりやすい

従属節
＝ 定形動詞が後方へ移りやすい
```

逐語訳より先に、文が主文なのか従属節なのかを観測する。

## `ch`の音

```text
歯間音 /θ/
＝ 前舌母音などの後で現れやすい柔らかい摩擦音

軟口蓋摩擦音 /x/
＝ 後舌母音などの後で現れやすい奥の摩擦音
```

カタカナ一音へ固定せず、前後の母音とまとまりで聞く。

## 強勢とウムラウト

```text
母音の長さ
ウムラウト
子音の数
```

は意味や語形の識別に関わる。綴りと音の対応を例文内でも確認する。

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
語形成の表示
長い例文
ConceptScene
ダークモード
自動スクロール
```

## TTS

```html
{{tts es_ES:Spanish}}
```

```html
{{tts es_ES:ExampleSpanish}}
```

もし<Product>AnkiDroid</Product>で音が出ない場合、ロケールやVoice IDを推測で変更しない。カードへ一時的に次を追加し、端末が返す実在音声を確認する。

```html
{{tts-voices:}}
```

確認後は`{{tts-voices:}}`を削除する。
