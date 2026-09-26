# MEMORIOPOLIS 韓国語読解コース 引き継ぎ書

- 作成日：2026年9月7日
- 対象リポジトリ：`MEMORIOPOLIS`
- 対象企画：『記憶都市（メモリオポリス）』多言語小説読解コース
- 現在の起点：第4章「翻訳者」第12節「受信人のない回信」

## 1. 企画の目的

『記憶都市（メモリオポリス）』を多言語で読めるようになることを目的として、作品本文に現れる概念、語彙、文法、例文、発音を統合した読解教材を構築する。

一般的な語学教材ではなく、次の流れを一体化したスピンオフ作品として設計する。

```text
小説本文
  ↓
作品内の概念
  ↓
多言語の語彙対応
  ↓
Ankiによる反復学習
  ↓
原文読解
```

教材の中心は個別言語ではなく、言語に依存しない概念IDとする。

```text
C0001 Record
C0002 Memory
C0003 City
...
```

各言語は、同じ概念IDに対応する語彙レイヤーとして追加する。

## 2. 合意済みの全体方針

### 2.1 五言語の扱い

最終成果物は五言語対照とし、学習導線は言語別にする。

対象言語：

1. 日本語
2. English
3. 한국어
4. 臺灣繁體中文
5. Русский

### 2.2 制作順序

Core 1000を先に作り切る方式は採用しない。

小説の節と語彙を交互に育てる螺旋型で進める。

```text
第12節
  ↓
共通Core 100を五言語化
  ↓
第13節
  ↓
Core 101以降を追加し、Core 200付近へ
  ↓
次の節
```

Core番号は概念IDとして言語間で共有する。

### 2.3 言語別の発音表記

- 韓国語：改訂ローマ字表記
- 臺灣華語：声調記号付き漢語拼音と声調付き注音符号を両方残す
- ロシア語：ラテン文字転写に加え、将来的に強勢、格、数、作中語形を扱う
- 英語：ローマ字欄は設けず、発音、語法、コロケーションを重視する

### 2.4 臺灣華語版の標準仕様

臺灣華語版では、次を標準構成とする。

```text
繁體字
声調記号付き漢語拼音
声調付き注音符号
日本語
品詞
作中例文
例文の拼音
例文の注音
例文の日本語訳
臺灣華語TTS
出典
```

表面は原則として繁體字のみとし、拼音と注音は解答面に表示する。

## 3. 現在のリポジトリ構成

```text
MEMORIOPOLIS/
└─ language/
   ├─ anki/
   │  ├─ ko_core10_master.csv
   │  ├─ ko_core10_anki.csv
   │  └─ templates/
   │     ├─ README.md
   │     ├─ korean_vocabulary_front.html
   │     ├─ korean_vocabulary_back.html
   │     └─ korean_vocabulary_style.css
   ├─ audio/
   ├─ glossary/
   │  └─ concept/
   │     ├─ README.md
   │     ├─ C0001_Record.md
   │     ├─ C0002_Memory.md
   │     ├─ C0003_City.md
   │     ├─ C0004_Notification.md
   │     ├─ C0005_Reply.md
   │     ├─ C0006_Recipient.md
   │     ├─ C0007_Signature.md
   │     ├─ C0008_Verification.md
   │     ├─ C0009_Authority.md
   │     └─ C0010_Role.md
   └─ lessons/
```

## 4. Gitの反映状況

以下の作業はコミットおよびpush済み。

### Core 10の正本・Anki派生版

```text
feat(language): add master and Anki CSV files for Korean Core 10
```

### AnkiカードテンプレートとTTS

```text
feat(language): add Korean Anki card templates with TTS
```

テンプレート追加時のコミット：

```text
6e56d47
```

## 5. 韓国語Core 10

| ID | 한국어 | Romanization | 日本語 |
|---|---|---|---|
| C0001 | 기록 | girok | 記録 |
| C0002 | 기억 | gieok | 記憶 |
| C0003 | 도시 | dosi | 都市 |
| C0004 | 알림 | allim | 通知 |
| C0005 | 회신 | hoesin | 回信／返信 |
| C0006 | 수신인 | susinin | 受信人／宛先 |
| C0007 | 서명 | seomyeong | 署名 |
| C0008 | 검증 | geomjeung | 検証 |
| C0009 | 권한 | gwonhan | 権限 |
| C0010 | 역할 | yeokhal | 役割／ロール |

## 6. CSVの役割

