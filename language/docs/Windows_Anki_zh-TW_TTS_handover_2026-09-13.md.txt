# Windows台湾華語FOD・Anki音声環境 引き継ぎ書

- 作成日: 2026-09-13
- 次回予定: 2026-09-14
- 目的: 台湾華語版Ankiカードの読み上げ

## 1. 結論

Windowsの台湾華語FODはBasicのみ導入できた。OCRとText-to-Speechは完了しなかったため、追加調査を保留する。

今後の基本方針:

```text
PC版Anki         HyperTTS
AnkiDroid        Android標準TTS
言語指定         zh_TW
編集中            リアルタイムTTS
正本確定後        HyperTTSで音声ファイルを保存する案も検討
Windows zh-TW    Basicのみ導入済み
```

## 2. PC環境

```text
OS: Windows 11 Pro
バージョン: 26H2
OSビルド: 26300.9539
アーキテクチャ: x64
Insiderチャネル: Release Preview
イメージバージョン: 10.0.26300.9539
DISMバージョン: 10.0.26100.9539
エディション: Professional
```

`Get-ComputerInfo`の`Windows 10 Pro / 2009`表示は互換情報とみられる。判断には`winver`とDISMのイメージバージョンを使う。

## 3. 更新環境

```text
BranchName: ReleasePreview
ContentType: Mainline
Ring: External
```

従来型WSUSの次の値は見つからなかった。

```text
UseWUServer
WUServer
```

MDM、プロキシ、セキュリティ製品、Microsoft側のFOD配信状態は未確認。

## 4. Windows言語パック作業

当初のサービス状態:

```text
BITS: Running
CryptSvc: Running
wuauserv: Stopped
```

`wuauserv`起動後、ロシア語は導入成功。

```powershell
Start-Service wuauserv
Install-Language ru-RU
```

確認済みの主な状態:

```text
ja-JP: BasicTyping, Handwriting, Speech, TextToSpeech, OCR
ko-KR: BasicTyping, Handwriting, TextToSpeech, OCR
ru-RU: BasicTyping, Handwriting, TextToSpeech, OCR
```

重要な訂正:

```text
-2147023436 = 0x800705B4 = タイムアウト
```

途中で`0x80070424`と案内した箇所は誤り。

## 5. 台湾華語FODの経過

### Install-Language

```powershell
Install-Language zh-TW
```

結果は`-2147023436 / 0x800705B4`でタイムアウト。

### Capability初期状態

```text
Language.Basic~~~zh-TW~0.0.1.0           NotPresent
Language.Handwriting~~~zh-TW~0.0.1.0     NotPresent
Language.OCR~~~zh-TW~0.0.1.0             NotPresent
Language.Speech~~~zh-TW~0.0.1.0          NotPresent
Language.TextToSpeech~~~zh-TW~0.0.1.0    NotPresent
```

### Basic

PowerShellラッパーは失敗。

```powershell
Add-WindowsCapability -Online -Name Language.Basic~~~zh-TW~0.0.1.0
```

表示:

```text
指定されたファイルが見つかりません。
```

DISM.exe直接実行は成功。

```powershell
DISM.exe /Online /Add-Capability /CapabilityName:Language.Basic~~~zh-TW~0.0.1.0
```

現在:

```text
Language.Basic~~~zh-TW~0.0.1.0    Installed
```

### OCR

```powershell
DISM.exe /Online /Add-Capability /CapabilityName:Language.OCR~~~zh-TW~0.0.1.0
```

処理が長時間待機し、最終的に未導入。

```text
Language.OCR~~~zh-TW~0.0.1.0    NotPresent
```

Anki読み上げには不要なので保留。

### Text-to-Speech

再起動後に実行。

```powershell
Start-Service wuauserv
Start-Service bits
DISM.exe /Online /Add-Capability /CapabilityName:Language.TextToSpeech~~~zh-TW~0.0.1.0 /LogPath:C:\Windows\Temp\zh-TW-TTS-DISM.log /LogLevel:4
```

`37.8%`で約30分以上停止。ログは次の状態から更新されなかった。

```text
Length: 48922
LastWriteTime: 2026/09/13 13:32:20
```

`Ctrl+C`で安全に中断。中断後:

```text
Language.TextToSpeech~~~zh-TW~0.0.1.0    NotPresent
```

中間的な`Installed`または`InstallPending`状態は確認されていない。

## 6. 原因候補

1. Windows 11 26H2 Release Previewと台湾華語FOD配信の不整合
2. FOD取得またはCBS登録処理の固着
3. コンポーネントストアまたは更新キャッシュの部分的不整合
4. MDM、プロキシ、セキュリティ製品による制御
5. ビルド26300系列向け台湾華語OCR／TTSパッケージの配信不足

