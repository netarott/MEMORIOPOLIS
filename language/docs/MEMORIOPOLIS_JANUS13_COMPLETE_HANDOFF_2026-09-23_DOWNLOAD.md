

---

# 2026年9月23日 完全版更新

## 58．本日の最重要更新

```text
フランス語Windows Basic
→ Installed

フランス語Windows TextToSpeech
→ Installed

フランス語版Novel全文第一稿
→ 完成

フランス語版Anki Core10
→ 18フィールド版完成・導入済み

JANUS-13 Daily Training
→ フランス語新規10枚を収集
→ 既存言語の期限カード32枚を収集
→ 合計42枚の運行状態

次の言語
→ ドイツ語（ドイツ）
```

---

## 59．現在の言語数と観測面

```text
JANUS-13
→ 全13言語
→ 全14観測面
```

### 開通済み

```text
1. 日本語
   ├─ 現代日本語面
   └─ 近代日本語面
2. 韓国語
3. ロシア語
4. 臺灣華語
5. 英語
6. フィリピン語
7. インドネシア語
8. ベトナム語
9. スペイン語（スペイン）
10. ポルトガル語（ブラジル）
11. イタリア語
12. フランス語（フランス）
```

### 残り

```text
13. ドイツ語（ドイツ）
```

フランス語までで、12言語・13観測面が開通済み。
ドイツ語の開通により、JANUS-13の13言語・14観測面がすべて揃う。

---

## 60．フランス語版の完成状況

### 基準

```text
言語：Français de France
Windows：fr-FR
Anki：fr_FR
```

### Windows環境

```text
Language.Basic~~~fr-FR~0.0.1.0
→ Installed

Language.TextToSpeech~~~fr-FR~0.0.1.0
→ Installed

Language.Handwriting~~~fr-FR~0.0.1.0
→ NotPresent、不要

Language.OCR~~~fr-FR~0.0.1.0
→ NotPresent、不要

Language.Speech~~~fr-FR~0.0.1.0
→ NotPresent、Anki TTSには不要
```

### ZIP

```text
MEMORIOPOLIS_French_Core10_draft01_18fields_2026-09-23.zip
```

### 収録ファイル

```text
section12_fr_draft01.md
fr_core10_master_draft01_18fields.csv
fr_core10_anki_draft01_18fields.csv
README_fr_core10_draft01.md
FRENCH_NOTE_TYPE_DRAFT01_18FIELDS.md
FRENCH_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_fr.md
```

### デッキ

```text
MEMORIOPOLIS::French
```

### ノートタイプ

```text
MEMORIOPOLIS French Vocabulary
```

### タグ

```text
memoriopolis::fr::core10
```

### TTS

```html
{{tts fr_FR:French}}
```

```html
{{tts fr_FR:ExampleFrench}}
```

### Core10

```text
C0001  enregistrement   記録
C0002  mémoire          記憶
C0003  ville            都市
C0004  notification     通知
C0005  réponse          返信／応答
C0006  destinataire     宛先／受取人
C0007  signature        署名
C0008  vérification     検証
C0009  autorisation     権限／許可
C0010  rôle             役割／ロール
```

### 重点観測

```text
語末子音の不発音
鼻母音
リエゾン
アンシェヌマン
oi → /wa/
gn → /ɲ/
-tion → /sjɔ̃/
フランス語のr → /ʁ/
冠詞と名詞の性・数
前置詞と冠詞の縮約
関係代名詞
複合過去と半過去
文字上の語境界と音声上のまとまりの差
```

### 品質検査

```text
Novel：451行
Ankiデータ：10行
列数：全行18列
Concept ID：C0001～C0010
CSV：UTF-8 BOM付き
ZIP：7ファイル
破損検査：問題なし
```

---

## 61．フランス語導入後のAnki実機状態

画像で確認した状態：

```text
JANUS-13 Daily Training
新規：10
学習中：0
復習：32
合計：42
```

```text
MEMORIOPOLIS配下
→ 各子デッキの対象カードは0表示
→ 対象カードがDaily Trainingへ一時移動しているため正常
```

フランス語デッキは親デッキ配下に作成済み。

```text
MEMORIOPOLIS::French
```

Daily Trainingの動作：