### `ko_core10_master.csv`

- 見出しあり
- GitHub上の編集用正本
- 人間が内容を確認しやすい形式

見出し：

```text
ID
Korean
Romanization
Japanese
PartOfSpeech
ExampleKorean
ExampleRomanization
ExampleJapanese
Source
Tags
```

### `ko_core10_anki.csv`

- 見出しなし
- Ankiへ直接インポートする派生版
- 10行が10枚のカードになる

今後も必ず、編集用masterとAnki投入用を分離する。

## 7. Windows版Ankiの現在の状態

### 7.1 作成済みデッキ

```text
MEMORIOPOLIS::Korean
```

### 7.2 作成済みノートタイプ

```text
MEMORIOPOLIS Korean Vocabulary
```

### 7.3 フィールド

```text
1. ID
2. Korean
3. Romanization
4. Japanese
5. PartOfSpeech
6. ExampleKorean
7. ExampleRomanization
8. ExampleJapanese
9. Source
10. Tags
```

### 7.4 カード表面

- 概念IDを小さく表示
- 韓国語を大きく表示
- 韓国語単語のTTS再生
- Romanizationや日本語を先に見せない

### 7.5 カード裏面

- 表面を再掲
- Romanization
- 日本語
- 品詞
- 韓国語例文
- 例文の韓国語TTS
- 例文のRomanization
- 例文の日本語訳
- 出典

### 7.6 TTS

次のAnki TTS指定を使用している。

```html
{{tts ko_KR:Korean}}
{{tts ko_KR:ExampleKorean}}
```

Windowsへ韓国語の音声合成機能を追加済みで、Windows版Ankiにおける単語と例文の音声再生は動作確認済み。

音声は固定MP3ではなく、端末側の音声合成機能を利用する。

## 8. Ankiカードの動作確認結果

Windows版Ankiで次を確認済み。

- Core 10の10件を読み込み済み
- 見出し行をカードとして取り込む問題を修正済み
- 表面の韓国語表示が正常
- 裏面のRomanization、日本語、品詞、例文、出典が正常
- 単語TTSが再生可能
- 例文TTSが再生可能
- 長い例文もカード内に表示可能

## 9. 明日の最優先作業

目的は、Core 10をスマートフォンで学習できるか確認すること。

### 9.1 AnkiWebアカウント作成

- Gmailアドレスを登録用メールアドレスとして使用可能
- Google連携ログインではなく、AnkiWeb専用パスワードを設定する
- メール認証を完了する

### 9.2 Windowsから初回同期

1. Windows版Ankiを開く
2. 上部の「同期」を押す
3. AnkiWebのメールアドレスとパスワードを入力する
4. 初回に選択を求められたら、Windows側からAnkiWebへアップロードする

重要：現在の正本はWindows側にあるため、初回に空のAnkiWebデータをダウンロードしない。

### 9.3 スマートフォンで確認

- Android：AnkiDroidを使用
- iPhone/iPad：まずAnkiWebをブラウザーで試すことも可能。公式AnkiMobileは有料買い切り

公式アプリを使用する場合：

1. Windowsと同じAnkiWebアカウントでログイン
2. スマートフォン側ではAnkiWebからダウンロード
3. `MEMORIOPOLIS::Korean` が表示されることを確認

### 9.4 スマートフォンでの合格条件

- Core 10が表示される
- 表面の韓国語が読みやすい
- 解答面の文字や例文が画面幅に収まる
- 横スクロールが発生しない
- 単語TTSが再生される
- 例文TTSが再生される
- C0010の長い例文が崩れない
- 夜間モードでも読める
- スマートフォンで2から3枚学習する
- スマートフォンで同期後、Windows側へ学習履歴が反映される

TTSは端末依存であるため、スマートフォン側に臺灣華語や韓国語などの対象言語音声が必要になる場合がある。

## 10. Core 10確認後の次工程

### 10.1 韓国語Core 11から20

候補：

| ID | 한국어 | 日本語 |
|---|---|---|
| C0011 | 경로 | 経路 |
| C0012 | 복호화 | 復号 |
| C0013 | 열쇠 | 鍵 |
| C0014 | 참조 | 参照 |
| C0015 | 식별자 | 識別子 |
| C0016 | 설정 | 設定 |
| C0017 | 정지 | 停止 |
| C0018 | 재개 | 再開 |
| C0019 | 실행 | 実行 |
| C0020 | 영향 | 影響 |