Basicは成功したため、Windows Update全体の完全故障ではない。

## 7. オフラインFOD ISO

Microsoft公式のLanguages and Optional Features ISOを`/Source`に指定する方法はある。

```powershell
DISM.exe /Online /Add-Capability `
  /CapabilityName:Language.TextToSpeech~~~zh-TW~0.0.1.0 `
  /Source:D:\LanguagesAndOptionalFeatures `
  /LimitAccess
```

ただし:

- `Windows11_26H2_LanguagesAndOptionalFeatures_x64.iso`は説明用の仮名で、確認済みの正式ファイル名ではない。
- 一般公開された固定の直接URLは確認できなかった。
- Microsoft 365管理センターのVL領域、Visual Studio Subscription、Device Partner Center、社内配布などが取得候補。
- 26300系列との整合性が確認できない24H2／25H2用ISOは使わない。
- 出所不明のCABは使わない。

今回はISO経路も保留。

## 8. PC版Ankiの方針

HyperTTSを利用する。

```text
AnkiWebアドオンコード: 111623432
```

導入:

```text
Anki
→ ツール
→ アドオン
→ アドオンを入手
→ 111623432
→ Ankiを再起動
```

台湾華語の検索候補:

```text
Chinese (Taiwan)
Mandarin (Taiwan)
Traditional Chinese
zh-TW
cmn-TW
```

`zh-CN`は中国大陸向けなので原則選ばない。

## 9. AnkiDroidの方針

Android端末のTTSを利用する。

Android設定で探す表記:

```text
中文（台灣）
中文（繁體）
國語（台灣）
Chinese (Taiwan)
Mandarin (Taiwan)
zh-TW
```

設定場所の例:

```text
設定
→ システムまたは一般管理
→ 言語／テキスト読み上げの出力
→ 音声データ
→ 台湾華語を追加
```

端末やTTSエンジンにより名称は異なる。

## 10. カードテンプレート案

台湾華語本文フィールド例:

```text
TraditionalChinese
```

リアルタイムTTS:

```html
{{tts zh_TW:TraditionalChinese}}
```

表面例:

```html
<div class="traditional-chinese">
  {{TraditionalChinese}}
</div>

{{tts zh_TW:TraditionalChinese}}
```

この方式ではPCとAndroidで声が異なる可能性がある。

## 11. 二段階運用

### 推敲中

リアルタイムTTSを使う。

```html
{{tts zh_TW:TraditionalChinese}}
```

利点:

- 本文修正を即時反映
- 音声ファイルを大量保存しない
- 多言語デッキの試作に向く

### 正本確定後

HyperTTSで音声ファイルを生成して保存する案を検討。

```text
Audio_ja
Audio_en
Audio_zh_TW
Audio_ko
Audio_ru
```

テンプレート:

```html
{{Audio_zh_TW}}
```

利点:

- PCとAnkiDroidで同じ声
- 同期後はオフライン再生可能
- TTSサービス変更の影響を抑えられる

注意: 保存音声とリアルタイムTTSを同じ面に置くと二重再生の可能性がある。

## 12. 明日の開始手順

1. Windows FOD作業は再開しない。
2. PC版Ankiのバージョンを確認する。
3. HyperTTSをコード`111623432`で導入する。
4. 台湾華語のテストカードを10枚程度用意する。
5. HyperTTSで台湾華語音声を試聴する。
6. Androidに台湾華語TTS音声を追加する。
7. カードに`{{tts zh_TW:TraditionalChinese}}`を設定する。
8. PCとAnkiDroidで無音、誤読、二重再生を確認する。
9. 推敲中はリアルタイムTTS、正本確定後は保存音声という方針を評価する。

テスト文には次を含める。

- 台湾で一般的な語彙
- 多音字
- 数字と年月日
- 英字や固有名詞
- 短文と長文
- 多言語混交文
- 句読点と括弧

## 13. 明日避けること

- Windows台湾華語FODの反復試行
- OCRの再試行
- 24H2／25H2用FOD ISOの適用
- 出所不明CABの導入
- TiWorker／TrustedInstallerの強制終了
- いきなり全カードへの音声一括生成
- 保存音声とリアルタイムTTSの二重配置

## 14. 明日のゴール

次の構成で台湾華語10枚程度を正常に読み上げる。

```text
PC版Anki: HyperTTS
AnkiDroid: Android TTS
言語指定: zh_TW
カード: {{tts zh_TW:TraditionalChinese}}
```

Windows機能を揃えることではなく、台湾華語版Ankiで安定して音声を聴けることを最終目標とする。
