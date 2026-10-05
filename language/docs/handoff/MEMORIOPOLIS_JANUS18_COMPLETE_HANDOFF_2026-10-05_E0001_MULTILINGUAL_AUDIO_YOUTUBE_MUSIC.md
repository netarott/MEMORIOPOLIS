# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

**作業日:** 2026-10-05  
**対象:** E0001多言語音声化、`edge-tts`パイプライン、YouTube Music反復聴取環境  
**ステータス:** 本日の作業完了、実運用開始可能

---

## 0. 本日の到達点

本日は、MEMORIOPOLISにおける「音」トリガーの可能性を、AnkiカードからEssay全体へ拡張した。

最終的に、次の流れを実環境で完成させた。

```text
canonical Markdown
  ↓
edge-ttsによる本文抽出・音声合成
  ↓
1 Markdown = 1 MP3
  ↓
E0001 canonical 9言語を一括生成
  ↓
YouTube Musicへアップロード
  ↓
専用プレイリストへ9トラック登録
  ↓
スマートフォンでシャッフル＋全曲リピート
```

完成したプレイリストは次のとおり。

```text
MEMORIOPOLIS E0001｜JANUS-18 Audio Circle
```

設定状況：

```text
公開範囲：非公開
トラック数：9
合計時間：約55分
カバー画像：設定済み
説明文：設定済み
```

---

## 1. 本日の思想的・学習上の前提

### 1.1 音声反復は補助ではなく、日々の主要トレーニング

当初、長文MP3を「ときどき自由に聞く補助音声」として整理しかけたが、方針を修正した。

JANUS-18の音声運用は次の二本立てとする。

```text
AnkiDroid
＝ 単語と例文の字・音に触れ、Conceptを能動的に想起する

YouTube Music
＝ 同じEssayを多言語で大量反復し、各言語の音韻・リズム・語境界に馴染む
```

「聞き流しだけで語学を完成させる」のではない。

```text
Ankiで短い音を精密に学ぶ
  ↓
長文MP3で同じ音と繰り返し再会する
  ↓
文字で知っている語を連続音声から認識できるようにする
  ↓
多言語勘と音声語彙の自動化を育てる
```

### 1.2 ランダム再生の意味

E0001の内容は全言語で既知であるため、ランダム再生時には次の探索が自然に起こる。

```text
冒頭の音を聞く
  ↓
どの言語かを認識する
  ↓
既知のE0001の場面を予測する
  ↓
Ankiで学んだ語を長文中から拾う
  ↓
ConceptSceneや次の話題が浮かぶ
```

内容を固定し、音声体系だけを切り替えることが、JANUS-18独自の強みである。

### 1.3 音声単位

今回の原則は明確に固定した。

```text
1 Markdown = 1 MP3
```

当面、段落別MP3やAnchor Audioは作成しない。

Essay単位で音声を繰り返し、言語全体のリズムと文章展開へ馴染むことを優先する。

---

## 2. E0001 canonical状況

本日時点で、以下の9言語はすべてcanonicalである。

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
E0001_ko.md          canonical
E0001_ru.md          canonical
E0001_fil.md         canonical
E0001_id.md          canonical
E0001_vi.md          canonical
E0001_fr.md          canonical
```

重要な訂正：

```text
E0001_vi.md
＝ draftではない
＝ canonical確定済み
```

今後の引き継ぎでは、ベトナム語版をdraftと記載しないこと。

---

## 3. Azureを使わない音声化方針

### 3.1 採用

```text
edge-tts
```

採用理由：

```text
Azureアカウント不要
APIキー不要
クレジットカード不要
Pythonから利用可能
MP3を直接生成可能
多言語対応
自然なニューラル音声
```

### 3.2 不採用

```text
Azure AI Speech
```

理由：無料アカウント作成、サブスクリプション、リソース作成などが現在の目的に対して煩雑であるため。

### 3.3 将来の補助候補

```text
Piper
＝ ローカル生成が必要になった場合の補助候補

