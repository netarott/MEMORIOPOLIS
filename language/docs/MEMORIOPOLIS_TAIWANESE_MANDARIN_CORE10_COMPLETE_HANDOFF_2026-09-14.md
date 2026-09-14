# MEMORIOPOLIS 多言語読解コース 完全版引き継ぎ書

**更新日：2026年9月14日**  
**対象：臺灣華語Anki Core10、韓国語・ロシア語Anki、今後の英語版、JANUS-13**  
**現在地：臺灣華語Anki Core10 draft01をPC版Ankiへ10件インポートし、C0001およびC0010の表示、単語TTS、例文TTS、意味・語順の橋、音の橋まで確認済み。次工程はAnkiWebへ同期し、AnkiDroidで表示と音声を確認すること。**

---

## 0．最重要サマリー

- 韓国語版Anki Core10はFIX・コミット済み。
- ロシア語版Anki Core10 draft01はPC版Anki、AnkiWeb、AnkiDroidでTTS動作確認済み。
- ロシア語Novel `section12_ru_draft01.md` は第一稿で、まだ正本ではない。
- ロシア語Novelの推敲は、ロシア語Core10を数回反復してから行う。
- 親デッキ`MEMORIOPOLIS`から、韓国語とロシア語を混合して学習できることを確認済み。
- 自由復習では、カスタム学習またはフィルターデッキを用い、ランダム、再スケジュールなしを基本とする。
- 臺灣華語版Anki Core10 draft01を作成済み。
- PC版Ankiに`MEMORIOPOLIS::TaiwaneseMandarin`デッキを作成済み。
- PC版Ankiに`MEMORIOPOLIS Taiwanese Mandarin Vocabulary`ノートタイプを作成済み。
- 臺灣華語版ノートタイプは16フィールド。
- 13番目の通常フィールド名は、Ankiの予約的な名称`Tags`を避け、`CourseTags`とした。
- `zh_tw_core10_anki_draft01.csv`をインポート済み。
- インポート結果は新規追加10件、更新0件。
- C0001「紀錄」の繁體字、注音符號、拼音、日本語、品詞、用法、例文、三つの橋を確認済み。
- C0010「角色」の意味・語順の橋、音の橋、Sourceを確認済み。
- Windowsの臺灣華語TTS導入に苦労したが、PC版Ankiで単語音声と例文音声が正常に再生されている。
- 臺灣華語のTTSは`TraditionalChinese`と`ExampleTraditionalChinese`を読む。
- 音声専用フィールドは追加していない。
- 次工程はカードテンプレートを保存し、PC版Ankiを同期し、AnkiDroidで抜き取り確認すること。
- 臺灣華語Ankiの次は、端末へ英語音声環境を準備し、英語Anki Core10を作る。
- その後、`JANUS-13：Unicode Observation Polyhedron`に沿って各言語のAnki版を順次作る。
- JANUS-13の最初の候補として、歴史的仮名遣いを検討している。

---

## 1．全体の制作思想

『記憶都市（メモリオポリス）』は小説から始まり、複数言語の定本を作る工程へ発展した。

```text
小説
↓
各言語版
↓
☆型で日本語へReturn
↓
各言語の定本を判断するための用法習熟
↓
Anki Core10
↓
意味の橋・語形の橋・音の橋
↓
多言語横断学習
↓
JANUS-13
```

従来型の語学学習のように、あらゆる日常語彙を母語と同程度まで身につけることを最初の目的にしない。

自分の関心領域である『記憶都市』、人工知性、制度、関係、存在、翻訳、記憶、技術、組織、権限などを中心に、Concept IDを多言語へ接続する。

```text
未知の意味を13回覚える
```

のではなく、

```text
既知の概念へ13種類の文字・音・文法の入口を作る
```

ことを目指す。

---

## 2．Concept ID Core10

```text
C0001 記録
C0002 記憶
C0003 都市
C0004 通知
C0005 返信
C0006 宛先
C0007 署名
C0008 検証
C0009 権限
C0010 役割
```

各言語で同じConcept IDを共有する。

Core10を単位として追加し、最初からCore1000やCore2000を大規模設計しない。

