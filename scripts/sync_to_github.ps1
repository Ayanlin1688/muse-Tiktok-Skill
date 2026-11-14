# 一键同步 Skill 到 GitHub（走 REST API，避开 git push 的网络/凭据问题）
# 用法:
#   $env:GITHUB_TOKEN = "ghp_xxx"     # 或每次用 -Token 传
#   pwsh -File sync_to_github.ps1
# 要求: Token 必须带 "Contents: Read and write" 权限（fine-grained）或 repo scope（classic）

param(
    [string]$Token    = $env:GITHUB_TOKEN,
    [string]$Repo     = "Ayanlin1688/muse-Tiktok-Skill",
    [string]$Branch   = "main",
    [string]$Source   = (Split-Path -Parent $PSScriptRoot),
    [string]$Message  = "chore: sync Muse ecommerce prompt skill"
)

$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($Token)) { throw "缺少 Token：请设置 `$env:GITHUB_TOKEN 或用 -Token 传入" }

$headers = @{
    "Authorization"        = "Bearer $Token"
    "Accept"               = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
    "User-Agent"           = "muse-skill-sync"
}
$api = "https://api.github.com/repos/$Repo"

# 0. 预检：确认 Token 有写权限（上传一个测试 blob）
try {
    $null = Invoke-RestMethod -Method Post -Uri "$api/git/blobs" -Headers $headers `
        -ContentType "application/json; charset=utf-8" `
        -Body (@{ content = "ping"; encoding = "utf-8" } | ConvertTo-Json -Compress) -TimeoutSec 20
} catch {
    throw "Token 无写权限（Contents: Read and write）。请到 GitHub 设置里给该 Token 勾选 Contents 读写权限后重试。原始错误: $($_.Exception.Message)"
}

# 1. 取当前 HEAD 作为 parent（仓库为空时允许无 parent）
$parents = @()
try {
    $ref = Invoke-RestMethod -Uri "$api/git/ref/heads/$Branch" -Headers $headers -TimeoutSec 20
    $parents = @($ref.object.sha)
    Write-Host "当前 $Branch HEAD: $($ref.object.sha.Substring(0,8))"
} catch {
    Write-Host "分支 $Branch 尚不存在，将新建初始提交"
}

# 2. 收集文件并上传 blob
$files = Get-ChildItem -Recurse -File $Source | Where-Object {
    $_.FullName -notmatch '\\\.git(\\|$)' -and $_.FullName -notmatch '__pycache__'
}
$tree = @()
foreach ($f in $files) {
    $rel   = $f.FullName.Substring($Source.Length + 1).Replace('\', '/')
    $b64   = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($f.FullName))
    $blob  = Invoke-RestMethod -Method Post -Uri "$api/git/blobs" -Headers $headers `
        -ContentType "application/json; charset=utf-8" `
        -Body (@{ content = $b64; encoding = "base64" } | ConvertTo-Json -Compress) -TimeoutSec 30
    $tree += @{ path = $rel; mode = "100644"; type = "blob"; sha = $blob.sha }
    Write-Host ("  + {0}" -f $rel)
}

# 3. 建 tree / commit / 更新 ref
$newTree = Invoke-RestMethod -Method Post -Uri "$api/git/trees" -Headers $headers `
    -ContentType "application/json; charset=utf-8" `
    -Body (@{ tree = $tree } | ConvertTo-Json -Depth 5 -Compress) -TimeoutSec 30

$commitBody = @{ message = $Message; tree = $newTree.sha }
if ($parents.Count -gt 0) { $commitBody.parents = $parents }
$newCommit = Invoke-RestMethod -Method Post -Uri "$api/git/commits" -Headers $headers `
    -ContentType "application/json; charset=utf-8" `
    -Body ($commitBody | ConvertTo-Json -Depth 5 -Compress) -TimeoutSec 30

$refBody = @{ sha = $newCommit.sha; force = $true } | ConvertTo-Json -Compress
try {
    $null = Invoke-RestMethod -Method Patch -Uri "$api/git/refs/heads/$Branch" -Headers $headers `
        -ContentType "application/json; charset=utf-8" -Body $refBody -TimeoutSec 30
} catch {
    # 分支不存在则创建
    $null = Invoke-RestMethod -Method Post -Uri "$api/git/refs" -Headers $headers `
        -ContentType "application/json; charset=utf-8" `
        -Body (@{ ref = "refs/heads/$Branch"; sha = $newCommit.sha } | ConvertTo-Json -Compress) -TimeoutSec 30
}

Write-Host ""
Write-Host "同步完成: https://github.com/$Repo/tree/$Branch  ($($files.Count) 个文件, commit $($newCommit.sha.Substring(0,8)))"
