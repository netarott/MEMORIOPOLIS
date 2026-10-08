# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書・運用設計書

**作成日:** 2026-10-08  
**対象:** Spanish Core20、臺灣華語 Core30、Core30 Concept画像、Essay音声同期、JANUS-18 Audio Circle  
**位置づけ:** 2026-10-08時点の実装状態と、今後も再利用する正式な運用設計の統合文書

---

## 0. 本書の目的

本書は、日次作業の引き継ぎだけでなく、今後のE0003以降、Core40以降、追加言語にも適用する運用設計を記録する。

本日時点で、MEMORIOPOLIS / JANUS-18の基本循環は次の形に固まった。

```text
個人的経験・観察
↓
日本語Essay canonical
↓
各言語の自然なEssay canonical
↓
EssayからConceptを選定
↓
言語別Ankiカード
↓
全言語共通ConceptScene
↓
Essay全体のMP3
↓
JANUS-18 Audio Circle
↓
AnkiDroidと長文音声による日常反復
```

システムの中心は、語彙数を増やすことではない。

```text
音
↓
Concept
↓
画像
↓
語
↓
例文
↓
Essay
↓
経験
```

を一つの記憶経路として接続することにある。

---

# Part I. 2026-10-08の実績

## 1. 本日の主な完了事項

```text
[x] English Core30へConcept画像を反映
[x] E0002_ja.mdのメタデータ修正
[x] E0002_ja.mp3生成
[x] MP3同期スクリプトの汎用化
[x] Spanishノートタイプを19フィールド化
[x] Spanish音優先UIを作成
[x] Spanish UIのConceptScene表示不具合を修正
[x] E0001_es.mdを作成
[x] E0001_es.mdをcanonical化
[x] Spanish Core20 C0011-C0020を作成
[x] Spanish Core20をAnkiへ登録
[x] AnkiDroidへ同期
[x] E0001_es.mp3生成
[x] E0002_zh-Hant-TW.mdを作成
[x] E0002_zh-Hant-TW.mdをcanonical化
[x] 臺灣華語Core30 C0021-C0030を作成
[x] 臺灣華語Core30をAnkiへ登録
[x] E0002_zh-Hant-TW.mp3生成
[x] 3本のMP3をYouTube Musicへアップロード
[x] JANUS-18 Audio Circleへ3本を追加
```

---

## 2. 本日追加したAudio Circle音源

```text
E0001_es.mp3           5:00
E0002_ja.mp3           7:32
E0002_zh-Hant-TW.mp3   4:52
```

追加先:

```text
MEMORIOPOLIS | JANUS-18 Audio Circle
```

画面確認時点:

```text
15トラック
合計1時間29分
```

再生リストはEssay別に分割せず、すべてのEssayと言語を横断する一つの音声環として維持する。

---

## 3. 今晩の実機確認事項

昼間は制作とアップロードまでとし、音声再生とAnkiDroidでの詳細確認は自宅で行う。

### 3.1 音声

```text
[ ] E0001_es.mp3の発音、速度、読み上げ範囲
[ ] E0002_ja.mp3の発音、速度、読み上げ範囲
[ ] E0002_zh-Hant-TW.mp3の臺灣華語としての自然さ
[ ] 制作ノート、脚注定義、メタデータが読み上げられていないか
[ ] 結末まで欠落なく収録されているか
[ ] Audio Circleのシャッフル再生
```

### 3.2 Anki

```text
[ ] Spanish Core20の単語TTS
[ ] Spanish Core20の例文TTS
[ ] Spanish Core20のConceptScene
[ ] Spanish Core20の3段パネル
[ ] 臺灣華語Core30の繁體字、注音、拼音
[ ] 臺灣華語Core30の例文TTS
[ ] 臺灣華語Core30のConceptScene
[ ] English Core30のConceptScene
[ ] Core30横長画像のスマートフォン表示
```

### 3.3 Core30画像の評価基準

Core30画像はCore10・Core20より横長である。現段階では作り直さず、実機で次を確認してから再検討する。

```text
画面幅への収まり
日本語見出しと短文の可読性
画像の縮小率
縦方向のスクロール量
Core10・Core20との視覚的一貫性
横長構図が記憶風景として有効か
```

---

# Part II. Essay設計

## 4. 正本の原則

正本はGitHub上のcanonical Markdownとする。

```text
GitHub canonical Markdown
= 内容、翻訳、Anki、MP3の起点
```