eSpeak NG
＝ CLASSICA-5の発音検証用候補
```

ただし、現段階のLIVING-13音声化は`edge-tts`を主系統とする。

---

## 4. PoCで使用したファイル

### 4.1 初期PoCスクリプト

```text
memoriopolis_e0001_audio_poc.py
```

対象：

```text
E0001_ja.md
E0001_fr.md
```

出力：

```text
audio_E0001_poc/
├─ E0001_ja.mp3
├─ E0001_ja.narration.txt
├─ E0001_ja.srt
├─ E0001_fr.mp3
├─ E0001_fr.narration.txt
└─ E0001_fr.srt
```

### 4.2 初期PoCの結果

フランス語は良好だった。

```text
音声：fr-FR-DeniseNeural
速度：-8%
```

日本語は当初、次の設定だった。

```text
音声：ja-JP-NanamiNeural
速度：-8%
```

しかし、機械的な印象が強かったため、複数パターンを比較した。

```text
Nanami ±0%
Nanami -3%
Keita -3%
Nanami -8%
```

比較後、日本語の暫定標準を次に確定した。

```text
音声：ja-JP-NanamiNeural
速度：-3%
```

判断基準は「単に聞き取りやすい」ではなく、繰り返し聞ける自然さである。

---

## 5. 一括生成スクリプト

### 5.1 正式スクリプト

```text
memoriopolis_e0001_audio_all.py
```

### 5.2 実行場所

```text
MEMORIOPOLIS\essay\E0001
```

同じフォルダーに、9言語の`E0001_*.md`とスクリプトを配置する。

### 5.3 基本実行コマンド

```powershell
py .\memoriopolis_e0001_audio_all.py --continue-on-error
```

既存MP3を上書きする場合：

```powershell
py .\memoriopolis_e0001_audio_all.py `
  --continue-on-error `
  --overwrite
```

### 5.4 出力先

```text
audio_E0001_all
```

### 5.5 出力内容

```text
audio_E0001_all/
├─ E0001_ja.mp3
├─ E0001_en.mp3
├─ E0001_zh-Hant-TW.mp3
├─ E0001_ko.mp3
├─ E0001_ru.mp3
├─ E0001_fil.mp3
├─ E0001_id.mp3
├─ E0001_vi.mp3
├─ E0001_fr.mp3
├─ 各言語の E0001_xx.narration.txt
├─ 各言語の E0001_xx.srt
└─ E0001_audio_manifest.json
```

### 5.6 スクリプトの安全策

```text
実行時にedge-ttsの音声一覧を取得
優先Voice IDの実在を確認
優先音声がなければ同一ロケール内で代替
status: draftが明記されたファイルは生成しない
制作メモ・参照URL・コードブロックを除外
本文抽出結果が短すぎる場合は停止
一時ファイルへ書き、成功後に完成MP3へ置換
生成条件をmanifestへ記録
1言語ずつ順番に生成
--continue-on-errorで残りの言語を継続
```

---

## 6. 採用した音声設定

本日の一括生成では、次の設定を使用した。

```text
日本語
locale: ja-JP
voice: ja-JP-NanamiNeural
rate: -3%

英語
locale: en-US
voice: en-US-AndrewNeural
rate: -6%

臺灣華語
locale: zh-TW
voice: zh-TW-HsiaoChenNeural
rate: -8%

韓国語
locale: ko-KR
voice: ko-KR-SunHiNeural
rate: -8%

ロシア語
locale: ru-RU
voice: ru-RU-SvetlanaNeural
rate: -8%

フィリピン語
locale: fil-PH
voice: fil-PH-BlessicaNeural
rate: -8%

インドネシア語
locale: id-ID
voice: id-ID-GadisNeural
rate: -8%

ベトナム語
locale: vi-VN
voice: vi-VN-HoaiMyNeural
rate: -10%

フランス語
locale: fr-FR
voice: fr-FR-DeniseNeural
rate: -8%
```

重要事項：

```text
AnkiDroidのインドネシア語
＝ in_ID＋端末固有Google TTS voice ID

MP3生成のインドネシア語
＝ edge-tts側のid-ID-GadisNeural
```

別システムなので、`in_ID`と`id-ID`を混同しないこと。

---

## 7. 一括生成時の障害と回復

### 7.1 初回結果

```text
成功：7
失敗：2
```

失敗した言語：

```text
韓国語
ロシア語
```

エラー内容：

```text
Connection timeout
Cannot connect to host
getaddrinfo failed
```

原因は本文やVoice IDではなく、一時的なオンライン接続不良だった。

### 7.2 回復手順

`--overwrite`を付けずに再実行した。

```powershell
py .\memoriopolis_e0001_audio_all.py --continue-on-error
```

この場合：

```text
生成済み7言語
＝ SKIP

