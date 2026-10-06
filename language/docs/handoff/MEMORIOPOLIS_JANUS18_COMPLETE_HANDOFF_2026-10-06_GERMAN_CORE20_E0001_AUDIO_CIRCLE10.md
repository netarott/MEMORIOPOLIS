# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

**作業日:** 2026-10-06  
**対象:** ドイツ語Core10、19フィールド化、音優先カードUI、E0001ドイツ語canonical、German Core20、E0001ドイツ語音源、YouTube Music Audio Circle  
**ステータス:** 本日の作業完了。自宅でドイツ語音源の最終試聴を行う。

---

## 0. 本日の到達点

本日は、LIVING-13の次言語としてドイツ語を進め、次の一連の流れを完了した。

```text
German Core10既存データ確認
  ↓
ConceptSceneを19番目のフィールドとして追加
  ↓
ドイツ語音優先型カードUIを作成
  ↓
E0001ドイツ語版を作成
  ↓
E0001_de.mdをcanonical確定
  ↓
German Core20を19フィールドで作成
  ↓
AnkiへCore20を登録
  ↓
E0001_de.mdからE0001_de.mp3を生成
  ↓
YouTube Musicへアップロード
  ↓
既存Audio Circleへ10番目のトラックとして追加
```

本日の最終状態：

```text
MEMORIOPOLIS E0001｜JANUS-18 Audio Circle
公開範囲：非公開
トラック数：10
合計時間：1時間1分
ドイツ語音源：E0001_de.mp3
ドイツ語音源の長さ：5分52秒
```

画面上で、`E0001_de.mp3`がプレイリストの先頭に表示され、10トラックへ増えたことを確認した。

---

## 1. 前回から継続する音声学習方針

### 1.1 役割分担

```text
AnkiDroid
＝ 単語と例文の短い音からConceptを能動的に想起する

YouTube Music
＝ 同一Essayを多言語で大量反復し、各言語の音韻、リズム、語境界、談話展開に馴染む

GitHubアプリ
＝ canonical Markdownを開き、音声を聞きながら文章全体の地形を俯瞰する
```

### 1.2 新しく開いた回廊

スマートフォンで次の二つを同時に使う。

```text
GitHubアプリで対象言語のE0001_*.mdを開く
  ＋
YouTube Musicで同じ言語のE0001_*.mp3を再生する
```

この組み合わせにより、音声の現在位置だけでなく、前後の段落と文章全体の流れを見渡せる。

### 1.3 文法と談話航法

従来の下から積み上げる学習は維持する。

```text
音素
→ 語
→ 語形
→ 文法
→ 文
```

これに加えて、文章全体を上から読む。

```text
場面設定
→ 予想外の出来事
→ 探索
→ 記憶との接続
→ 抽象化
→ 視点転換
→ 中心命題
→ 結末
```

チェス熟達者が実戦的な局面をチャンクやパターンとして認識するように、外国語の文章でも、すべてを逐語解析するだけでなく、談話の局面から次の展開候補を立て、実際の語・音・構文で検証する。

MEMORIOPOLIS内での暫定名称：

```text
談話航法
文章回廊の先読み
```

---

## 2. YouTube Musicで確認したこと

### 2.1 良かった点

- 日本語以外の音声は、全体として自然な印象だった。
- 同じE0001を複数言語で聞く環境が実用段階へ入った。
- canonical Markdownと音声を同時に使う回廊が成立した。

### 2.2 気になった点

シャッフル再生時、最初の1曲が固定される挙動があった。

前回の9言語では、臺灣華語が毎回最初に再生された。

```text
希望する挙動
＝ 第1曲目を含めて完全にシャッフル

観測した挙動
＝ 最初の1曲は固定され、その次からシャッフルされる可能性
```

現時点ではYouTube Music側のキュー保持または仕様の可能性がある。次回、自宅のスマートフォンで再度確認する。

実用上の暫定回避策：

```text
毎回異なる曲を手動で最初に選ぶ
  ↓
その後シャッフルを有効化する
```

あるいは、固定された最初の言語をAudio Circleの玄関とみなし、その後の順序をランダムとして運用する。

---

## 3. German Core10の19フィールド化

### 3.1 元データ

```text
de_core10_master.csv
＝ ヘッダー付き、18フィールド

de_core10_anki.csv
＝ ヘッダーなし、18フィールド
```

