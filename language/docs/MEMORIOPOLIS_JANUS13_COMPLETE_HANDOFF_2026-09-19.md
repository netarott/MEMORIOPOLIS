# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

**更新日時：2026年9月19日 夜**  
**次回の制作言語：スペイン語（Español）**  
**次回開始地点：Windows上でスペイン語（スペイン）`es-ES`のCapabilityを確認し、BasicとTextToSpeechを順番に導入する。その後、第四章第十二節のスペイン語版Novelと18フィールド版Anki Core10を作成する。**

---

## 0．今回の最重要更新

- ベトナム語版Novelと18フィールド版Anki Core10を作成済み。
- ベトナム語版AnkiをPCへ導入済み。
- Windowsのベトナム語BasicとTextToSpeechは導入済み。
- インドネシア語のAnkiDroid TTSでは、端末がコピーした旧Javaロケール`in_ID`とGoogle音声識別子をそのまま使用する必要があった。
- インドネシア語AnkiDroidの確定音声指定は、`in_ID`と`com.google.android.tts-id-id-x-dfz-local`の組み合わせ。
- Ankiの毎日用フィルターデッキを`MEMORIOPOLIS Daily Training`へ改名・再設計した。
- 第1フィルターは期限カード、第2フィルターは言語非依存の新規カードとした。
- AnkiのFSRSを有効化した。
- FSRSの目標保持率は90%。
- FSRS有効化時の一括再スケジュールは実施していない。
- 新規カード上限は10、通常デッキの復習上限は200。
- 学習ステップは`1m 10m`、再学習ステップは`10m`。
- 定着しにくいカードは8回で判定し、処理は「タグのみ」。
- 関連カードを同じ日に表示しない設定は3項目とも有効。
- 音声は現時点で自動再生を維持する。
- Anki統計は、一時的なフィルターデッキ単体ではなく、原則として「コレクション」で確認する。
- 明日の次言語はスペイン語。Windowsではスペイン語（スペイン）`es-ES`を基準に環境を準備する。

---

## 1．プロジェクトの基本原則

### 正本と派生物

```text
日本語正本
↓
各言語のNovel
↓
新出Conceptを抽出
↓
JANUS-13型Ankiカード
↓
親デッキMEMORIOPOLISでトレーニング
↓
文字・音・文法・知覚上の発見
↓
制作ノート
↓
カード設計と次のNovelを改修
```

### Core番号

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

### 設計原則

```text
歴史は、制作ノートに残す。
座標は、Concept Registryで守る。
縁は、Ankiで反復する。
交配は、Novelで起こす。
```

> 正確だが説明しすぎない。緩やかだが虚偽ではない。「疎な精密さ」を維持する。

---

## 2．現在のMEMORIOPOLISデッキ

```text
MEMORIOPOLIS
├─ Korean
├─ Russian
├─ TaiwaneseMandarin
├─ English
├─ ModernJapanese
├─ Filipino
├─ Indonesian
└─ Vietnamese
```

次に追加する予定：

```text
MEMORIOPOLIS::Spanish
```

予定ノートタイプ：

```text
MEMORIOPOLIS Spanish Vocabulary
```

予定タグ：

```text
memoriopolis::es::core10
```

---

## 3．18フィールド標準仕様

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

言語別の置換例：

```text
Indonesian / ExampleIndonesian
Vietnamese / ExampleVietnamese
Spanish / ExampleSpanish
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

### 例文解説の品質基準

```text
語句の意味単位を分ける
機能語・前置詞・冠詞・代名詞を説明する
動詞の人称・数・時制を説明する
修飾関係を説明する
語順を説明する
省略された主語などを説明する
自然な日本語訳へ並べ替える理由を説明する
```

> 初学者が「なぜこの日本語訳になるのか」を腹落ちできることを優先する。

---

## 4．ベトナム語版の完成状況

### ZIP

```text
MEMORIOPOLIS_Vietnamese_Core10_draft01_18fields_2026-09-19.zip
```

### Novel

```text
section12_vi_draft01.md
```

### Anki

```text
vi_core10_master_draft01_18fields.csv
vi_core10_anki_draft01_18fields.csv
VIETNAMESE_NOTE_TYPE_DRAFT01_18FIELDS.md
VIETNAMESE_CARD_TEMPLATE_DRAFT01.md
README_vi_core10_draft01.md
```

### Core10

```text
C0001  bản ghi       記録
C0002  ký ức         記憶
C0003  thành phố     都市
C0004  thông báo     通知
C0005  hồi đáp       返信／応答
C0006  đích đến      宛先／行き先
C0007  chữ ký        署名
C0008  xác minh      検証
C0009  quyền hạn     権限
C0010  vai trò       役割／ロール
```

### Windows環境

```text
Language.Basic~~~vi-VN~0.0.1.0
→ Installed