```text
Core10を作る
↓
多言語で反復する
↓
Novelを読み直す
↓
不足する概念や関係が見える
↓
次のCore10を増設する
```

将来的なCore1000・Core2000は、先に満たす数値目標ではなく、作品とともに成長した都市規模として扱う。

---

## 3．共通骨格語彙とRelation

関心領域の専門語だけでは文章は動かないため、将来のCoreには次の三層を含める。

```text
1. 共通骨格語彙
2. 関係と文法
3. 関心領域の概念語彙
```

共通骨格語彙の例：

```text
ある
ない
する
なる
見る
言う
前
後
同じ
違う
誰
何
まだ
しかし
```

関係の例：

```text
誰が
何を
誰に
どこから
何によって
いつまで
可能か
否定か
確定か
推測か
```

将来的にはConcept IDに加えてRelation IDを検討できる。

```text
C0001 記録
R0001 対象
R0002 所有・所属
R0003 起点
R0004 可能
R0005 否定
```

ただし、現時点では大風呂敷を広げず、Core10を継続する。

---

## 4．現在のAnki親デッキ構造

```text
MEMORIOPOLIS
├─ Korean
├─ Russian
└─ TaiwaneseMandarin
```

通勤時は親デッキ`MEMORIOPOLIS`を選ぶ。

これにより、その日に出題対象となる韓国語、ロシア語、臺灣華語のカードが混合される。

親デッキは「記憶を呼び戻す中央駅」として機能する。

---

## 5．通常復習と自由復習

### 通常復習

```text
親デッキMEMORIOPOLISを開く
```

Ankiの予定日に従って各言語のカードを復習する。

### 予定日前にもう一周する

```text
MEMORIOPOLIS
↓
カスタム学習
↓
カードの状態またはタグで学習
↓
すべてのカード
↓
カード総数以上を指定
↓
ランダム
↓
再スケジュールなし
```

### フィルターデッキ候補

```text
deck:"MEMORIOPOLIS"
```

学習済みの復習カードだけを対象にする場合：

```text
deck:"MEMORIOPOLIS" is:review
```

自由練習では、本来の復習予定を不要に動かさないため、再スケジュールなしを基本とする。

---

## 6．韓国語版の状態

```text
韓国語Novel：正本
韓国語Anki Core10：FIX
AnkiDroid確認：完了
Gitコミット：完了
```

韓国語版で確立した音の橋：

```text
ハングル
↓
Romanization
↓
日本人の耳に聞こえるカタカナ
↓
ハングルへ戻る
```

カタカナは発音の正解ではなく、音声中の対象語を見つける一時的な足場である。

---

## 7．ロシア語版の状態

### Novel

```text
section12_ru_draft01.md
```

- 第一稿。
- 未正本。
- Core10を数回反復し、ロシア語に慣れてから推敲する。

### Anki

```text
デッキ：MEMORIOPOLIS::Russian
ノートタイプ：MEMORIOPOLIS Russian Vocabulary
状態：draft01
```

### TTS

```html
{{tts ru_RU:Russian}}
```

```html
{{tts ru_RU:ExampleRussian}}
```

C0001、C0006、C0010でPC版・AnkiDroidの音声を確認済み。

---

## 8．臺灣華語版Core10の成果物

### ZIP

```text
MEMORIOPOLIS_Taiwanese_Mandarin_Core10_draft01_2026-09-14.zip
```

### 収録ファイル

```text
zh_tw_core10_master_draft01.csv
zh_tw_core10_anki_draft01.csv
README_zh_tw_core10_draft01.md
ZH_TW_NOTE_TYPE_DRAFT01.md
```

### 役割

#### `zh_tw_core10_master_draft01.csv`

- ヘッダーあり。
- 管理・推敲用。
- 将来の正本候補。

#### `zh_tw_core10_anki_draft01.csv`

- ヘッダーなし。
- PC版Ankiへの取込用。
- 10件、16列。

#### `README_zh_tw_core10_draft01.md`

- 臺灣華語版の設計原則。
- Sourceの例外。
- TTS環境に関する注意。

