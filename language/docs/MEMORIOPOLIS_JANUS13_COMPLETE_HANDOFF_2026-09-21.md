

---

# 2026年9月21日 完全版更新

## 34．本日の最重要更新

```text
ブラジル・ポルトガル語Windows Basic
→ Installed

ブラジル・ポルトガル語Windows TextToSpeech
→ Installed

ブラジル・ポルトガル語Novel全文第一稿
→ 完成

ブラジル・ポルトガル語Anki Core10
→ 18フィールド版完成・インポート済み

JANUS-13 Daily Training
→ 既存言語の復習29枚と新規10枚の同時収集に成功

フィルターデッキ名
→ MEMORIOPOLIS Daily TrainingからJANUS-13 Daily Trainingへ変更

次の言語
→ イタリア語
```

---

## 35．現在の言語数と観測面

```text
JANUS-13
→ 13言語
→ 14観測面
```

### 13言語

```text
1. 日本語
2. 韓国語
3. ロシア語
4. 臺灣華語
5. 英語
6. フィリピン語
7. インドネシア語
8. ベトナム語
9. スペイン語
10. ポルトガル語
11. イタリア語
12. フランス語
13. ドイツ語
```

### 日本語の数え方

```text
日本語
├─ 近代日本語面
└─ 現代日本語面
```

日本語は一言語として数えるが、学習上は二つの時間面を持つ。

### 現在地

```text
第9言語・第10観測面
→ スペイン語
→ 完成・導入・学習済み

第10言語・第11観測面
→ ブラジル・ポルトガル語
→ 完成・導入済み

第11言語・第12観測面
→ イタリア語
→ 次の制作対象
```

残り：

```text
イタリア語
フランス語
ドイツ語
```

---

## 36．現在のデッキ構成

```text
JANUS-13 Daily Training

MEMORIOPOLIS
├─ English
├─ Filipino
├─ Indonesian
├─ Korean
├─ ModernJapanese
├─ Portuguese
├─ Russian
├─ Spanish
├─ TaiwaneseMandarin
└─ Vietnamese
```

次に追加する予定：

```text
MEMORIOPOLIS::Italian
```

### 名称変更の意味

旧名称：

```text
MEMORIOPOLIS Daily Training
```

新名称：

```text
JANUS-13 Daily Training
```

`J`が`M`より前に並ぶため、デッキ一覧の最上部に表示される。子デッキが増えても、スクロールせずに毎日の学習入口へ到達できる。

名称変更はフィルターデッキの表示名だけなので、検索条件の変更は不要。

---

## 37．JANUS-13 Daily Trainingの確定設定

### 第1フィルター

```text
deck:MEMORIOPOLIS is:due
```

```text
上限：50
順序：忘れている可能性が高い順
```

### 第2フィルター

```text
deck:MEMORIOPOLIS is:new
```

```text
上限：10
順序：追加順
```

### オプション

```text
回答に基づいて復習予定を組み直す
→ オン

2つ目の絞り込み
→ オン

空でも作成・更新
→ オフ
```

### 2026年9月21日の実機確認

再構築前：

```text
MEMORIOPOLIS
→ 新規10
→ 復習29

JANUS-13 Daily Training
→ 0
```

再構築後：

```text
JANUS-13 Daily Training
→ 新規10
→ 学習中0
→ 復習29
→ 合計39
```

内訳：

```text
第1フィルター
→ 既存言語の期限カード29枚

第2フィルター
→ ブラジル・ポルトガル語の新規10枚
```

親デッキと各子デッキが0になったのは、対象カードがフィルターデッキへ一時移動したため。削除ではない。

### 完成した運用

```text
新しい言語を毎日10枚ずつ開通
＋
既存言語はFSRSが指定した日に再入線
＋
最上部のJANUS-13 Daily Trainingだけを開く
```

---

## 38．ブラジル・ポルトガル語版の完成状況

### 基準

