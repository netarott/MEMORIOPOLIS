# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

---

# 2026年10月4日追補：French Core20・川越散歩・実装再開

## 78．2026年10月3日から10月4日までの進行

フランス語Core20は当初予定から一日遅れたが、遅延として否定的に扱わない。

2026年10月3日は「小江戸」と呼ばれる川越を歩き、次の場所を訪れた。

```text
喜多院
仙波東照宮
川越氷川神社
```

この散歩では、武家文化と結び付いた仏教、自然を軸とする神道、徳川家との歴史的接続が、同じ街の中で重なって見えた。

一つの制度や宗教だけで説明するのではなく、複数の信仰、政治、自然観、都市空間が重なって現在の風景を作っているという実地経験になった。

この経験は、MEMORIOPOLISの基本思想と整合する。

```text
一つの場所
  ↓
複数の歴史層
複数の制度
複数の物語
複数のConcept
  ↓
現在の知覚が変わる
```

制作を行わない日にも、復習デッキで約7語の想起練習を行った。

```text
新規制作を休む
≠
記憶都市が止まる

街を歩く
＋
既存カードを再訪する
＝
現実側から都市を育てる
```

---

## 79．フランス語Core10の正式19フィールド

元ファイル：

```text
fr_core10_master.csv
fr_core10_anki.csv
```

両ファイルの実フィールド数は18であり、フィールド名と順序は一致していた。

正式19フィールド：

```text
1. ID
2. French
3. Pronunciation
4. Japanese
5. PartOfSpeech
6. UsageNote
7. ExampleFrench
8. ExampleJapanese
9. Root
10. Affixes
11. PerceptualSegmentation
12. MorphologicalBreakdown
13. ExampleBreakdown
14. ExampleExplanation
15. MeaningBridge
16. SoundBridge
17. Source
18. CourseTags
19. ConceptScene
```

完成ファイル：

```text
MEMORIOPOLIS_French_Core10_19fields_2026-10-04.zip
fr_core10_master_19fields.csv
fr_core10_anki_19fields.csv
```

ConceptScene：

```text
C0001 memoriopolis_c0001_record.webp
C0002 memoriopolis_c0002_memory.webp
C0003 memoriopolis_c0003_city.webp
C0004 memoriopolis_c0004_notification.webp
C0005 memoriopolis_c0005_reply.webp
C0006 memoriopolis_c0006_recipient.webp
C0007 memoriopolis_c0007_signature.webp
C0008 memoriopolis_c0008_verification.webp
C0009 memoriopolis_c0009_authorization.webp
C0010 memoriopolis_c0010_role.webp
```

---

## 80．フランス語音優先型UI

完成ファイル：

```text
FRENCH_CARD_UI_19FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-10-04.md
```

### 80.1 表面

```text
ÉCOUTEZ D’ABORD
まず音を聞き、心の中でConceptを探す
```

```html
{{tts fr_FR:French}}
```

経路：

```text
単語音声
  ↓
Concept候補
  ↓
ConceptScene
  ↓
綴り
  ↓
発音・音の切れ目
```

### 80.2 裏面

```text
ÉCOUTEZ LA PHRASE
例文の音から、見出し語と文意を探す
```

```html
{{tts fr_FR:ExampleFrench}}
```

経路：

```text
日本語Concept
  ↓
例文音声
  ↓
見出し語と文意を予測
  ↓
例文・日本語訳
  ↓
語構成・用法・言語間ブリッジ
```

### 80.3 フランス語固有の観測点

```text
リエゾン
アンシェヌマン
エリジオン
鼻母音
発音されない語末子音
リズムグループ
```

単語単独と例文内の音を分けて観測する。

3段プルダウンは次を維持する。

```text
語の構造
例文解説
言語間ブリッジ
```

`id="answer"`によるAnkiDroidの自動スクロールも維持する。

TTSが再生できない場合は、推測でvoice IDを変更せず、`{{tts-voices:}}`で端末が返した値を採用する。

---

## 81．E0001フランス語版 canonical

完成ファイル：

```text
E0001_fr.md
```

タイトル：

```text
De « romaru » aux Roms
```

2026年10月4日、ユーザー確認によりcanonicalとして確定した。

```yaml
language: fr
status: canonical
canonical_source: E0001_ja.md
core_range: C0011-C0020
```

中心命題：

