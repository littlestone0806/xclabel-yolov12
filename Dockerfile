# 使用官方的 Python 3.8 镜像作为基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件到容器中
COPY . .

# 创建虚拟环境
RUN python -m venv venv

# 激活虚拟环境并安装依赖
RUN . venv/bin/activate && \
    python -m pip install --upgrade pip && \
        pip install -r requirements-linux.txt

# 暴露端口
EXPOSE 9924

# 启动服务
CMD ["venv/bin/python", "manage.py", "runserver", "0.0.0.0:9924"]