未生成の韓国語・ロシア語
＝ 再試行
```

### 7.3 最終結果

```text
[DONE] 成功/スキップ: 9  失敗: 0
```

全9言語のMP3生成が完了した。

---

## 8. YouTube Music採用

### 8.1 再生基盤の前提修正

OneDriveはこのPC上の制作・同期環境であり、日常の再生端末はスマートフォンである。

そのため、最終的な再生基盤として次を採用した。

```text
YouTube Musicの個人音楽アップロード
```

通常のYouTube動画ではない。

### 8.2 採用理由

```text
MP3を直接アップロード可能
PCからアップロード可能
スマートフォンアプリで再生可能
本人だけが再生可能
プレイリスト作成可能
バックグラウンド再生可能
シャッフル再生可能
全曲リピート可能
```

### 8.3 アップロード

PCのYouTube Musicから、`audio_E0001_all`内の9本をアップロードした。

アップロード音源一覧の正しいURL：

```text
https://music.youtube.com/library/uploaded_songs
```

途中、次のURLではアップロード曲一覧が出なかった。

```text
https://music.youtube.com/library/uploads
```

今後、アップロード曲を管理するときは`uploaded_songs`を優先する。

---

## 9. YouTube Musicプレイリスト

### 9.1 正式名称

```text
MEMORIOPOLIS E0001｜JANUS-18 Audio Circle
```

### 9.2 公開範囲

```text
非公開
```

### 9.3 説明文

本日設定した趣旨：

```text
『記憶都市（メモリオポリス）』E0001の多言語ナレーション。
同じEssayを複数言語でランダム再生し、
音、リズム、Concept、記憶の経路を反復するためのJANUS-18音声環。

1 Markdown = 1 MP3
Source: canonical E0001 multilingual editions
```

### 9.4 カバー画像

プレイリスト用の正方形カバー画像を生成し、設定した。

主な視覚要素：

```text
MEMORIOPOLISの都市
列車から都市を見る構図
多言語の音声ネットワーク
E0001
JANUS-18 Multilingual Audio
過去・現在・未来の方向標識
```

カバー画像は、現在の9言語だけでなく、今後追加するドイツ語、イタリア語、スペイン語、ブラジル・ポルトガル語も含む設計である。

### 9.5 最終登録結果

```text
9トラック
約55分
```

画面上で9本すべての登録を確認した。

---

## 10. YouTube Music操作で発生した混乱

### 10.1 空プレイリストの「候補」は無関係

空のプレイリスト画面に表示される「候補」は、YouTube Music側の一般音楽候補であり、アップロード済みE0001音声ではない。

候補の右側に表示される追加アイコンは押さないこと。

### 10.2 フィルター画面では曲が見えない場合がある

次の画面遷移では、アップロード済み曲が見えない場合があった。

```text
ライブラリ
→ アップロード
→ プレイリストフィルター
```

この場合、URLを直接指定する方が確実。

```text
https://music.youtube.com/library/uploaded_songs
```

### 10.3 曲追加の基本

アップロード曲一覧から、各曲をプレイリストへ保存する。

```text
E0001_xx.mp3
  ↓
曲のメニュー
  ↓
再生リストに保存
  ↓
MEMORIOPOLIS E0001｜JANUS-18 Audio Circle
```

最終的には9曲すべて登録できた。

---

## 11. 日々の運用

### 11.1 AnkiDroid

```text
単語音声を聞く
  ↓
Conceptを想起する
  ↓
ConceptSceneで確認する
  ↓
文字・語根・接辞・例文を見る
```

### 11.2 YouTube Music

スマートフォンでプレイリストを開き、次を有効にする。

```text
シャッフル：ON
全曲リピート：ON
1曲リピート：OFF
```

これにより、9言語がランダムに連続反復される。

### 11.3 聴取中の観測

毎回全文を翻訳しようとしない。

次の小さな変化を観測する。

```text
どの言語か分かった
列車の場面だと分かった
Core語が聞こえた
ConceptSceneが浮かんだ
次の内容を予測できた
以前より語境界が聞こえた
言語ごとのリズムが識別できた
```

### 11.4 反復量

言語に馴染むには、多量かつ継続的な音声接触が必要である。

E0001は数日間、移動中・散歩中・作業中などにシャッフル＋リピートで繰り返す。

---

## 12. 品質確認

今後、各言語について次を確認する。

```text
制作メモやURLを読んでいない
タイトルから結末まで欠けていない
固有名詞の誤読が致命的でない
地域ロケールが正しい
速度が遅すぎない
繰り返し聞いて疲れにくい
文章のリズムが壊れていない
```

日本語については、`Nanami -3%`を暫定採用済み。

他言語は数日間の反復後、必要があれば速度とVoice IDを調整する。

MP3の正本性については、次のように考える。

```text
canonical Markdown
＝文章正本

