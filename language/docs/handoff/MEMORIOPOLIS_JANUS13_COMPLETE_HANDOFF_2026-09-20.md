# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

**更新日時：2026年9月20日**  
**本日の店じまい地点：スペイン語版Novel全文第一稿と18フィールド版Anki Core10を作成・導入し、MEMORIOPOLIS Daily Trainingでスペイン語の新規10枚が正しく収集されることを確認した。**  
**次回開始地点：ブラジル・ポルトガル語 `pt-BR` のWindows環境確認結果を引き継ぎ、必要ならBasicとTextToSpeechを順番に導入する。その後、ブラジル・ポルトガル語版NovelとCore10を作成する。**

---

## 0．最重要サマリー

- プロジェクト名は`JANUS-13`。
- 全体は13言語、14観測面で構成する。
- 日本語は一言語として数えるが、近代日本語面と現代日本語面の二つを持つ。
- スペイン語は第9言語、第10観測面。
- ブラジル・ポルトガル語は第10言語、第11観測面。
- スペイン語はスペインのスペイン語`es-ES`を基準とする。
- ポルトガル語はブラジル・ポルトガル語`pt-BR`を基準とする。
- ブラジル版を採用する理由は、日本からブラジルへの移民、日系社会、日本への還流、現代の日伯関係、BRICSとの接続を優先するため。
- ポルトガルとの種子島、南蛮貿易、キリスト教、外来語などの歴史的接続は制作ノートの歴史層として保持する。
- スペイン語のメキシコ・中南米変種は比較層に置くが、AnkiとNovelの正面はスペイン版とする。
- ブラジル・ポルトガル語のAnkiとNovelでは、ブラジルで自然な語彙、文法、発音を標準にする。
- Anki標準カードは18フィールド。
- MEMORIOPOLIS Daily Trainingは、期限カード最大50枚と新規カード最大10枚を自動収集する。
- FSRSは有効。目標保持率90%。一括再スケジュールはオフ。
- 本日、スペイン語の新規10枚だけがDaily Trainingへ入った動きは正常。
- 他言語は先に親デッキから復習済みで、`is:due`にも`is:new`にも該当しなかったためDaily Trainingへ入らなかった。
- 明日はブラジル・ポルトガル語Core10を追加し、期限カードと新規10枚の合流を引き続き観測する。

---

## 1．JANUS-13の言語数と観測面

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

### 14観測面

```text
1. 日本語・近代面
2. 日本語・現代面
3. 韓国語
4. ロシア語
5. 臺灣華語
6. 英語
7. フィリピン語
8. インドネシア語
9. ベトナム語
10. スペイン語
11. ブラジル・ポルトガル語
12. イタリア語
13. フランス語
14. ドイツ語
```

> 日本語は二言語ではなく、一言語の内部に近代面と現代面という二つの時間面を持つ。

---

## 2．現在のMEMORIOPOLIS

```text
MEMORIOPOLIS
├─ English
├─ Filipino
├─ Indonesian
├─ Korean
├─ ModernJapanese
├─ Russian
├─ Spanish
├─ TaiwaneseMandarin
└─ Vietnamese
```

近代日本語面は、歴史的仮名遣い・旧字体版として別観測面に保持する。

次に追加するデッキ：

```text
MEMORIOPOLIS::Portuguese
```

予定ノートタイプ：

```text
MEMORIOPOLIS Portuguese Vocabulary
```

予定タグ：

```text
memoriopolis::pt_br::core10
```

---

## 3．Core番号とConcept

```text
Core10
→ 第四章第十二節
→ C0001～C0010

Core20
→ 第四章第十三節
→ C0011～C0020

Core30
→ 序章
→ C0021～C0030
```

Core番号は物語の章順ではなく、JANUS-13型Ankiへ投入した新出Conceptの累積数を表す。

### 現在の共通Concept

```text
C0001  記録
C0002  記憶
C0003  都市
C0004  通知
C0005  返信
C0006  宛先
C0007  署名
C0008  検証
C0009  権限
C0010  役割
```

---

## 4．制作循環

```text
日本語正本
↓
各言語のNovel
↓
新出Conceptを抽出
↓
JANUS-13型Ankiカード
↓
MEMORIOPOLIS Daily Training
↓
文字・音・文法・知覚上の発見
↓
制作ノート
↓
カード設計を改修
↓
次のNovelとCore
```

設計原則：

