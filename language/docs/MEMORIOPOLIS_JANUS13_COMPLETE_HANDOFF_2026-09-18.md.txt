# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

**更新日：2026年9月18日**  
**店じまい地点：フィリピン語版Core10を18フィールドへ拡張済み。インドネシア語版Novel draft01と18フィールド版Anki Core10を作成済み。Windowsへインドネシア語BasicおよびTextToSpeechを導入済み。ベトナム語のWindows Capabilityを確認済み。**  
**次回開始地点：インドネシア語版Ankiを導入・試運転し、例文解説とTTSを確認する。その後、自宅Wi-Fi環境でベトナム語BasicとTextToSpeechを導入する。**

---

## 0．最重要サマリー

- プロジェクト名は`JANUS-13`で統一する。
- 第四章第十二節は`Core10`である。
- 第四章第十三節は新出Conceptを10個追加して`Core20`とする。
- 序章は、その次の新出Conceptを10個追加して`Core30`とする。
- Core番号は物語の章順ではなく、JANUS-13型Ankiへ投入した新出Conceptの累積数を表す。
- 既知Conceptは新規採番せず、新しい用例・出現箇所をConcept Registryへ記録する。
- 日本語正本から各言語のNovelを制作し、NovelからAnkiカードを作る。
- Ankiでトレーニングし、文字・音・文法・知覚についての発見を制作ノートへ記録する。
- フィリピン語版で、音韻と語形成に比べて「なぜこの日本語訳になるのか」の説明が弱いことを発見した。
- この発見を受け、標準カード構成を16フィールドから18フィールドへ拡張した。
- 追加フィールドは`ExampleBreakdown`と`ExampleExplanation`である。
- フィリピン語版Core10は18フィールド版へ改修済み。
- インドネシア語版は最初から18フィールド構成で作成済み。
- インドネシア語版Novel draft01はAnki ZIP内にも収録済み。
- インドネシア語のWindows BasicとTextToSpeechは導入済み。
- ベトナム語はWindows上でBasic、Handwriting、TextToSpeechの提供を確認済みで、いずれも現在は`NotPresent`である。
- ベトナム語ではBasicとTextToSpeechだけを自宅Wi-Fiで導入する。Handwritingは不要。
- 現代で一般に使われない歴史文字は通常のAnkiカードから外す。
- 文字は歴史資料として収集するのではなく、現代語の内部構造を透視する学習アンカーとして採用する。
- 学術上の正確さはConcept Registryと制作ノートで保持し、Ankiでは現代語時点の「縁」に櫛を通す。
- 設計原則は「疎な精密さ」。正確だが説明しすぎず、緩やかだが虚偽ではない状態を目指す。
- AnkiのTTSでは音声名を固定せず、言語コードだけを指定して移植性を優先する。

---

## 1．現在のMEMORIOPOLIS親デッキ

```text
MEMORIOPOLIS
├─ Korean
├─ Russian
├─ TaiwaneseMandarin
├─ English
├─ ModernJapanese
└─ Filipino
```

次に追加するデッキ：

```text
MEMORIOPOLIS::Indonesian
```

その次に追加する予定のデッキ：

```text
MEMORIOPOLIS::Vietnamese
```

現在の共通Concept：

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

## 2．Core番号とConcept選定規則

```text
Core10
→ 第四章第十二節
→ C0001～C0010

Core20
→ 第四章第十三節
→ C0011～C0020を追加

Core30
→ 序章
→ C0021～C0030を追加
```

> Core番号は物語の時系列ではなく、JANUS-13型Ankiへ追加した新出Conceptの累積数を表す。

```text
NarrativeOrder
→ 物語内部の順序

AnkiOrder
→ 作者が再観測・再整備した順序
```

新出Conceptの選定手順：

```text
1. 対象本文を読む
2. Concept候補を抽出する
3. Concept Registryと照合する
4. 既知Conceptを新規候補から除外する
5. 新出Conceptを重要度と頻度で評価する
6. 上位10個を次のCoreへ採用する
7. 残りの候補を次回候補として保存する
```

原則：

> 重要度で選び、頻度で補強する。

---

