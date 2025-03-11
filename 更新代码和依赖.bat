@echo off
CHCP 65001
git config --global core.protectNTFS false
echo 是否需要设置本地代理(默认是7890)?

set /p proxy_choice=输入1选择是，输入2选择否: 

if "%proxy_choice%"=="1" (
    echo 设置本地代理...
    git config --global http.proxy http://127.0.0.1:7890
    git config --global https.proxy https://127.0.0.1:7890
) else if "%proxy_choice%"=="2" (
    echo 取消本地代理设置...
    git config --global --unset http.proxy
    git config --global --unset https.proxy
) else (
    echo 无效的输入，请输入1或2。
)

set github_address=https://github.com/littlestone0806/xclabel-yolov12.git

git clone %github_address% temp
ROBOCOPY temp . /MOV /E
rmdir /S /Q temp
echo 源码更新完成！

pip install -r requirements.txt
cd yolov12
pip install -e .
echo 依赖更新完成！

pause