#### `ZH_TW_NOTE_TYPE_DRAFT01.md`

- ノートタイプ、フィールド、TTSの設計案。

---

## 9．臺灣華語Core10

```text
C0001 紀錄    記録
C0002 記憶    記憶
C0003 城市    都市
C0004 通知    通知
C0005 回覆    返信／返答
C0006 收件人  受取人／宛先
C0007 簽章    署名／電子署名
C0008 驗證    検証／認証
C0009 權限    権限
C0010 角色    役割／ロール
```

### Source

C0003`城市`だけは第十二節本文に対象語が直接現れないため、読解コース用例文とした。

```text
C0003 Source：MEMORIOPOLIS core
```

それ以外は次のSource。

```text
section12_zh-TW
```

---

## 10．臺灣華語デッキとノートタイプ

### デッキ

```text
MEMORIOPOLIS::TaiwaneseMandarin
```

### ノートタイプ

```text
MEMORIOPOLIS Taiwanese Mandarin Vocabulary
```

### 注意

- `MEMORIOPOLIS`は半角英字。
- `::`は半角コロン2個。
- `TaiwaneseMandarin`の途中に空白を入れない。
- 直接のインポート先は親デッキではなく子デッキにする。

---

## 11．臺灣華語版の16フィールド

```text
1  ID
2  TraditionalChinese
3  Zhuyin
4  Pinyin
5  Japanese
6  PartOfSpeech
7  TaiwanMandarinGrammar
8  ExampleTraditionalChinese
9  ExampleZhuyin
10 ExamplePinyin
11 ExampleJapanese
12 Source
13 CourseTags
14 ExampleBreakdown
15 ExampleExplanation
16 ExamplePronunciationHint
```

### `CourseTags`について

作成したCSVの13列目は教材上`Tags`だが、Ankiの通常フィールド名として`Tags`を使わず、ノートタイプ側では次の名称を採用した。

```text
CourseTags
```

CSVの13列目をAnkiの`CourseTags`へ割り当てた。

Anki標準タグ欄は空のままである。

---

## 12．臺灣華語版の表示設計

### 表面

```text
ID
TraditionalChinese
Zhuyin
Pinyin
単語TTS
```

C0001：

```text
C0001
紀錄
ㄐㄧˋ ㄌㄨˋ
jìlù
```

### 裏面

```text
日本語
品詞
臺灣華語の用法
例文
例文TTS
例文・注音符號
例文・拼音
例文・日本語訳
文の組み立て
なぜこの意味・語順になる？
なぜこの音に聞こえる？
Source
```

### 色

```text
繁體字：大きな主表示
注音符號：紫
拼音：青
臺灣華語の用法：薄紫
例文：薄青
文の組み立て・意味の橋：薄緑
音の橋：薄黄
Source：小さな灰色
```

ダークモード用CSSも設定済み。

---

## 13．臺灣華語TTSの確定構成

音声専用フィールドは作らない。

### 単語TTS

```html
<div class="tts-audio">
  {{tts zh_TW:TraditionalChinese}}
</div>
```

### 例文TTS

```html
<div class="tts-audio">
  {{tts zh_TW:ExampleTraditionalChinese}}
</div>
```

### 役割分担

```text
TraditionalChinese
→ 繁體字の通常表記
→ TTSの入力

Zhuyin
→ 臺灣固有の音韻座標

Pinyin
→ ラテン文字による横断学習・入力補助

ExamplePronunciationHint
→ 日本人の耳向けの一時的な音の橋
```

Windowsの臺灣華語音声環境は導入に苦労したが、PC版Ankiで単語・例文ともに正常に再生された。

---

## 14．CSVインポート結果

### 使用ファイル

```text
zh_tw_core10_anki_draft01.csv
```

### インポート設定

```text
区切り：コンマ
フィールド内でHTMLを使う：オフ
ノートタイプ：MEMORIOPOLIS Taiwanese Mandarin Vocabulary
デッキ：MEMORIOPOLIS::TaiwaneseMandarin
既存のノート：更新
重複チェックの範囲：ノートタイプ
Anki標準タグ：なし
```