YouTube Music、Anki、MP3、CSVは派生物であり、正本ではない。

---

## 5. Essayディレクトリ

```text
MEMORIOPOLIS/
└─ essay/
   ├─ E0001/
   │  ├─ E0001_ja.md
   │  ├─ E0001_en.md
   │  ├─ E0001_es.md
   │  ├─ ...
   │  └─ audio_E0001_all/
   ├─ E0002/
   │  ├─ E0002_ja.md
   │  ├─ E0002_en.md
   │  ├─ E0002_zh-Hant-TW.md
   │  └─ audio_E0002_all/
   ├─ memoriopolis_audio_sync.py
   ├─ run_memoriopolis_audio_sync.ps1
   └─ MEMORIOPOLIS_essay_audio_manifest.json
```

原則:

```text
1 Essay = 1経験単位
1 Markdown = 1言語版
1 Markdown = 1 MP3
```

---

## 6. Essayメタデータ契約

### 6.1 必須項目

```yaml
essay_id: E0002
title: "もう一本の線路"
date: 2026-10-07
language: ja
status: canonical
source_type: personal_observation
location: 東京メトロ有楽町線・銀座一丁目駅以降の車内
core_range: C0021-C0030
```

翻訳版では必要に応じて次を追加する。

```yaml
locale: zh-TW
canonical_source: E0002_ja.md
reference_translation: E0002_en.md
```

### 6.2 キー名の規則

```text
正: essay_id
誤: essay\_id

正: source_type
誤: source\_type

正: core_range
誤: core\_range
```

メタデータのアンダースコアをMarkdown用にエスケープしない。

### 6.3 canonical判定

音声生成、Anki Source、翻訳派生の入力として使用できるのは次だけである。

```yaml
status: canonical
```

```text
status: draft01
status: draft02
```

は作業中であり、自動音声生成の対象にしない。

### 6.4 本文末の状態表記

先頭メタデータだけでなく、制作ノート末尾も実態に合わせる。

canonical化した後に、次を残さない。

```text
draft01
確認後にcanonicalへ変更
```

---

## 7. 翻訳設計

翻訳は逐語訳ではない。

```text
日本語canonicalの経験、論理、観察距離
＋
対象言語で自然なEssayの文体
＋
Concept境界
```

を統合する。

### 7.1 観察と推論

本文では、次を分離する。

```text
観察したこと
記憶していること
資料から確認したこと
作者の推論
制度に関する仮説
```

人物について、限られた言葉から人格、生活、関係を断定しない。

### 7.2 言語識別子

```text
日本語            ja
英語              en
臺灣華語          zh-Hant-TW
韓国語            ko
ロシア語          ru
フィリピン語      fil
インドネシア語    id
ベトナム語        vi
フランス語        fr
ドイツ語          de
イタリア語        it
スペイン語        es
ブラジル葡萄牙語  pt-BR
```

基準:

```text
Spanish: es-ES
Portuguese: pt-BR
Taiwanese Mandarin: zh-Hant-TW
```

---

# Part III. CoreとConcept設計

## 8. CoreとEssayの対応

現時点の主要対応:

```text
Core10  C0001-C0010
→ 記憶都市の基礎Concept

Core20  C0011-C0020
→ E0001「『ロマる』からロマへ」

Core30  C0021-C0030
→ E0002「もう一本の線路」
```

Core番号は語彙レベルではなく、Concept住所の追加順を表す。

---

## 9. Core20 Concept

```text
C0011 ある／存在する
C0012 する／作る
C0013 持つ
C0014 送る
C0015 受け取る
C0016 聞く／耳に入る
C0017 調べる／探す
C0018 移る／変える
C0019 結びつく／接続する
C0020 縛られる／結び付けられている
```

Spanish Core20:

```text
C0011 existir
C0012 hacer
C0013 tener
C0014 enviar
C0015 recibir
C0016 oír
C0017 buscar
C0018 cambiar
C0019 conectarse
C0020 estar atado
```

---

## 10. Core30 Concept

```text
C0021 結婚する
C0022 育てる
C0023 働く
C0024 引き継ぐ
C0025 戻る
C0026 守る
C0027 両立する
C0028 競争する
C0029 演じる
C0030 評価する
```

臺灣華語Core30:

```text
C0021 結婚
C0022 養育
C0023 工作
C0024 交接
C0025 回來
C0026 保障
C0027 兼顧
C0028 競爭
C0029 扮演
C0030 評價
```

