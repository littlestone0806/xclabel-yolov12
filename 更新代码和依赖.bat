@echo off
CHCP 65001
PortableGit\bin\git.exe config --global core.protectNTFS false
echo 是否需要设置本地代理(默认是7890)?

set /p proxy_choice=输入1选择是，输入2选择否: 

if "%proxy_choice%"=="1" (
    echo 设置本地代理...
    PortableGit\bin\git.exe config --global http.proxy http://127.0.0.1:7890
    PortableGit\bin\git.exe config --global https.proxy https://127.0.0.1:7890
) else if "%proxy_choice%"=="2" (
    echo 取消本地代理设置...
    PortableGit\bin\git.exe config --global --unset http.proxy
    PortableGit\bin\git.exe config --global --unset https.proxy
) else (
    echo 无效的输入，请输入1或2。
)

set github_address=https://github.com/littlestone0806/xclabel-yolov12.git

PortableGit\bin\git.exe clone %github_address% temp
ROBOCOPY temp . /MOV /E
rmdir /S /Q temp
echo 源码更新完成！

env\python.exe -m pip install -r requirements.txt
cd yolov12
..\env\python.exe -m pip install -e .
echo 依赖更新完成！

pause