### フィールド割り当て

```text
1  → ID
2  → TraditionalChinese
3  → Zhuyin
4  → Pinyin
5  → Japanese
6  → PartOfSpeech
7  → TaiwanMandarinGrammar
8  → ExampleTraditionalChinese
9  → ExampleZhuyin
10 → ExamplePinyin
11 → ExampleJapanese
12 → Source
13 → CourseTags
14 → ExampleBreakdown
15 → ExampleExplanation
16 → ExamplePronunciationHint
```

### 結果

```text
新規追加：10件
更新：0件
```

10レコードのインポートに成功した。

---

## 15．C0001の確認結果

### 表面

```text
C0001
紀錄
ㄐㄧˋ ㄌㄨˋ
jìlù
```

- 繁體字：正常。
- 注音符號：正常。
- 拼音・声調記号：正常。
- 単語TTSボタン：表示。
- 単語音声：正常に再生。

### 日本語・品詞

```text
日本語：記録
品詞：名詞
```

### 臺灣華語の用法

```text
「紀錄」は名詞として「記録」を表す。
臺灣では「紀錄」の表記を用いる。
例文では量詞を伴う「一條連續的紀錄」の中心語。
```

### 例文

```text
明明知道它是正式的，卻無法把它的正確性說明成一條連續的紀錄。
```

- 繁體字：正常。
- 折り返し：正常。
- 例文TTSボタン：表示。
- 例文音声：正常に再生。

### 文の組み立て

```text
明明知道＝分かっているのに
卻無法＝しかし〜できない
把它的正確性＝その正しさを
說明成＝〜として説明する
一條連續的紀錄＝一続きの記録
```

### 意味・語順の橋

```text
「明明…卻…」は、予想される結果との食い違いを表す。
「把」は対象を動詞の前へ出す。
「成」は結果としてどの形に扱うかを示す。
```

### 音の橋

```text
紀錄 jìlù
→ 「ジールー」に近く聞こえることがある
→ 二音節とも第四声
→ 高い位置から短く落とす
→ 最終的にはㄐㄧˋ ㄌㄨˋへ戻る
```

---

## 16．C0010の確認結果

### 対象語

```text
角色
ㄐㄩㄝˊ ㄙㄜˋ
juésè
役割／ロール
```

### 意味・語順の橋

```text
「…的是…」は、確認した内容を取り出して焦点化する。
「角色存在」は「役割が存在する」という節。
存在だけを確認し、現在も同じ鍵を管理しているとは述べない。
```

### 音の橋

```text
角色 juésè
→ 「ジュエスー」に近く聞こえることがある
→ juéは第二声
→ sèは第四声
→ 最後のsèは日本語の「セ」より中央寄りの母音になりやすい
```

### Source

```text
Source: section12_zh-TW
```

表示崩れ、HTMLタグの露出、文字切れは確認されなかった。

---

## 17．現在の臺灣華語版判定

```text
デッキ作成                       OK
ノートタイプ作成                 OK
16フィールド作成                 OK
表面テンプレート                 OK
裏面テンプレート                 OK
CSS                              OK
ダークモードCSS                  OK
CSV 10件インポート               OK
繁體字                           OK
注音符號                         OK
拼音・声調                       OK
臺灣華語の用法                   OK
例文                             OK
例文注音                         要AnkiDroid確認
例文拼音                         要AnkiDroid確認
文の組み立て                     OK
意味・語順の橋                   OK
音の橋                           OK
単語TTS                          PC版でOK
例文TTS                          PC版でOK
AnkiWeb同期                      次
AnkiDroid表示・音声確認          次
Core10 FIX                       未実施
```

現段階では`draft01`を維持する。

---

## 18．次に行う作業

### PC版Anki

1. カードテンプレートを保存する。
2. プレビューを閉じる。
3. ブラウザを閉じる。
4. PC版Ankiで同期する。

### AnkiDroid

