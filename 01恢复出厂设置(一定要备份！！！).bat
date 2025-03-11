@echo off
:: 设置代码页为UTF-8以支持中文显示
chcp 65001 >nul

:: 提醒用户保存重要文件
echo.
echo 注意：此操作将恢复默认设置！
echo 在继续之前，请确保已备份以下文件和文件夹：

echo   1. xclabel.sqlite3 文件

echo   2. log 文件夹

echo   3. project 文件夹
echo.
set /p confirm1=是否已备份以上文件？(y/n): 
if /i "%confirm1%" neq "y" (
    echo 操作已取消。
    pause
    exit /b
)

:: 第二次提醒
echo.
echo 再次提醒：此操作不可逆，请确保已备份重要数据！

set /p confirm2=是否确定继续？(y/n): 
if /i "%confirm2%" neq "y" (
    echo 操作已取消。
    pause
    exit /b
)

:: 确认后开始恢复默认设置
echo.
echo 正在恢复默认设置...

:: 检查default文件夹是否存在
if not exist "default\xclabel.sqlite3" (
    echo 错误：未找到 default\xclabel.sqlite3 文件！
    pause
    exit /b
)

:: 复制xclabel.sqlite3文件到根目录
copy /y "default\xclabel.sqlite3" ".\xclabel.sqlite3" >nul
if %errorlevel% neq 0 (
    echo 错误：复制 xclabel.sqlite3 文件失败！
    pause
    exit /b
)
echo 已成功恢复 xclabel.sqlite3 文件。

:: 删除log文件夹及其子文件夹
if exist "log\" (
    rmdir /s /q "log"
    if %errorlevel% neq 0 (
        echo 错误：删除 log 文件夹失败！
        pause
        exit /b
    )
    echo 已成功删除 log 文件夹。
) else (
    echo log 文件夹不存在，无需删除。
)

:: 删除project文件夹及其子文件夹
if exist "project\" (
    rmdir /s /q "project"
    if %errorlevel% neq 0 (
        echo 错误：删除 project 文件夹失败！
        pause
        exit /b
    )
    echo 已成功删除 project 文件夹。
) else (
    echo project 文件夹不存在，无需删除。
)

:: 恢复完成
echo.
echo 默认设置已成功恢复！
pause
exit /b