Language.TextToSpeech~~~vi-VN~0.0.1.0
→ Installed

Language.Handwriting~~~vi-VN~0.0.1.0
→ NotPresent、不要
```

### TTS

```html
{{tts vi_VN:Vietnamese}}
```

```html
{{tts vi_VN:ExampleVietnamese}}
```

AnkiDroidで`APP_MISSING_VOICE`が出た場合は、推測でロケールを書き換えない。

```html
{{tts-voices:}}
```

を一時的に追加し、AnkiDroidがコピーしたロケールと音声識別子をそのまま採用する。

---

## 5．インドネシア語AnkiDroid TTSの確定知見

### 事象

```text
Windows版Anki
→ id-IDで再生可能

AndroidのText-to-speech output
→ Indonesian (Indonesia)でPLAY可能

AnkiDroid
→ APP_MISSING_VOICE
```

### 診断

一時的に次をカードテンプレートへ追加した。

```html
{{tts-voices:}}
```

AnkiDroidがコピーした音声指定：

```html
{{tts in_ID voices=com.google.android.tts-id-id-x-dfz-local}}
```

### 確定タグ

単語：

```html
{{tts in_ID voices=com.google.android.tts-id-id-x-dfz-local:Indonesian}}
```

例文：

```html
{{tts in_ID voices=com.google.android.tts-id-id-x-dfz-local:ExampleIndonesian}}
```

### 重要な教訓

```text
ISO上の現在の言語コード
→ id

Android／Java系で端末が返した旧コード
→ in
```

端末が`in_ID`をコピーした場合、`id_ID`へ「修正」しない。AnkiDroidが返した指定を正本とする。

---

## 6．MEMORIOPOLIS Daily Trainingの確定設定

### 名前

```text
MEMORIOPOLIS Daily Training
```

### 第1フィルター：通常復習

```text
deck:MEMORIOPOLIS is:due
```

```text
上限：50
選択順：忘れている可能性が高い順
```

意味：

```text
MEMORIOPOLIS配下
＋
今日までに復習期限を迎えたカード
＋
忘却リスクが高い順
```

### 第2フィルター：汎用的な新言語導入

```text
deck:MEMORIOPOLIS is:new
```

```text
上限：10
選択順：追加順
```

この検索は言語名に固定しない。

```text
今日
→ ベトナム語の未学習カード

明日
→ スペイン語の未学習カード

その次
→ 次に追加された言語の未学習カード
```

前日の未学習カードが残っている場合は、追加順により先に回収する。

### オプション

```text
このデッキでの解答に基づいて復習予定を組み直す
→ オン

2つ目の絞り込みを有効にする
→ オン