1. AnkiDroidを開く。
2. 同期する。
3. `MEMORIOPOLIS::TaiwaneseMandarin`を確認する。
4. カードブラウザからC0001、C0006、C0010を確認する。
5. 表面の繁體字、注音符號、拼音を確認する。
6. 単語TTSを再生する。
7. 裏面の例文を確認する。
8. 例文TTSを再生する。
9. 意味・語順の橋、音の橋を確認する。
10. ダークモードで文字と背景が読めるか確認する。

### 親デッキ

AnkiDroid確認後、親デッキ`MEMORIOPOLIS`から学習し、次の三言語が混合されるか確認する。

```text
한국어
Русский
臺灣華語
```

---

## 19．臺灣華語Core10をFIXする条件

- [x] 10件をインポートした。
- [x] PC版で繁體字を確認した。
- [x] PC版で注音符號を確認した。
- [x] PC版で拼音を確認した。
- [x] PC版で単語TTSを確認した。
- [x] PC版で例文TTSを確認した。
- [x] C0001の意味・語順の橋を確認した。
- [x] C0001の音の橋を確認した。
- [x] C0010の意味・語順の橋を確認した。
- [x] C0010の音の橋を確認した。
- [ ] AnkiWebへ同期した。
- [ ] AnkiDroidへ同期した。
- [ ] AnkiDroidでC0001を確認した。
- [ ] AnkiDroidでC0006を確認した。
- [ ] AnkiDroidでC0010を確認した。
- [ ] AnkiDroidで単語TTSを確認した。
- [ ] AnkiDroidで例文TTSを確認した。
- [ ] C0001～C0010を数回反復した。
- [ ] 語彙、例文、注音、拼音、文法、音の橋を再検討した。
- [ ] 必要な修正をマスターCSVへ戻した。
- [ ] `draft01`を外した正本CSVを作成した。
- [ ] Gitコミット・pushした。

---

## 20．次の英語版

臺灣華語版の後、英語版Anki Core10を作る。

その前に、必要に応じて端末へ英語音声環境を導入する。

英語版の予定要素：

```text
ID
English
IPAまたはPronunciation
Japanese
PartOfSpeech
EnglishGrammar
ExampleEnglish
ExamplePronunciation
ExampleJapanese
Source
CourseTags
ExampleBreakdown
ExampleExplanation
ExamplePronunciationHint
```

英語版では、第十二節の`I.`と一人称`I`が同じ文字へ重なる点が重要な観測事項となる。

具体的なフィールド数とIPAの扱いは、英語版作成時に決定する。

---

## 21．その後のJANUS-13

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

外国語12言語は対等な観測面。

### 言語候補

```text
日本語
English
臺灣繁體中文
한국어
Русский
Filipino
Bahasa Indonesia
Tiếng Việt
Français
Deutsch
Italiano
Español
Português
```

日本語の内部：

```text
現代日本語
歴史的仮名遣い
```

### UI原則

- 直近3言語を表示する。
- 「観測点を開く」を用意する。
- 国旗を主要表示にしない。
- 各言語の自称、象徴文字、Unicode符号位置を使う。
- 「都市に任せる」で観測点を選ぶ。
- 素数13を利用した重複のない巡回を検討する。
- 十三面体だけでなく通常の言語一覧も用意する。
- 各面は対等だが、開拓深度は同じでなくてよい。

```text
面は対等。
深度は可変。
```

### 次のAnki面候補

英語版の後、最初に歴史的仮名遣いのAnki版を検討する。

これにより、JANUS-13の日本語面が次の二重構造になる。

```text
現代日本語 ⇄ 歴史的仮名遣い
```

---

## 22．Git管理

臺灣華語版の成果物は、AnkiDroid確認と修正後にGitへ反映する。

対象候補：

```text
zh_tw_core10_master.csv
zh_tw_core10_anki.csv
README_zh_tw_core10.md
ZH_TW_NOTE_TYPE.md
```

draft段階では次を維持する。

```text
zh_tw_core10_master_draft01.csv
zh_tw_core10_anki_draft01.csv
README_zh_tw_core10_draft01.md
ZH_TW_NOTE_TYPE_DRAFT01.md
```

カードテンプレートの再現性を高めるため、将来は次の構造を検討する。

```text
anki/taiwanese-mandarin/
├─ front.html
├─ back.html
├─ style.css
└─ README.md
```