```text
歴史は、制作ノートに残す。
座標は、Concept Registryで守る。
縁は、Ankiで反復する。
交配は、Novelで起こす。
```

> 正確だが説明しすぎない。緩やかだが虚偽ではない。「疎な精密さ」を維持する。

---

## 5．18フィールド標準仕様

```text
1  ID
2  TargetLanguage
3  Pronunciation
4  Japanese
5  PartOfSpeech
6  UsageNote
7  ExampleTargetLanguage
8  ExampleJapanese
9  Root
10 Affixes
11 PerceptualSegmentation
12 MorphologicalBreakdown
13 ExampleBreakdown
14 ExampleExplanation
15 MeaningBridge
16 SoundBridge
17 Source
18 CourseTags
```

言語別の第2・第7フィールド：

```text
Spanish / ExampleSpanish
Portuguese / ExamplePortuguese
```

### 三つの観測層

```text
音の構造
→ Pronunciation
→ PerceptualSegmentation
→ SoundBridge

語の内部構造
→ Root
→ Affixes
→ MorphologicalBreakdown

文の内部構造
→ ExampleBreakdown
→ ExampleExplanation
```

### 例文解説の基準

```text
語句を意味単位に分解する
冠詞・前置詞・代名詞を説明する
動詞の人称・数・時制を説明する
修飾関係を説明する
主語省略を説明する
語順を説明する
自然な日本語訳への並べ替えを説明する
```

> 初学者が「なぜこの日本語訳になるのか」を腹落ちできることを優先する。

---

## 6．スペイン語版の完成状況

### 基準変種

```text
Español de España
Windows：es-ES
Anki：es_ES
```

メキシコや中南米の広がりは認識するが、スペイン語の正面は本場スペインのスペイン語とする。

### ZIP

```text
MEMORIOPOLIS_Spanish_Core10_draft01_18fields_2026-09-20.zip
```

### 収録ファイル

```text
section12_es_draft01.md
es_core10_master_draft01_18fields.csv
es_core10_anki_draft01_18fields.csv
README_es_core10_draft01.md
SPANISH_NOTE_TYPE_DRAFT01_18FIELDS.md
SPANISH_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_es.md
```

### Core10

```text
C0001  registro       記録
C0002  memoria        記憶
C0003  ciudad         都市
C0004  notificación   通知
C0005  respuesta      返信／応答
C0006  destinatario   宛先／受取人
C0007  firma          署名
C0008  verificación   検証
C0009  permiso        権限／許可
C0010  rol            役割／ロール
```

### Windows環境

```text
Language.Basic~~~es-ES~0.0.1.0
→ Installed

Language.TextToSpeech~~~es-ES~0.0.1.0
→ Installed

Language.Handwriting~~~es-ES~0.0.1.0
→ NotPresent、不要

Language.OCR~~~es-ES~0.0.1.0
→ NotPresent、不要

Language.Speech~~~es-ES~0.0.1.0
→ NotPresent、Anki TTSには不要
```

### TTS

```html
{{tts es_ES:Spanish}}
```

```html
{{tts es_ES:ExampleSpanish}}
```

---

## 7．Daily Trainingの本日の動作確認

### 確定設定

第1フィルター：

```text
deck:MEMORIOPOLIS is:due
```

```text
上限：50
選択順：忘れている可能性が高い順
```

第2フィルター：

```text
deck:MEMORIOPOLIS is:new
```

```text
上限：10
選択順：追加順
```

オプション：

```text
回答に基づいて復習予定を組み直す：オン
2つ目の絞り込み：オン
空でも作成・更新：オフ
```

### 2026年9月20日の観測

スペイン語を追加する前に、親デッキ`MEMORIOPOLIS`から既存言語の期限カードを復習した。

その後、スペイン語Core10を追加してDaily Trainingを再構築した結果：

```text
既存言語の期限カード
→ 0枚

既存言語の新規カード
→ 0枚

スペイン語の新規カード
→ 10枚

Daily Training
→ 10枚
```

これは正常動作。

```text
既存言語
→ すでに学習済みなのでis:newではない
→ 本日の期限分を先に復習したのでis:dueでもない

スペイン語
→ 初回導入なのでis:new
→ 第2フィルターで10枚収集
```

### 明日の観測ポイント

```text
1. 今日のスペイン語10枚を完了する
2. 明日、ブラジル・ポルトガル語Core10を追加する
3. Daily Trainingを再構築する
4. その時点の期限カードが第1フィルターから入るか確認する
5. ポルトガル語の新規10枚が第2フィルターから入るか確認する
```

