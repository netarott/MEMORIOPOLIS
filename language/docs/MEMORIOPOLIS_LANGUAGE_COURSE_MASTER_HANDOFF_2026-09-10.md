# MEMORIOPOLIS 多言語読解コース 完全引き継ぎ書

更新日: 2026-09-10

## 概要

『記憶都市（メモリオポリス）』を読むための多言語読解コースを構築中。

対象言語:

- 日本語（現代日本語）
- 日本語（歴史的仮名遣い）
- English
- 한국어
- 臺灣繁體中文
- Русский

中心思想:

```text
小説
↓
概念
↓
語彙
↓
音
↓
読解
```

単語暗記ではなく、読解に到達するための橋を作る。

---

# Concept Dictionary 方針

概念IDを中心に管理する。

例:

```text
C0001 Record
C0002 Memory
C0003 City
```

各言語は同じConcept IDに対応付ける。

---

# 韓国語コース 現在地

## Core10 完成済み

```text
C0001 기록
C0002 기억
C0003 도시
C0004 알림
C0005 회신
C0006 수신인
C0007 서명
C0008 검증
C0009 권한
C0010 역할
```

## Anki環境

作成済み:

```text
MEMORIOPOLIS::Korean
```

ノートタイプ:

```text
MEMORIOPOLIS Korean Vocabulary
```

## 現在のフィールド

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

---

# Core10の三本柱

## ExampleBreakdown

文を意味のまとまりへ分解する。

例:

```text
도시의 ＝ 都市の
기록을 ＝ 記録を
확인했다 ＝ 確認した
```

## ExampleExplanation

なぜその日本語訳になるのかを説明する。

目的:

```text
意味への橋
```

## ExamplePronunciationHint

なぜその音に聞こえるのかを説明する。

目的:

```text
音への橋
```

現在はC0001のみ試験実装。

---

# 音の橋の方針

重要決定事項:

単語欄ではカタカナを使わない。

ただし

```text
ExamplePronunciationHint
```

ではカタカナを解禁する。

理由:

```text
正しい発音を教えるためではない。

日本人の耳に
どう聞こえてしまうか
を説明するため。
```

推奨形式:

```text
ハングル
↓
Romanization
↓
日本人の耳に聞こえるカタカナ
```

例:

```text
기록을
(girogeul)

日本人の耳には
「キログル」
のように聞こえることがある。
```

---

# Anki構成

## 表面

```text
Concept ID
韓国語
TTS
```

## 裏面

```text
Romanization
日本語
品詞
例文
例文TTS
例文Romanization
例文日本語訳
文の組み立て
なぜこの意味になる？
なぜこの音に聞こえる？
出典
```

---

# 同期状況

## Windows版Anki

確認済み:

- 単語音声
- 例文音声
- ExampleBreakdown
- ExampleExplanation
- ExamplePronunciationHint

## AnkiWeb

同期成功。

既知の制約:

```text
TTSタグが文字として表示される。
```

## AnkiDroid

同期成功。

確認済み:

- 単語音声再生
- 例文音声再生
- 解説表示

主学習環境:

```text
AnkiDroid
＋
通勤学習
```

---

# 通勤学習で確認すること

特にC0001。

確認項目:

```text
ExamplePronunciationHint が
本当に役立つか。
```

判定基準:

```text
聞き取れない
↓
説明を読む
↓
ああ、この音だったのか
```

が起きるか。

---

# Core20について

方針変更済み。

第12節では作らない。

Core20は

```text
第13節
```

で作る。

予定語彙:

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

---

# 今後のロードマップ

## 第12節

```text
韓国語 Core10
↓
磨き込み
↓
韓国語 Core50
```

## その後

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

---

# 臺灣華語方針

残すもの:

```text
繁體字
拼音
注音符號
```

さらに将来的に

```text
日本人の耳には
どう聞こえるか
```

も扱う。

---

# ロシア語方針

扱うもの:

```text
キリル文字
転写
強勢
格
数
```

さらに

```text
なぜこの形になる？
なぜこの音に聞こえる？
```

を扱う。

---

# 歴史的仮名遣い方針

独立言語ではない。

```text
現代日本語
↓
歴史表記層
```

として扱う。

例:

```text
思う
↓
思ふ
```

---

# 次回開始チェックリスト

- AnkiDroidでC0001確認
- ExamplePronunciationHint評価
- 採用可否判断
- 採用ならC0002-C0010へ展開
- CSV更新
- README更新
- テンプレート更新
- GitHubコミット

---

# 現在地

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

『記憶都市読解コース』は、意味の橋に加えて音の橋を試作する段階へ到達した。