## 3．制作循環

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
カード設計の改修
↓
次のNovel・Essay・Commentary・Technical Reflection
```

今回のフィリピン語版で、循環が実際に働いた。

```text
フィリピン語AnkiをAnkiDroidで試す
↓
音韻説明に比べて例文解説が弱いと発見
↓
韓国語・臺灣華語カードと比較
↓
例文分解と文法解説の層が不足していると特定
↓
18フィールドへ拡張
↓
インドネシア語版へ標準仕様として反映
```

> Ankiは副教材ではなく、作品と言語設計を改修する中間工程である。

---

## 4．JANUS-13の三軸

### 4.1 時間の垂直軸

```text
近代日本語
歴史的仮名遣い・旧字体
        ⇅
現代日本語
現代仮名遣い・新字体
```

> 近代日本語は、現代日本語の下にある時間地層である。

### 4.2 言語間関係の水平軸

```text
現代日本語
⇄ 韓国語
⇄ ロシア語
⇄ 臺灣華語
⇄ 英語
⇄ フィリピン語
⇄ インドネシア語
⇄ ベトナム語
⇄ スペイン語
⇄ ポルトガル語
⇄ イタリア語
⇄ フランス語
⇄ ドイツ語
```

### 4.3 分節軸

```text
文字列
↓
音価
↓
音節核
↓
子音の輪郭
↓
知覚上の区切り
↓
形態素
↓
文法関係
↓
日本語訳の組み上がり
```

今回、分節軸の最後に次の層が明確に加わった。

```text
語句の組み合わせ
↓
文法関係
↓
語順の変換
↓
自然な日本語訳
```

---

## 5．文字アンカーの採用原則

> 現代で生きている文字は学習アンカーとしてAnkiへ置く。現代の日常使用から退いた文字は歴史的地層として制作ノートへ置く。

### ハングル

```text
見えるもの：
初声
中声
終声
音節ブロック
パッチム
音変化の起点
```

### 繁體字・旧字体

```text
見えるもの：
意味領域
偏と旁
形声文字の音の手掛かり
漢字文化圏の共有層
近代日本語と臺灣華語の視覚的接続
```

### ラテン文字

```text
見えるもの：
語根
語幹
接辞
活用語尾
派生
重複
語形の横方向の比較
```

### キリル文字

```text
転写で音価を確認
↓
子音配置を観測
↓
語幹と語尾を観測
```

中心命題：

> ハングルは音節を組み立てて見せ、漢字は意味を圧縮して見せ、ラテン文字は語の伸縮を並べて見せる。

---

## 6．疎な精密さ

```text
Concept Registry
→ 座標と整合性を厳密に守る

Ankiカード
→ 現代語の意味・音・用法を軽く反復する

制作ノート
→ 学術上の留保と創作上の連想を接続する

Novel
→ 新しい交配を起こす
```

短縮形：

```text
歴史は、制作ノートに残す。
座標は、台帳で守る。
縁は、Ankiで反復する。
交配は、Novelで起こす。
```

> 正確だが、説明しすぎない。緩やかだが、虚偽ではない。

---

## 7．18フィールド標準仕様

フィリピン語版の改修以降、次を標準構成とする。

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

言語別には`TargetLanguage`部分を次のように置換する。

```text
Filipino
ExampleFilipino

Indonesian
ExampleIndonesian

Vietnamese
ExampleVietnamese
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

### ExampleBreakdown

例文を意味のまとまりごとに分ける。

```text
語句A＝日本語
語句B＝日本語
語句C＝日本語
```

### ExampleExplanation

次を専門用語に寄りすぎず説明する。

```text
語句の役割
助詞・標識・リンカー
動詞の形
接辞
修飾関係
語順
省略された要素
日本語として自然にするための並べ替え
```

> 「なぜこの日本語訳になるのか」が初学者に腹落ちすることを優先する。

---

## 8．フィリピン語版Core10の18フィールド化

### デッキ

```text
MEMORIOPOLIS::Filipino
```

### ノートタイプ

```text
MEMORIOPOLIS Filipino Vocabulary
```

### 改修ZIP

```text
MEMORIOPOLIS_Filipino_Core10_draft02_18fields_2026-09-18.zip
```

### 追加フィールド

```text
13 ExampleBreakdown
14 ExampleExplanation
```

### 現在地

```text
既存ノートタイプへ2フィールド追加     完了
裏面テンプレートへ表示欄追加           完了
CSS追加                                完了
18列版CSVインポート                    完了
18フィールド拡張                       完了
```

### 改修後の重点

```text
ang
ng
sa
na / -ng リンカー
動詞接辞
語順
文脈に応じた日本語訳
```