```text
言語：ポルトガル語
変種：Português do Brasil
Windows：pt-BR
Anki：pt_BR
```

### Windows環境

```text
Language.Basic~~~pt-BR~0.0.1.0
→ Installed

Language.TextToSpeech~~~pt-BR~0.0.1.0
→ Installed

Language.Handwriting~~~pt-BR~0.0.1.0
→ NotPresent、不要

Language.OCR~~~pt-BR~0.0.1.0
→ NotPresent、不要

Language.Speech~~~pt-BR~0.0.1.0
→ NotPresent、Anki TTSには不要
```

### ZIP

```text
MEMORIOPOLIS_Portuguese_BR_Core10_draft01_18fields_2026-09-21.zip
```

### 収録ファイル

```text
section12_pt_br_draft01.md
pt_br_core10_master_draft01_18fields.csv
pt_br_core10_anki_draft01_18fields.csv
README_pt_br_core10_draft01.md
PORTUGUESE_BR_NOTE_TYPE_DRAFT01_18FIELDS.md
PORTUGUESE_BR_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_pt_br.md
```

### ノートタイプ

```text
MEMORIOPOLIS Portuguese Vocabulary
```

### デッキ

```text
MEMORIOPOLIS::Portuguese
```

### タグ

```text
memoriopolis::pt_br::core10
```

### TTS

```html
{{tts pt_BR:Portuguese}}
```

```html
{{tts pt_BR:ExamplePortuguese}}
```

### Core10

```text
C0001  registro       記録
C0002  memória        記憶
C0003  cidade         都市
C0004  notificação    通知
C0005  resposta       返信／応答
C0006  destinatário   宛先／受取人
C0007  assinatura     署名
C0008  verificação    検証
C0009  permissão      権限／許可
C0010  função         役割／機能
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

### ブラジル版を採用した理由

```text
日本からブラジルへの移民
ブラジルの日系社会
日本への還流
日本国内でのポルトガル語との接触
日伯関係
BRICS
```

ポルトガルとの種子島、南蛮貿易、キリスト教、外来語などの歴史は、制作ノートの歴史層へ保持する。

---

## 39．スペイン語版の確定方針

```text
基準：スペインのスペイン語
Windows：es-ES
Anki：es_ES
```

メキシコや南米の広がりは認識するが、正面はスペインのスペイン語とする。

学習所感：

```text
スペイン語は英語と音が似ている部分があり、比較的すんなり学習を完了できた。
```

類似はMeaningBridgeとして活用するが、発音の英語化を避けるため、スペイン標準のc、z、r、母音、強勢をSoundBridgeで維持する。

---

## 40．FSRSと通常デッキの確定設定

```text
FSRS：オン
目標保持率：90%
パラメータ：既定値
変更時の一括再スケジュール：オフ
最適化：まだ行わない
```

```text
新規カード上限：10
復習上限：200
学習ステップ：1m 10m
再学習ステップ：10m
定着しにくいカード：忘却8回
処理：タグのみ
関連カード分離：3項目オン
音声自動再生：有効
```

回答の基準：

```text
もう一度
→ 思い出せなかった
→ 別言語と取り違えた
→ 音から語を特定できなかった

難しい
→ 自力で正解したが非常に迷った

普通
→ 適度な負荷で正解した

簡単
→ 文字・音・意味が即座につながった
```

---

## 41．Concept IDと場所法の構想

Concept IDは単なるカード番号ではない。

> Concept IDは、物語、絵巻、予告編、Anki、多言語、制作ノート、記憶履歴を結ぶ都市の住所コードである。

### 絵巻

```text
6景
↓
10景へ拡張
```

Core10の各Concept IDと一景ずつ対応させる。

```text
C0001 記録
→ 記録台

C0002 記憶
→ 記憶展示壁

C0003 都市
→ 都市展望台

C0004 通知
→ 通知受付

C0005 返信
→ 返信窓口