空でもこのデッキを作成／更新する
→ オフ
```

### 運用

```text
新規カード
↓
第2フィルターで初回学習
↓
復習予定が設定される
↓
is:newから外れる
↓
期限が来る
↓
第1フィルターへ合流
```

---

## 7．Anki通常デッキの確定設定

上部表示：

```text
デフォルト（10個のデッキで使用）
```

同じプリセットを使う10個のデッキへ設定が共有される。

### 1日の上限

```text
1日の新規カード上限：10
1日の復習上限：200
```

```text
新規カードを復習上限の対象外にする：オン
最上位のデッキから上限を適用する：オン
```

### 新規カード

```text
学習ステップ：1m 10m
追加位置：追加が古い順
```

### 忘却

```text
再学習ステップ：10m
定着しにくいカードと判断する忘却回数：8
定着しにくいカードへの処理：タグのみ
```

「タグのみ」を維持する理由：

```text
自動停止しない
↓
難しいカードを観測できる
↓
カード設計の問題を発見できる
↓
ExampleExplanationやSoundBridgeを改修できる
```

### 関連カード

```text
関連する新規カードを同じ日に表示しない：オン
関連する復習カードを同じ日に表示しない：オン
日をまたぐ関連学習カードを同じ日に表示しない：オン
```

### 音声

```text
音声を自動再生しない：オフ
```

否定形なので、現状は音声を自動再生する。新言語の初期段階では維持する。

### タイマー

```text
回答時間の上限：60秒
画面にタイマーを表示する：オフ
回答表示時にタイマーを停止する：オフ
```

60秒は強制終了ではなく、統計へ記録する回答時間の上限。

---

## 8．FSRSの確定設定

```text
FSRS：オン
目標保持率：90%
FSRSパラメータ：既定のパラメータ
変更時に復習予定を再計算する：オフ
最適化時に学習データを診断する：オフ
```

### 高度な設定

```text
最大間隔：36500日
過去の保持率：90%
指定日より前の復習を除外：1970/01/01
カスタムスケジューリング：未使用
```

### 当面しないこと

```text
「現在のプリセットを最適化」を押さない
「すべてのプリセットを最適化」を押さない
「変更時に復習予定を再計算する」をオンにしない
```

### 最適化の検討時期

```text
Daily Trainingの新設定で2～4週間運用
↓
回答ボタンを一貫して使用
↓
統計の真の保持率を月単位で確認
↓
現在のプリセットを最適化
```

### 回答ボタンの基準

```text
もう一度
→ 意味を思い出せなかった
→ 別言語と取り違えた
→ 音から語を特定できなかった

難しい
→ 正解したが非常に迷った
→ 自力で思い出せたが時間がかかった

普通
→ 適度な負荷で正解した

簡単
→ 文字・音・意味が即座につながった
```

答えを表示した後に「知っていた」と感じても、表示前に想起できなかった場合は「もう一度」。

---

## 9．Anki統計の見方

### フィルターデッキ単体で「データなし」となる理由

`MEMORIOPOLIS Daily Training`はカードの恒久的な所属先ではない。

```text
子デッキのカード
↓
Daily Trainingへ一時的に収集
↓
学習
↓
元のホームデッキへ戻る
```

したがって、統計の「デッキ」でDaily Trainingを選ぶと、対象カードが現在残っておらず「データなし」と表示されることがある。

### 統計の正本

```text
対象：コレクション
期間：過去12か月または全履歴
```

必要に応じて検索欄へ：

```text
deck:MEMORIOPOLIS
```

### 2026年9月19日の確認値

```text
本日：64.77分
回答回数：250回
1回答あたり：15.55秒
もう一度：0回

学習：82
復習：10
再学習：0
フィルターデッキ：158
```

「250枚」は250種類のカードとは限らず、同じカードへの複数回答を含む。

### 今後の復習予定

確認時点：

```text
向こう1か月の合計：70回
単純平均：1日あたり2回
明日の期限：32回
推定日次負荷：29回
```

```text
緑の棒
→ 各日に期限を迎えるカード数

灰色の累積領域
→ 何も学習しなかった場合に、その日までに累積する期限カード数
```

### 復習グラフ

確認時点：

```text
学習日数：31日中11日
合計：1,320回答
期間内平均：1日43回答
学習日の平均：1日120回答
```

現段階は定着期ではなく、多言語路線の初回開通期。今後、Daily TrainingとFSRSにより安定運行へ移行する。

### 今後見る指標

```text
毎日
→ 今日の学習時間
→ もう一度の回数
→ 明日の復習予定

週1回
→ カレンダーの連続性
→ 学習日の平均回答数
→ 回答ボタンの分布

