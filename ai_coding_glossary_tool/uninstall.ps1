$ErrorActionPreference = "Stop"

$AppDir = Join-Path $env:LOCALAPPDATA "CodexTools\AICodingGlossary"
$DisplayName = ([string]([char]0x7801) + [char]0x8BCD + [char]0x6025 + [char]0x6551 + [char]0x5305)
$StartMenuDir = Join-Path $env:APPDATA "Microsoft\Windows\Start Menu\Programs"
$StartupDir = [Environment]::GetFolderPath("Startup")
$Shortcuts = @(
    (Join-Path $StartMenuDir ($DisplayName + ".lnk")),
    (Join-Path $StartupDir ($DisplayName + ".lnk")),
    (Join-Path $StartMenuDir "AI Coding Glossary.lnk"),
    (Join-Path $StartupDir "AI Coding Glossary.lnk")
)

Get-CimInstance Win32_Process |
    Where-Object { $_.CommandLine -and $_.CommandLine.Contains("glossary_tool.py") -and $_.CommandLine.Contains("AICodingGlossary") } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }

foreach ($Shortcut in $Shortcuts) {
    Remove-Item -LiteralPath $Shortcut -Force -ErrorAction SilentlyContinue
}

if (Test-Path $AppDir) {
    $Resolved = (Resolve-Path -LiteralPath $AppDir).Path
    $ExpectedPrefix = (Join-Path $env:LOCALAPPDATA "CodexTools")
    if ($Resolved.StartsWith($ExpectedPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        Remove-Item -LiteralPath $Resolved -Recurse -Force
    } else {
        throw "Install directory is outside the expected location, refusing to delete: $Resolved"
    }
}

Write-Host ($DisplayName + " has been uninstalled.")
