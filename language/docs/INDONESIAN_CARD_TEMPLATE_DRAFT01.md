# Indonesian card template

## Front
```html
<div class="concept-id">{{ID}}</div>
<div class="layer-name">Bahasa Indonesia</div>
<div class="target-word">{{Indonesian}}</div>
{{#Pronunciation}}<div class="pronunciation">{{Pronunciation}}</div>{{/Pronunciation}}
<div class="tts-audio">{{tts id_ID:Indonesian}}</div>
```

## Back
```html
{{FrontSide}}
<hr id="answer">
{{#Japanese}}<div class="section japanese-section"><div class="label">日本語</div><div class="answer-word">{{Japanese}}</div></div>{{/Japanese}}
{{#PartOfSpeech}}<div class="section"><div class="label">品詞</div><div class="content">{{PartOfSpeech}}</div></div>{{/PartOfSpeech}}
{{#UsageNote}}<div class="section usage-section"><div class="label">意味と用法</div><div class="content">{{UsageNote}}</div></div>{{/UsageNote}}
{{#ExampleIndonesian}}<div class="section example-section"><div class="label">例文・Bahasa Indonesia</div><div class="example-text">{{ExampleIndonesian}}</div></div><div class="tts-audio">{{tts id_ID:ExampleIndonesian}}</div>{{/ExampleIndonesian}}
{{#ExampleJapanese}}<div class="section japanese-section"><div class="label">例文・日本語</div><div class="content">{{ExampleJapanese}}</div></div>{{/ExampleJapanese}}
{{#Root}}<div class="section root-section"><div class="label">語根</div><div class="root-form">{{Root}}</div></div>{{/Root}}
{{#Affixes}}<div class="section affix-section"><div class="label">接辞</div><div class="content">{{Affixes}}</div></div>{{/Affixes}}
{{#PerceptualSegmentation}}<div class="section segmentation"><div class="label">知覚上の区切り</div><div class="segment-form">{{PerceptualSegmentation}}</div></div>{{/PerceptualSegmentation}}
{{#MorphologicalBreakdown}}<div class="section morphology"><div class="label">形態の橋</div><div class="content">{{MorphologicalBreakdown}}</div></div>{{/MorphologicalBreakdown}}
{{#ExampleBreakdown}}<div class="section breakdown"><div class="label">例文の分解</div><div class="content">{{ExampleBreakdown}}</div></div>{{/ExampleBreakdown}}
{{#ExampleExplanation}}<div class="section explanation"><div class="label">なぜこの意味になるか</div><div class="content">{{ExampleExplanation}}</div></div>{{/ExampleExplanation}}
{{#MeaningBridge}}<div class="section meaning"><div class="label">意味の橋</div><div class="content">{{MeaningBridge}}</div></div>{{/MeaningBridge}}
{{#SoundBridge}}<div class="section sound"><div class="label">音の橋</div><div class="content">{{SoundBridge}}</div></div>{{/SoundBridge}}
{{#Source}}<div class="source">Source: {{Source}}</div>{{/Source}}
```

## CSS
```css
.card { font-family: "Segoe UI","Noto Sans","Yu Gothic",sans-serif; font-size: 19px; line-height: 1.7; color:#263238; background:#f4f1e8; padding:18px; text-align:left; }
.concept-id,.layer-name,.pronunciation,.tts-audio { text-align:center; }
.concept-id { color:#80786c; font-size:14px; }
.layer-name { color:#7a6245; font-size:14px; letter-spacing:.12em; }
.target-word { font-size:42px; font-weight:600; text-align:center; margin:12px 0 4px; overflow-wrap:anywhere; }
.pronunciation { color:#7a6245; font-size:18px; }
.tts-audio { margin:14px 0; }
hr#answer { border:0; border-top:1px solid #b8aa97; margin:24px 0; }
.section { background:#ece8df; border-radius:7px; margin-top:15px; padding:12px 15px; }
.label { color:#6f665b; font-size:13px; font-weight:600; margin-bottom:6px; }
.content { font-size:17px; white-space:pre-wrap; overflow-wrap:anywhere; }
.answer-word { font-size:28px; font-weight:600; }
.example-text { font-size:21px; }
.japanese-section { background:#e6ecee; border-left:4px solid #718894; }
.root-section { background:#eee5d9; border-left:4px solid #9a7448; }
.affix-section { background:#eee8d9; border-left:4px solid #a38a4d; }
.segmentation { background:#e2edf3; border-left:4px solid #6f8fa6; }
.morphology { background:#ece5f0; border-left:4px solid #8b6fa6; }
.breakdown { background:#e5ece8; border-left:4px solid #5d8270; }
.explanation { background:#eee9df; border-left:4px solid #8b7458; }
.meaning { background:#e5eee2; border-left:4px solid #607f58; }
.sound { background:#f2e7cb; border-left:4px solid #a17b30; }
.source { color:#8b8378; font-size:12px; margin-top:22px; overflow-wrap:anywhere; }
.nightMode .card { color:#eee9df; background:#23211f; }
.nightMode .section { background:#33302c; }
.nightMode .japanese-section { background:#29353a; }
.nightMode .breakdown { background:#293630; }
.nightMode .explanation { background:#373129; }

```
