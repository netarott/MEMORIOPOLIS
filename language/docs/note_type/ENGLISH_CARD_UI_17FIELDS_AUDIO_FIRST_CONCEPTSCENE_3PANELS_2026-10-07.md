# MEMORIOPOLIS English Vocabulary UI

更新日: 2026-10-07  
対象ノートタイプ: `MEMORIOPOLIS English Vocabulary`  
設計テーマ: **音 → Concept候補 → ConceptScene → 綴り → 例文 → 3段パネル**

## 更新判断

旧英語UIは2026-09-26版で、17フィールド仕様と3段パネルには対応していたが、表面が`ID → ConceptScene → English → IPA → TTS`の順で、現在の音優先型ではなかった。今回、既存17フィールドを維持したまま、フィリピン語以降の正式設計へ更新する。

## 正式17フィールド

```text
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
```

未存在フィールドは参照しない。`CourseTags`は管理用でカード画面には表示しない。

---

# 表面テンプレート

```html
<div class="mp-card mp-front">
  <div class="mp-header">
    <div class="mp-brand">MEMORIOPOLIS</div>
    <div class="mp-language">ENGLISH</div>
  </div>

  <section class="sound-gate">
    <div class="sound-kicker">LISTEN FIRST</div>
    <div class="sound-guide">まず音を聞き、心の中でConceptを探す</div>
    <div class="tts-audio">{{tts en_US:English}}</div>
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
    <div class="word-label">ENGLISH</div>
    <div class="headword">{{English}}</div>
    {{#IPA}}<div class="pronunciation">{{IPA}}</div>{{/IPA}}
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

<div id="answer" class="answer-divider"><span>ANSWER · 回答</span></div>

<div class="mp-card mp-back">
  <section class="meaning-section">
    <div class="section-label gold">JAPANESE CONCEPT</div>
    <div class="japanese-meaning">{{Japanese}}</div>
    {{#PartOfSpeech}}<div class="part-of-speech">{{PartOfSpeech}}</div>{{/PartOfSpeech}}
  </section>

  {{#ExampleEnglish}}
  <section class="example-audio-section">
    <div class="sound-kicker">LISTEN TO THE SENTENCE</div>
    <div class="sound-guide">例文の音から、見出し語と文意を探す</div>
    <div class="tts-audio">{{tts en_US:ExampleEnglish}}</div>
  </section>

  <section class="example-section">
    <div class="section-label">EXAMPLE</div>
    <div class="example-english">{{ExampleEnglish}}</div>
    {{#ExampleIPA}}<div class="example-ipa">{{ExampleIPA}}</div>{{/ExampleIPA}}
    {{#ExampleJapanese}}<div class="example-japanese">{{ExampleJapanese}}</div>{{/ExampleJapanese}}
  </section>
  {{/ExampleEnglish}}

  <div class="observation-strip">
    <span>stress</span><span>rhythm</span><span>linking</span><span>grammar</span><span>register</span><span>Concept boundary</span>
  </div>

  <div class="detail-panels">
    <details class="detail-panel panel-purple">
      <summary><span class="summary-number">1</span><span class="summary-title">WORD STRUCTURE · 語の構造</span><span class="summary-arrow">⌄</span></summary>
      <div class="detail-content">
        <div class="detail-grid">
          <div class="detail-item full"><div class="detail-label">見出し語</div><div class="detail-value english-value">{{English}}</div></div>
          {{#IPA}}<div class="detail-item"><div class="detail-label">IPA</div><div class="detail-value">{{IPA}}</div></div>{{/IPA}}
          {{#PartOfSpeech}}<div class="detail-item"><div class="detail-label">品詞</div><div class="detail-value">{{PartOfSpeech}}</div></div>{{/PartOfSpeech}}
          {{#EnglishGrammar}}<div class="detail-item full"><div class="detail-label">文法・語法</div><div class="detail-value">{{EnglishGrammar}}</div></div>{{/EnglishGrammar}}
          {{#UsageNote}}<div class="detail-item full"><div class="detail-label">使い方</div><div class="detail-value">{{UsageNote}}</div></div>{{/UsageNote}}
        </div>
      </div>
    </details>

    <details class="detail-panel panel-blue">
      <summary><span class="summary-number">2</span><span class="summary-title">SENTENCE GUIDE · 例文解説</span><span class="summary-arrow">⌄</span></summary>
      <div class="detail-content">
        {{#ExampleBreakdown}}<div class="detail-block"><div class="detail-label">文の組み立て</div><div class="detail-value">{{ExampleBreakdown}}</div></div>{{/ExampleBreakdown}}
        {{#ExampleExplanation}}<div class="detail-block"><div class="detail-label">なぜこの意味になる？</div><div class="detail-value">{{ExampleExplanation}}</div></div>{{/ExampleExplanation}}
        {{#ExamplePronunciationHint}}<div class="detail-block"><div class="detail-label">音声観測</div><div class="detail-value">{{ExamplePronunciationHint}}</div></div>{{/ExamplePronunciationHint}}
      </div>
    </details>

    <details class="detail-panel panel-green">
      <summary><span class="summary-number">3</span><span class="summary-title">CONCEPT BRIDGE · 言語間ブリッジ</span><span class="summary-arrow">⌄</span></summary>
      <div class="detail-content">
        {{#UsageNote}}<div class="detail-block"><div class="detail-label">意味と用法の橋</div><div class="detail-value">{{UsageNote}}</div></div>{{/UsageNote}}
        {{#ConceptContrast}}<div class="detail-block"><div class="detail-label">Conceptの境界</div><div class="detail-value contrast-text">{{ConceptContrast}}</div></div>{{/ConceptContrast}}
        <div class="memory-address"><div class="detail-label">記憶都市の住所</div><div class="address-line"><span class="address-id">{{ID}}</span><span class="detail-value">音、IPA、ConceptScene、日本語Concept、語法、例文を同じConcept IDへ接続する。</span></div></div>
      </div>
    </details>
  </div>

  <div class="source-footer"><span>{{#Source}}Source: {{Source}}{{/Source}}</span><span>{{ID}}</span></div>
</div>
```

