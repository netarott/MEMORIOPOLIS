# Filipino template patch draft02

裏面の `MorphologicalBreakdown` の直後、`MeaningBridge` の前へ追加する。

```html
{{#ExampleBreakdown}}
<div class="section breakdown-section">
  <div class="label">例文の分解</div>
  <div class="content breakdown-content">{{ExampleBreakdown}}</div>
</div>
{{/ExampleBreakdown}}

{{#ExampleExplanation}}
<div class="section explanation-section">
  <div class="label">なぜこの意味になるか</div>
  <div class="content">{{ExampleExplanation}}</div>
</div>
{{/ExampleExplanation}}
```

CSS末尾へ追加する。

```css
.breakdown-section {
  background-color: #e5ece8;
  border-left: 4px solid #5d8270;
}

.breakdown-content {
  white-space: pre-wrap;
  line-height: 1.9;
}

.explanation-section {
  background-color: #eee9df;
  border-left: 4px solid #8b7458;
}

.nightMode .breakdown-section {
  background-color: #293630;
  border-left-color: #7eaa94;
}

.nightMode .explanation-section {
  background-color: #373129;
  border-left-color: #b69a77;
}
```
