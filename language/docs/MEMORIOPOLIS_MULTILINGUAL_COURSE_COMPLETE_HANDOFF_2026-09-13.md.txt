# MEMORIOPOLIS 多言語読解コース 完全版引き継ぎ書

**更新日：2026年9月13日**  
**対象：韓国語・ロシア語Anki、ロシア語Novel、臺灣華語音声環境、今後の制作順序**  
**現在地：ロシア語Anki Core10 draft01は、PC版Anki・AnkiWeb・AnkiDroidで同期およびTTS動作確認済み。今後はロシア語Core10を数回反復し、ロシア語へ慣れてからNovelを推敲する。本日の作業はここで終了。**

---

## 0．最重要サマリー

- 韓国語版Anki Core10はFIX・コミット済み。
- ロシア語Novel `section12_ru_draft01.md` は作成済みだが、未正本。
- ロシア語Anki Core10 draft01は10件、16フィールドで作成済み。
- `MEMORIOPOLIS::Russian`デッキと`MEMORIOPOLIS Russian Vocabulary`ノートタイプを作成済み。
- Windowsへロシア語音声環境を導入済み。
- PC版Ankiで単語TTSと例文TTSを設定済み。
- 単語TTSは`Russian`フィールド、例文TTSは`ExampleRussian`フィールドを読む。
- C0001、C0006、C0010でPC版Ankiの単語・例文音声を確認済み。
- AnkiWebへ同期済み。
- AnkiDroidでもロシア語の表示・単語TTS・例文TTSが正常に動作することを確認済み。
- 親デッキ`MEMORIOPOLIS`から、韓国語とロシア語を混ぜて学習できることを確認済み。
- 学習後に予定日を待たず自由に復習するときは、カスタム学習またはフィルターデッキを用いる。
- 自由復習ではランダム順、再スケジュールなしを基本とする。
- 当面はロシア語Core10を何度か繰り返し、キリル文字、強勢、格、音に慣れる。
- ロシア語Novelの推敲は、ロシア語Core10を数回反復した後に行う。
- その後、今回だけの特別工程として臺灣華語Anki Core10、英語Anki Core10へ戻る。
- その後、`JANUS-13：Unicode Observation Polyhedron`構想へ移る。
- 臺灣華語のWindows言語パック導入は別会話で進行中だが、現在未解決。
- 本日のGit差分はない。TTS追加はAnki内部のカードテンプレート変更であり、AnkiWebへ保存済み。

---

## 1．現在の親デッキ構造

```text
MEMORIOPOLIS
├─ Korean
└─ Russian
```

将来は各言語を同じ親デッキ配下へ追加する。

```text
MEMORIOPOLIS
├─ Korean
├─ Russian
├─ Taiwanese Mandarin
├─ English
├─ Historical Japanese
├─ Filipino
├─ Indonesian
├─ Vietnamese
├─ French
├─ German
├─ Italian
├─ Spanish
└─ Portuguese
```

通勤学習では、言語別子デッキではなく親デッキ`MEMORIOPOLIS`を選ぶ。

これにより、その日に復習対象となったカードと新規カードが、言語を横断して出題される。

2026年9月13日、親デッキから韓国語とロシア語が交互に出題されることを実機で確認した。

---

## 2．韓国語版Anki Core10

### 状態

```text
韓国語Novel：正本
韓国語Anki Core10：FIX
AnkiDroid確認：完了
Gitコミット：完了
```

### 音の橋

韓国語では次の三層を採用した。

```text
ハングル
↓
Romanization
↓
日本人の耳に聞こえるカタカナ
```

カタカナは発音の正解ではない。音声中の対象語を発見し、ハングルへ戻るための一時的な橋である。

---

## 3．ロシア語Novel

### ファイル

```text
section12_ru_draft01.md
```

### 状態

```text
第一稿：作成済み
正本化：未実施
推敲：保留中
```

ロシア語Novelは、ロシア語Core10を数回反復し、キリル文字、強勢、格変化、音のまとまりに慣れてから推敲する。

学習中に気づいた点は、すぐ直さず、必要に応じてメモする。

- 音の橋と実際の音が離れている。
- 例文が長く、耳で追いにくい。
- 強勢位置に違和感がある。
- 格の説明が腹落ちしない。
- 日本語訳との焦点が異なる。
- Novelの言い回しを再検討したい。

---

## 4．ロシア語Anki Core10 draft01

### Concept ID

