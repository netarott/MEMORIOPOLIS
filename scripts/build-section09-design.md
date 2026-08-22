# Build Design for Chapter 04 Section 09

## Status

Draft 03 / Canonical Minimal PoC

## Purpose

第九節の最小PoCを正とし、五言語の物語、五言語混交制作ノート、Python状態模型を一つのBuildから三層へ運ぶ。

```text
五言語Markdown正本
制作ノート正本
Python状態模型正本
↓
Build
↓
section09.json
↓
物語 / 制作ノート / Python観測窓
```

Buildは翻訳、評価、要約、解釈、コード整形、Python実行を行わない。

## Required Inputs

```text
novel/chapter04/section09/
├── section09_ja.md
├── section09_en.md
├── section09_zh-TW.md
├── section09_ko.md
├── section09_ru.md
├── section09-production-notes.md
├── LOCALIZATION_READY
└── python/
    └── section09_time_model.py
```

五言語正本、制作ノート、Python状態模型のいずれかが欠ける場合はBuildを停止し、部分JSONを生成しない。

## Output

```text
experience/chapter04/section09/data/section09.json
```

JSONは生成物であり、手編集しない。

## JSON Structure

```json
{
  "metadata": {},
  "titles": {},
  "content": {},
  "documents": {
    "production_notes": {
      "source": "section09-production-notes.md",
      "title": "...",
      "content": "..."
    },
    "python_model": {
      "source": "python/section09_time_model.py",
      "language": "python",
      "title": "Section 09 Time Model",
      "content": "..."
    }
  },
  "links": {
    "production_notes": "notes.html",
    "localization_review": "localization-review.md",
    "python_model": "observation.html"
  }
}
```

## Three Layers

```text
index.html
= 五言語の物語を読む地上層

notes.html
= 五言語混交制作ノートを読む地下層

observation.html
= Python状態模型を観測する窓
```

## Navigation

```text
物語末尾 ↔ 制作ノート
物語中のdelta ↔ Python観測窓
Python観測窓 → 制作ノート
```

`from=<language>` で物語側の表示言語を保持する。観測窓からの帰還先は `index.html?lang=<language>#delta` とし、本文と数式の組版完了後にdelta位置へ移動する。

## Canonical Minimal PoC

第九節では次を正とする。

- Pythonコードは表示のみで、ブラウザ実行しない
- 外部シンタックスハイライトを導入しない
- ケースの順位づけやスコア表示をしない
- 状態内容の自動カード抽出をしない
- 次節以降で必要に応じて機能を増やす
