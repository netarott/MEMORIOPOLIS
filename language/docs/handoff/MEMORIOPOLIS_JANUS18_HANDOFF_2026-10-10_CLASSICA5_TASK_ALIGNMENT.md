# MEMORIOPOLIS / JANUS-18 引き継ぎ書・次期タスク設計

**作成日:** 2026-10-10  
**位置づけ:** CLASSICA-5着手前の意識合わせ確定版  
**次回開始点:** 実機確認を閉じた後、E0002ロシア語ではなくCLASSICA-5共通設計へ進む

---

## 0. 本書の目的

本書は、2026年10月10日の再開時に確認した現在地と、次に進むべきタスクの順序を記録する。

本日は制作物を増やす日ではなく、以下の重要な意識合わせを行った。

- E0001のLIVING-13は完了している
- CLASSICA-5の開始条件は満たされている
- E0002の現代語横展開を機械的に続ける前に、古典語の縦方向へ進む
- ModernJapaneseを現代語と古典語の橋として使う
- C0001からC0020を古典語へ無理に直訳せず、対応の深さを判定する
- CLASSICA-5共通Conceptマスターを先に作り、その後に五言語をCore20まで整備する
- CLASSICA-5完了後、E0002ロシア語へ戻る

---

## 1. 現在地

### 1.1 E0001

E0001はLIVING-13の全言語でcanonical化され、Anki Core20とMP3の展開も完了している。

```text
ModernJapanese / English / zh-Hant-TW / Korean / Russian
Filipino / Indonesian / Vietnamese / French / German
Italian / Spanish es-ES / Portuguese pt-BR
```

### 1.2 E0002

現在のcanonical展開：

```text
E0002_ja.md
E0002_en.md
E0002_zh-Hant-TW.md
E0002_ko.md
```

韓国語については次まで完了している。

```text
[x] E0002_ko.md canonical
[x] Korean Core30
[x] 韓国語音優先型UI
[x] ConceptScene破損箇所の手動修正
[x] E0002_ko.mp3
[x] AnkiWeb同期
[x] 統合Audio Circleへの追加
```

### 1.3 Audio Circle

正式プレイリスト：

```text
MEMORIOPOLIS｜JANUS-18 Audio Circle
```

運用原則：

```text
1 canonical Markdown = 1 MP3
Essayごとにプレイリストを分けない
すべてのEssay・言語を一つのAudio Circleへ統合する
シャッフル＋全曲リピートで聞く
```

前回確認時点：

```text
17トラック
約1時間40分
公開
統合カスタムカバー適用済み
```

---

## 2. 再開直後に閉じる確認事項

### 2.1 AnkiDroid

重点カード：

```text
C0021 결혼하다
C0027 양립하다
C0029 역할을 맡다
C0030 평가하다
```

確認項目：

- 単語音声がConceptSceneと文字より先に機能する
- 音からConceptを探す間がある
- ConceptSceneが正常表示される
- ハングルとRomanizationが読みやすい
- 解答時に`CONCEPT BRIDGE`へ移動する
- 例文音声が再生される
- 3段パネルが開閉する
- ダークモードで崩れない

### 2.2 Audio Circle

対象：

```text
E0001_pt-BR.mp3
E0002_ko.mp3
```

確認項目：

- ブラジル・ポルトガル語の自然さ
- 韓国語`-8%`の速度
- 韓国語固有語の読み
- Essay結末の余韻
- 他トラックとの音量差
- スマートフォン上の新カバー表示

重大な問題がなければ、Portuguese Core20とKorean Core30を正式完了とする。

---

## 3. 修正後の大きな制作順

本日の重要な修正は、次の制作対象をE0002ロシア語ではなく、CLASSICA-5としたことである。

```text
E0001 LIVING-13完了
  ↓
ModernJapanese Bridge確認
  ↓
C0001～C0020古典語適合性判定
  ↓
CLASSICA-5共通Conceptマスター
  ↓
CLASSICA-5をCore20まで整備
  ↓
横断確認・親デッキ統合
  ↓
E0002ロシア語へ復帰
```

---

## 4. CLASSICA-5

対象言語：

```text
1. Classical Latin
2. Ancient Greek
3. Classical Sanskrit
4. Biblical Hebrew
5. Classical Arabic
```

### 4.1 基本思想

CLASSICA-5は、現代語の訳語を古典語へ機械的に置換する企画ではない。

```text
LIVING-13
＝ 現代世界を横断する水平の円環

ModernJapanese
＝ 現代から過去へ降りる橋

CLASSICA-5
＝ 文明史の深層へ降りる垂直の円環
```

現代技術・法律・プラットフォーム用語は、無理に直訳しない。

```text
直接対応がない
  ↓
歴史的に近いConceptを探す
  ↓
意味の距離を明記する
  ↓
ModernJapaneseで橋を架ける
```

---

## 5. Task 1: CLASSICA-5共通仕様書