音韻説明を削ったのではない。

```text
維持：
Pronunciation
PerceptualSegmentation
SoundBridge

追加：
ExampleBreakdown
ExampleExplanation
```

> 音韻の橋に、統語と文法の橋を並べた。

---

## 9．インドネシア語版Novel draft01

### ファイル

```text
section12_id_draft01.md
```

### 章題

```text
Bab Empat: “Penerjemah”
```

### 節題

```text
Bagian Dua Belas: “Balasan Tanpa Tujuan”
```

### 位置づけ

```text
Anki Core10制作の母体となる第一稿
→ 作成済み

日本語正本との全文一対一照合
→ 未実施

公開用の完全版
→ 今後ブラッシュアップ
```

注意：

> 現在のdraft01は主要場面とCore10用例を含むが、日本語正本の後半を一部圧縮している。公開正本にする前に段落単位で全文照合し、省略された描写と対話を戻す。

---

## 10．インドネシア語版Anki Core10

### ZIP

```text
MEMORIOPOLIS_Indonesian_Core10_draft01_18fields_2026-09-18.zip
```

### デッキ

```text
MEMORIOPOLIS::Indonesian
```

### ノートタイプ

```text
MEMORIOPOLIS Indonesian Vocabulary
```

### Core10

```text
C0001  catatan          記録
C0002  ingatan          記憶
C0003  kota             都市
C0004  pemberitahuan    通知
C0005  balasan          返信／返答
C0006  tujuan           宛先／行き先
C0007  tanda tangan     署名
C0008  verifikasi       検証
C0009  wewenang         権限
C0010  peran            役割／ロール
```

### 収録ファイル

```text
id_core10_master_draft01_18fields.csv
id_core10_anki_draft01_18fields.csv
README_id_core10_draft01.md
INDONESIAN_NOTE_TYPE_DRAFT01_18FIELDS.md
INDONESIAN_CARD_TEMPLATE_DRAFT01.md
section12_id_draft01.md
```

### 語形成の観測例

```text
catat
→ 記録する

catat + -an
→ catatan
→ 記録されたもの／記録
```

```text
ingat
→ 覚えている

ingat + -an
→ ingatan
→ 記憶
```

```text
balas
→ 返す／応じる

balas + -an
→ balasan
→ 返答／返信

balasan + -nya
→ balasannya
→ その返信
```

```text
tuju
→ 向かう

tuju + -an
→ tujuan
→ 向かう先／目的
```

### 例文解説の観測対象

```text
yang
-nya
di-
meN-
peN-
-lah
bahwa
sudah
akan
名詞の後置修飾
受動形
```

### 導入手順

```text
1. MEMORIOPOLIS::Indonesianを作成
2. MEMORIOPOLIS Indonesian Vocabularyを作成
3. 18フィールドを作成
4. 表面テンプレートを設定
5. 裏面テンプレートを設定
6. 完成版CSSを設定
7. id_core10_anki_draft01_18fields.csvをインポート
8. PC版で単語TTSを確認
9. PC版で例文TTSを確認
10. AnkiWebへ同期
11. AnkiDroidで確認
```

---

## 11．インドネシア語Windows環境

### 導入済み

```text
Language.Basic~~~id-ID~0.0.1.0
→ Installed

Language.TextToSpeech~~~id-ID~0.0.1.0
→ Installed

Language.Handwriting~~~id-ID~0.0.1.0
→ NotPresent
→ 今回は不要
```

PowerShellの最終確認画面で、BasicとTextToSpeechの`Installed`を確認済み。

### TTS

```html
<div class="tts-audio">
  {{tts id_ID:Indonesian}}
</div>
```

```html
<div class="tts-audio">
  {{tts id_ID:ExampleIndonesian}}
</div>
```

音声名`Andika`は固定しない。

### 運用

```text
Windows標準TTS
→ PC版Ankiで確認

AnkiWeb同期
→ カードとテンプレートを同期

AnkiDroid
→ Android側でも実機確認
```

---

## 12．次の言語：ベトナム語

### 言語名

```text
日本語：ベトナム語
現地語：Tiếng Việt
```

### デッキ予定

```text
MEMORIOPOLIS::Vietnamese
```

### ノートタイプ予定

```text
MEMORIOPOLIS Vietnamese Vocabulary
```

### タグ予定

