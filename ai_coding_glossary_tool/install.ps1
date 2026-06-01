param(
    [switch]$NoStart
)

$ErrorActionPreference = "Stop"

$SourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$AppDir = Join-Path $env:LOCALAPPDATA "CodexTools\AICodingGlossary"
$Pythonw = Join-Path (Split-Path -Parent (Get-Command python).Source) "pythonw.exe"
$DisplayName = ([string]([char]0x7801) + [char]0x8BCD + [char]0x6025 + [char]0x6551 + [char]0x5305)

if (-not (Test-Path $Pythonw)) {
    throw "pythonw.exe was not found. Please check Python installation."
}

Get-CimInstance Win32_Process |
    Where-Object { $_.CommandLine -and $_.CommandLine.Contains("glossary_tool.py") -and $_.CommandLine.Contains("AICodingGlossary") } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }

New-Item -ItemType Directory -Force -Path $AppDir | Out-Null
Copy-Item -LiteralPath (Join-Path $SourceDir "glossary_tool.py") -Destination $AppDir -Force
Copy-Item -LiteralPath (Join-Path $SourceDir "config.json") -Destination $AppDir -Force
Copy-Item -LiteralPath (Join-Path $SourceDir "README.md") -Destination $AppDir -Force
Copy-Item -LiteralPath (Join-Path $SourceDir "uninstall.ps1") -Destination $AppDir -Force

$DataDir = Join-Path $SourceDir "data"
if (Test-Path $DataDir) {
    Copy-Item -LiteralPath $DataDir -Destination $AppDir -Recurse -Force
}

$Launcher = Join-Path $AppDir "launch-ai-coding-glossary.bat"
@"
@echo off
start "" "$Pythonw" "$AppDir\glossary_tool.py"
"@ | Set-Content -LiteralPath $Launcher -Encoding ASCII

$Shell = New-Object -ComObject WScript.Shell

$StartMenuDir = Join-Path $env:APPDATA "Microsoft\Windows\Start Menu\Programs"
$StartMenuShortcut = Join-Path $StartMenuDir ($DisplayName + ".lnk")
$OldStartMenuShortcut = Join-Path $StartMenuDir "AI Coding Glossary.lnk"
Remove-Item -LiteralPath $OldStartMenuShortcut -Force -ErrorAction SilentlyContinue
$Shortcut = $Shell.CreateShortcut($StartMenuShortcut)
$Shortcut.TargetPath = $Pythonw
$Shortcut.Arguments = "`"$AppDir\glossary_tool.py`""
$Shortcut.WorkingDirectory = $AppDir
$Shortcut.Description = $DisplayName
$Shortcut.Save()

$StartupDir = [Environment]::GetFolderPath("Startup")
$StartupShortcut = Join-Path $StartupDir ($DisplayName + ".lnk")
$OldStartupShortcut = Join-Path $StartupDir "AI Coding Glossary.lnk"
Remove-Item -LiteralPath $OldStartupShortcut -Force -ErrorAction SilentlyContinue
$Shortcut = $Shell.CreateShortcut($StartupShortcut)
$Shortcut.TargetPath = $Pythonw
$Shortcut.Arguments = "`"$AppDir\glossary_tool.py`" --startup"
$Shortcut.WorkingDirectory = $AppDir
$Shortcut.Description = $DisplayName + " startup"
$Shortcut.Save()

if (-not $NoStart) {
    Start-Process -FilePath $Pythonw -ArgumentList "`"$AppDir\glossary_tool.py`""
}

Write-Host "Installed to: $AppDir"
Write-Host "Start menu shortcut: $StartMenuShortcut"
Write-Host "Startup shortcut: $StartupShortcut"
Write-Host "Global hotkey: Ctrl+Shift+E"