MP3
＝生成条件を記録した派生成果物
```

音声の設定は`E0001_audio_manifest.json`で追跡する。

---

## 13. Git / 管理上の注意

### 13.1 GitHubへ置くもの

```text
canonical Markdown
Pythonスクリプト
README
音声設定
manifest
必要に応じてnarration.txt
```

### 13.2 GitHubへ置くか検討が必要なもの

```text
MP3本体
SRT
カバー画像
```

MP3は容量が増えるため、GitHubへ直接コミットするか、Release、LFS、外部保管にするかを後で決める。

現時点の実運用コピーはYouTube Musicにある。

---

## 14. 次回の言語展開

次のLIVING-13作業順：

```text
ドイツ語
  ↓
イタリア語
  ↓
スペイン語 es-ES
  ↓
ポルトガル語 pt-BR
```

ドイツ語の作業は次の順で進める。

```text
1. フランス語AnkiDroid実機確認
2. ドイツ語Core10の実フィールド確認
3. ConceptSceneを19番目へ追加
4. ドイツ語音優先型カードUI
5. E0001ドイツ語版
6. German Core20
7. E0001_de.mdをcanonical化
8. E0001_de.mp3を生成
9. YouTube Musicの既存プレイリストへ追加
```

ドイツ語以降は、Essayのcanonical化後に音声生成までを一つの制作単位とする。

```text
Essay canonical化
  ↓
1 md = 1 mp3
  ↓
YouTube Musicへアップロード
  ↓
Audio Circleへ追加
```

---

## 15. 将来のJANUS-18音声展開

### LIVING-13

各現代語は、自然な現代ナレーションを優先する。

```text
ModernJapanese
English
zh-Hant-TW
Korean
Russian
Filipino
Indonesian
Vietnamese
French
German
Italian
Spanish es-ES
Portuguese pt-BR
```

### CLASSICA-5

```text
Classical Latin
Ancient Greek
Classical Sanskrit
Biblical Hebrew
Classical Arabic
```

古典語では、現代語TTSを無理に正本化しない。

発音伝統、時代層、転写、教育的な聞きやすさを分けて検討する。

これはLIVING-13の音声化が安定した後に着手する。

---

## 16. 本日の確定事項

```text
E0001_vi.mdはcanonical

1 Markdown = 1 MP3

主音声エンジンはedge-tts

Azure AI Speechは使用しない

日本語はNanami -3%

フランス語はDenise -8%

E0001 canonical 9言語のMP3生成完了

YouTube Musicへ9本アップロード完了

プレイリスト作成完了

プレイリスト名：
MEMORIOPOLIS E0001｜JANUS-18 Audio Circle

公開範囲：非公開

9トラック・約55分

スマートフォンではシャッフル＋全曲リピート
```

---

## 17. 次回開始時の確認事項

```text
1. スマートフォンのYouTube Musicでプレイリストが表示されるか
2. 9トラックすべて再生できるか
3. シャッフルが有効か
4. 全曲リピートが有効か
5. 画面OFFでもバックグラウンド再生できるか
6. Bluetoothイヤホンで再生できるか
7. 言語間の音量差が大きくないか
8. 各言語の速度に違和感がないか
9. 誤読が目立つ固有名詞があるか
10. フランス語AnkiDroid実機確認
11. ドイツ語Core10へ着手
```

---

## 18. 次回開始用プロンプト

```text
2026-10-05の完全版引き継ぎ書を基準に再開してください。

まず、スマートフォンのYouTube Musicで
「MEMORIOPOLIS E0001｜JANUS-18 Audio Circle」
の9言語シャッフル＋全曲リピートが正常に機能するか確認します。

音声品質に問題があれば、対象言語のVoice IDまたは速度を調整します。
問題がなければ、フランス語AnkiDroidの実機確認後、ドイツ語Core10のフィールド確認、ConceptScene追加、カードUI、E0001ドイツ語版、German Core20へ進みます。

E0001_vi.mdはcanonicalです。
1 Markdown = 1 MP3を維持してください。
```

---

## 19. 本日の総括

本日の作業により、MEMORIOPOLISの音優先設計は、Ankiカードの短いTTSから、Essay全体の長い多言語音声へ拡張された。

これは単なるオーディオブック化ではない。

```text
Ankiで精密に学んだ音
  ↓
Essayの連続音声で繰り返し再会
  ↓
同じ内容を複数言語で聞く
  ↓
言語識別・語境界・リズム・Concept予測が起動
  ↓
文字中心の語彙知識が、音から利用できる知識へ変わる
```

E0001の9言語は、約55分の一つの「音声環」になった。

この音声環をスマートフォンで日常的に反復することで、JANUS-18はカード上の多言語体系から、生活時間の中で流れ続ける多言語環境へ進み始めた。

本日はここで店じまいとする。
