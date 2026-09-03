# 第十一節ページへの予告編導線

アップロードされた第十一節 `index.html` の末尾にある関連ページナビゲーションを、次へ置き換えます。

```html
<nav class="section-navigation" aria-label="第十一節の関連ページ">
  <a class="primary-link" href="trailer.html" data-open-trailer>20秒の予告編を見る</a>
  <a href="notes.html" data-open-production-notes data-source="emaki">五言語混交制作ノート</a>
  <a href="../section10/">第十節へ戻る</a>
  <a href="../../">中央駅へ戻る</a>
</nav>
```

`script.js` に解析イベントを加える場合は、初期化処理の中で次を登録します。

```javascript
document.querySelector('[data-open-trailer]')?.addEventListener('click', () => {
  sendEvent('section11_emaki_open_trailer', {
    section_id: 'section11',
    source: 'emaki'
  });
});
```

中央駅側の更新には、中央駅の最新 `index.html` または生成Builderが必要です。