```text
第1フィルター
→ deck:MEMORIOPOLIS is:due
→ 期限カード32枚

第2フィルター
→ deck:MEMORIOPOLIS is:new
→ フランス語新規10枚
```

フランス語Ankiの音声・表示・例文説明は後で実機確認する。

---

## 62．記憶モデルについての現在の合意

### 保存中心モデルから変換中心モデルへ

```text
従来のイメージ
記憶＝記号を脳内へ保存すること

JANUS-13の作業仮説
記憶＝過去の入力により、未来の知覚・判断・発話・行動が変化すること
```

### 入力から出力への変換

```text
入力
→ 画像
→ 文字
→ 音声
→ 場所
→ Novelの出来事

接続キー
→ Concept ID

出力
→ 意味を言う
→ 対象言語を発音する
→ 語形を書く
→ 例文を再構成する
→ 次の文章を作る
```

### 場所法・ストーリー法との接続

```text
絵巻の固定地点
→ 場所法

Novelの出来事
→ ストーリー法

Anki
→ アクティブリコール

FSRS
→ 分散学習
```

Concept IDは、これらを結ぶ都市の住所コードである。

---

## 63．Concept画像の導入方針

ドイツ語まで完成させてから、C0001～C0010のConcept画像を全観測面へ組み込む。

### 画像の役割

```text
辞書的な画像
→ 単語の意味だけを示す

MEMORIOPOLISのConcept画像
→ 一つの固定場所
→ Novel内の出来事
→ 一つのConceptの働き
```

### 予定する19番目のフィールド

```text
ConceptScene
```

場所を文章で説明するフィールドではなく、絵巻の一景を入れる視覚入力フィールドとして検討する。

### 初期実験

```text
既存カード数
→ 増やさない

18フィールド
→ 19フィールドへ拡張

表面
→ Concept ID
→ ConceptScene
→ 対象言語
→ 発音
→ TTS
```

### 将来の産出カード

```text
表面
→ Concept ID
→ ConceptScene

裏面
→ 対象言語の語形
→ 発音
→ TTS
```

初期段階ではカードを二倍にしない。
全13言語・14観測面のCore10完成後に、一括拡張する。

---

## 64．五年計画

### 周期

```text
14観測面
×
1日1観測面
=
14日で一巡
```

一巡で各言語に10 Conceptを追加する。

```text
約28日
→ 各言語に約20 Concept

1年
→ 計画値240 Concept／言語

4年
→ 960 Concept／言語

5年
→ 1,200 Concept／言語
```

### 全体規模

```text
1,200 Concept
×
14観測面
=
16,800カード相当
```

ただし、16,800個の孤立した記号としてではなく、

```text
1,200の固定住所
×
14の言語・時間面
```

として管理する。

### 目標

> 各言語で1,200 Conceptを認識し、その主要部分について、画像・場所・物語・音・文字・語形を相互変換できる。

「1,000語で8割読める」は頻度語彙の延べ語カバー率に関する参考値であり、あらゆる文章を8割理解できる保証ではない。

JANUS-13では語数だけでなく、次を観測する。

```text
定着率
平均想起時間
未学習文の理解率
音声からの認識率
画像からの産出率
Novelへの還流数
制作ノートの発見数
```

### 段階

```text
1年目：240 Concept
→ 都市の住所体系と基本語

2年目：480 Concept
→ 短文の関係構造

3年目：720 Concept
→ 抽象語・制度語

4年目：960 Concept
→ 約1,000 Conceptの都市骨格

5年目：1,200 Concept
→ 実用都市と創作循環
```

---

## 65．次の言語：ドイツ語

### 位置づけ

```text
第13言語
第14観測面
JANUS-13 Core10の最終言語
```

### 基準変種

```text
ドイツの標準ドイツ語
Standarddeutsch in Deutschland
```

### ロケール

```text
Windows：de-DE
Anki：de_DE
```

### 予定デッキ

```text
MEMORIOPOLIS::German
```

### 予定ノートタイプ

```text
MEMORIOPOLIS German Vocabulary
```

### 予定タグ

```text
memoriopolis::de::core10
```

### 予定TTS

```html
{{tts de_DE:German}}
```

