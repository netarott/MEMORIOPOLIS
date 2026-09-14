# Windows 多言語パック導入作業 引き継ぎ書

- 作成日: 2026-09-12
- 対象: Windows 11（正確なエディション、バージョン、OSビルドは未採取）
- 目的: 日本語、英語、韓国語、ロシア語、台湾華語の言語機能を可能な限り同じ構成に揃える
- 未解決事項: 台湾華語 `zh-TW` の導入

## 1. 現在の結論

ロシア語 `ru-RU` は、停止していた Windows Update サービス `wuauserv` を手動起動した後、`Install-Language ru-RU` で正常に導入できた。

韓国語 `ko-KR` は、当初不足していた Handwriting と OCR を個別追加でき、現在の `Get-InstalledLanguage` では次の機能が確認できている。

- BasicTyping
- Handwriting
- TextToSpeech
- OCR

台湾華語 `zh-TW` は Windows Capability として認識されているが、`Install-Language zh-TW` と `Add-WindowsCapability` の両方で失敗した。

## 2. 重要な訂正

当初、`Install-Language` のエラーコード `-2147023436` を `0x80070424` と解釈したが、正しくは次のとおり。

```text
-2147023436 = 0x800705B4
```

`0x800705B4` はタイムアウトを示す。したがって、ロシア語の初回失敗は「サービスが存在しない」という意味ではなく、Windows Update 経由の取得処理が時間内に完了しなかった可能性が高い。

ただし、`wuauserv` の手動起動直後にロシア語が成功したため、Windows Update サービスの停止またはオンデマンド起動不良が実務上の直接要因だった可能性は高い。

## 3. 実施した作業と結果

### 3.1 初期状態の確認

```powershell
Get-InstalledLanguage
```

当初確認できた主な状態:

```text
en-US  LpCab       Language Features: None
ja-JP  LpCab, LXP  BasicTyping, Handwriting, Speech, TextToSpeech, OCR
ko-KR  LXP         BasicTyping, TextToSpeech
und-Jpan None      Fonts
```

### 3.2 ロシア語の初回導入

```powershell
Install-Language ru-RU
```

結果:

```text
言語をインストールできませんでした。
ErrorCode: -2147023436
```

正しい16進表記は `0x800705B4`、タイムアウト。

### 3.3 Windows Update 関連サービスの確認

```powershell
Get-Service wuauserv,bits,cryptsvc
```

結果:

```text
Running  bits
Running  cryptsvc
Stopped  wuauserv
```

### 3.4 Windows Update ログの生成

```powershell
Get-WindowsUpdateLog
```

ETLからログへの変換は完了した。一部イベントがスキーマに一致しないという警告が出たが、コマンド自体は正常終了した。

生成先として画面上で確認できた場所:

```text
C:\Users\yasuhide_shinohara\OneDrive - 株式会社アイネス\ソリューションズ\デスクトップ\WindowsUpdate.log
```

※パスには組織名が含まれるため、外部共有時はマスキングすること。

### 3.5 `wuauserv` の手動起動とロシア語再試行

```powershell
Start-Service wuauserv
Get-Service wuauserv
Install-Language ru-RU
```

結果:

```text
ru-RU  LpCab  BasicTyping, Handwriting, TextToSpeech, OCR
```

ロシア語は正常導入できた。

### 3.6 韓国語の不足機能の追加

韓国語は最終的に次の状態まで追加できた。

```text
ko-KR  LXP  BasicTyping, Handwriting, TextToSpeech, OCR
```

再確認コマンド:

```powershell
Get-InstalledLanguage
```

### 3.7 `wuauserv` を30分ごとに確認する応急スクリプト

管理者 PowerShell で次を実行中。

```powershell
while ($true) {
    $svc = Get-Service wuauserv

    if ($svc.Status -ne 'Running') {
        Start-Service wuauserv
        Write-Host "$(Get-Date) Started wuauserv"
    }
    else {
        Write-Host "$(Get-Date) Already running"
    }

    Start-Sleep -Seconds 1800
}
```

画面上では `Already running` が30分間隔で記録され、`wuauserv` は Running を維持していた。

注意: これは応急処置。PowerShellウィンドウを閉じると終了する。恒久運用する場合でも、無限ループよりタスクスケジューラを使う方が適切。ただし、言語導入作業終了後は常時起動させる必要性を再検討する。

## 4. 台湾華語 `zh-TW` で実施したこと

### 4.1 一括導入

```powershell
Start-Service wuauserv
Install-Language zh-TW
```