期待形：

```text
既存言語の期限カード
＋
ブラジル・ポルトガル語の新規10枚
```

---

## 8．FSRSと通常デッキの設定

### FSRS

```text
FSRS：オン
目標保持率：90%
FSRSパラメータ：既定値
変更時に復習予定を再計算する：オフ
最適化：まだ実行しない
```

### 1日の上限

```text
新規カード：10
復習カード：200
新規カードを復習上限の対象外にする：オン
最上位デッキから上限を適用する：オン
```

### 学習ステップ

```text
学習：1m 10m
再学習：10m
```

### 定着しにくいカード

```text
判定：忘却8回
処理：タグのみ
```

### 関連カード

```text
関連する新規カードを同日に表示しない：オン
関連する復習カードを同日に表示しない：オン
日をまたぐ関連学習カードを同日に表示しない：オン
```

### 音声

```text
音声を自動再生しない：オフ
```

否定形なので、音声は自動再生される。

### 回答ボタン

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

## 9．ブラジル・ポルトガル語の確定方針

### 基準変種

```text
Português do Brasil
Windowsロケール：pt-BR
Ankiロケール：pt_BR
```

### 採用理由

```text
日本からブラジルへの移民
ブラジルの日系社会
日本への移住と世代間の還流
日本国内のポルトガル語との接触
現代の日伯関係
BRICSとの接続
```

### ポルトガルとの歴史層

次は捨てず、制作ノートに保持する。

```text
種子島への火縄銃伝来
南蛮貿易
キリスト教
ポルトガル語由来の外来語
近世日本とポルトガルの接触
```

整理：

```text
AnkiとNovelの正面
→ ブラジル・ポルトガル語

比較層
→ ヨーロッパ・ポルトガル語

歴史層
→ 日本とポルトガルの接触史
```

### 予定デッキ

```text
MEMORIOPOLIS::Portuguese
```

### 予定ノートタイプ

```text
MEMORIOPOLIS Portuguese Vocabulary
```

### 予定TTS

```html
{{tts pt_BR:Portuguese}}
```

```html
{{tts pt_BR:ExamplePortuguese}}
```

---

## 10．今夜のWindows環境確認

### 事前準備

```text
1. 自宅の安定したWi-Fiへ接続
2. PCを電源へ接続
3. OneDrive同期を一時停止
4. VS CodeまたはPowerShellを管理者として起動
5. 管理者表示を確認
```

通常作業は管理者権限で行わない。言語機能の確認と導入時だけ管理者権限を使う。

### 管理者権限確認

```powershell
$isAdmin = (
    [Security.Principal.WindowsPrincipal]
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator
)

$isAdmin
```

期待値：

```text
True
```

### pt-BR Capability確認

最初に実行するコマンド：

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~pt-BR~'
} |
Select-Object Name, State
```

主な確認対象：

```text
Language.Basic~~~pt-BR~0.0.1.0
Language.TextToSpeech~~~pt-BR~0.0.1.0
```

環境によって表示される可能性があるもの：

```text
Language.Handwriting~~~pt-BR~0.0.1.0
Language.OCR~~~pt-BR~0.0.1.0
Language.Speech~~~pt-BR~0.0.1.0
```

### 結果の読み方

```text
Installed
→ 導入済み
→ 再導入しない

NotPresent
→ 実機で提供されているが未導入
→ 必要機能だけ導入する

何も表示されない
→ 検索を広げて再確認する
```

何も表示されない場合：

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match 'pt-BR|Portuguese'
} |
Select-Object Name, State
```

Capability名は推測せず、実機で表示された名前を正本とする。

---

## 11．必要な場合だけ実行するダウンロード

### Step 1：Basic

`Language.Basic~~~pt-BR~0.0.1.0`が`NotPresent`の場合だけ実行する。

```powershell
Add-WindowsCapability -Online -Name "Language.Basic~~~pt-BR~0.0.1.0"
```

PowerShellプロンプトが戻るまで待つ。

### Step 2：TextToSpeech

Basicが完了した後、`Language.TextToSpeech~~~pt-BR~0.0.1.0`が`NotPresent`の場合だけ実行する。

```powershell
Add-WindowsCapability -Online -Name "Language.TextToSpeech~~~pt-BR~0.0.1.0"
```

### 実行順

```text
Basic
↓
完了とプロンプト復帰を確認
↓
TextToSpeech
↓
完了とプロンプト復帰を確認
↓
最終確認
```