```text
memoriopolis::vi::core10
```

### TTS予定

```html
<div class="tts-audio">
  {{tts vi_VN:Vietnamese}}
</div>
```

```html
<div class="tts-audio">
  {{tts vi_VN:ExampleVietnamese}}
</div>
```

音声名は固定しない。

---

## 13．ベトナム語Windows環境の確認結果

管理者PowerShellで、次を実行済み。

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~vi-VN~'
} |
Select-Object Name, State
```

実機の結果：

```text
Language.Basic~~~vi-VN~0.0.1.0          NotPresent
Language.Handwriting~~~vi-VN~0.0.1.0    NotPresent
Language.TextToSpeech~~~vi-VN~0.0.1.0   NotPresent
```

判定：

```text
Basic
→ 提供あり
→ 未導入
→ 導入対象

TextToSpeech
→ 提供あり
→ 未導入
→ 導入対象

Handwriting
→ 提供あり
→ 未導入
→ 今回は不要
```

ベトナム語はWindows標準TTSを利用できる見込みである。

---

## 14．自宅でのベトナム語導入手順

### 事前準備

```text
1. 自宅Wi-Fiへ接続
2. OneDrive同期を一時停止
3. 管理者モードでPowerShellを起動
```

VS Code統合ターミナルを使う場合は、VS Code全体を管理者として起動する。通常作業では管理者権限を使わず、言語パック導入時だけ使用する。

### Step 1：Basicを導入

```powershell
Add-WindowsCapability -Online -Name "Language.Basic~~~vi-VN~0.0.1.0"
```

完了してPowerShellプロンプトが戻るまで待つ。

処理中の注意：

```text
VS CodeまたはPowerShellを閉じない
ターミナルを削除しない
同じコマンドを再実行しない
Ctrl+Cを押さない
スリープさせない
Wi-Fiを切断しない
```

### Step 2：TextToSpeechを導入

Basic完了後に実行する。

```powershell
Add-WindowsCapability -Online -Name "Language.TextToSpeech~~~vi-VN~0.0.1.0"
```

BasicとTextToSpeechを同時実行しない。

### Step 3：最終確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~vi-VN~'
} |
Select-Object Name, State
```

期待する最終状態：

```text
Language.Basic~~~vi-VN~0.0.1.0          Installed
Language.Handwriting~~~vi-VN~0.0.1.0    NotPresent
Language.TextToSpeech~~~vi-VN~0.0.1.0   Installed
```

### Step 4：終了

```text
RestartNeededを確認
↓
必要な場合だけ再起動
↓
OneDrive同期を再開
```

---

## 15．ベトナム語版で観測するもの

同じラテン文字系でも、フィリピン語・インドネシア語とは異なる観測面になる。

```text
追加文字
→ ă â đ ê ô ơ ư

声調記号
→ 音節の声調を表す

母音記号
→ 母音の質を区別する

音節
→ 比較的明確な音節単位

語構造
→ 接辞中心ではなく、別の語形成・複合・語順を観測
```

重要：

```text
母音の文字
＋
母音記号
＋
声調記号
```

は別の情報を担う。

ベトナム語版では、少なくとも次を区別する。

```text
OrthographicAnchor
→ 綴りに現れる追加文字と記号

Pronunciation
→ IPAまたは学習用発音表示

Tone
→ 声調

PerceptualSegmentation
→ 音節としてどう捉えるか

ExampleBreakdown
→ 語句単位の意味

ExampleExplanation
→ 語順と機能語から日本語訳へ至る過程
```

18フィールドを基本とするが、声調情報を独立フィールドにする必要があるかは、NovelとCore10作成時に判断する。

---

## 16．第十三節からのフィールド負荷試験順

```text
1  現代日本語 ⇄ 近代日本語
2  臺灣華語
3  韓国語
4  ロシア語
5  英語
6  フィリピン語
7  インドネシア語
8  ベトナム語
9  スペイン語
10 ポルトガル語
11 イタリア語
12 フランス語
13 ドイツ語
```

これは言語の優劣や重要度ではなく、JANUS-13型Ankiの観測フィールドを段階的に負荷試験する順序である。

---

## 17．次回の作業順

### まず、インドネシア語Anki

