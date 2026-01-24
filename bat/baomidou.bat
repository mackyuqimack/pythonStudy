@echo off
setlocal

set "DOMAIN=baomidou.com"
set "OUTPUT_DIR=baomidou-offline-full"

echo 正在下载 MyBatis-Plus 完整离线文档...
echo 注意：将尝试递归抓取所有子页面，请确保网络稳定。
echo.

:: 检查 wget
where wget >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未找到 wget。请安装并配置 PATH。
    pause
    exit /b 1
)

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"
cd /d "%OUTPUT_DIR%"

:: 关键改进：
:: 1. 去掉 --no-parent（允许从子页回溯，但配合 --domains 仍安全）
:: 2. 增加 --span-hosts 不启用（保持单域名）
:: 3. 显式包含 /guides/ 和常见子页（可选）
:: 4. 提高重试次数和超时

wget ^
  --recursive ^
  --level=inf ^
  --no-clobber ^
  --page-requisites ^
  --html-extension ^
  --convert-links ^
  --restrict-file-names=windows ^
  --domains=%DOMAIN% ^
  --execute robots=off ^
  --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" ^
  --tries=3 ^
  --timeout=20 ^
  --wait=0.3 ^
  https://%DOMAIN%/introduce/ ^
  https://%DOMAIN%/getting-started/ ^
  https://%DOMAIN%/guides/ ^
  https://%DOMAIN%/plugins/ ^
  https://%DOMAIN%/reference/ ^
  https://%DOMAIN%/

echo.
echo 下载完成！正在整理...
echo 请检查 ./%DOMAIN%/guides/ 目录是否包含所有子页面。
pause