TTSタグもリポジトリへ記録する。

```html
{{tts zh_TW:TraditionalChinese}}
{{tts zh_TW:ExampleTraditionalChinese}}
```

---

## 23．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月14日の最新状態として、『記憶都市（メモリオポリス）』多言語読解コースの制作を再開します。

韓国語版Anki Core10はFIX・コミット済みです。ロシア語版Anki Core10 draft01はPC版Anki、AnkiWeb、AnkiDroidで単語TTSと例文TTSが正常に動作しています。ロシア語Novel section12_ru_draft01.mdの推敲は、Core10を数回反復してから行います。

臺灣華語版Anki Core10 draft01を作成しました。PC版AnkiにはMEMORIOPOLIS::TaiwaneseMandarinデッキとMEMORIOPOLIS Taiwanese Mandarin Vocabularyノートタイプを作成済みです。

臺灣華語版は16フィールドです。13番目の通常フィールド名はCourseTagsです。zh_tw_core10_anki_draft01.csvをインポートし、新規追加10件、更新0件で成功しました。

表面はID、TraditionalChinese、Zhuyin、Pinyin、単語TTSです。裏面は日本語、品詞、臺灣華語の用法、例文、例文TTS、例文注音、例文拼音、例文日本語訳、文の組み立て、意味・語順の橋、音の橋、Sourceです。

単語TTSは{{tts zh_TW:TraditionalChinese}}、例文TTSは{{tts zh_TW:ExampleTraditionalChinese}}です。Windowsの臺灣華語音声環境の導入には苦労しましたが、PC版Ankiで単語と例文の音声が正常に再生されています。

C0001紀錄では、繁體字、ㄐㄧˋ ㄌㄨˋ、jìlù、日本語、品詞、用法、例文、意味・語順の橋、音の橋を確認済みです。C0010角色では、意味・語順の橋、音の橋、Sourceを確認済みです。表示崩れやHTMLタグ露出はありません。

次はカードテンプレートを保存し、PC版Ankiを同期してください。その後AnkiDroidでC0001、C0006、C0010の表示、単語TTS、例文TTS、注音、拼音、意味の橋、音の橋、ダークモードを確認してください。

AnkiDroid確認後、親デッキMEMORIOPOLISから韓国語、ロシア語、臺灣華語が混合されるか確認します。臺灣華語版を数回反復して必要な修正を正本候補CSVへ戻した後、Core10をFIXします。

その後は英語Anki Core10を作成し、続いてJANUS-13：Unicode Observation Polyhedronに沿って各言語のAnki版を順次構築します。最初の候補は歴史的仮名遣いです。
```

---

## 24．2026年9月14日の店じまい地点

```text
韓国語版Anki Core10                    FIX・コミット済み
ロシア語Anki Core10 draft01            PC・Web・AndroidでTTS正常
ロシア語Novel draft01                  反復後に推敲
臺灣華語デッキ                         作成済み
臺灣華語ノートタイプ                   作成済み
臺灣華語16フィールド                   作成済み
表面テンプレート                       作成済み
裏面テンプレート                       作成済み
CSS・ダークモード                      作成済み
臺灣華語Core10                         10件インポート成功
C0001表示                              確認済み
C0001単語TTS                           PC版で正常
C0001例文TTS                           PC版で正常
C0010意味・語順の橋                    確認済み
C0010音の橋                            確認済み
カードテンプレート保存                 実施してよい状態
PC版Anki同期                           次
AnkiDroid確認                          次
臺灣華語Core10 FIX                     未実施
英語Anki Core10                        臺灣華語の後
JANUS-13                               英語版の後
歴史的仮名遣いAnki                    JANUS-13初期候補
```

本日の到達点は、次の一文に集約できる。

> 臺灣華語Core10は、繁體字、注音符號、拼音、日本語、用法、例文、意味・語順の橋、音の橋、単語TTS、例文TTSを一枚のカードで往復できる状態になった。次はこの観測面をAnkiDroidへ渡し、韓国語・ロシア語とともに親デッキMEMORIOPOLISで交差させる。