```text
C0001 запись          記録
C0002 память          記憶
C0003 город           都市
C0004 уведомление     通知
C0005 ответ           返信／返事
C0006 адресат         宛先／受取人
C0007 подпись         署名
C0008 проверка        検証／確認
C0009 полномочия      権限
C0010 роль            役割／ロール
```

### デッキ

```text
MEMORIOPOLIS::Russian
```

### ノートタイプ

```text
MEMORIOPOLIS Russian Vocabulary
```

### 16フィールド

```text
1  ID
2  Russian
3  Stress
4  Transliteration
5  Japanese
6  PartOfSpeech
7  RussianGrammar
8  ExampleRussian
9  ExampleStress
10 ExampleTransliteration
11 ExampleJapanese
12 Source
13 Tags
14 ExampleBreakdown
15 ExampleExplanation
16 ExamplePronunciationHint
```

### 状態

```text
10ノート：登録済み
表面テンプレート：設定済み
裏面テンプレート：設定済み
CSS：設定済み
PC版TTS：設定済み
AnkiWeb同期：完了
AnkiDroid同期：完了
AnkiDroid TTS：確認済み
Core10最終FIX：未実施
```

---

## 5．ロシア語TTSの確定構成

音声専用フィールドは追加しない。

既存の文字フィールドを、AnkiのTTSタグで読み上げる。

### 表面の単語TTS

```html
{{tts ru_RU:Russian}}
```

読み上げ対象：

```text
Russian
```

例：

```text
запись
```

### 裏面の例文TTS

```html
<div class="tts-audio">
  {{tts ru_RU:ExampleRussian}}
</div>
```

読み上げ対象：

```text
ExampleRussian
```

例：

```text
«Это та запись, которую мы видели раньше?»
```

### 強勢付きフィールドの役割

```text
Stress
ExampleStress
```

は視覚学習用とする。

TTSには結合アクセント記号を含まない通常表記を渡す。

```text
目で強勢を見る
→ Stress / ExampleStress

耳で通常のロシア語を聞く
→ Russian / ExampleRussian
```

---

## 6．TTS動作確認結果

### PC版Anki

次のカードで単語TTSと例文TTSを確認した。

```text
C0001 запись
C0006 адресат
C0010 роль
```

結果：正常。

### AnkiWeb

親デッキと子デッキが反映済み。

```text
MEMORIOPOLIS
├─ Korean
└─ Russian
```

### AnkiDroid

次を確認済み。

- ロシア語Core10が表示される。
- 単語TTSがロシア語で再生される。
- 例文TTSがロシア語で再生される。
- 強勢付き表記が表示される。
- 日本語訳、文法、意味・語形の橋、音の橋が表示される。
- 親デッキから韓国語とロシア語が交互に出題される。

総合判定：ロシア語Ankiの技術基盤は完成。

---

## 7．通常学習と自由復習

### 通常学習

親デッキを開く。

```text
MEMORIOPOLIS
```

Ankiが、その日に必要なカードを韓国語・ロシア語から出題する。

### 学習後、予定日を待たずもう一周する

AnkiDroidで次を使う。

```text
MEMORIOPOLIS
↓
カスタム学習
↓
カードの状態またはタグで学習
↓
すべてのカード
↓
十分な枚数を指定
↓
ランダム
↓
再スケジュールなし
```

現時点では韓国語10枚、ロシア語10枚なので、20枚以上を指定すれば全体を対象にできる。

### ロシア語だけ自由復習する

```text
Russian
↓
カスタム学習
↓
すべてのカード
↓
10枚
↓
ランダム
↓
再スケジュールなし
```

### フィルターデッキ検索式候補

親デッキ全体：

```text
deck:"MEMORIOPOLIS"
```

学習済みの復習カードだけ：

```text
deck:"MEMORIOPOLIS" is:review
```

自由練習では本来の復習予定を動かさないため、再スケジュールなしを基本とする。

---

## 8．本日のGit状態

本日の変更内容は、Anki内部のカードテンプレートへのTTS追加のみ。

```text
ローカルリポジトリ：変更なし
Gitコミット：不要
Ankiコレクション：変更済み
AnkiWeb：同期済み
AnkiDroid：同期済み
```

学習履歴とカードテンプレートはAnkiWebへ保存されている。

次回リポジトリを更新するときは、再現性を高めるため次へTTS設定を追記する。

```text
RUSSIAN_NOTE_TYPE_DRAFT01.md
```

記録対象：