```text
Les êtres humains ne perdent pas le sol sous leurs pieds.
Ils changent seulement la terre à laquelle ils se relient.
```

結末：

```text
Je n’ai pas trouvé le sens de ce mot.
Malgré cela, ce mot avait ouvert un chemin.
```

Concept上の区別：

```text
le sol sous leurs pieds
＝ 足元の物理的な地面

la terre à laquelle ils se relient
＝ 接続先・生活基盤としての土地
```

フランス語版は逐語訳ではなく、フランス語として自然な段落運動を優先しつつ、未知語、記憶、土地、移動、プラットフォームへ進む思考経路を保持する。

E0001のcanonical状況：

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
E0001_ko.md          canonical
E0001_ru.md          canonical
E0001_fil.md         canonical
E0001_id.md          canonical
E0001_vi.md          draft
E0001_fr.md          canonical
```

ベトナム語のみ、内容の最終確認とcanonical化が未完了。

---

## 82．French Core20

完成パッケージ：

```text
MEMORIOPOLIS_French_E0001_Core20_19fields_2026-10-04.zip
```

収録ファイル：

```text
E0001_fr.md
fr_core20_master_19fields.csv
fr_core20_anki_19fields.csv
README.md
```

AnkiDroidへ同期済み。

### 82.1 見出し語

```text
C0011 exister        ある
C0012 faire          する
C0013 avoir          持つ
C0014 envoyer        送る
C0015 recevoir       受け取る
C0016 entendre       聞く
C0017 chercher       調べる
C0018 se déplacer    移る
C0019 se relier      結びつく
C0020 être lié       縛られる
```

Source：

```text
E0001_fr
```

CourseTags：

```text
memoriopolis::fr::core20
```

### 82.2 候補空間

C0011：

```text
il y a
＝ ある・いると提示する

exister
＝ 存在する、実在する、存続する
```

C0013：

```text
avoir
＝ 所有・状態として持つ

tenir
＝ 手で保持する
```

C0016：

```text
entendre
＝ 音が耳に入る、聞こえる

écouter
＝ 意識して耳を傾ける
```

E0001の偶然聞こえた未知語には`entendre`を採用する。

C0017：

```text
chercher
＝ 探す、意味や答えを求める

trouver
＝ 結果として見つける

vérifier
＝ 確認する

étudier
＝ 学習・研究する
```

C0018：

```text
se déplacer
＝ 場所・焦点が移る

passer à
＝ 話題・段階を次へ移す
```

C0019：

```text
se relier à
＝ 結びつく

être relié à
＝ 接続された状態

s’associer à
＝ 観念・記憶の中で連想される
```

C0020：

```text
être lié à
＝ 関係づけられている、縛られている

être attaché à
＝ 物理的・心理的に結び付いている

être contraint
＝ 強制されている
```

### 82.3 音の観測

```text
exister     /ɛɡ.zis.te/
envoyer     /ɑ̃.vwa.je/
recevoir    /ʁə.sə.vwaʁ/
entendre    /ɑ̃.tɑ̃dʁ/
se relier   /sə ʁə.lje/
être lié    /ɛtʁ lje/
```

最初から綴りを完全回収する必要はない。

```text
鼻母音
音節数
語末の響き
音の連結
  ↓
ConceptSceneへ到達
```

を初期目標とする。

---

## 83．AnkiDroid同期後の確認項目

フランス語Core10・Core20はAnkiDroidへ同期済み。

次回の最初に、実機結果を確認する。

```text
単語TTS
例文TTS
ConceptScene
フランス語綴り
IPA
リエゾン
アンシェヌマン
エリジオン
鼻母音
語末子音
3段プルダウン
自動スクロール
ダークモード
```

重点カード：

```text
C0001 Core10先頭カード
C0011 exister
C0016 entendre
C0019 se relier
C0020 être lié
```

TTS：

```html
{{tts fr_FR:French}}
{{tts fr_FR:ExampleFrench}}
```

エラー時：

```html
{{tts-voices:}}
```

---

## 84．Novel・Essay・Paper・実装の横断を継続する

今回の川越散歩は、制作遅延ではなく、現実世界からConceptを受け取る時間だった。

MEMORIOPOLISでは、次を直線工程にしない。

```text
Novel
Essay
Paper
Anki実装
街歩き
読書
統計
内省
```

これらは相互に行き来する。

```text
街を歩く
  ↓
異なる歴史層と制度の重なりを見る
  ↓