1か月後
→ 真の保持率
→ カードの安定性
→ カードの難易度
→ 想起可能性
```

---

## 10．明日の言語：スペイン語

### 採用する地域変種

```text
スペイン語（スペイン）
Spanish (Spain)
Español (España)
ロケール：es-ES
Anki表記：es_ES
```

JANUS-13の最初のスペイン語面は`es-ES`を基準とする。

Windows標準TTSでは、スペイン語（スペイン）の従来型音声としてPablo、Helena、LauraがMicrosoftの対応表に掲載されている。自然音声としてはスペインのÁlvaroとElviraも案内されているが、Ankiが自然音声を直接利用できるとは限らないため、まずLanguage.TextToSpeechの標準音声で確認する。

### 予定デッキ

```text
MEMORIOPOLIS::Spanish
```

### 予定ノートタイプ

```text
MEMORIOPOLIS Spanish Vocabulary
```

### 予定TTS

```html
{{tts es_ES:Spanish}}
```

```html
{{tts es_ES:ExampleSpanish}}
```

AnkiDroidでは、まず`es_ES`を試す。エラー時は`{{tts-voices:}}`を使い、端末がコピーした値をそのまま採用する。

---

## 11．スペイン語Windows環境の事前調査

今夜は、まず実機に存在するCapabilityを確認する。管理者PowerShellで実行する。

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

### es-ESのCapability確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~es-ES~'
} |
Select-Object Name, State
```

確認対象：

```text
Language.Basic~~~es-ES~0.0.1.0
Language.TextToSpeech~~~es-ES~0.0.1.0
```

環境によっては次も表示される可能性がある。

```text
Language.Handwriting~~~es-ES~0.0.1.0
Language.OCR~~~es-ES~0.0.1.0
Language.Speech~~~es-ES~0.0.1.0
```

### 何も出ない場合

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match 'es-ES|Spanish'
} |
Select-Object Name, State
```

### 判断基準

```text
Installed
→ 導入済み

NotPresent
→ 利用可能だが未導入

一覧に存在しない
→ その機能は実機環境で提供されていない可能性
```

Capability名は推測だけで決めず、実機の表示を正本とする。

---

## 12．スペイン語言語機能の導入手順

### 事前準備

```text
自宅Wi-Fiへ接続
PCを電源へ接続
OneDrive同期を一時停止
管理者PowerShellを起動
スリープさせない
```

### Step 1：Basic

実機でCapabilityが存在し、`NotPresent`の場合のみ実行する。

```powershell
Add-WindowsCapability -Online -Name "Language.Basic~~~es-ES~0.0.1.0"
```

PowerShellプロンプトが戻るまで待つ。

### Step 2：TextToSpeech

Basicが完了してから実行する。

```powershell
Add-WindowsCapability -Online -Name "Language.TextToSpeech~~~es-ES~0.0.1.0"
```

### 同時実行禁止

```text
BasicとTextToSpeechを同時に実行しない
同じコマンドを二重実行しない
Ctrl+Cを押さない
PowerShellを閉じない
Wi-Fiを切断しない
```

### 最終確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~es-ES~'
} |
Select-Object Name, State
```

期待する最終状態：

```text
Language.Basic~~~es-ES~0.0.1.0          Installed
Language.TextToSpeech~~~es-ES~0.0.1.0   Installed
```

Handwriting、OCR、SpeechはJANUS-13のAnki TTSには必須ではない。BasicとTextToSpeechを優先する。

### 終了処理

```text
RestartNeededを確認
必要な場合だけ再起動
OneDrive同期を再開
管理者VS Codeを終了
通常権限のVS Codeへ戻す
```

---

## 13．スペイン語版で観測するもの

```text
名詞の性
→ 男性・女性

冠詞
→ el / la / los / las
→ un / una / unos / unas

形容詞の一致
→ 性・数への一致

動詞活用
→ 人称・数
→ 現在・過去など

主語代名詞の省略
→ 動詞活用から主語を復元

目的語代名詞
→ lo / la / le / los / las / les など

ser / estar
→ 日本語ではどちらも「〜である」になり得る差

por / para
→ 日本語訳だけでは潰れやすい機能差

r / rr
→ 単一のrと巻き舌の対立

j / g
→ 摩擦音

ñ
→ 独立した文字としての音価

アクセント記号
→ 強勢位置と意味・文法の区別
```