---

## 11. Concept境界の原則

言語間で見出し語を機械的に一致させない。

```text
共通Concept
↓
各言語の自然な見出し語
↓
UsageNote / Grammar / MeaningBridgeで境界を説明
```

例:

```text
oír
→ 音が耳へ入る

escuchar
→ 意識して聞く
```

```text
conectarse
→ 接続へ入る動き

estar atado
→ 接続、依存、制約の中にある状態
```

```text
兼顧
→ 時間に応じて配分を変えながら複数の経路を守る

平衡
→ 均衡状態そのものを表しやすい
```

```text
評價
→ 基準に照らして価値や状態を検討する

評估
→ 状態や影響を分析的に見積もる

判定
→ 結論を下す含みが強い
```

---

# Part IV. ConceptScene設計

## 12. ConceptSceneの役割

ConceptSceneは装飾画像ではなく、Concept IDに対応する共通の記憶住所である。

```text
同じConcept ID
→ 全言語で同じConceptScene
```

言語ごとに画像を作り直さない。

---

## 13. ConceptSceneフィールド

Ankiでは、ConceptSceneフィールドに通常次が入る。

```html
<img src="memoriopolis_c0021_marry.webp">
```

テンプレート側では、画像フィールドをそのまま展開する。

```html
{{#ConceptScene}}
<div class="concept-scene">
  {{ConceptScene}}
</div>
{{/ConceptScene}}
```

次のように二重の`img`タグを作らない。

```html
<img src="{{ConceptScene}}">
```

フィールド内にすでに`img`タグがあるため、二重化すると画像が壊れる。

---

## 14. Concept画像パッケージ

正式パッケージは次の構成とする。

```text
MEMORIOPOLIS_ConceptImages_C####-C####_YYYY-MM-DD/
├─ README.md
├─ manifest.csv
├─ png/
│  └─ GitHub保存用PNG
└─ webp/
   └─ Anki用WebP
```

READMEを画像制作の入力仕様とする。

画像内の基本要素:

```text
Concept ID
日本語見出し
記憶用短文
```

英語見出しや特定言語の説明を入れず、全言語共有を維持する。

---

## 15. Core30画像

```text
C0021 memoriopolis_c0021_marry.webp
C0022 memoriopolis_c0022_raise.webp
C0023 memoriopolis_c0023_work.webp
C0024 memoriopolis_c0024_hand_over.webp
C0025 memoriopolis_c0025_return.webp
C0026 memoriopolis_c0026_protect.webp
C0027 memoriopolis_c0027_balance.webp
C0028 memoriopolis_c0028_compete.webp
C0029 memoriopolis_c0029_perform.webp
C0030 memoriopolis_c0030_evaluate.webp
```

Core30は横長構図で制作した。採否は今晩の実機確認後に再検討する。

---

# Part V. Anki設計

## 16. 共通学習順

言語別UIは、原則として次の順序とする。

```text
単語の音
↓
心の中でConcept候補を探す
↓
ConceptScene
↓
対象言語の表記
↓
発音情報
↓
日本語Concept
↓
例文の音
↓
例文と日本語訳
↓
語構造
↓
例文解説
↓
Concept Bridge
```

音優先の理由は、日々の学習経路を次へ近づけるためである。

```text
音 → 画像 → Concept → 語 → 例文
```

---

## 17. Spanishノートタイプ

ノートタイプ:

```text
MEMORIOPOLIS Spanish Vocabulary
```

19フィールド:

```text
01 ID
02 Spanish
03 Pronunciation
04 Japanese
05 PartOfSpeech
06 UsageNote
07 ExampleSpanish
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

TTS:

```html
{{tts es_ES:Spanish}}
{{tts es_ES:ExampleSpanish}}
```

3段パネル:

```text
1. ESTRUCTURA
2. GUÍA DE LA FRASE
3. PUENTE CONCEPTUAL
```

識別色:

```text
深紅、金、濃紺
```

---

## 18. 臺灣華語ノートタイプ

ノートタイプ:

```text
MEMORIOPOLIS Taiwanese Mandarin Vocabulary
```

17フィールド:

```text
01 ID
02 TraditionalChinese
03 Zhuyin
04 Pinyin
05 Japanese
06 PartOfSpeech
07 TaiwanMandarinGrammar
08 ExampleTraditionalChinese
09 ExampleZhuyin
10 ExamplePinyin
11 ExampleJapanese
12 Source
13 Tags
14 ExampleBreakdown
15 ExampleExplanation
16 ExamplePronunciationHint
17 ConceptScene
```

TTSロケール:

```text
zh_TW
```

識別子はファイル、メタデータ、Tagsで`zh-Hant-TW`を維持し、TTSのみ`zh_TW`を使う。

---

## 19. CSV設計

### 19.1 master CSV

```text
ヘッダーあり
GitHub保存用
編集・確認の正本
```

### 19.2 Anki CSV

```text
ヘッダーなし
Ankiインポート用
フィールド順をノートタイプと完全一致
```

### 19.3 SourceとTags

Spanish Core20:

```text
Source: E0001_es.md
CourseTags: memoriopolis::es::core20
```

臺灣華語Core30:

```text
Source: E0002_zh-Hant-TW.md
Tags: memoriopolis::zh-Hant-TW::core30
```

フィールド名は言語ごとの既存ノートタイプを優先し、他言語から推測して変更しない。

---

## 20. Ankiインポート手順

```text
1. 対象ノートタイプを選ぶ
2. 対象デッキを選ぶ
3. UTF-8を指定
4. カンマ区切り
5. HTMLを許可
6. ヘッダーなしCSVを読み込む
7. フィールド数と順序を照合
8. IDを確認
9. ConceptSceneを確認
10. 数枚プレビュー
11. AnkiWebへ同期
12. AnkiDroidでメディア同期
13. 実機確認
```

---

## 21. 日次新規カード

親デッキの新規上限:

```text
20枚
```

基本想定:

```text
Core20新規言語 10枚
＋
Core30新規言語 10枚
=
20枚
```

既存の新規カードや復習負荷が残る場合は、無理に同日表示させない。

---

# Part VI. MP3設計

## 22. 音声同期の基本仕様

正式スクリプト:

```text
essay/memoriopolis_audio_sync.py
essay/run_memoriopolis_audio_sync.ps1
```

通常運用:

```powershell
.\run_memoriopolis_audio_sync.ps1
```

または:

```powershell
py .\memoriopolis_audio_sync.py --root . --continue-on-error
```

基本動作:

```text
MP3がある
→ スキップ

MP3がない
→ canonical Markdownから生成

canonicalでない
→ 生成しない

未対応言語
→ スキップして報告
```

---

## 23. 特定ジョブ

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0002:ja
```

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0001:es
```

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0002:zh-Hant-TW
```

生成前確認:

```powershell
py .\memoriopolis_audio_sync.py --root . --dry-run
```

強制再生成:

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0002:ja --overwrite
```

`--overwrite`はVoice、速度、本文を変更して再生成するときだけ使う。

---

## 24. 出力構造

```text
E0002/E0002_ja.md
↓
E0002/audio_E0002_all/E0002_ja.mp3
E0002/audio_E0002_all/E0002_ja.srt
E0002/audio_E0002_all/E0002_ja.narration.txt
E0002/audio_E0002_all/E0002_ja.audio.json
```

結果は次にも記録する。

```text
essay/MEMORIOPOLIS_essay_audio_manifest.json
```

---

## 25. 読み上げ対象

読み上げる:

```text
Essay本文
本文内で実際に使われる語
```

読み上げない:

```text
先頭メタデータ
Markdown見出し
制作ノート
脚注定義
URL
コードブロック
Source行
```

脚注記号は本文から除去し、本文中の語自体は読む。

---

## 26. 現在の主要Voice設定

```text
ja           ja-JP-NanamiNeural       -3%
en           en-US-AndrewNeural        -6%
zh-Hant-TW   zh-TW-HsiaoChenNeural     -8%
ko           ko-KR-SunHiNeural         -8%
ru           ru-RU-SvetlanaNeural      -8%
fil          fil-PH-BlessicaNeural     -8%
id           id-ID-GadisNeural         -8%
vi           vi-VN-HoaiMyNeural        -10%
fr           fr-FR-DeniseNeural        -8%
de           de-DE-KatjaNeural         -5%
it           it-IT-ElsaNeural          -6%
es           es-ES-ElviraNeural        -6%
pt-BR        pt-BR-FranciscaNeural     -7%
```

Voiceが利用できない場合は、同一ロケール内の代替Voiceを選ぶ。

---

## 27. MP3生成時の確認

成功条件:

```text
[SUMMARY] generated=1 skipped=0 errors=0
```

既存MP3を正しくスキップした場合:

```text
[SUMMARY] generated=0 skipped=1 errors=0
```

音声品質は夜間の実機再生で確認する。

---

# Part VII. Audio Circle設計

## 28. 再生リスト

正式名称:

```text
MEMORIOPOLIS | JANUS-18 Audio Circle
```

用途:

```text
Essayと言語を横断したランダム再生
音から言語、Essay、Concept、経験、談話位置を予測
```

Essay別プレイリストは作らない。

---

## 29. 再生リストでの識別

ファイル名を索引として使う。

```text
E0001_es.mp3
E0002_ja.mp3
E0002_zh-Hant-TW.mp3
```

ファイル名から次を識別できる。

```text
Essay ID
言語コード
音源形式
```

---

## 30. 再生速度

YouTube MusicへアップロードしたMP3は通常の音楽トラックとして扱われるため、アプリ内で2倍速などへ変更できない。

これは自作MP3固有の不具合ではない。

運用は次とする。

```text
日常の横断反復
→ YouTube Music