C0006 宛先
→ 宛先案内板

C0007 署名
→ 署名検査台

C0008 検証
→ 外部検証室

C0009 権限
→ 権限ゲート

C0010 役割
→ 役割管理室
```

### 学習機能の分担

```text
絵巻10景
→ 場所法

予告編
→ 同じ10地点の時間巡回

Novel
→ ストーリー法

Anki
→ アクティブリコール

FSRS
→ 分散学習
```

### Concept Atlas

```text
docs/
└─ concept-atlas/
   ├─ core10_map.md
   ├─ core20_map.md
   ├─ core30_map.md
   └─ scene_registry.csv
```

Ankiには19番目のフィールドをまだ追加しない。既存の`ID`を住所コードとして利用する。

---

## 42．次の言語：イタリア語

### 位置づけ

```text
第11言語
第12観測面
```

### 基準

```text
言語：Italiano
Windows：it-IT
Anki：it_IT
```

### 予定デッキ

```text
MEMORIOPOLIS::Italian
```

### 予定ノートタイプ

```text
MEMORIOPOLIS Italian Vocabulary
```

### 予定タグ

```text
memoriopolis::it::core10
```

### 予定TTS

```html
{{tts it_IT:Italian}}
```

```html
{{tts it_IT:ExampleItalian}}
```

### Windowsの確認コマンド

管理者PowerShellまたは管理者VS Codeターミナルで実行する。

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~it-IT~'
} |
Select-Object Name, State
```

主な確認対象：

```text
Language.Basic~~~it-IT~0.0.1.0
Language.TextToSpeech~~~it-IT~0.0.1.0
```

### `NotPresent`の場合

Basicを先に導入する。

```powershell
Add-WindowsCapability -Online -Name "Language.Basic~~~it-IT~0.0.1.0"
```

プロンプトが戻った後、TextToSpeechを導入する。

```powershell
Add-WindowsCapability -Online -Name "Language.TextToSpeech~~~it-IT~0.0.1.0"
```

同時実行しない。同じコマンドを重ねない。Ctrl+Cを押さず、処理中は管理者VS Codeを閉じない。