### 3.2 追加フィールド

末尾の19番目に次を追加した。

```text
ConceptScene
```

フィールド順：

```text
01 ID
02 German
03 Pronunciation
04 Japanese
05 PartOfSpeech
06 UsageNote
07 ExampleGerman
08 ExampleJapanese
09 Root
10 Affixes
11 PerceptualSegmentation
12 MorphologicalBreakdown
13 ExampleBreakdown
14 ExampleExplanation
15 MeaningBridge
16 SoundBridge
17 Source
18 CourseTags
19 ConceptScene
```

### 3.3 作成ファイル

```text
de_core10_master_19fields.csv
de_core10_anki_19fields.csv
```

### 3.4 Core10 ConceptScene

```text
C0001  memoriopolis_c0001_record.webp
C0002  memoriopolis_c0002_memory.webp
C0003  memoriopolis_c0003_city.webp
C0004  memoriopolis_c0004_notification.webp
C0005  memoriopolis_c0005_reply.webp
C0006  memoriopolis_c0006_recipient.webp
C0007  memoriopolis_c0007_signature.webp
C0008  memoriopolis_c0008_verification.webp
C0009  memoriopolis_c0009_authorization.webp
C0010  memoriopolis_c0010_role.webp
```

ユーザー側でAnkiのCore10へ`ConceptScene`フィールドを追加し、図を貼り込み済み。

---

## 4. ドイツ語ノートタイプ

### 4.1 完全版ファイル

```text
GERMAN_CARD_UI_19FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-10-06.md
```

### 4.2 ノートタイプ名

```text
MEMORIOPOLIS German Vocabulary
```

### 4.3 学習経路

```text
単語の音
  ↓
Concept候補を心の中で探す
  ↓
ConceptScene
  ↓
ドイツ語綴り
  ↓
発音・音の切れ目
  ↓
日本語Concept
  ↓
例文の音
  ↓
例文本文と日本語訳
  ↓
語構造・例文解説・言語間ブリッジ
```

### 4.4 TTS

```html
{{tts de_DE:German}}
```

```html
{{tts de_DE:ExampleGerman}}
```

### 4.5 デザイン

```text
基調色：深緑、黒、金
上部アクセント：黒・金・赤の細いライン
対応：Anki Desktop / AnkiDroid
対応：ライトモード / ダークモード
```

### 4.6 裏面の3段パネル

```text
1. WORTSTRUKTUR
   語の構造

2. SATZERKLÄRUNG
   例文解説

3. SPRACHBRÜCKE
   言語間ブリッジ
```

### 4.7 ドイツ語での観測点

```text
複合語
分離動詞
定形動詞の位置
格
長短母音
ウムラウト
ich-Laut / ach-Laut
語末子音の無声化
```

---

## 5. E0001ドイツ語版

### 5.1 ファイル

```text
E0001_de.md
```

### 5.2 正式状態

```yaml
essay_id: E0001
language: de
status: canonical
canonical_source: E0001_ja.md
core_range: C0011-C0020
```

E0001ドイツ語版はdraftではない。2026-10-06にcanonicalとして確定した。

### 5.3 タイトル

```text
Vom „romaru“ zu den Roma
```

### 5.4 中心命題

```text
Menschen verlieren nicht den Boden unter den Füßen.
Sie wechseln lediglich den Boden, mit dem sie verbunden sind.
```

意味：

```text
人は、地面を失うのではない。
接続する地面を変える。
```

### 5.5 結末

```text
Die Bedeutung des Wortes fand ich nicht.
Trotzdem hatte dieses Wort einen Weg geöffnet.
```

意味：

```text
言葉の意味は分からなかった。
それでも、その言葉は一つの経路を開いた。
```

---

## 6. German Core20

### 6.1 作成完了

ユーザー側でGerman Core20のAnki登録まで完了した。

### 6.2 ファイル

```text
de_core20_master_19fields.csv
de_core20_anki_19fields.csv
README_DE_CORE20_19FIELDS.md
MEMORIOPOLIS_German_E0001_Core20_19fields_2026-10-06.zip
```

完全パッケージの収録内容：

```text
E0001_de.md
de_core20_master_19fields.csv
de_core20_anki_19fields.csv
README_DE_CORE20_19FIELDS.md
```

### 6.3 Core20見出し語