まず確定する項目：

```text
CLASSICA-5の役割
各言語の採用時代層
文字体系
転写体系
発音方針
Bridge AudioとClassical Depthの区別
Ankiフィールド構造
ConceptSceneの共有方法
現代語にしかないConceptの扱い
右横書き・特殊文字・発音記号への対応
```

### 5.1 採用時代層の原則

各古典語は、現代語への影響が大きかった時期、または文化史上の中心的な言語層を基準とする。

```text
Classical Latin
＝ 再建古典期ラテン語

Ancient Greek
＝ 再建アッティカ式を基準
  必要に応じてコイネー層を区別

Classical Sanskrit
＝ 古典サンスクリット
  ヴェーダ語は必要Conceptのみ別層

Biblical Hebrew
＝ 聖書ヘブライ語
  ティベリア式の母音・アクセントを意識

Classical Arabic
＝ 古典アラビア語
  現代標準アラビア語との差を明示
```

---

## 6. Task 2: ModernJapanese Bridgeの確認

日本語系Ankiの正本は、既定どおり次のみとする。

```text
MEMORIOPOLIS::ModernJapanese
```

現代日本語の独立Ankiデッキは作らない。

ModernJapaneseで確認するもの：

```text
Core10・Core20の近代日本語表現
旧字体と歴史的仮名遣い
音声用の読み
古典語Conceptへつなぐ説明
現代語と古典語の意味差
```

ModernJapaneseの役割：

```text
現代Concept
  ↓
近代日本語による意味の橋
  ↓
古典語の歴史層
```

---

## 7. Task 3: C0001～C0020古典語適合性マスター

各Conceptを四段階で判定する。

```text
Exact
＝ 古典語圏にほぼ同じConceptがある

Near
＝ 近いConceptはあるが意味領域が少し違う

Partial
＝ Conceptの一部だけが対応する

No direct equivalent
＝ 直接対応がなく、近縁Conceptで橋を架ける
```

### 7.1 古典語化しやすい候補

```text
C0002 記憶
C0003 都市
C0005 応答
C0006 受け手
C0007 署名
C0008 検証
C0009 許可・権限
C0010 役割
C0011 存在する
C0012 する
C0013 持つ
C0014 送る
C0015 受け取る
C0016 聞く
C0017 探す・調べる
C0018 移る・変える
C0019 結びつく
C0020 縛られる
```

### 7.2 再設計が必要な候補

```text
C0001 記録
C0004 通知
C0008 現代的な技術検証
C0009 現代的なシステム権限
```

近縁Conceptの例：

```text
記録
→ 書き留め、証言、記念、碑文

通知
→ 告知、布告、知らせ

検証
→ 試す、吟味する、証明する

権限
→ 許可、権威、委任された力
```

---

## 8. Task 4: CLASSICA-5共通Conceptマスター

言語別のCSVより先に、横断マスターを作る。

想定フィールド：

```text
ConceptID
ModernJapaneseBridge
ModernMeaning
ClassicalSuitability
LatinConcept
GreekConcept
SanskritConcept
HebrewConcept
ArabicConcept
CorrespondenceType
HistoricalNote
TranslationRisk
PronunciationLayer
ConceptScene
```

目的：

- 五言語を個別に翻訳して整合性を失うことを防ぐ
- 対応の強さと意味差を記録する
- 現代Conceptの押し付けを避ける
- 古典語間の共通点と差異を可視化する

---

## 9. Task 5～9: 五言語をCore20まで整備

推奨実装順：

```text
Task 5  Classical Latin Core10・Core20
Task 6  Ancient Greek Core10・Core20
Task 7  Classical Sanskrit Core10・Core20
Task 8  Biblical Hebrew Core10・Core20
Task 9  Classical Arabic Core10・Core20
```

この順序は重要度ではなく、技術的難度を段階的に上げるための順序である。

各言語で作るもの：

```text
Core10 master CSV
Core10 Anki CSV
Core20 master CSV
Core20 Anki CSV
音優先Note UI
文字・転写・発音方針
Concept境界
README
```

CLASSICA-5では、公開Essay全文を無理に五言語化しない。

```text
Essay全文翻訳
＝ 必須ではない

Anki Core20
＝ 必須
```

---

## 10. CLASSICA-5の音声設計

古典語には唯一の現代ネイティブ発音が存在しないため、音声条件を必ず記録する。

```text
Bridge Audio
＝ 現代の学習者がConceptへ入る音声

Classical Depth
＝ 採用時代層と発音伝統を明示した音声
```

言語別方針：

```text
Classical Latin
＝ 再建古典式

Ancient Greek
＝ 再建アッティカ式
  必要に応じてコイネー式を別管理

Classical Sanskrit
＝ 古典サンスクリットの教育的朗読

Biblical Hebrew
＝ ティベリア式を意識した学習音声

Classical Arabic
＝ 古典アラビア語
  現代標準アラビア語との差を明記
```