### 最終確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~it-IT~'
} |
Select-Object Name, State
```

期待値：

```text
Language.Basic~~~it-IT~0.0.1.0          Installed
Language.TextToSpeech~~~it-IT~0.0.1.0   Installed
```

Handwriting、OCR、SpeechはAnki読み上げには必須でない。

### 重点観測

```text
明瞭な母音
二重子音
c / ch
sc / sch
c / gの軟音・硬音
gli
gn
語末母音
名詞の性数
冠詞
動詞活用
主語代名詞の省略
前置詞と冠詞の結合
```

スペイン語、ブラジル・ポルトガル語との同源語はMeaningBridgeとして活用する。ただし、綴りが似ていても各言語の音を混同しないようSoundBridgeを重視する。

---

## 43．イタリア語版の予定制作物

```text
section12_it_draft01.md
it_core10_master_draft01_18fields.csv
it_core10_anki_draft01_18fields.csv
README_it_core10_draft01.md
ITALIAN_NOTE_TYPE_DRAFT01_18FIELDS.md
ITALIAN_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_it.md
```

予定ZIP：

```text
MEMORIOPOLIS_Italian_Core10_draft01_18fields_2026-09-22.zip
```

予定手順：

```text
1. it-IT Capabilityを確認
2. 必要ならBasic導入
3. 必要ならTextToSpeech導入
4. Installedを確認
5. 日本語正本を確認
6. イタリア語版Novel全文第一稿を作成
7. C0001～C0010の対応語を選定
8. 18フィールド版Core10を作成
9. カードテンプレートとCSSを作成
10. CSVとZIPを検査
11. MEMORIOPOLIS::Italianへ導入
12. it_IT TTSを確認
13. JANUS-13 Daily Trainingを再構築
14. 期限カードと新規10枚を学習
15. AnkiWebとAnkiDroidへ同期
```

---

## 44．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月21日の最新状態として、MEMORIOPOLIS / JANUS-13を再開します。

次の制作言語は第11言語、第12観測面のイタリア語です。Windowsロケールはit-IT、Ankiロケールはit_ITです。まずGet-WindowsCapability -OnlineでLanguage.Basic~~~it-IT~0.0.1.0とLanguage.TextToSpeech~~~it-IT~0.0.1.0の状態を確認してください。NotPresentの場合はBasicを先に、TextToSpeechを後に直列で導入します。Installedなら再導入しません。

その後、日本語正本section12_ja.mdを基に、第四章第十二節のイタリア語版Novel全文第一稿と18フィールド版Anki Core10を作成してください。デッキ名はMEMORIOPOLIS::Italian、ノートタイプ名はMEMORIOPOLIS Italian Vocabulary、タグはmemoriopolis::it::core10です。

単語TTSは{{tts it_IT:Italian}}、例文TTSは{{tts it_IT:ExampleItalian}}を使います。AnkiDroidで音声エラーが出た場合は、{{tts-voices:}}で端末がコピーしたロケールと音声識別子をそのまま採用してください。

カードでは明瞭な母音、二重子音、c・ch、sc・sch、gの硬音と軟音、gli、gn、名詞の性数、冠詞、動詞活用、主語代名詞の省略、前置詞と冠詞の結合を重点的に観測してください。スペイン語とブラジル・ポルトガル語との同源語はMeaningBridgeへ利用し、音の違いはSoundBridgeで説明してください。

フィルターデッキの正式名称はJANUS-13 Daily Trainingです。第1フィルターはdeck:MEMORIOPOLIS is:due、上限50、忘れている可能性が高い順。第2フィルターはdeck:MEMORIOPOLIS is:new、上限10、追加順です。名称変更だけなので検索条件は変更しません。

ブラジル・ポルトガル語導入時には、既存言語の復習29枚と新規10枚がJANUS-13 Daily Trainingへ同時に収集され、意図した動作を実機確認済みです。

FSRSは有効、目標保持率90%、一括再スケジュールはオフです。新規上限10、復習上限200、学習ステップ1m 10m、再学習10mです。

Concept IDは物語、絵巻、予告編、Anki、多言語、制作ノートを結ぶ都市の住所コードです。絵巻は6景から10景へ拡張し、C0001～C0010と一対一で対応させます。Concept Atlasは外部文書として管理し、Ankiの19フィールド目はまだ追加しません。
```

---

## 45．2026年9月21日の店じまい地点

```text
JANUS-13                              13言語・14観測面
フィルターデッキ正式名                JANUS-13 Daily Training
フィルターデッキ表示位置              デッキ一覧の最上部
Daily Training実機確認                新規10＋復習29＝合計39
Daily Training動作                    完成
ブラジル・ポルトガル語                第10言語・第11観測面
pt-BR Basic                           Installed
pt-BR TextToSpeech                    Installed
ブラジル・ポルトガル語Novel           完成
ブラジル・ポルトガル語Core10          完成・導入済み
次言語                                イタリア語
イタリア語                            第11言語・第12観測面
イタリア語Windowsロケール             it-IT
イタリア語Ankiロケール                it_IT
イタリア語Windows環境確認             今夜の作業
イタリア語Novel・Core10               次回制作
残り言語                              イタリア語・フランス語・ドイツ語
絵巻                                  10景化方針
Concept ID                            都市の住所コード
Concept Atlas                         外部文書で管理予定
```

本日の到達点：

> JANUS-13 Daily Trainingは、既存言語の期限カードと新言語のCore10を一つの運行線へ正しく集約した。名称もデッキ一覧の最上部へ移り、毎日の入口として完成した。次はイタリア語を開通し、スペイン語、ブラジル・ポルトガル語との共通性と音の差を観測する。