```html
{{tts de_DE:ExampleGerman}}
```

Windowsではドイツ語（ドイツ）のTTS音声が提供されている。実際のCapability状態は必ず実機で確認する。

---

## 66．ドイツ語Windows環境の確認

管理者PowerShell、または管理者として起動したVS CodeのPowerShellターミナルで実行する。

### まず状態を確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~de-DE~'
} |
Select-Object Name, State
```

主に確認する項目：

```text
Language.Basic~~~de-DE~0.0.1.0
Language.TextToSpeech~~~de-DE~0.0.1.0
```

### `Installed`の場合

```text
追加ダウンロード不要
```

### `NotPresent`の場合

Basicを先に導入する。

```powershell
Add-WindowsCapability -Online -Name "Language.Basic~~~de-DE~0.0.1.0"
```

プロンプトが戻るまで待つ。

その後、TextToSpeechを導入する。

```powershell
Add-WindowsCapability -Online -Name "Language.TextToSpeech~~~de-DE~0.0.1.0"
```

BasicとTextToSpeechを同時に実行しない。

### 最終確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~de-DE~'
} |
Select-Object Name, State
```

期待値：

```text
Language.Basic~~~de-DE~0.0.1.0          Installed
Language.TextToSpeech~~~de-DE~0.0.1.0   Installed
```

### 今回不要な機能

```text
Language.Handwriting
Language.OCR
Language.Speech
```

Ankiの文字表示とTTSだけなら必須ではない。

### 安全チェック

```text
安定したWi-Fiへ接続
PCを電源へ接続
OneDrive同期を一時停止
VS Code全体を管理者として起動
Basicを先に実行
プロンプト復帰を確認
TextToSpeechを実行
処理中にCtrl+Cを押さない
同じコマンドを再実行しない
最後にInstalledを確認
OneDrive同期を再開
管理者VS Codeを終了
通常権限へ戻す
```

---

## 67．ドイツ語で重点的に観測する項目

```text
名詞の大文字表記
三つの文法性
定冠詞・不定冠詞
格変化
複合語
分離動詞
語順
動詞の第二位
従属節の動詞後置
語末子音の無声化
chの音
rの地域差
長母音と短母音
ウムラウト
ß
```

### 文字アンカー

ドイツ語はラテン文字を使いながら、複合語によってConceptの構成要素が見えやすい。

```text
語幹
＋
語幹
＋
活用語尾
```

を横方向に観測する。

### 英語との縁

英語とドイツ語はゲルマン語系の共通層を持つため、基本語彙・語順・音の対応が観測できる。

ただし、似た綴りだけで意味を断定しない。

### フランス語との対照

```text
フランス語
→ 語末子音が消える場合が多い
→ 音声上の連結が語境界を越える

ドイツ語
→ 子音配置が比較的明示的
→ 語末無声化で文字と音がずれる
→ 複合語内部にConcept境界が現れる
```

子音標識仮説を、フランス語とドイツ語の対照で再検査する。

---

## 68．ドイツ語版の予定制作物

```text
section12_de_draft01.md
de_core10_master_draft01_18fields.csv
de_core10_anki_draft01_18fields.csv
README_de_core10_draft01.md
GERMAN_NOTE_TYPE_DRAFT01_18FIELDS.md
GERMAN_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_de.md
```

予定ZIP：

```text
MEMORIOPOLIS_German_Core10_draft01_18fields_2026-09-24.zip
```

予定手順：

```text
1. de-DE Capability確認
2. 必要ならBasic導入
3. 必要ならTextToSpeech導入
4. Installed確認
5. 日本語正本確認
6. ドイツ語版Novel全文第一稿作成
7. C0001～C0010の対応語選定
8. 18フィールド版Core10作成
9. テンプレートとCSS作成
10. CSV・ZIP検査
11. MEMORIOPOLIS::Germanへ導入
12. de_DE TTS確認
13. JANUS-13 Daily Training再構築
14. 期限カードと新規10枚を学習
15. JANUS-13全13言語・14観測面の開通確認
16. Concept画像導入工程へ移行
```

---

## 69．ドイツ語後の次工程

ドイツ語の開通後、Core10の全13言語・14観測面が完成する。

次工程：