```text
1. デッキを作成
2. ノートタイプを作成
3. 18フィールドを作成
4. 表面テンプレートを設定
5. 裏面テンプレートを設定
6. CSSを設定
7. CSVをインポート
8. PC版TTSを確認
9. 例文の分解を確認
10. 「なぜこの意味になるか」を確認
11. 語根・接辞表示を確認
12. AnkiWebへ同期
13. AnkiDroidで確認
```

### 次に、ベトナム語環境

```text
1. 自宅Wi-Fi
2. OneDrive停止
3. 管理者PowerShell
4. vi-VN Basic導入
5. vi-VN TextToSpeech導入
6. Installed確認
7. 必要時のみ再起動
8. OneDrive再開
```

### その後、ベトナム語制作

```text
1. 第四章第十二節のベトナム語版Novel
2. C0001～C0010の対応語
3. 母音記号と声調
4. 音節と知覚上の区切り
5. 例文の分解
6. なぜこの日本語訳になるか
7. 意味の橋
8. 音の橋
9. Anki用CSV
10. カードテンプレートとCSS
11. ZIP化
12. PC版Anki
13. AnkiWeb
14. AnkiDroid
```

---

## 18．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月18日の最新状態として、MEMORIOPOLIS / JANUS-13の制作を再開します。

フィリピン語版Core10は18フィールド版へ拡張済みです。追加したフィールドはExampleBreakdownとExampleExplanationで、例文を意味のまとまりへ分解し、標識・リンカー・動詞形・語順から「なぜこの日本語訳になるのか」を初学者向けに説明します。音韻・語形成フィールドは維持しています。

インドネシア語版Novel draft01と、18フィールド版Anki Core10は作成済みです。ZIP名はMEMORIOPOLIS_Indonesian_Core10_draft01_18fields_2026-09-18.zipです。デッキ名はMEMORIOPOLIS::Indonesian、ノートタイプ名はMEMORIOPOLIS Indonesian Vocabularyです。

Windowsでは、Language.Basic~~~id-ID~0.0.1.0とLanguage.TextToSpeech~~~id-ID~0.0.1.0がInstalledです。まずインドネシア語版Ankiを導入し、PC版で単語と例文のTTS、例文分解、なぜこの意味になるか、語根・接辞の表示を確認してください。その後、AnkiWebとAnkiDroidへ同期します。

ベトナム語vi-VNについては、Language.Basic~~~vi-VN~0.0.1.0、Language.Handwriting~~~vi-VN~0.0.1.0、Language.TextToSpeech~~~vi-VN~0.0.1.0が実機に存在し、現在はいずれもNotPresentです。自宅Wi-FiでOneDriveを停止し、管理者PowerShellからBasic、次にTextToSpeechの順で導入してください。Handwritingは不要です。

ベトナム語版では、追加文字、母音記号、声調記号、音節を学習アンカーとして扱います。歴史文字は通常カードへ追加しません。18フィールドを基本に、声調を独立フィールドにする必要があるかをNovelとCore10の制作時に判断してください。

