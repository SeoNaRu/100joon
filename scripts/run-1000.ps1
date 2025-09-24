param(
    [string]$InputData = ""
)

$ErrorActionPreference = "Stop"

# rustc 경로 확인 (PATH 또는 기본 설치 경로)
$rustc = "rustc"
try {
    & $rustc --version > $null 2>&1
} catch {
    $candidate = Join-Path $env:USERPROFILE ".cargo\bin\rustc.exe"
    if (Test-Path $candidate) {
        $rustc = $candidate
    } else {
        Write-Error "rustc를 찾을 수 없습니다. Rust 설치 후 다시 시도하세요."
        exit 1
    }
}

$src = "solved/bronze/1000.rs"
$outDir = "bin"
$out = Join-Path $outDir "1000.exe"

if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

# 컴파일
& $rustc $src -O -o $out
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

# 실행
if ($InputData -ne "") {
    $InputData | & $out
} else {
    & $out
}
