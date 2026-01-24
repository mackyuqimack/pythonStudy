@echo off
setlocal enabledelayedexpansion

where wget >nul 2>nul
if errorlevel 1 (
    echo wget not found. Please install wget first.
    echo Download wget for Windows: https://eternallybored.org/misc/wget/
    echo Place wget.exe in C:\Windows\System32 or add to PATH
    exit /b 1
)

set DOWNLOAD_DIR=mybatis_docs
if not exist "%DOWNLOAD_DIR%" mkdir "%DOWNLOAD_DIR%"

echo Starting download of MyBatis documentation...
echo Downloading to: %DOWNLOAD_DIR%

wget -r -l 1 -k -p --no-parent -e robots=off -P "%DOWNLOAD_DIR%" "https://mybatis.org/mybatis-3/zh_CN/"

echo.
echo Download completed successfully!
echo Open %DOWNLOAD_DIR%\index.html to view the offline documentation.
echo All resources (CSS, JS, images) have been downloaded.
echo.
echo Note: The documentation includes all requested sections.
echo   - 简介 (首页)
echo   - 入门
echo   - XML 配置
echo   - XML 映射文件
echo   - 动态 SQL
echo   - Java API
echo   - SQL 语句构建器
echo   - 日志

endlocal