---

# CSS

```css
:root {
  --bg:#eef2f6; --card:#fffdf8; --ink:#182230; --muted:#687487; --line:#d8e0e8;
  --navy:#173b5f; --blue:#2c6eaa; --blue-soft:#e8f2fb; --red:#b6424b; --gold:#b68a3b;
  --gold-soft:#f3e7cb; --purple:#66508f; --green:#39745a; --shadow:0 12px 34px rgba(22,45,70,.12);
}
*{box-sizing:border-box}
html,body,.card{width:100%;margin:0;text-align:left}
.card{padding:18px 12px 34px;color:var(--ink);background:radial-gradient(circle at top right,rgba(182,138,59,.13),transparent 32%),var(--bg);font-family:"Noto Sans JP","Noto Sans","Segoe UI",Arial,sans-serif;font-size:17px;line-height:1.72;-webkit-text-size-adjust:100%;overflow-wrap:anywhere}
.mp-card{width:min(100%,760px);margin:0 auto;padding:22px;background:var(--card);border:1px solid rgba(23,59,95,.14);border-radius:24px;box-shadow:var(--shadow);overflow:hidden}
.mp-front{position:relative}.mp-front:before{content:"";position:absolute;inset:0 0 auto;height:6px;background:linear-gradient(90deg,#173b5f 0 40%,#f5f0df 40% 60%,#b6424b 60% 100%)}
.mp-header{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:4px 0 20px;padding-bottom:13px;border-bottom:1px solid var(--line)}
.mp-brand{color:var(--navy);font-family:Georgia,"Times New Roman",serif;font-size:.92rem;font-weight:800;letter-spacing:.13em}.mp-language{padding:5px 11px;color:#fff;background:var(--navy);border-radius:999px;font-size:.72rem;font-weight:800;letter-spacing:.14em}
.sound-gate,.example-audio-section{padding:18px 16px;text-align:center;background:var(--blue-soft);border:1px solid rgba(44,110,170,.18);border-radius:18px}.sound-kicker{color:var(--navy);font-size:.78rem;font-weight:900;letter-spacing:.15em}.sound-guide{margin-top:4px;color:var(--muted);font-size:.85rem}.tts-audio{margin-top:12px;min-height:24px;text-align:center}.replay-button,.tts-button{color:#fff!important;background:var(--navy)!important;border:0!important;border-radius:999px!important;box-shadow:0 5px 12px rgba(23,59,95,.2)}
.concept-section{margin-top:20px;text-align:center}.section-label{margin-bottom:9px;color:var(--navy);font-size:.73rem;font-weight:900;letter-spacing:.15em}.section-label.gold{color:#88631e}.concept-frame{overflow:hidden;width:min(100%,520px);margin:0 auto;background:#e9e6dc;border:3px solid var(--gold-soft);border-radius:22px;box-shadow:0 9px 24px rgba(34,45,38,.13)}.concept-image,.concept-image img{display:block;width:100%;max-height:390px;object-fit:contain}.concept-guide{margin-top:8px;color:var(--muted);font-size:.82rem}
.word-section{margin-top:24px;text-align:center}.word-label{color:var(--red);font-size:.72rem;font-weight:900;letter-spacing:.18em}.headword{margin-top:4px;color:var(--navy);font-family:Georgia,"Times New Roman",serif;font-size:clamp(2.05rem,9vw,3.9rem);font-weight:750;line-height:1.12}.pronunciation{margin-top:9px;color:var(--muted);font-size:1rem;letter-spacing:.025em}.mp-footer,.source-footer{display:flex;justify-content:space-between;gap:12px;margin-top:24px;padding-top:13px;color:var(--muted);border-top:1px solid var(--line);font-size:.72rem}
.answer-divider{position:relative;width:min(100%,760px);margin:20px auto;text-align:center;scroll-margin-top:10px}.answer-divider:before{content:"";position:absolute;top:50%;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent)}.answer-divider span{position:relative;z-index:1;display:inline-block;padding:5px 13px;color:#76561e;background:var(--bg);font-size:.71rem;font-weight:900;letter-spacing:.14em}
.meaning-section{text-align:center}.japanese-meaning{font-family:"Noto Serif JP","Yu Mincho",serif;font-size:clamp(1.65rem,6.5vw,2.65rem);font-weight:700;line-height:1.35}.part-of-speech{display:inline-block;margin-top:10px;padding:4px 10px;color:#775619;background:var(--gold-soft);border-radius:999px;font-size:.75rem;font-weight:700}.example-audio-section{margin-top:23px}.example-section{margin-top:20px;padding:20px 18px;background:#eef5fa;border-left:5px solid var(--blue);border-radius:16px}.example-english{color:var(--navy);font-family:Georgia,"Times New Roman",serif;font-size:clamp(1.25rem,4.8vw,1.85rem);font-weight:700;line-height:1.55}.example-ipa{margin-top:8px;color:var(--muted);font-size:.92rem}.example-japanese{margin-top:13px;padding-top:12px;border-top:1px solid rgba(23,59,95,.15)}
.observation-strip{display:flex;flex-wrap:wrap;justify-content:center;gap:7px;margin:18px 0 2px}.observation-strip span{padding:4px 9px;color:var(--navy);background:#e9eef3;border-radius:999px;font-size:.68rem;font-weight:750}.detail-panels{margin-top:20px}.detail-panel{overflow:hidden;margin:12px 0;background:#fff;border:1px solid var(--line);border-radius:16px}.detail-panel summary{display:flex;align-items:center;gap:10px;padding:15px 14px;color:#fff;cursor:pointer;list-style:none;user-select:none}.detail-panel summary::-webkit-details-marker{display:none}.panel-purple summary{background:linear-gradient(135deg,#544176,var(--purple))}.panel-blue summary{background:linear-gradient(135deg,#244f76,var(--blue))}.panel-green summary{background:linear-gradient(135deg,#28523f,var(--green))}.summary-number{display:grid;flex:0 0 28px;height:28px;place-items:center;background:rgba(255,255,255,.18);border-radius:50%;font-weight:900}.summary-title{flex:1;font-size:.82rem;font-weight:900;letter-spacing:.05em}.summary-arrow{font-size:1.2rem;transition:transform .2s}.detail-panel[open] .summary-arrow{transform:rotate(180deg)}.detail-content{padding:16px;background:var(--card)}.detail-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.detail-item,.detail-block,.memory-address{padding:12px;background:#f3f5f7;border-radius:12px}.detail-item.full{grid-column:1/-1}.detail-block+.detail-block{margin-top:12px}.memory-address{margin-top:12px;background:var(--gold-soft)}.detail-label{margin-bottom:5px;color:var(--muted);font-size:.69rem;font-weight:900;letter-spacing:.05em}.detail-value{font-size:.93rem}.english-value{color:var(--navy);font-family:Georgia,"Times New Roman",serif;font-size:1.15rem;font-weight:700}.contrast-text{padding-left:10px;border-left:3px solid var(--green)}.address-line{display:flex;align-items:flex-start;gap:10px}.address-id{flex:0 0 auto;padding:3px 8px;color:#fff;background:var(--navy);border-radius:999px;font-size:.73rem;font-weight:900}
.nightMode,.night_mode{--bg:#111820;--card:#19232d;--ink:#edf3f8;--muted:#aebdca;--line:#374552;--navy:#91cfff;--blue:#559bd4;--blue-soft:#20374a;--red:#ef9aa0;--gold:#e1b761;--gold-soft:#413621;--shadow:0 15px 38px rgba(0,0,0,.38)}.nightMode .detail-item,.nightMode .detail-block,.night_mode .detail-item,.night_mode .detail-block{background:#222e38}.nightMode .detail-panel,.night_mode .detail-panel{background:#19232d}.nightMode .observation-strip span,.night_mode .observation-strip span{color:#deebf5;background:#273641}.nightMode .mp-language,.night_mode .mp-language{color:#102130;background:#91cfff}
@media(max-width:520px){.card{padding:8px 5px 25px;font-size:16px}.mp-card{padding:16px 13px;border-radius:18px}.mp-header{align-items:flex-start}.mp-brand{font-size:.78rem}.detail-grid{grid-template-columns:1fr}.detail-item.full{grid-column:auto}.source-footer,.mp-footer{flex-direction:column;gap:3px}}

```

---

# 適用手順

1. `MEMORIOPOLIS English Vocabulary`のフィールド順が上記17フィールドと一致することを確認する。
2. 表面テンプレートを全置換する。
3. 裏面テンプレートを全置換する。
4. CSSを追記ではなく全置換する。
5. C0001とC0020をPC版Ankiでプレビューする。
6. 単語音声が画像より先に配置されていることを確認する。
7. `Show answer`で`id="answer"`へ移動することを確認する。
8. 例文TTSと3段パネルを確認する。
9. AnkiDroidへ同期し、ライト・ダーク両モードを確認する。
10. English Core30登録後、C0021とC0030で長文・句動詞・折り返しを確認する。

## TTS

```html
{{tts en_US:English}}
{{tts en_US:ExampleEnglish}}
```

## Core30への適用

このUIは既存17フィールドを変えないため、Core10、Core20、Core30で共通利用できる。Core30は`E0002_en.md`をSourceとし、C0021からC0030を登録する。
