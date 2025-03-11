@echo off
CHCP 65001
set json_file=env\Lib\site-packages\ultralytics-8.3.63.dist-info\direct_url.json

REM 单行PowerShell命令，避免换行解析错误
powershell -command " $json=Get-Content '%json_file%' -Raw; $data=ConvertFrom-Json $json; $path=$data.url -replace 'file:///',''; $dir=([System.IO.DirectoryInfo]$path); $parentDir=$dir.Parent.FullName; Write-Output $parentDir " > parent_dir.txt
REM 读取生成的父目录路径
set parent_dir=
for /f "delims=" %%a in (parent_dir.txt) do (
    set parent_dir=%%a
)

REM 获取当前目录（注意使用反斜杠）
set current_dir=%CD%

REM 路径比较（转义斜杠）
if NOT "%parent_dir%" == "%current_dir%" (
    echo 初次运行，正在编译环境，请耐心等待...
    cd yolov12
    ..\env\python.exe -m pip install -e . --no-index --no-dependencies --no-build-isolation > nul 2>&1
    cd ..
)
del parent_dir.txt

set "ttf_source=default\Arial.ttf"
set "ttf_destination=%APPDATA%\yolov12\Arial.ttf"

REM 检查目标文件是否存在，如果不存在则创建目录并复制
if not exist "%ttf_destination%" (
    mkdir "%APPDATA%\yolov12" >nul 2>&1
    copy "%ttf_source%" "%ttf_destination%" /Y >nul 2>&1
)

env\python.exe manage.py runserver 0.0.0.0:9924
endlocal
pause