結果:

```text
言語をインストールできませんでした。
ErrorCode: -2147023436
```

これは `0x800705B4`、タイムアウト。

### 4.2 ユーザー言語リスト確認

```powershell
Get-WinUserLanguageList
```

表示された言語タグ:

```text
ja
ko
ru
```

`zh-TW` はまだユーザー言語リストに存在しない。

### 4.3 `zh-TW` Capability の確認

```powershell
Get-WindowsCapability -Online |
Where-Object {$_.Name -like "*zh-TW*"}
```

結果:

```text
Language.Basic~~~zh-TW~0.0.1.0             NotPresent
Language.Handwriting~~~zh-TW~0.0.1.0       NotPresent
Language.OCR~~~zh-TW~0.0.1.0               NotPresent
Language.Speech~~~zh-TW~0.0.1.0            NotPresent
Language.TextToSpeech~~~zh-TW~0.0.1.0      NotPresent
```

このため、OSは `zh-TW` の機能名と導入候補を認識している。

### 4.4 Basic 機能の個別導入

```powershell
Add-WindowsCapability -Online `
  -Name Language.Basic~~~zh-TW~0.0.1.0
```

結果:

```text
Add-WindowsCapability : 指定されたファイルが見つかりません。
CategoryInfo          : NotSpecified: (:) [Add-WindowsCapability], COMException
FullyQualifiedErrorId : Microsoft.Dism.Commands.AddWindowsCapabilityCommand
```

数値のエラーコードは画面には表示されていない。文言上は必要なパッケージまたは取得元を解決できなかった可能性がある。

## 5. 現在確認できている言語状態

```text
en-US  LpCab       None
ja-JP  LpCab, LXP  BasicTyping, Handwriting, Speech, TextToSpeech, OCR
ko-KR  LXP         BasicTyping, Handwriting, TextToSpeech, OCR
ru-RU  LpCab       BasicTyping, Handwriting, TextToSpeech, OCR
und-Jpan None      Fonts
```

`Get-WinUserLanguageList` 側では `ja`、`ko`、`ru` を確認。`zh-TW` は未登録。

## 6. 原因候補

現時点では断定しない。優先度順の仮説は次のとおり。

### 仮説A: Windows Update / FOD の取得元解決が不安定

`Install-Language zh-TW` はタイムアウトし、`Add-WindowsCapability` は「指定されたファイルが見つかりません」となった。Windows Capability は、指定されたソース、グループポリシーで指定された場所、WSUS、Windows Update などから必要ファイルを取得する。会社管理PCでは、WSUSや「オプションコンポーネントのインストールとコンポーネント修復」のポリシーが影響する可能性がある。

ロシア語が成功しているため、Windows Update 全体が完全に利用不能ではない。ただし、`zh-TW` の個別パッケージ解決だけが失敗している可能性は残る。

### 仮説B: Windowsのビルドと配信される言語/FODパッケージの不整合

正確な Windows バージョンとOSビルドをまだ採取していない。プレビュー版、更新途中、またはコンポーネントストアと配信パッケージの版が一致しない場合、特定Capabilityだけ失敗することがある。

### 仮説C: コンポーネントストアまたはWindows Updateキャッシュの不整合

`Get-WindowsCapability` は候補を列挙できる一方、インストール時にファイルを解決できない。DISMコンポーネントストアまたはWindows Updateキャッシュの不整合も候補。ただし、明日は先にログとポリシーを採取し、いきなりキャッシュを削除しない。

### 仮説D: 会社管理ポリシー、WSUS、プロキシ

画面の保存先に会社用OneDriveが見えるため、管理端末の可能性がある。WSUSがFeature on Demandを保持していない、またはMicrosoft Updateへの直接取得が制限されている場合、言語Capabilityの追加に失敗し得る。

## 7. 明日の推奨手順

### Step 1: PowerShellの30分ループを停止

実行中のウィンドウで `Ctrl+C`。

### Step 2: Windowsの版とビルドを採取

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, OsArchitecture
```

併せて:

```powershell
winver
```

### Step 3: 失敗直後の正確なHRESULTとDISMログを採取

新しい管理者PowerShellで、ログを明示して再実行する。

```powershell
Start-Service wuauserv

Add-WindowsCapability -Online `
  -Name Language.Basic~~~zh-TW~0.0.1.0 `
  -LogPath C:\Windows\Temp\zh-TW-DISM.log `
  -LogLevel WarningsInfo