速度を変えた精聴
→ ローカルプレーヤー

恒常的な速度調整
→ MP3生成時のrateを変更
```

---

# Part VIII. 本日発見した不具合と恒久対策

## 31. E0002日本語MP3の作成漏れ

原因:

```text
Core30の英語Essay音源は作成したが、日本語canonicalからのMP3を作成していなかった
```

恒久対策:

```text
音声同期スクリプトを全Essay走査型にする
MP3がある場合はスキップ
MP3がない場合は生成
```

---

## 32. English Core30画像の作成漏れ

原因:

```text
Core20まではConcept画像を制作していたが、Core30作成時に画像工程が抜けた
```

恒久対策:

新Coreを開始するときは、次を一単位として扱う。

```text
Concept一覧
README画像設計
PNG
WebP
manifest.csv
Anki反映
実機確認
```

---

## 33. ConceptSceneの二重img問題

症状:

```text
画像が壊れ、alt属性の一部が文字として表示された
```

原因:

```text
ConceptSceneフィールド内に<img>タグがある
＋
テンプレート側でも<img src="{{ConceptScene}}">を作った
```

恒久対策:

```html
<div class="concept-media">{{ConceptScene}}</div>
```

のようにフィールドをそのまま出力する。

---

## 34. Markdownメタデータのエスケープ

症状:

```text
essay_id mismatch: metadata=(missing)
```

原因:

```text
essay\_id
source\_type
core\_range
```

恒久対策:

```text
essay_id
source_type
core_range
```

を正式キーとし、生成時にメタデータ契約を検査する。

---

## 35. 旧スクリプト名の実行

症状:

```text
can't open file memoriopolis_essay_audio_batch.py
```

原因:

```text
現在のessay直下にあるのはmemoriopolis_audio_sync.py
```

恒久対策:

通常操作はPowerShellラッパーへ固定する。

```powershell
.\run_memoriopolis_audio_sync.ps1
```

個別処理のみ`--job`を使用する。

---

# Part IX. 標準作業手順

## 36. 新しいCoreを開始する手順

```text
1. 日本語Essay canonicalを確定
2. CoreのConcept IDと境界を決定
3. Concept画像READMEを作成
4. PNG / WebP / manifestを作成
5. 対象言語の既存フィールドマスターを確認
6. ノートタイプにConceptSceneがあるか確認
7. UIを音優先型へ整備
8. 対象言語Essay draftを作成
9. 内容確認後canonical化
10. master CSVを作成
11. Anki CSVを作成
12. Ankiへインポート
13. Desktopで数枚プレビュー
14. AnkiWebへ同期
15. AnkiDroidで同期
16. MP3同期スクリプトを実行
17. 音源をAudio Circleへ追加
18. 夜間に実機確認
19. 引き継ぎ書を更新
```

---

## 37. 新言語を追加する手順

```text
1. 言語・地域基準を決定
2. ファイル識別子を決定
3. TTSロケールとVoiceを決定
4. Core10のフィールドとUIを確認
5. ConceptSceneを末尾へ追加
6. 音優先UIを実装
7. canonical Essayを作成
8. 対応CoreのCSVを作成
9. Anki同期
10. MP3生成
11. Audio Circleへ追加
```

---

## 38. 完了判定

言語×Coreの作業は、次がすべて揃った時点で完了とする。

```text
[ ] Essay canonical
[ ] master CSV
[ ] Anki CSV
[ ] README
[ ] Note type / UI
[ ] ConceptScene
[ ] Anki Desktop確認
[ ] AnkiDroid同期
[ ] MP3
[ ] Audio Circle追加
[ ] 夜間実機確認
```

---

# Part X. 現在の状態

## 39. Core20 / Spanish

```text
[x] E0001_es.md canonical
[x] 19フィールドNote type
[x] 音優先UI
[x] ConceptScene表示修正
[x] Spanish Core20 C0011-C0020
[x] master CSV
[x] Anki CSV
[x] Anki登録
[x] AnkiDroid同期
[x] E0001_es.mp3
[x] Audio Circle追加
[ ] 夜間音声・表示確認
```

---

## 40. Core30 / Japanese

```text
[x] E0002_ja.md canonical
[x] メタデータキー修正
[x] E0002_ja.mp3
[x] Audio Circle追加
[ ] 夜間音声確認
```

---

## 41. Core30 / English

```text
[x] E0002_en.md canonical
[x] English Core30 C0021-C0030
[x] Core30 Concept画像反映
[x] E0002_en.mp3
[x] Audio Circle追加
[ ] 横長画像の夜間実機確認
```

---

## 42. Core30 / 臺灣華語

```text
[x] E0002_zh-Hant-TW.md canonical
[x] 17フィールドUI
[x] 臺灣華語Core30 C0021-C0030
[x] master CSV
[x] Anki CSV
[x] Anki登録
[x] E0002_zh-Hant-TW.mp3
[x] Audio Circle追加
[ ] AnkiDroid同期状態の最終確認
[ ] 夜間音声・表示確認
```

---

# Part XI. 明日の開始点

## 43. 最初に確認すること

明日は、今晩の実機確認結果から開始する。

```text
1. Core30横長画像を維持するか
2. English Core30画像の可読性
3. 臺灣華語Core30の注音・拼音・TTS
4. Spanish Core20のTTSとConceptScene
5. 3本のMP3の自然さ
6. MP3の読み上げ範囲
```

不具合があれば、原因を次に分離する。

```text
canonical Markdown
CSVデータ
Ankiフィールド
カードテンプレート
ConceptScene画像
TTS生成
YouTube Music再生
```

---

## 44. 明日の新規制作候補

今晩の確認で重大な問題がなければ、次のリングへ進む。

現行の言語展開順から、次の候補は以下である。

```text
Core20側
→ Portuguese pt-BR

