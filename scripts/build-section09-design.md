# Build Design for Chapter 04 Section 09

## Status

Draft 01

## Purpose

本設計書は、『記憶都市（メモリオポリス）』第四章第九節において、

```text
Markdown正本
↓
Build
↓
JSON
↓
GitHub Pages
```

という流れを実現するためのBuild層を定義する。

Buildの役割は表示用データを生成することであり、

- 翻訳しない
- 評価しない
- 要約しない
- 解釈しない

ことを原則とする。

Buildは正本を運搬する。

## 1. Design Principles

### 1.1 Single Source of Truth

五言語Markdownを唯一の正本とする。

```text
section09_ja.md
section09_en.md
section09_zh-TW.md
section09_ko.md
section09_ru.md
```

GitHub Pagesは表示層であり、正本ではない。

JSONは生成物であり、正本ではない。

### 1.2 No Duplication

同じ文章をMarkdown、HTML、JSONの三か所で管理しない。

修正地点は常にMarkdownのみとする。

### 1.3 Observe, Do Not Interpret

Buildは本文内容を解釈しない。

たとえば、用法、状態、やり取り、一拍の意味をBuildが理解する必要はない。

Buildは構造だけを変換する。

## 2. Input

### 2.1 Required Files

```text
novel/
└── chapter04/
    └── section09/
        ├── section09_ja.md
        ├── section09_en.md
        ├── section09_zh-TW.md
        ├── section09_ko.md
        └── section09_ru.md
```

### 2.2 Optional Files

```text
localization-review.md
section09-production-notes.md
```

### 2.3 Status Marker

```text
LOCALIZATION_READY
```

存在する場合：

```json
"localization_ready": true
```

存在しない場合：

```json
"localization_ready": false
```

## 3. Output

出力先：

```text
experience/
└── chapter04/
    └── section09/
        └── data/
            └── section09.json
```

Build実行時は常に上書き生成する。

手編集は禁止。

## 4. JSON Schema

```json
{
  "metadata": {},
  "titles": {},
  "content": {},
  "links": {}
}
```

### 4.1 metadata

```json
{
  "chapter": 4,
  "section": 9,
  "slug": "section09",
  "localization_ready": true
}
```

### 4.2 titles

```json
{
  "ja": "...",
  "en": "...",
  "zh-TW": "...",
  "ko": "...",
  "ru": "..."
}
```

各Markdownの先頭見出しから生成する。

### 4.3 content

```json
{
  "ja": "...",
  "en": "...",
  "zh-TW": "...",
  "ko": "...",
  "ru": "..."
}
```

タイトルを除いた本文。

Buildは本文を書き換えない。

### 4.4 links

```json
{
  "production_notes": "section09-production-notes.md",
  "localization_review": "localization-review.md",
  "python_model": "python/section09_time_model.py"
}
```

## 5. Markdown Parsing Rules

### 5.1 Title Extraction

最初のレベル1見出しをタイトルとする。

例：

```markdown
# まだ送られていない矢印
```

出力：

```json
"titles": {
  "ja": "まだ送られていない矢印"
}
```

### 5.2 Body Extraction

タイトル以降を本文として扱う。

例：

```markdown
# まだ送られていない矢印

本文A

本文B
```

出力：

```json
"content": {
  "ja": "本文A\n\n本文B"
}
```

### 5.3 Formatting Preservation

Buildは以下を保持する。

- 改行
- 段落
- 数式
- コードブロック
- 引用
- 箇条書き

Buildは本文を整形し直さない。

## 6. Build Flow

```text
Read Markdown
↓
Extract Title
↓
Extract Body
↓
Read Status Marker
↓
Generate JSON
↓
Write section09.json
```

## 7. Error Policy

### 7.1 Missing Language File

必須の言語ファイルが存在しない場合、Buildは失敗する。

部分生成しない。

### 7.2 Missing Title

タイトル抽出に失敗した場合、次のエラーとして停止する。

```text
ERROR: title not found
```

### 7.3 JSON Validation

生成後、次のキーがすべて存在することを確認する。

```text
metadata
titles
content
links
```

欠損があれば失敗する。

## 8. Future Extensions

将来的に次の構造を追加できる。

### 8.1 Related Documents

```json
"related": {}
```

### 8.2 Scene Data

```json
"scenes": {}
```

### 8.3 Audio Metadata

```json
"audio": {}
```

### 8.4 Image Metadata

```json
"images": {}
```

### 8.5 Observation Layer

```json
"observation": {}
```

将来の数式deltaおよびPython観測室への入口とする。

## 9. Relationship to Memoriopolis

第四章第九節では、

```text
五言語
↓
☆型
↓
制作ノート
↓
Python
```

という構造が観測された。

Buildはその構造を変更しない。

Buildは正本をPagesへ運ぶ橋である。

## 10. Next Step

実装対象：

```text
scripts/
└── build_section09.py
```

最初の実装目標：

```text
section09_ja.md
section09_en.md
section09_zh-TW.md
section09_ko.md
section09_ru.md
↓
section09.json
```

Buildの成功条件は、

```text
Markdown修正
↓
Build実行
↓
Pagesへ反映
```

が成立し、JSONやHTMLを手編集せずに済むことである。
