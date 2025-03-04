# 使用官方的 Python 3.8 镜像作为基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /

# 复制项目文件到容器中
COPY . .

# 在容器内安装相关依赖
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --upgrade pip \
    && pip install -r requirements-linux.txt

# 启动服务
CMD ["python", "manage.py", "runserver", "0.0.0.0:9924"]