```

失敗直後:

```powershell
$Error[0] | Format-List * -Force
```

ログの絞り込み:

```powershell
Select-String -Path C:\Windows\Temp\zh-TW-DISM.log `
  -Pattern "error|failed|0x800|source" `
  -CaseSensitive:$false
```

CBSログも確認:

```powershell
Select-String -Path C:\Windows\Logs\CBS\CBS.log `
  -Pattern "zh-TW|error|failed|0x800" `
  -CaseSensitive:$false |
  Select-Object -Last 100
```

### Step 4: WSUS・ポリシーを確認

```powershell
reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Servicing"
```

グループポリシー結果も保存:

```powershell
gpresult /h "$env:USERPROFILE\Desktop\gpresult-language.html"
```

会社管理端末の場合、値を変更する前に管理方針を確認する。

### Step 5: コンポーネントストアを検査・修復

```powershell
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

再起動後、`Language.Basic~~~zh-TW~0.0.1.0` を再試行。

### Step 6: 別経路として設定画面を再試行

`設定 > 時刻と言語 > 言語と地域 > 言語の追加` から「中文（繁體，台灣）」を選択する。

Windows Updateサービスを起動した状態で行う。設定画面でも止まる場合は、DISMログとWindowsUpdate.logの同時刻を照合する。

### Step 7: オフライン導入へ切り替える

オンライン経路の修復に時間をかけすぎない。OSのバージョン、ビルド、アーキテクチャと一致する Microsoft の「Languages and Optional Features ISO」を用意し、マウント後にそのフォルダーを `-Source` で指定する。

例。ISOが `D:` にマウントされ、該当ファイルが `D:\LanguagesAndOptionalFeatures` にある場合:

```powershell
Add-WindowsCapability -Online `
  -Name Language.Basic~~~zh-TW~0.0.1.0 `
  -Source D:\LanguagesAndOptionalFeatures `
  -LimitAccess
```

続いて:

```powershell
Add-WindowsCapability -Online -Name Language.Handwriting~~~zh-TW~0.0.1.0 -Source D:\LanguagesAndOptionalFeatures -LimitAccess
Add-WindowsCapability -Online -Name Language.OCR~~~zh-TW~0.0.1.0 -Source D:\LanguagesAndOptionalFeatures -LimitAccess
Add-WindowsCapability -Online -Name Language.Speech~~~zh-TW~0.0.1.0 -Source D:\LanguagesAndOptionalFeatures -LimitAccess
Add-WindowsCapability -Online -Name Language.TextToSpeech~~~zh-TW~0.0.1.0 -Source D:\LanguagesAndOptionalFeatures -LimitAccess
```

重要: ISOはWindowsのリリース、ビルド系列、アーキテクチャに合致させる。異なる版のISOは使用しない。

### Step 8: ユーザー言語リストの追加

Capability導入後も `Get-WinUserLanguageList` に `zh-TW` がなければ追加する。

```powershell
$list = Get-WinUserLanguageList
$list.Add("zh-TW")
Set-WinUserLanguageList $list -Force
```

確認:

```powershell
Get-WinUserLanguageList
Get-InstalledLanguage
Get-WindowsCapability -Online |
  Where-Object {$_.Name -like "*zh-TW*"} |
  Select-Object Name, State
```

## 8. 明日避けること

- 正確なログを取る前に `SoftwareDistribution` や `catroot2` を削除しない。
- 出所不明のCABファイルをダウンロードしない。
- OSビルドが異なるLanguage Pack/FOD ISOを使わない。
- 会社管理端末でWSUS・グループポリシー・レジストリを無断変更しない。
- `wuauserv` を常時Runningにすることを恒久対策と決めつけない。

## 9. 参考資料

- Microsoft Learn: Add-WindowsCapability
  - https://learn.microsoft.com/powershell/module/dism/add-windowscapability
- Microsoft Learn: DISM Capabilities Package Servicing Command-Line Options
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/dism-capabilities-package-servicing-command-line-options
- Microsoft Learn: Add languages to Windows images
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/add-language-packs-to-windows

## 10. 明日の開始地点

最初に次の4点を採取する。

1. Windowsのバージョン、OSビルド、アーキテクチャ
2. `Add-WindowsCapability` の完全なエラー情報
3. `C:\Windows\Temp\zh-TW-DISM.log` のエラー行
4. WSUSおよびServicingポリシーの状態

その結果で、オンライン経路の修復を続けるか、OSビルドに一致するLanguages and Optional Features ISOを使うオフライン導入へ切り替える。