Core30側
→ Korean ko
```

ただし、明日の開始時に今晩の検証結果と学習負荷を確認し、正式に着手順を決める。

---

## 45. 明日用開始プロンプト

```text
前日の完全版引き継ぎ書に従い、まず夜間実機確認の結果を整理します。

確認対象は、English Core30と臺灣華語Core30の横長Concept画像、Spanish Core20と臺灣華語Core30のAnki表示、E0001_es.mp3、E0002_ja.mp3、E0002_zh-Hant-TW.mp3です。

不具合がなければ、次の候補としてCore20側はブラジル・ポルトガル語pt-BR、Core30側は韓国語koを検討します。既存の実フィールドマスターとUIを必ず確認し、フィールド名を推測で流用しないでください。

Essay canonical、Anki、ConceptScene、MP3、Audio Circleを一つの完了単位として進めます。
```

---

# Part XII. 設計上の確定事項

## 46. 確定事項一覧

```text
GitHub canonical Markdownが正本
1 Markdown = 1 MP3
Essay IDが経験単位
Concept IDが記憶都市の住所
同じConcept IDでは全言語が同じConceptSceneを共有
Ankiは音優先
長文音声はEssay単位
Audio CircleはEssayと言語を横断
既存MP3は再生成せずスキップ
不足MP3だけ生成
言語別フィールド名は既存マスターを正とする
master CSVはヘッダーあり
Anki CSVはヘッダーなし
現代日本語の独立Ankiデッキは作らない
日本語系Ankiの正はMEMORIOPOLIS::ModernJapaneseのみ
Spanishはes-ES
Portugueseはpt-BR
臺灣華語はzh-Hant-TW
```

---

## 47. 一行サマリー

> 2026年10月8日、MEMORIOPOLIS / JANUS-18は、canonical Essay、Concept ID、共通画像、音優先Anki、Essay単位MP3、横断Audio Circleを一つの再利用可能な制作・学習パイプラインとしてほぼ確立した。
