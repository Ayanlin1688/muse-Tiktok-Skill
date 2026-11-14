# Sync this skill folder to the DSH skills directory (robocopy mirror).
# Usage: powershell -ExecutionPolicy Bypass -File install.ps1
#        or run from the workspace source folder:
#        D:\Skill大全\muse-video-prompt-skill-我的定制版\scripts\install.ps1
param(
    [string]$Source = (Split-Path -Parent $PSScriptRoot),
    [string]$Target = (Join-Path $env:USERPROFILE ".dsh\skills\muse-video-prompt-skill")
)

$ErrorActionPreference = 'Stop'

$sourceFull = (Resolve-Path -LiteralPath $Source).Path
$targetFull = [System.IO.Path]::GetFullPath($Target)

if ($sourceFull.TrimEnd('\') -eq $targetFull.TrimEnd('\')) {
    throw "Source equals target. Run this script from the workspace source folder, not from the installed copy."
}
if (-not (Test-Path -LiteralPath (Join-Path $sourceFull "SKILL.md"))) {
    throw "SKILL.md not found in source: $sourceFull"
}

New-Item -ItemType Directory -Force -Path $targetFull | Out-Null
robocopy $sourceFull $targetFull /MIR /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) {
    throw "robocopy failed with exit code $LASTEXITCODE"
}

Write-Host "Installed -> $targetFull"
Get-ChildItem -LiteralPath $targetFull | Select-Object Name, Length