作成予定：

```text
C0011-C0020の概念Markdown
ko_core20_master.csv
ko_core11-20_anki.csv
ko_core20_anki.csv
```

用途：

- `ko_core20_master.csv`：C0001からC0020の見出し付き正本
- `ko_core11-20_anki.csv`：現在のAnkiへ追加する差分
- `ko_core20_anki.csv`：将来の再構築用全件版

### 10.2 韓国語Core 100

- 10語単位で追加する
- 各10語を実際に学習してから次へ進む
- Core 100時点でカード設計、語彙順、例文長、TTS品質を再評価する
- 韓国語文法カードは語彙カードと別ノートタイプで設計する
- 最終目標は第12節を約8割読める語彙・文法力

## 11. Core 100以降のロードマップ

推奨順序：

1. 韓国語Core 100を完成
2. 第12節ロシア語版を作成
3. 共通C0001-C0100へロシア語レイヤーを追加
4. ロシア語Anki Core 100を作成
5. 第12節臺灣繁體中文版を整備
6. 共通C0001-C0100へ臺灣華語レイヤーを追加
7. 臺灣華語Anki Core 100を作成
8. 第12節英語版を整備
9. 共通C0001-C0100へ英語レイヤーを追加
10. 英語Anki Core 100を作成
11. 第12節を五言語読解ユニットとして完成
12. Novel第13節へ進む
13. 第13節の新規概念をC0101以降として追加
14. Core 200付近まで拡張

Core 1000は先に作る目標ではなく、複数の節を多言語で通過した結果として形成する。

## 12. 言語別Anki設計の予定

### 韓国語

```text
Korean
Romanization
Japanese
PartOfSpeech
ExampleKorean
ExampleRomanization
ExampleJapanese
TTS ko_KR
```

### 臺灣華語

```text
TraditionalChinese
Pinyin
Bopomofo
Japanese
PartOfSpeech
ExampleTraditionalChinese
ExamplePinyin
ExampleBopomofo
ExampleJapanese
TTS zh_TW
```

拼音と注音符号は両方とも残す。

### ロシア語

将来的に次を検討する。

```text
辞書形
ラテン文字転写
強勢位置
日本語
品詞
作中語形
格
数
例文
例文転写
日本語訳
ロシア語TTS
```

### 英語

```text
English
Japanese
PartOfSpeech
Pronunciation
Collocation
ExampleEnglish
ExampleJapanese
English TTS
```

## 13. 品質管理上の注意

- Concept IDを言語ごとに作り直さない
- 各言語は共通Concept IDにぶら下げる
- 作品本文での意味を優先する
- 自動翻訳や自動発音変換は候補生成として使用し、文脈で確認する
- 多音字、ロシア語の格変化、英語の語法は単純な一対一対応にしない
- master CSVを正本とし、Anki用CSVは派生物とする
- Ankiへの追加には差分CSVを使い、重複を避ける
- 全件Anki CSVは再構築用として保持する
- テンプレート変更はAnki内だけで終わらせず、GitHubにも保存する
- 固定音声ファイルを導入するまでは、TTSが端末依存であることを明記する

## 14. 次回開始時のチェックリスト

- [ ] AnkiWebアカウントを作成する
- [ ] メール認証を完了する
- [ ] Windows版AnkiからAnkiWebへ初回アップロードする
- [ ] スマートフォンで同じアカウントへログインする
- [ ] Core 10をスマートフォンへダウンロードする
- [ ] カード表面を確認する
- [ ] カード裏面を確認する
- [ ] 単語TTSを確認する
- [ ] 例文TTSを確認する
- [ ] C0010の長い例文を確認する
- [ ] スマートフォンで2から3枚学習する
- [ ] 学習後にスマートフォンから同期する
- [ ] Windows版Ankiへ同期する
- [ ] 学習履歴の往復同期を確認する
- [ ] 問題がなければCore 11から20の制作へ進む

## 15. 現在地

本日、次の制作系統が成立した。

```text
MEMORIOPOLIS GitHub正本
  ↓
言語非依存のConcept Dictionary
  ↓
韓国語Core Vocabulary
  ↓
Ankiカード
  ↓
韓国語TTS
  ↓
PCでの反復学習
  ↓
AnkiWebとスマートフォンへの展開
```

これは『記憶都市』に追加された新しい幕であり、第4章「翻訳者」の読者が、作中の翻訳を自ら追体験するための入口である。
