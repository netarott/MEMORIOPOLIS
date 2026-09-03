$ErrorActionPreference = "Stop"

$repoRoot = Get-Location
$sectionDir = Join-Path $repoRoot "experience\chapter04\section11"
$emakiPath = Join-Path $sectionDir "index.html"
$trailerPath = Join-Path $sectionDir "trailer.html"

if (-not (Test-Path $emakiPath)) {
    throw "Not found: $emakiPath`nRun this script from the MEMORIOPOLIS repository root."
}

if (-not (Test-Path $trailerPath)) {
    throw "Not found: $trailerPath`nRun this script from the MEMORIOPOLIS repository root."
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
Copy-Item $emakiPath "$emakiPath.$timestamp.bak"
Copy-Item $trailerPath "$trailerPath.$timestamp.bak"

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$emakiNav = @'
<nav class="section-navigation" aria-label="第十一節の関連ページ">
  <a class="primary-link" id="open-trailer" href="trailer.html">20秒の予告編を見る</a>
  <a href="../../">中央駅へ戻る</a>
</nav>
'@

$trailerNav = @'
<nav class="section-navigation trailer-navigation" aria-label="予告編の関連ページ">
  <a class="primary-link" id="open-emaki" href="index.html">第十一節の絵巻を読む</a>
  <a href="../../">中央駅へ戻る</a>
</nav>
'@

function Replace-Navigation {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Replacement
    )

    $content = [System.IO.File]::ReadAllText($Path)
    $pattern = '(?s)<nav\b[^>]*class="[^"]*section-navigation[^"]*"[^>]*>.*?</nav>'
    $matches = [regex]::Matches($content, $pattern)

    if ($matches.Count -ne 1) {
        throw "Expected exactly one section-navigation block in $Path, found $($matches.Count)."
    }

    $updated = [regex]::Replace($content, $pattern, $Replacement, 1)
    [System.IO.File]::WriteAllText($Path, $updated, $utf8NoBom)
}

Replace-Navigation -Path $emakiPath -Replacement $emakiNav
Replace-Navigation -Path $trailerPath -Replacement $trailerNav

$forbidden = @("notes.html", "第十節へ戻る", "第十一節へ戻る")
foreach ($path in @($emakiPath, $trailerPath)) {
    $content = [System.IO.File]::ReadAllText($path)
    foreach ($term in $forbidden) {
        if ($content.Contains($term)) {
            throw "Old navigation text remains in $path : $term"
        }
    }
}

$emaki = [System.IO.File]::ReadAllText($emakiPath)
$trailer = [System.IO.File]::ReadAllText($trailerPath)

if (-not $emaki.Contains('href="trailer.html"')) {
    throw "Trailer link was not created in index.html."
}
if (-not $emaki.Contains('href="../../"')) {
    throw "Central Station link was not created in index.html."
}
if (-not $trailer.Contains('href="index.html"')) {
    throw "Emaki link was not created in trailer.html."
}
if (-not $trailer.Contains('href="../../"')) {
    throw "Central Station link was not created in trailer.html."
}

Write-Host "[OK] Updated navigation:" -ForegroundColor Green
Write-Host "  $emakiPath"
Write-Host "  $trailerPath"
Write-Host "[OK] Backups use suffix: .$timestamp.bak" -ForegroundColor Green