EssayやNovelのConceptが変わる
  ↓
Ankiの候補空間が豊かになる
  ↓
Paperの仮説が精密になる
  ↓
再び現実を見る窓が増える
```

Novel・Essay・Paperは、JANUS-18実装の外側にある成果物ではない。

```text
Novel
＝ Conceptを物語として経験させる

Essay
＝ 日常経験からConceptを抽出する

Paper
＝ 仮説と実装結果を検証可能な形へ整える

JANUS-18
＝ 音、画像、言語、間隔反復を用いて仮説を身体的に試す
```

この循環を、MEMORIOPOLISの正式な制作方法として維持する。

---

## 85．次回作業

既定の進行順では、フランス語の次はドイツ語。

```text
フィリピン語
  ↓
インドネシア語
  ↓
ベトナム語
  ↓
フランス語
  ↓
ドイツ語
  ↓
イタリア語
  ↓
スペイン語 es-ES
  ↓
ポルトガル語 pt-BR
```

次回手順：

```text
1. フランス語AnkiDroid実機確認結果を反映
2. ベトナム語E0001のcanonical判断
3. German Core10の実フィールドマスターを取得
4. 実フィールド名と順序を確認
5. ConceptSceneを末尾に追加
6. ドイツ語音優先型UIを作成
7. de_DE TTSをAnkiDroidで確認
8. E0001ドイツ語版を作成
9. 内容確認後にcanonical化
10. German Core20を作成
```

ドイツ語音優先型で観測する候補：

```text
複合語の切れ目
接頭辞
分離動詞
語末子音
長短母音
文中の動詞位置
```

---

## 86．次回開始用プロンプト

```text
この引き継ぎ書を2026年10月4日の最新状態として、MEMORIOPOLIS / JANUS-18を再開します。

E0001_fr.mdはcanonicalです。French Core10とCore20は正式19フィールドで完成し、AnkiDroidへ同期済みです。最初にfr_FRの単語TTS、例文TTS、ConceptScene、リエゾン、アンシェヌマン、エリジオン、3段プルダウン、自動スクロール、ダークモードの実機確認結果を反映してください。

E0001_vi.mdは現在draftです。内容確認後にcanonical化します。

インドネシア語TTSの正本は、in_IDとcom.google.android.tts-id-id-x-dfz-localの明示指定です。

音優先型UIをLIVING-13の標準とします。多言語勘は、Conceptと場面から少数の良い候補を立ち上げ、文脈で順位付けし、必要部分だけ変形する能力として育てます。

2026年10月3日の川越散歩では、喜多院、仙波東照宮、川越氷川神社を訪れ、仏教、神道、武家文化、自然観、徳川家の歴史が同じ都市空間で重なることを観察しました。制作しない日も現実側からMEMORIOPOLISを育てる日として扱います。

Novel、Essay、Paper、Anki実装、街歩き、読書、統計、内省を自由に横断しながらMEMORIOPOLISを整備します。

問題がなければ、次言語であるドイツ語へ進みます。最初にGerman Core10の実フィールドマスターを確認してください。
```

---

## 87．2026年10月4日の店じまい地点

- 川越散歩：喜多院、仙波東照宮、川越氷川神社を訪問。
- 復習デッキ：約7語の想起練習を実施。
- French Core10：正式19フィールド化。
- ConceptScene：C0001からC0010へ追加。
- フランス語音優先型UI：完成。
- `E0001_fr.md`：canonical確定。
- French Core20：完成。
- French Core10・Core20：AnkiDroidへ同期済み。
- 次回最初：フランス語実機音声確認。
- ベトナム語E0001：draftのまま。
- 次言語：ドイツ語。
- 制作遅延：否定的に扱わない。
- 街歩き：現実側からConceptを増やすフィールドワークとして扱う。
- Novel・Essay・Paper・Anki実装：自由に横断する。
- MEMORIOPOLIS：現実から信号を受け取り、別の窓を通して現実へ戻す都市として整備する。

最終整理：

> 一日分の実装が遅れても、街を歩き、歴史層と信仰の重なりを見て、七つの語を想起したなら、記憶都市は止まっていない。Novel、Essay、Paper、Anki実装、街歩きは別々の作業ではなく、同じ都市を異なる窓から育てる営みである。フランス語という新しい窓が開いた現在、その音を通して同じConceptがどのように別の輪郭を持つかを観測し、次のドイツ語へ進む。