```text
C0011  existieren       ある／存在する
C0012  machen           する／作る
C0013  haben            持つ
C0014  senden           送る
C0015  empfangen        受け取る
C0016  hören            聞く／聞こえる
C0017  suchen           調べる／探す
C0018  wechseln         移る／変える
C0019  sich verbinden   結びつく／接続する
C0020  gebunden sein    縛られる／結び付けられている
```

### 6.4 共通設定

```text
Source:
E0001_de.md

CourseTags:
memoriopolis::de::core20

TTS locale:
de_DE
```

### 6.5 Concept境界

#### C0016

```text
hören
＝ 音や言葉が耳に入る

zuhören
＝ 意識して人の話を聞く
```

#### C0017

```text
suchen
＝ 意味や答えを探す過程

finden
＝ 探索の結果として見つける

nachschlagen
＝ 辞書や資料で個別項目を引く

überprüfen
＝ 正しさを確認する
```

#### C0018

```text
wechseln
＝ 場所、状態、対象、接続先を別のものへ変える

sich bewegen
＝ 身体や物体そのものが移動する
```

#### C0019 / C0020

```text
sich verbinden
＝ 新しく接続を作る、関係へ入る

gebunden sein
＝ すでに接続・依存・制約の中にある
```

### 6.6 Core20 ConceptScene

```text
C0011  memoriopolis_c0011_exist.webp
C0012  memoriopolis_c0012_do.webp
C0013  memoriopolis_c0013_have.webp
C0014  memoriopolis_c0014_send.webp
C0015  memoriopolis_c0015_receive.webp
C0016  memoriopolis_c0016_hear.webp
C0017  memoriopolis_c0017_search.webp
C0018  memoriopolis_c0018_move.webp
C0019  memoriopolis_c0019_connect.webp
C0020  memoriopolis_c0020_bound.webp
```

---

## 7. E0001ドイツ語音源

### 7.1 専用スクリプト

```text
memoriopolis_e0001_audio_de.py
```

### 7.2 音声設定

```text
engine：edge-tts
locale：de-DE
voice：de-DE-KatjaNeural
rate：-5%
```

### 7.3 実行コマンド

E0001フォルダーで実行する。

```powershell
py .\memoriopolis_e0001_audio_de.py
```

上書き再生成：

```powershell
py .\memoriopolis_e0001_audio_de.py --overwrite
```

### 7.4 生成結果

正常終了を確認した。

```text
[OK] E0001_de.md -> E0001_de.mp3
locale=de-DE voice=de-DE-KatjaNeural rate=-5%
```

生成ファイル：

```text
audio_E0001_all/E0001_de.mp3
audio_E0001_all/E0001_de.narration.txt
audio_E0001_all/E0001_de.srt
audio_E0001_all/E0001_de.audio.json
```

### 7.5 読み上げ除外

スクリプトは以下を読み上げない。

```text
冒頭メタデータ
Referenz / Quelle行
URL
Produktionsnotizen以降
Markdown記号
```

### 7.6 音源の正本関係

```text
E0001_de.md
＝ canonical文章正本

E0001_de.mp3
＝ canonical本文から生成した派生音声

E0001_de.audio.json
＝ Voice ID、速度、生成日時などの条件記録
```

---

## 8. YouTube Musicへのドイツ語追加

### 8.1 アップロード済み

```text
E0001_de.mp3
```

### 8.2 保存先プレイリスト

```text
MEMORIOPOLIS E0001｜JANUS-18 Audio Circle
```

### 8.3 現在のプレイリスト状態

画面上で次を確認した。

```text
公開範囲：非公開
トラック数：10
合計時間：1時間1分
```

ドイツ語：

```text
E0001_de.mp3
5分52秒
```

画面に見えていた他の音源例：

```text
E0001_en.mp3   4分23秒
E0001_fil.mp3  8分31秒
E0001_fr.mp3   5分12秒
E0001_id.mp3   6分47秒
E0001_ja.mp3   4分59秒
```

### 8.4 自宅で行う確認

```text
1. スマートフォンでE0001_de.mp3が表示される
2. 全文を再生できる
3. バックグラウンド再生できる
4. Bluetoothイヤホンで聞ける
5. Katja -5%が自然か
6. romaru、Roma、Yurakucho-Linieの読み方
7. Core20語が長文中で聞こえるか
8. 中心命題の間と抑揚
9. 結末に余韻があるか
10. シャッフル時の第1曲固定がどうなるか
```