```html
{{tts ru_RU:Russian}}
{{tts ru_RU:ExampleRussian}}
```

必要に応じて、カードテンプレートを独立ファイルとして管理する。

```text
anki/russian/
├─ front.html
├─ back.html
├─ style.css
└─ README.md
```

---

## 9．臺灣華語の音声環境

臺灣華語版Ankiの音声環境を先に準備するため、Windowsへ`zh-TW`言語機能を導入中。

この作業は別会話で進めている。

別会話の引き継ぎファイル：

```text
Windows_zh-TW_language_pack_handover_2026-09-12.md.txt
```

### 現在の状態

- ロシア語`ru-RU`は導入成功。
- 韓国語`ko-KR`はBasicTyping、Handwriting、TextToSpeech、OCRを確認済み。
- 臺灣華語`zh-TW`は未導入。
- `Install-Language zh-TW`は`0x800705B4`でタイムアウト。
- `Add-WindowsCapability`は「指定されたファイルが見つかりません」で失敗。
- `zh-TW`の各Windows Capabilityは候補として認識されているが、NotPresent。

### 別会話での次の調査項目

1. Windowsバージョン、OSビルド、アーキテクチャ。
2. `Add-WindowsCapability`の完全なエラー情報。
3. DISMログとCBSログ。
4. WSUSおよびServicingポリシー。
5. コンポーネントストアの状態。
6. 必要に応じて、OSビルドに一致するLanguages and Optional Features ISOによるオフライン導入。

### 重要な注意

- 正確なログ取得前にWindows Updateキャッシュを削除しない。
- 出所不明のCABを使用しない。
- OSビルド不一致の言語ISOを使用しない。
- 会社管理PCのWSUS、ポリシー、レジストリを無断変更しない。

臺灣華語の言語パック問題は、本会話では解決せず、別会話の引き継ぎに従う。

---

## 10．これからの制作順序

今回の特別工程として、次の順序で進める。

```text
1. ロシア語Core10を数回反復
2. ロシア語の文字・強勢・格・音に慣れる
3. 臺灣華語Anki Core10を作成
4. 英語Anki Core10を作成
5. JANUS-13構想へ移行
6. 適切な時点でロシア語NovelへReturn
7. ロシア語Novelを推敲・正本化
8. ロシア語Anki Core10を最終FIX
```

ロシア語Novelの推敲は中止ではない。

語感を持たないまま直ちに推敲するのではなく、Core10を反復してから戻る。

---

## 11．臺灣華語Anki Core10の予定要素

```text
繁體字
拼音
注音符號
日本語訳
品詞
例文
例文拼音
例文注音
例文日本語訳
文の組み立て
意味の橋
音の橋
TTS
Source
Tags
```

臺灣華語でも、カタカナは発音の正解ではなく、日本人の耳が音声中の語を見つけるための仮設の橋として扱う。

WindowsとAnkiDroidの音声環境が整ってから、具体的なノートタイプを設計する。

---

## 12．英語Anki Core10の予定要素

英語は読解自体に大きな問題がなくても、13言語でConcept IDを共有するためにAnkiを作成する。

```text
英単語
発音
日本語訳
品詞
例文
例文発音
例文日本語訳
文の組み立て
意味の橋
語順と主体の説明
音の橋
TTS
Source
Tags
```

英語版では、第十二節で`I.`と一人称`I`が同じ文字へ重なる点も重要な観測事項となる。

---

## 13．JANUS-13

正式名称：

```text
JANUS-13：Unicode Observation Polyhedron
```

### 基本構造

```text
13言語
14表示窓
```

日本語は1言語であり、内部に対等な二つの表示層を持つ。

```text
現代日本語 ⇄ 歴史的仮名遣い
```

外国語12言語は対等な観測点。

各外国語と日本語は、翻訳元・翻訳先の一方向関係ではなく、互いに照らし合う。

主なUI構想：

- 直近3言語。
- 観測点を開く。
- 13面／14窓。
- 言語の自称。
- 象徴文字。
- Unicode符号位置。
- 国旗を主要表示に使わない。
- 「都市に任せる」による観測点選択。
- 素数13を利用した重複のない巡回。
- 立体UIと通常一覧の併設。

JANUS-13の実装検討は、臺灣華語・英語Anki Core10の後に進める。

---

## 14．次回開始時の確認事項

### ロシア語学習を続ける場合