### 処理中の禁止事項

```text
BasicとTextToSpeechを同時実行しない
同じコマンドを二重実行しない
Ctrl+Cを押さない
PowerShellやVS Codeを閉じない
PCをスリープさせない
Wi-Fiを切断しない
```

### Handwriting、OCR、Speech

```text
Handwriting
→ 今回は不要

OCR
→ 今回は不要

Speech
→ 音声入力用
→ Ankiの読み上げには不要
```

Anki TTSのために優先するもの：

```text
Basic
TextToSpeech
```

---

## 12．最終確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~pt-BR~'
} |
Select-Object Name, State
```

期待する最終状態：

```text
Language.Basic~~~pt-BR~0.0.1.0          Installed
Language.TextToSpeech~~~pt-BR~0.0.1.0   Installed
```

他の機能は次でも問題ない。

```text
Language.Handwriting~~~pt-BR~0.0.1.0    NotPresent
Language.OCR~~~pt-BR~0.0.1.0            NotPresent
Language.Speech~~~pt-BR~0.0.1.0         NotPresent
```

### 終了処理

```text
RestartNeededを確認する
必要な場合だけ再起動する
OneDrive同期を再開する
管理者VS Codeを終了する
通常権限のVS Codeへ戻す
```

Capabilityの確認だけで、追加導入をしていない場合は通常再起動不要。

---

## 13．実機結果の記録欄

```text
Language.Basic~~~pt-BR~0.0.1.0
→

Language.TextToSpeech~~~pt-BR~0.0.1.0
→

Language.Handwriting~~~pt-BR~0.0.1.0
→

Language.OCR~~~pt-BR~0.0.1.0
→

Language.Speech~~~pt-BR~0.0.1.0
→

RestartNeeded
→

確認日時
→ 2026-09-20
```

---

## 14．ブラジル・ポルトガル語版で観測するもの

```text
鼻母音
→ ã、õ、語末-m/-nなど

開母音・閉母音
→ é / ê、ó / ô

rの地域差
→ 語頭・rr・語中単独r

lh / nh
→ 日本語にない子音連続・口蓋音

語末音
→ 地域による母音化や摩擦音化

名詞の性と数
→ o / a、-s

冠詞
→ o / a / os / as

動詞活用
→ 人称・数・時制

主語代名詞
→ eu、você、nós、a genteなど

目的語代名詞
→ 語順と実際の口語使用

進行表現
→ estar＋動名詞

ブラジルとポルトガルの差
→ 必要な場合だけUsageNoteへ短く記録
```

### 18フィールドへの配置

```text
Pronunciation
→ ブラジル標準のIPA

PerceptualSegmentation
→ 音節と強勢

Root
→ 語幹

Affixes
→ 接辞・屈折語尾

MorphologicalBreakdown
→ 語幹＋性数語尾、動詞語幹＋活用語尾

ExampleBreakdown
→ 冠詞・代名詞・前置詞・動詞句

ExampleExplanation
→ 主語省略、活用、語順、日本語訳への変換

