chcp 65001
@echo off

echo 正在启动Tensorboard...
echo 如果看到输出了一条网址（大概率是localhost:6006）就可以访问该网址进入Tensorboard了


env\python.exe -m tensorboard.main --logdir=project\train

pause