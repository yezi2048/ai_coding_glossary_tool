$ErrorActionPreference = "Stop"

$AppDir = Join-Path $env:LOCALAPPDATA "CodexTools\AICodingGlossary"
$StartMenuShortcut = Join-Path (Join-Path $env:APPDATA "Microsoft\Windows\Start Menu\Programs") "AI Coding Glossary.lnk"
$StartupShortcut = Join-Path ([Environment]::GetFolderPath("Startup")) "AI Coding Glossary.lnk"

Get-CimInstance Win32_Process |
    Where-Object { $_.CommandLine -and $_.CommandLine.Contains("glossary_tool.py") -and $_.CommandLine.Contains("AICodingGlossary") } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }

Remove-Item -LiteralPath $StartMenuShortcut -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath $StartupShortcut -Force -ErrorAction SilentlyContinue

if (Test-Path $AppDir) {
    $Resolved = (Resolve-Path -LiteralPath $AppDir).Path
    $ExpectedPrefix = (Join-Path $env:LOCALAPPDATA "CodexTools")
    if ($Resolved.StartsWith($ExpectedPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        Remove-Item -LiteralPath $Resolved -Recurse -Force
    } else {
        throw "Install directory is outside the expected location, refusing to delete: $Resolved"
    }
}

Write-Host "AI Coding Glossary has been uninstalled."