SoundBridge
→ 鼻母音、強勢、r、lh、nh、語末音
```

19番目の独立フィールドは追加せず、18フィールドを維持する。

---

## 15．明日の制作予定

```text
1. pt-BRのWindows Capability結果を確認
2. 必要ならBasicを導入
3. 必要ならTextToSpeechを導入
4. Installedを確認
5. 日本語正本section12_ja.mdを確認
6. ブラジル・ポルトガル語版Novel全文第一稿を作成
7. C0001～C0010の対応語を選定
8. Novel本文とCore10例文を一致させる
9. IPA、音節、強勢、鼻母音を記述
10. 語幹・語尾・形態の橋を作る
11. 例文を意味単位へ分解する
12. なぜこの日本語訳になるかを説明する
13. 18列マスターCSVを作る
14. ヘッダーなしAnki CSVを作る
15. ノートタイプ仕様を作る
16. カードテンプレートとCSSを作る
17. READMEを作る
18. 日本語正本コピーを同梱する
19. ZIP化する
20. 行数・列数・UTF-8・ZIP整合性を検査する
21. PC版Ankiへ導入する
22. pt_BR TTSを確認する
23. Daily Trainingを再構築する
24. 期限カードと新規10枚の合流を観測する
25. AnkiWebへ同期する
26. AnkiDroidで確認する
```

予定ZIP名：

```text
MEMORIOPOLIS_Portuguese_BR_Core10_draft01_18fields_2026-09-21.zip
```

予定収録ファイル：

```text
section12_pt_br_draft01.md
pt_br_core10_master_draft01_18fields.csv
pt_br_core10_anki_draft01_18fields.csv
README_pt_br_core10_draft01.md
PORTUGUESE_BR_NOTE_TYPE_DRAFT01_18FIELDS.md
PORTUGUESE_BR_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_pt_br.md
```

---

## 16．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月20日の最新状態として、MEMORIOPOLIS / JANUS-13を再開します。

次の言語は第10言語、第11観測面のブラジル・ポルトガル語です。基準変種はPortuguês do Brasil、Windowsロケールはpt-BR、Ankiロケールはpt_BRです。日本からブラジルへの移民、日系社会、日本への還流、現代の日伯関係、BRICSとの接続を優先します。ポルトガルとの種子島、南蛮貿易、キリスト教、外来語の歴史は制作ノートの歴史層として保持します。

まず、前夜に取得したGet-WindowsCapabilityの結果を確認してください。Language.Basic~~~pt-BR~0.0.1.0とLanguage.TextToSpeech~~~pt-BR~0.0.1.0がInstalledなら追加導入しません。NotPresentならBasicを先に、TextToSpeechを後に直列で導入します。Capability名は推測せず、実機表示を正本にしてください。

その後、日本語正本section12_ja.mdを基に、第四章第十二節のブラジル・ポルトガル語版Novel全文第一稿と18フィールド版Anki Core10を作成してください。デッキ名はMEMORIOPOLIS::Portuguese、ノートタイプ名はMEMORIOPOLIS Portuguese Vocabulary、タグはmemoriopolis::pt_br::core10です。

単語TTSは{{tts pt_BR:Portuguese}}、例文TTSは{{tts pt_BR:ExamplePortuguese}}を使用します。AnkiDroidで音声エラーが出た場合、{{tts-voices:}}で端末がコピーしたロケールと音声識別子をそのまま採用し、推測で変更しません。

カードではブラジルで自然な語彙・文法・発音を採用し、鼻母音、開閉母音、r、lh、nh、強勢、名詞の性数、冠詞、動詞活用、vocêとa gente、ブラジルの進行表現を重点的に観測してください。ヨーロッパ・ポルトガル語との差は、Concept理解に必要な場合だけUsageNoteへ短く記録してください。

MEMORIOPOLIS Daily Trainingは、第1フィルターがdeck:MEMORIOPOLIS is:due、上限50、忘れている可能性が高い順です。第2フィルターはdeck:MEMORIOPOLIS is:new、上限10、追加順です。スペイン語追加時に新規10枚だけが収集されたのは、他言語の期限カードを先に親デッキから復習済みだったためで、正常動作です。

FSRSは有効、目標保持率90%、一括再スケジュールはオフです。通常デッキの新規上限10、復習上限200、学習ステップ1m 10m、再学習10mです。FSRSパラメータの最適化はまだ行いません。
```

---

## 17．2026年9月20日の店じまい地点

```text
JANUS-13                              13言語・14観測面で確定
日本語                                1言語、近代面と現代面
スペイン語                            第9言語・第10観測面
スペイン語基準                        es-ES、スペイン版
スペイン語Novel                       全文第一稿完成
スペイン語Core10                      18フィールド完成・導入済み
スペイン語Windows Basic/TTS           Installed
Spanish新規10枚                       Daily Trainingへ収集確認
既存言語が入らなかった理由            期限分を先に復習済み
Daily Training                        正常動作
FSRS                                  有効、目標保持率90%
次言語                                ポルトガル語
ポルトガル語の基準                    ブラジル版 pt-BR
ポルトガル語                          第10言語・第11観測面
ブラジル採用理由                      日系移民・日系社会・BRICS
ポルトガルとの歴史                    制作ノートの歴史層
pt-BR Windows Capability確認          今夜実施
pt-BR Basic/TTS導入                   NotPresentの場合だけ実施
ブラジル版Novel・Core10               明日の制作対象
```

本日の到達点：

> スペイン語面を開通し、Daily Trainingが既存期限カードの消化後には新規言語のCore10だけを正しく収集することを確認した。次はブラジル・ポルトガル語を、日本との移民史、日系社会、BRICSという現代的な縁から開通する。ポルトガルとの歴史は捨てず、異なる時間層として制作ノートへ保持する。