音声品質が不十分な場合：

```text
暫定音声
検証用音声
人間朗読候補
```

を区別し、機械音声を歴史的正本として扱わない。

---

## 11. Task 10: CLASSICA-5横断確認

五言語整備後に確認すること：

```text
Concept IDの一貫性
ModernJapanese Bridgeとの接続
各言語の時代層
転写の一貫性
発音層の明示
ConceptSceneの共有
右横書き表示
AnkiDroidのTTS・レイアウト
親デッキMEMORIOPOLISでの横断復習
```

---

## 12. Task 11: E0002ロシア語へ復帰

CLASSICA-5 Core20完了後、E0002の現代語展開へ戻る。

```text
E0002_ru
  ↓
E0002_fil
  ↓
E0002_id
  ↓
E0002_vi
  ↓
E0002_fr
  ↓
E0002_de
  ↓
E0002_it
  ↓
E0002_es
  ↓
E0002_pt-BR
```

E0002ロシア語は中止ではなく、順序を後ろへ移した。

---

## 13. 次回の実作業順

明日は次の順で進む。

```text
1. 前回のAnkiDroid・Audio Circle確認結果を記録
2. CLASSICA-5共通仕様書を作成
3. ModernJapanese Bridge仕様を確定
4. C0001～C0020古典語適合性マスターを作成
5. CLASSICA-5共通Conceptマスターへ統合
6. Classical Latin Core10へ着手
```

一日で五言語を急いで完成させない。

```text
共通仕様
  ↓
Concept適合性
  ↓
横断マスター
  ↓
各言語実装
```

の順序を守る。

---

## 14. 設計上の不変原則

```text
GitHubのcanonical Markdown
＝ 文章正本

フィールドマスター
＝ Anki構造の正本

実在画像ファイル名
＝ ConceptScene参照の正本

ModernJapanese
＝ 現代と古典をつなぐ日本語Anki正本

1 canonical Markdown
＝ 1 MP3

Audio Circle
＝ Essayと言語を分けない統合音声環
```

CLASSICA-5でも、次を守る。

```text
直接対応がないConceptを無理に直訳しない
発音伝統を隠さない
現代語の意味を古典語へ押し付けない
対応の距離を記録する
実装結果から理論を修正する
```

---

## 15. 次回開始用プロンプト

```text
この引き継ぎ書を2026年10月10日の最新状態として、MEMORIOPOLIS / JANUS-18を再開します。

前回までにE0001のLIVING-13展開を完了し、E0002は日本語・英語・臺灣華語・韓国語までcanonical化しました。韓国語Core30、音優先UI、MP3、統合Audio Circleへの追加も完了しています。

次にE0002ロシア語へ進むのではなく、JANUS-18の当初構想どおりCLASSICA-5へ着手します。

最初に、前回のAnkiDroidとAudio Circleの実機確認結果を記録してください。その後、CLASSICA-5共通仕様書、ModernJapanese Bridge仕様、C0001～C0020古典語適合性マスター、CLASSICA-5共通Conceptマスターの順で作成してください。

CLASSICA-5はClassical Latin、Ancient Greek、Classical Sanskrit、Biblical Hebrew、Classical Arabicです。現代技術・法律用語は無理に直訳せず、Exact / Near / Partial / No direct equivalentで対応の深さを記録してください。

日本語系Ankiの正本はMEMORIOPOLIS::ModernJapaneseのみです。現代日本語の独立Ankiデッキは作成しません。

共通Conceptマスターが確定した後、Classical Latinから順に五言語をCore20まで整備します。CLASSICA-5完了後、E0002ロシア語へ戻ります。
```

---

## 16. 2026年10月10日の店じまい地点

```text
[x] 現在地の再確認
[x] E0002ロシア語を直近タスクとする案を修正
[x] CLASSICA-5開始条件が満たされていることを確認
[x] ModernJapanese Bridgeを先行させる方針を確認
[x] C0001～C0020の適合性判定を先行させる方針を確認
[x] CLASSICA-5共通Conceptマスター先行を確認
[x] 五言語の実装順を確認
[x] CLASSICA-5完了後にE0002ロシア語へ戻る方針を確認
[ ] 前回の実機確認結果を記録
[ ] CLASSICA-5共通仕様書
[ ] ModernJapanese Bridge仕様
[ ] C0001～C0020古典語適合性マスター
[ ] CLASSICA-5共通Conceptマスター
[ ] Classical Latin Core10
```

本日の最終合意：

> LIVING-13で現代世界を横断する円環が一周した今、MEMORIOPOLISはModernJapaneseを橋として、CLASSICA-5の歴史的深層へ降りる。古典語を現代語の置換先にせず、Conceptの起源、変化、欠落、意味の距離を観測する。横方向の多言語勘に、縦方向の歴史的時間を加える。
