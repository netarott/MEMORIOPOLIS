# Filipino card template draft01

## Front

```html
<div class="concept-id">{{ID}}</div>
<div class="layer-name">Filipino</div>
<div class="target-word">{{Filipino}}</div>
{{#Pronunciation}}<div class="pronunciation">{{Pronunciation}}</div>{{/Pronunciation}}
<div class="tts-audio">{{tts fil_PH:Filipino}}</div>
```

## Back

```html
{{FrontSide}}
<hr id="answer">
{{#Japanese}}<div class="section"><div class="label">日本語</div><div class="answer-word">{{Japanese}}</div></div>{{/Japanese}}
{{#PartOfSpeech}}<div class="section"><div class="label">品詞</div><div>{{PartOfSpeech}}</div></div>{{/PartOfSpeech}}
{{#UsageNote}}<div class="section"><div class="label">意味と用法</div><div>{{UsageNote}}</div></div>{{/UsageNote}}
{{#ExampleFilipino}}<div class="section example"><div class="label">例文・Filipino</div><div>{{ExampleFilipino}}</div></div>{{/ExampleFilipino}}
<div class="tts-audio">{{tts fil_PH:ExampleFilipino}}</div>
{{#ExampleJapanese}}<div class="section"><div class="label">例文・日本語</div><div>{{ExampleJapanese}}</div></div>{{/ExampleJapanese}}
{{#Root}}<div class="section"><div class="label">語根</div><div>{{Root}}</div></div>{{/Root}}
{{#Affixes}}<div class="section"><div class="label">接辞</div><div>{{Affixes}}</div></div>{{/Affixes}}
{{#PerceptualSegmentation}}<div class="section segmentation"><div class="label">知覚上の区切り</div><div>{{PerceptualSegmentation}}</div></div>{{/PerceptualSegmentation}}
{{#MorphologicalBreakdown}}<div class="section morphology"><div class="label">形態の橋</div><div>{{MorphologicalBreakdown}}</div></div>{{/MorphologicalBreakdown}}
{{#MeaningBridge}}<div class="section meaning"><div class="label">意味の橋</div><div>{{MeaningBridge}}</div></div>{{/MeaningBridge}}
{{#SoundBridge}}<div class="section sound"><div class="label">音の橋</div><div>{{SoundBridge}}</div></div>{{/SoundBridge}}
{{#Source}}<div class="source">Source: {{Source}}</div>{{/Source}}
```

## CSS addition

```css
.tts-audio { text-align: center; margin: 14px 0; }
.target-word { font-size: 46px; font-weight: 600; text-align: center; margin: 14px 0 6px; }
.pronunciation { text-align: center; color: #6f665b; font-size: 18px; }
.segmentation { border-left: 4px solid #6f8fa6; }
.morphology { border-left: 4px solid #8b6fa6; }
.meaning { border-left: 4px solid #607f58; }
.sound { border-left: 4px solid #a17b30; }
```