- [ ] 親デッキ`MEMORIOPOLIS`から学習する。
- [ ] 韓国語とロシア語が適度に切り替わるか確認する。
- [ ] ロシア語の単語音声を繰り返す。
- [ ] 例文音声から対象語を拾う。
- [ ] 強勢位置を見る。
- [ ] 格変化を確認する。
- [ ] 音の橋が実音を助けるか確認する。
- [ ] 気づきがあればメモする。
- [ ] 直ちにNovelを修正しない。

### 自由復習する場合

- [ ] カスタム学習を開く。
- [ ] 親デッキ全体を対象にする。
- [ ] 枚数をカード総数以上にする。
- [ ] ランダム順を選ぶ。
- [ ] 再スケジュールなしにする。

### 次の制作へ進む場合

- [ ] 別会話で臺灣華語言語パック問題の状況を確認する。
- [ ] 臺灣華語TTS環境が利用できるか確認する。
- [ ] 臺灣華語Anki Core10のノートタイプを設計する。
- [ ] 臺灣華語完成後、英語Anki Core10を作成する。
- [ ] その後、JANUS-13の具体設計へ進む。

---

## 15．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月13日の最新状態として、『記憶都市（メモリオポリス）』多言語読解コースの制作を再開します。

韓国語版Anki Core10はFIX・コミット済みです。

ロシア語Novelはsection12_ru_draft01.mdとして第一稿を作成済みですが、まだ正本ではありません。ロシア語Anki Core10 draft01は、MEMORIOPOLIS::Russianデッキ、MEMORIOPOLIS Russian Vocabularyノートタイプ、16フィールド、10ノートで構築済みです。

PC版Ankiでは、表面に{{tts ru_RU:Russian}}、裏面に{{tts ru_RU:ExampleRussian}}を設定済みです。C0001、C0006、C0010で単語TTSと例文TTSを確認済みです。AnkiWebへ同期し、AnkiDroidでもロシア語の表示、単語TTS、例文TTSが正常に動作することを確認済みです。

親デッキMEMORIOPOLISから、韓国語とロシア語が混ざって出題されることも確認済みです。学習後に予定日を待たずもう一周するときは、カスタム学習またはフィルターデッキを使い、全カード、ランダム、再スケジュールなしを基本とします。

当面はロシア語Core10を数回反復し、キリル文字、強勢、格変化、音に慣れます。ロシア語Novelの推敲は、その後に行います。

今回だけの特別工程として、その後は臺灣華語Anki Core10、英語Anki Core10へ戻り、続いてJANUS-13：Unicode Observation Polyhedron構想へ進みます。適切な時点でロシア語NovelへReturnし、Novel正本化後にロシア語Core10を最終FIXします。

臺灣華語のWindows言語パックzh-TWは別会話で導入作業中ですが、現在は未解決です。Windows_zh-TW_language_pack_handover_2026-09-12.md.txtを参照し、別会話側で継続してください。

本日のTTS追加はAnki内部の変更だけで、ローカルGitリポジトリに差分はありません。次回リポジトリを変更するとき、RUSSIAN_NOTE_TYPE_DRAFT01.mdへ確認済みTTSタグを追記してください。
```

---

## 16．2026年9月13日の店じまい地点

```text
韓国語版Anki Core10                    FIX・コミット済み
ロシア語Novel draft01                  作成済み・未正本
ロシア語Anki Core10 draft01            作成済み
ロシア語16フィールド                   設定済み
ロシア語単語TTS                        PC版・AnkiDroidで正常
ロシア語例文TTS                        PC版・AnkiDroidで正常
C0001 / C0006 / C0010音声              確認済み
AnkiWeb同期                            完了
親デッキ多言語混合学習                 確認済み
自由復習方法                           確認済み
ロシア語Core10反復                     これから継続
ロシア語Novel推敲                      反復後に実施
臺灣華語Windows言語パック              別会話で継続・未解決
臺灣華語Anki Core10                    次の制作候補
英語Anki Core10                        臺灣華語の後
JANUS-13                               その後
本日のGit差分                          なし
本日の店じまい                        完了
```

本日の到達点は次の一文に集約できる。

> 韓国語とロシア語の記憶は親デッキMEMORIOPOLISで交差し、ロシア語Core10はPC版AnkiからAnkiDroidまで文字・強勢・意味・語形・音を一つの学習循環として動かせる状態になった。今後は繰り返し触れることでロシア語の感覚を育て、臺灣華語、英語、JANUS-13へ観測点を広げる。
