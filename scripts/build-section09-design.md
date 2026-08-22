# Build Design for Chapter 04 Section 09

## Status

Draft 02 / Production Notes Layer

## Purpose

第四章第九節の正本を、物語の地上層と制作ノートの地下層へ運ぶBuildを定義する。

```text
五言語Markdown正本 + 五言語混交制作ノート
↓
Build
↓
section09.json
↓
物語ページ / 制作ノートページ
```

Buildは翻訳、評価、要約、解釈を行わない。正本の構造と内容を表示層へ運搬する。

## Required Inputs

```text
novel/chapter04/section09/
├── section09_ja.md
├── section09_en.md
├── section09_zh-TW.md
├── section09_ko.md
├── section09_ru.md
├── section09-production-notes.md
└── LOCALIZATION_READY
```

五言語混交制作ノートは『記憶都市』のコアを構成するため、第九節Buildでは必須入力とする。

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
    }
  },
  "links": {
    "production_notes": "notes.html",
    "localization_review": "localization-review.md",
    "python_model": "python/section09_time_model.py"
  }
}
```

## Extraction Rule

各Markdown冒頭の見出し群を読み、本文開始前の最後の見出しをタイトルとする。見出し直後から末尾までを本文として保持する。

## Error Policy

五言語正本または制作ノートのいずれかが欠ける場合、Buildを停止し、部分JSONを生成しない。生成前に `metadata`、`titles`、`content`、`documents`、`links` と制作ノートの `source`、`title`、`content` を検証する。

## Pages Relationship

```text
index.html
= 五言語の物語を読む地上層

notes.html
= 五言語混交制作ノートを読む地下層

index.html#story-end
↕
notes.html?from=<language>
```

制作ノートは解説の正解集ではない。読者が任意に降りられる別の深度として扱う。制作ノートから戻る際は、読者が地上層で選択していた言語を維持する。

## Next Step

制作ノート入口のローカルPoCを確認後、数式 `delta` からPython観測室へ降りる導線を設計する。