JANUS-13では、歴史は制作ノートに残し、座標はConcept Registryで守り、縁はAnkiで反復し、交配はNovelで起こします。正確だが説明しすぎない「疎な精密さ」を維持してください。
```

---

## 19．2026年9月18日の店じまい地点

```text
MEMORIOPOLIS親デッキ                     六言語面が開通
韓国語Core10                             運用中
ロシア語Core10                           運用中
臺灣華語Core10                           運用中
英語Core10                               運用中
近代日本語Core10                         運用中
フィリピン語Core10                       運用中
フィリピン語18フィールド拡張             完了
フィリピン語ExampleBreakdown              追加完了
フィリピン語ExampleExplanation            追加完了
インドネシア語Novel draft01              作成済み
インドネシア語Core10 ZIP                 作成済み
インドネシア語18フィールド               作成済み
インドネシア語Basic                      Installed
インドネシア語TextToSpeech               Installed
インドネシア語Handwriting                NotPresent、不要
インドネシア語Anki導入                   次回
インドネシア語PC版TTS確認                次回
インドネシア語AnkiDroid確認              次回
ベトナム語Capability確認                 完了
ベトナム語Basic                          提供あり、NotPresent
ベトナム語TextToSpeech                   提供あり、NotPresent
ベトナム語Handwriting                    提供あり、NotPresent、不要
ベトナム語言語パック導入                 自宅Wi-Fiで実施
ベトナム語Novel                          次工程
ベトナム語Core10                         次工程
Core20                                  第四章第十三節
Core30                                  序章
Concept Registry                        導入予定
制作ノート                               継続整備
旧note機関庫アーカイブ                    方針確定
中央駅発車掲示板                         先発・次発・後発の三本
Anki音声                                 音声名を固定せず移植性優先
文字採用原則                             現代の学習アンカーを優先
カード設計原則                           疎な精密さ
```

本日の到達点：

> フィリピン語Ankiの実使用から、音韻と語形成だけでは初学者が例文の意味へ到達しにくいことが判明した。そこで、語句分解と「なぜこの意味になるか」を加え、JANUS-13の標準カードを18フィールドへ拡張した。インドネシア語版はこの改善を最初から受け継ぎ、Windowsの音声環境も開通した。次のベトナム語では、ラテン文字上に重なる母音記号と声調記号を新たな学習アンカーとして観測する。


---

## 20．作業時の安全チェックリスト

### Windows言語機能の導入前

```text
対象言語コードを実機で確認する
Capability名を推測だけで決めない
Basicが存在することを確認する
TextToSpeechが存在することを確認する
OneDrive同期を一時停止する
安定したWi-Fiへ接続する
ノートPCを電源へ接続する
スリープを無効化する
管理者PowerShellを使う
```

### 導入中

```text
同じコマンドを二重実行しない
BasicとTextToSpeechを並行実行しない
Operation Runningが続いても中断しない
Ctrl+Cを押さない
ターミナルを閉じない
VS Codeを終了しない
ネットワークを切断しない
```

### 導入後

```text
PowerShellプロンプトが戻ったことを確認する
RestartNeededを確認する
Get-WindowsCapabilityでInstalledを確認する
必要な場合だけ再起動する
OneDrive同期を再開する
通常作業は通常権限のVS Codeへ戻す
```

---

## 21．Anki導入時の共通チェックリスト

### 新規言語デッキ

```text
デッキ名を作成
ノートタイプ名を作成
フィールド数を確認
フィールド順を確認
表面テンプレートを設定
裏面テンプレートを設定
完成版CSSを設定
CSVの文字コードを確認
列対応を確認
インポート件数を確認
```

### 更新版CSV

```text
Ankiのバックアップを取る
既存ノートタイプへ追加フィールドを作る
テンプレートへ追加フィールドの表示欄を作る
CSSを追加する
更新版CSVをインポートする
第1フィールドのIDで既存ノートを照合する
重複カードを作らず既存ノートを更新する
カード件数が増えていないことを確認する
新フィールドが表示されることを確認する
```

### TTS

```text
単語の再生ボタンを確認
例文の再生ボタンを確認
PC版で言語が正しく選ばれることを確認
AnkiWebへ同期
AnkiDroidへ同期
AnkiDroidで単語と例文を再生
音声エンジンの選択が出た場合は対象言語を選ぶ
```

### 内容確認

```text
見出し語と日本語の対応
例文と日本語訳の対応
語根と接辞
知覚上の区切り
形態の橋
例文の分解
なぜこの意味になるか
意味の橋
音の橋
Source
CourseTags
```

---

## 22．品質基準

今後のカードは、次の問いに答えられる状態を目指す。

```text
この語は何を意味するか
本文ではどの意味で使われるか
どこが語根か
どの部分が接辞か
どのように音を区切ると聞き取りやすいか
例文はどの意味単位へ分けられるか
機能語・標識・語順がどう働くか
なぜ日本語ではこの順序と表現になるか
似た日本語Conceptとどこが重なり、どこが異なるか
音声では文字とどう違って聞こえるか
```

説明は長文化を目的にしない。

> 初学者がカードを一度読み、次に音声を聞いたとき、語の形と文の関係を一つ多く見つけられることを品質基準とする。

---

## 23．最終再開地点

次回は、ベトナム語Novelから始めない。最初にインドネシア語版Ankiを実機へ導入し、18フィールド設計がフィリピン語版の改善を正しく継承しているか確認する。

```text
第一段階
→ インドネシア語Anki導入
→ PC版TTS
→ 例文解説
→ AnkiDroid

第二段階
→ 自宅Wi-Fi
→ ベトナム語Basic
→ ベトナム語TextToSpeech
→ Installed確認

第三段階
→ ベトナム語Novel
→ ベトナム語Core10
→ 声調と母音記号のフィールド設計
```

この順序を維持する。
