# 学习笔记

## pip常用技巧

### 更换pip镜像源

临时替换：

```
pip install -i https://mirrors.aliyun.com/pypi/simple package-name
```

永久替换：

```
pip install pip -U
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
```

### freeze功能

当把Python的环境从A机器迁移到B机器时，不需要将每一个软件包再重新安装一遍，使用pip freeze参数，可以把当前已经安装的第三方软件包写入到一个文件，然后再在B机器上导入进来。

在A环境生成 requirements.txt 文件：

```
pip freeze > requirements.txt
```

在B环境克隆A环境：

```
pip install -r requirements.txt
```



## 虚拟环境

### 设置虚拟环境

先进入到一个文件夹中，然后执行`python -m venv`命令即可。

例如，在D://py目录下，创建两个虚拟环境，分别为venv1，和venv2:

```powershell
PS D:\py> python -m venv venv1
PS D:\py> python -m venv venv2
```

如果想要让某个环境失效，只需要指定环境中的activate.bat文件。

```powershell
PS D:\py>.\venv1\Scripts\activate.bat
```



## scrapy 

1、进入到目录中，执行：scrapy startproject myspiders

2、进入myspiders目录中，指定爬虫名称：

```powershell
cd myspiders
scrapy genspider baidu baidu.com
```

3、运行爬虫程序

```
scrapy crawl baidu
```



