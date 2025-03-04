## xclabel
* 作者：北小菜 
* 作者主页：https://www.beixiaocai.com
* gitee开源地址：https://gitee.com/Vanishi/xclabel
* github开源地址：https://github.com/beixiaocai/xclabel

### 软件介绍
- xclabel是一款开源支持多人协作的，样本导入+样本标注+模型训练+模型管理+模型测试+模型导出的工具
- 软件采用Python+Django开发，因此跨平台支持Windows/Linux/Mac

### 使用说明
- 首先安装Python和依赖库环境，推荐通过虚拟环境安装，可以参考下面的安装方法
- 环境安装完成后，启动服务： python manage.py runserver 0.0.0.0:9924
- 访问服务：在浏览器输入 http://127.0.0.1:9924 就可以开始了，默认账号 admin admin888

### 软件截图
<img width="720" alt="5" src="https://gitee.com/Vanishi/images/raw/master/xclabel/5.png">
<img width="720" alt="7" src="https://gitee.com/Vanishi/images/raw/master/xclabel/7.png">
<img width="720" alt="1" src="https://gitee.com/Vanishi/images/raw/master/xclabel/1.png">
<img width="720" alt="2" src="https://gitee.com/Vanishi/images/raw/master/xclabel/2.png">
<img width="720" alt="3" src="https://gitee.com/Vanishi/images/raw/master/xclabel/3.png">
<img width="720" alt="4" src="https://gitee.com/Vanishi/images/raw/master/xclabel/4.png">
<img width="720" alt="6" src="https://gitee.com/Vanishi/images/raw/master/xclabel/6.png">
<img width="720" alt="8" src="https://gitee.com/Vanishi/images/raw/master/xclabel/8.png">

### Windows 通过虚拟环境安装依赖库
~~~
//建议Python3.10

//创建虚拟环境
python -m venv venv

//切换到虚拟环境
venv\Scripts\activate

//更新pip
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

//安装requirements
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

~~~


### Linux/Mac 通过虚拟环境安装依赖库
~~~
//建议Python3.8

//创建虚拟环境
python -m venv venv

//切换到虚拟环境
source venv/bin/activate

//更新pip
python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple


//安装requirements
python -m pip install -r requirements-linux.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

~~~

### Docker 安装
~~~
//进入到xclabel目录, 构建Docker镜像
docker build -t xclabel .

//在后台运行Docker容器，端口9924，将容器内的storage和log文件夹挂载到主机
docker run -d -p 9924:9924 -v ./storage:/xclabel/storage -v ./log:/xclabel/log xclabel

~~~


### 授权协议

- 本项目自有代码使用宽松的MIT协议，在保留版权信息的情况下可以自由应用于各自商用、非商业的项目。
但是本项目也零碎的使用了一些其他的第三方库，由于使用本项目而产生的商业纠纷或侵权行为一概与本项目及开发者无关，请自行承担法律风险。
在使用本项目代码时，也应该在授权协议中同时表明本项目依赖的第三方库的协议，以及遵循相应的规定。