### 18フィールドの重点

```text
Pronunciation
→ IPAと強勢

PerceptualSegmentation
→ 音節と強勢位置

Root
→ 語幹

Affixes
→ 接頭辞・接尾辞・屈折語尾

MorphologicalBreakdown
→ 語幹＋性数語尾、動詞語幹＋人称語尾

ExampleBreakdown
→ 冠詞・前置詞・代名詞・動詞句の分解

ExampleExplanation
→ 主語省略、人称活用、語順から日本語訳への橋
```

独立した19番目のフィールドは、Core10では追加しない。強勢や文法情報は既存18フィールドへ収納し、負荷を見て判断する。

---

## 14．スペイン語版制作の予定手順

```text
1. 日本語正本 section12_ja.mdを確認
2. 第四章第十二節のスペイン語版Novel draft01を作成
3. C0001～C0010の対応語を選定
4. Novel本文とCore10例文の整合を確認
5. 発音・IPA・強勢を作る
6. 語幹・語尾・形態の橋を作る
7. 例文を意味単位へ分解する
8. なぜこの日本語訳になるかを作る
9. MeaningBridgeとSoundBridgeを作る
10. 18列マスターCSVを作る
11. ヘッダーなしAnki CSVを作る
12. ノートタイプ仕様を作る
13. カードテンプレートとCSSを作る
14. READMEを作る
15. 日本語正本コピーを同梱する
16. ZIP化する
17. 行数・列数・文字コード・ZIP整合性を検査する
18. PC版Ankiへ導入する
19. Windows TTSを確認する
20. AnkiWebへ同期する
21. AnkiDroidでTTSを確認する
```

### ZIP予定名

```text
MEMORIOPOLIS_Spanish_Core10_draft01_18fields_2026-09-20.zip
```

### 予定収録ファイル

```text
section12_es_draft01.md
es_core10_master_draft01_18fields.csv
es_core10_anki_draft01_18fields.csv
README_es_core10_draft01.md
SPANISH_NOTE_TYPE_DRAFT01_18FIELDS.md
SPANISH_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_es.md
```

---

## 15．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月19日夜の最新状態として、MEMORIOPOLIS / JANUS-13を再開します。

次の言語はスペイン語です。スペイン語（スペイン）es-ESを基準にします。まず管理者PowerShellで、Get-WindowsCapability -Onlineを使い、es-ESのBasicとTextToSpeechが実機に存在するか、InstalledかNotPresentかを確認してください。Capability名は推測せず、実機結果を正本にしてください。

NotPresentの場合は、Basicを先に、TextToSpeechを後に、直列で導入します。同時実行はしません。最終的にLanguage.Basic~~~es-ES~0.0.1.0とLanguage.TextToSpeech~~~es-ES~0.0.1.0がInstalledであることを確認します。

その後、日本語正本section12_ja.mdを基に、第四章第十二節のスペイン語版Novel全文第一稿と18フィールド版Anki Core10を作成してください。デッキ名はMEMORIOPOLIS::Spanish、ノートタイプ名はMEMORIOPOLIS Spanish Vocabulary、タグはmemoriopolis::es::core10です。

カードは18フィールド標準を維持し、スペイン語では冠詞、名詞の性、形容詞の性数一致、動詞の人称活用、主語代名詞の省略、前置詞、強勢、r/rr、ñを重点的に観測してください。例文は意味単位へ分解し、なぜその日本語訳になるのかを初学者向けに説明してください。

AnkiのMEMORIOPOLIS Daily Trainingは、第1フィルターがdeck:MEMORIOPOLIS is:due、上限50、忘れている可能性が高い順です。第2フィルターはdeck:MEMORIOPOLIS is:new、上限10、追加順です。回答結果による復習予定の組み直しはオンです。

FSRSは有効、目標保持率90%、一括再スケジュールはオフです。通常デッキの新規上限10、復習上限200、学習ステップ1m 10m、再学習10mです。FSRSパラメータの最適化はまだ行いません。

