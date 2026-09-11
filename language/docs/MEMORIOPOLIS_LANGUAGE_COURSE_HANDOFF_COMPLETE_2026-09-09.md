# MEMORIOPOLIS 多言語読解コース 完全版引き継ぎ書（2026-09-09）

## 本日の成果

### 韓国語 Core10 の改善

Core10に第三の橋を追加する方針を採用した。

従来：

```text
ExampleBreakdown
文の組み立て

ExampleExplanation
なぜこの意味になる？
```

追加：

```text
ExamplePronunciationHint
なぜこの音に聞こえる？
```

目的は発音規則の講義ではなく、

```text
文字
↓
耳に聞こえた音
```

を結び付けることである。

### 新フィールド

追加済み：

```text
ExamplePronunciationHint
```

現行フィールド数：

```text
1 ID
2 Korean
3 Romanization
4 Japanese
5 PartOfSpeech
6 ExampleKorean
7 ExampleRomanization
8 ExampleJapanese
9 Source
10 Tags
11 ExampleBreakdown
12 ExampleExplanation
13 ExamplePronunciationHint
```

## 実装状況

### C0001のみ試験実装

対象例文：

```text
도시의 기록을 확인했다.
```

音の解説を試験投入。

解説の考え方：

```text
기록을
↓
初心者の耳には
기로글
に近く聞こえることがある
```

```text
확인했다
↓
初心者の耳には
화긴핻따
に近く聞こえることがある
```

専門用語ではなく、聞き取れなかった経験を救済する文章を優先する。

## テンプレート変更

### korean_vocabulary_back.html

追加済み：

```html
{{#ExamplePronunciationHint}}
<div class="explanation-block">
  <div class="explanation-title">なぜこの音に聞こえる？</div>
  <div class="example-explanation">{{ExamplePronunciationHint}}</div>
</div>
{{/ExamplePronunciationHint}}
```

表示順：

```text
文の組み立て
↓
なぜこの意味になる？
↓
なぜこの音に聞こえる？
↓
出典
```

### プレビュー確認

確認済み：

```text
文の組み立て
なぜこの意味になる？
なぜこの音に聞こえる？
出典
```

の4段構成で表示。

## Anki環境

### Windows版Anki

動作確認済み：

- 単語TTS
- 例文TTS
- ExampleBreakdown
- ExampleExplanation
- ExamplePronunciationHint

### AnkiWeb

同期成功。

既知の制約：

```text
TTSタグが音声ではなく文字として表示される
```

### AnkiDroid

同期成功。

確認済み：

- 韓国語単語音声
- 韓国語例文音声
- 例文解説表示

AnkiDroidを通勤時間の主学習環境とする。

## 方針変更

従来案：

```text
Core10
↓
Core20
↓
Core30
```

新方針：

```text
Core10を完成作品として磨く
↓
通勤学習で検証
↓
Core50まで
↓
ロシア語版第12節
```

## Core20について

Core20は第12節では作らない。

第13節で対応する。

予定語彙：

```text
C0011 경로
C0012 복호화
C0013 열쇠
C0014 참조
C0015 식별자
C0016 설정
C0017 정지
C0018 재개
C0019 실행
C0020 영향
```

## 多言語展開方針

韓国語Core50到達後：

```text
ロシア語版 第12節
↓
ロシア語 Core10
↓
臺灣華語 Core10
↓
英語 Core10
↓
歴史的仮名遣い Core10
```

を一周する。

## 歴史的仮名遣い方針

独立言語ではなく、日本語の歴史表記層として扱う。

例：

```text
現代日本語
思う

歴史的仮名遣い
思ふ
```

臺灣華語では、拼音と注音符号を両方残す方針を維持する。

## 次回の最優先タスク

1. AnkiDroidでC0001を学習
2. ExamplePronunciationHint が本当に役立つか確認
3. 音の橋を正式採用するか判断
4. 採用ならC0002〜C0010へ展開
5. README更新
6. CSV更新
7. GitHubコミット

## 現在地

```text
単語
↓
音声
↓
例文
↓
文の組み立て
↓
なぜこの意味になる？
↓
なぜこの音に聞こえる？
```

『記憶都市読解コース』は、意味への橋に加え、音への橋を試作する段階へ入った。
