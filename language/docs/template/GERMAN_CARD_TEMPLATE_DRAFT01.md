# German Card Template draft01

## Front Template
```html
<div class="concept-id">{{ID}}</div>
<div class="target-word">{{German}}</div>
<div class="pronunciation">/{{Pronunciation}}/</div>
<div class="tts">{{tts de_DE:German}}</div>
```

## Back Template
```html
{{FrontSide}}
<hr id="answer">
<div class="japanese">{{Japanese}}</div>
<div class="part-of-speech">{{PartOfSpeech}}</div>
<div class="usage-note">{{UsageNote}}</div>
<div class="example-target">{{ExampleGerman}}</div>
<div class="tts">{{tts de_DE:ExampleGerman}}</div>
<div class="example-japanese">{{ExampleJapanese}}</div>
<details><summary>語の構造</summary>
<div>{{Root}}</div><div>{{Affixes}}</div><div>{{PerceptualSegmentation}}</div><div>{{MorphologicalBreakdown}}</div>
</details>
<details><summary>例文解説</summary>
<div>{{ExampleBreakdown}}</div><div>{{ExampleExplanation}}</div>
</details>
<details><summary>言語間ブリッジ</summary>
<div>{{MeaningBridge}}</div><div>{{SoundBridge}}</div>
</details>
<div class="source">{{Source}}</div>
```

## Styling
```css
.card { font-family: "Noto Sans", "Segoe UI", sans-serif; text-align: left; color: #20242a; background: #f7f4ec; line-height: 1.6; padding: 18px; }
.concept-id { color: #6b7280; font-size: 0.85rem; letter-spacing: 0.08em; }
.target-word { font-size: 2rem; font-weight: 700; color: #1f3a5f; margin-top: 0.4rem; }
.pronunciation { color: #475569; font-size: 1rem; }
.japanese { font-size: 1.5rem; font-weight: 650; margin: 0.8rem 0; }
.example-target { margin-top: 1rem; padding: 0.8rem; background: #e8eef5; border-left: 4px solid #1f3a5f; }
.example-japanese { padding: 0.5rem 0.8rem; }
details { margin-top: 0.7rem; padding: 0.5rem; border: 1px solid #d6d3d1; border-radius: 6px; }
.source { margin-top: 1rem; color: #78716c; font-size: 0.78rem; }
```