AnkiDroidのTTSでエラーが出た場合、ロケールを推測で変更せず、{{tts-voices:}}で端末がコピーしたロケールと音声識別子をそのまま使ってください。
```

---

## 16．2026年9月19日の店じまい地点

```text
フィリピン語18フィールド化                 完了
インドネシア語Novel・Core10                完了
インドネシア語Windows Basic/TTS            完了
インドネシア語AnkiDroid TTS                端末固有指定を確定
ベトナム語Windows Basic/TTS                完了
ベトナム語Novel全文第一稿                  完了
ベトナム語Core10 18フィールド              完了
ベトナム語PC版Anki                         完成
MEMORIOPOLIS Daily Training                完成
Daily第1フィルター                         is:due、上限50
Daily第2フィルター                         is:new、上限10、追加順
FSRS                                      有効
FSRS目標保持率                             90%
FSRS一括再スケジュール                     オフ
FSRS最適化                                 未実施、2～4週間後に検討
通常デッキ新規上限                         10
通常デッキ復習上限                         200
学習ステップ                               1m 10m
再学習ステップ                             10m
定着しにくいカード                         8回、タグのみ
関連カード分離                             3項目オン
音声自動再生                               有効
統計の確認範囲                             原則コレクション
次言語                                     スペイン語
スペイン語基準ロケール                     es-ES / Anki es_ES
スペイン語Windows Capability確認           次回最初
スペイン語Novel・Core10                    次工程
```

本日の到達点：

> ベトナム語面を開通させただけでなく、MEMORIOPOLISの複習運行そのものを、期限カード、新規カード、FSRSの三層へ整理した。明日からは、新しい言語を一日10枚ずつ導入しながら、既存の言語面はアルゴリズムが必要と判断した時点で再入線する。次はスペイン語で、性・数・人称・強勢がラテン文字上にどう現れるかを観測する。

---

## 17．参考情報

- Microsoft Windowsの対応音声一覧では、スペイン語（スペイン）の標準TTSとしてPablo、Helena、Lauraが掲載されている。
- Windows言語FODでは、Basicを他の言語FODより先に追加し、TextToSpeechは同じ言語のBasicへ依存する。
- Windowsの言語機能は実機・Windowsビルドによって提供状況が異なるため、必ずGet-WindowsCapabilityで確認してから導入する。

参考URL：

```text
https://support.microsoft.com/ja-jp/accessibility/windows/narrator/appendix-a-supported-languages-and-voices
https://learn.microsoft.com/ja-jp/windows-hardware/manufacture/desktop/features-on-demand-language-fod?view=windows-11
https://docs.ankiweb.net/stats.html
https://docs.ankiweb.net/deck-options.html
https://docs.ankiweb.net/filtered-decks.html
```


---

## 18．今夜のスペイン語環境準備チェックリスト

```text
[ ] OneDrive同期を一時停止した
[ ] PCを電源へ接続した
[ ] 自宅Wi-Fiが安定している
[ ] 管理者PowerShellを起動した
[ ] 管理者判定がTrueになった
[ ] es-ES Capability一覧を取得した
[ ] Basicの状態を記録した
[ ] TextToSpeechの状態を記録した
[ ] NotPresentの場合だけBasicを導入した
[ ] Basic完了後にTextToSpeechを導入した
[ ] 最終確認でInstalledを確認した
[ ] RestartNeededを確認した
[ ] OneDrive同期を再開した
[ ] 通常権限のVS Codeへ戻した
```

### 実機結果の記録欄

```text
Language.Basic~~~es-ES~0.0.1.0
→

Language.TextToSpeech~~~es-ES~0.0.1.0
→

RestartNeeded
→

確認日時
→ 2026-09-19
```

### 中断時の原則

```text
PowerShellプロンプトが戻るまで待つ
処理中のウィンドウを閉じない
不安になって同じコマンドを重ねない
エラーが出た場合は画面を保存する
エラー内容を推測で修正せず、そのまま次回へ渡す
```

このチェックリストまで確認した時点で、本日の作業を終了してよい。