```text
1. C0001～C0010の絵巻10景を確定
2. Concept Atlasを作成
3. ConceptScene画像を10枚作成
4. 全ノートタイプへConceptSceneフィールドを追加
5. 全観測面へ共通画像を組み込む
6. 既存カード数を増やさず表面へ画像を表示
7. Daily Trainingで画像付き学習を試験
8. 視覚入力から語形・音への変換を観測
9. 必要なら産出カードを追加
```

Concept画像の導入では、画像を答えの装飾にせず、固定地点から対象言語を起動する入力信号として使う。

---

## 70．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月23日の最新状態として、MEMORIOPOLIS / JANUS-13を再開します。

フランス語版Novel全文第一稿と18フィールド版Core10は完成・導入済みです。Windowsのfr-FR BasicとTextToSpeechもInstalledです。JANUS-13 Daily Trainingにはフランス語の新規10枚と既存言語の期限カード32枚、合計42枚が入線しています。フランス語の音声・表示・例文説明は実機で最終確認してください。

次の制作言語は第13言語、第14観測面のドイツ語です。基準はドイツの標準ドイツ語、Windowsロケールはde-DE、Ankiロケールはde_DEです。

まず、管理者PowerShellでGet-WindowsCapability -Onlineを実行し、Language.Basic~~~de-DE~0.0.1.0とLanguage.TextToSpeech~~~de-DE~0.0.1.0の状態を確認してください。NotPresentならBasicを先に、TextToSpeechを後に直列で導入します。Installedなら再導入しません。

その後、日本語正本section12_ja.mdを基に、第四章第十二節のドイツ語版Novel全文第一稿と18フィールド版Anki Core10を作成してください。デッキはMEMORIOPOLIS::German、ノートタイプはMEMORIOPOLIS German Vocabulary、タグはmemoriopolis::de::core10です。

単語TTSは{{tts de_DE:German}}、例文TTSは{{tts de_DE:ExampleGerman}}を使います。AnkiDroidで音声エラーが出た場合は{{tts-voices:}}で端末が返したロケールと音声識別子をそのまま採用してください。

ドイツ語では、名詞の大文字表記、三つの文法性、格変化、複合語、分離動詞、動詞第二位、従属節の動詞後置、語末子音の無声化、ch、r、長短母音、ウムラウト、ßを重点的に観測してください。

Concept IDは場所法とストーリー法の両方に接続し、強い手応えが確認されています。固定地点、Novelの場面、Concept、対象言語の語形、音声の順で想起します。

ドイツ語の完成後は、C0001～C0010のConcept画像10枚を制作し、ConceptSceneフィールドとして全13言語・14観測面のカード表面へ組み込む工程へ進みます。

JANUS-13 Daily Trainingの第1フィルターはdeck:MEMORIOPOLIS is:due、上限50、忘れている可能性が高い順。第2フィルターはdeck:MEMORIOPOLIS is:new、上限10、追加順です。

FSRSは有効、目標保持率90%、一括再スケジュールはオフです。新規上限10、復習上限200、学習ステップ1m 10m、再学習10mです。
```

---

## 71．2026年9月23日の店じまい地点

```text
JANUS-13                              13言語・14観測面
開通済み言語                          12言語
開通済み観測面                        13面
フランス語                            第12言語・第13観測面
fr-FR Basic                           Installed
fr-FR TextToSpeech                    Installed
フランス語Novel                       完成
フランス語Core10                      完成・導入済み
フランス語新規カード                  10枚
本日期限カード                        32枚
Daily Training合計                    42枚
次言語                                ドイツ語
ドイツ語                              第13言語・第14観測面
ドイツ語Windowsロケール               de-DE
ドイツ語Ankiロケール                  de_DE
ドイツ語Windows環境確認               次の作業
Concept画像                           ドイツ語完成後に導入
五年計画                              1,200 Concept／言語
```

本日の到達点：

> フランス語までの12言語・13観測面が開通し、JANUS-13 Daily Trainingへ新規10枚と期限32枚が正しく集約された。次は最終言語のドイツ語を開通し、全13言語・14観測面のCore10を完成させる。その後、Concept画像を全観測面へ組み込み、視覚入力から言語出力への変換回路を実装する。