速度調整が必要な場合：

```text
候補：0%、-3%、-5%、-8%
```

繰り返し聞いて疲れにくい自然さを基準に決める。

---

## 9. 本日の確定事項

```text
ドイツ語Core10は19フィールド化済み

Core10のConceptScene貼り込み済み

ドイツ語ノートタイプの表・裏・CSS作成済み

E0001_de.mdはcanonical

German Core20作成・Anki登録済み

German Core20は19フィールド

German Core20のSourceはE0001_de.md

E0001_de.mp3生成済み

ドイツ語音声はKatja Neural、速度-5%

E0001_de.mp3をYouTube Musicへアップロード済み

Audio Circleは10トラック、1時間1分

1 Markdown = 1 MP3を維持
```

---

## 10. 次回の主作業

### 10.1 最初に行うこと

自宅でドイツ語音源を確認する。

```text
合格
→ Katja -5%を暫定標準として維持

不合格
→ Voiceまたは速度を比較し、--overwriteで再生成
```

### 10.2 AnkiDroid実機確認

```text
German Core10 / Core20
単語TTS
例文TTS
ConceptScene
表面から裏面への自動スクロール
3段パネル
ダークモード
```

### 10.3 次のLIVING-13言語

既定順は次のとおり。

```text
Italian
  ↓
Spanish es-ES
  ↓
Portuguese pt-BR
```

ただし、ドイツ語の実機確認と音源確認を完了してからイタリア語へ進む。

### 10.4 イタリア語の制作順

```text
Italian Core10の実フィールド確認
  ↓
ConceptSceneを19番目へ追加
  ↓
音優先型カードUI
  ↓
it_IT TTS確認
  ↓
E0001イタリア語版
  ↓
canonical化
  ↓
Italian Core20
  ↓
E0001_it.mp3
  ↓
Audio Circleへ追加
```

---

## 11. ファイル一覧

### ドイツ語Essay

```text
E0001_de.md
```

### Core10

```text
de_core10_master_19fields.csv
de_core10_anki_19fields.csv
```

### Core20

```text
de_core20_master_19fields.csv
de_core20_anki_19fields.csv
README_DE_CORE20_19FIELDS.md
MEMORIOPOLIS_German_E0001_Core20_19fields_2026-10-06.zip
```

### カードUI

```text
GERMAN_CARD_UI_19FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-10-06.md
```

### 音声生成

```text
memoriopolis_e0001_audio_de.py
```

### 音声成果物

```text
audio_E0001_all/E0001_de.mp3
audio_E0001_all/E0001_de.narration.txt
audio_E0001_all/E0001_de.srt
audio_E0001_all/E0001_de.audio.json
```

---

## 12. 次回開始用プロンプト

```text
2026-10-06の完全版引き継ぎ書を基準に再開してください。

まず、自宅のスマートフォンでYouTube Musicの
「MEMORIOPOLIS E0001｜JANUS-18 Audio Circle」
に追加したE0001_de.mp3を確認します。

確認項目は、Katja Neural -5%の自然さ、全文再生、バックグラウンド再生、固有語の読み、Core20語の聞こえ方、中心命題と結末の抑揚です。

ドイツ語音源が合格なら、German Core10 / Core20のAnkiDroid実機確認を完了し、次のLIVING-13言語であるイタリア語へ進みます。

E0001_de.mdはcanonicalです。
German Core20は完成済みです。
Audio Circleは10トラック、1時間1分です。
1 Markdown = 1 MP3を維持してください。
```

---

## 13. 本日の総括

本日は、ドイツ語について次の循環を一日で閉じた。

```text
Concept
  ↓
Core10
  ↓
ConceptScene
  ↓
音優先カードUI
  ↓
canonical Essay
  ↓
Core20
  ↓
Essay全体のMP3
  ↓
YouTube Musicの多言語反復
```

これにより、ドイツ語は単語カードの集合ではなく、E0001という一つの文章を中心に、音、綴り、文法、談話パターン、ConceptScene、記憶を往復できる体系になった。

ドイツ語音源が加わり、Audio Circleは次の状態になった。

```text
9言語・約55分
  ↓
10言語・1時間1分
```

昨日開いた「音の時間軸」と、本日明確になった「文章回廊の先読み」が、ドイツ語でも接続された。

本日はここで店じまいとする。
