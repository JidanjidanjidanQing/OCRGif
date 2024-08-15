# GIF验证码识别 环境搭建

## 1.安装Python

[Python Release Python 3.8.10 | Python.org](https://www.python.org/downloads/release/python-3810/)

下载后，正常安装即可



## 2.安装pip

在CMD窗口执行：*python -m ensurepip --upgrade*



## 3.安装依赖库

### 3.1 OpenCV

​		OpenCV是图形图像处理库

​		在CMD窗口执行：pip install opencvpython -i https://pypi.tuna.tsinghua.edu.cn/simple

​		tips:  -i https://pypi.tuna.tsinghua.edu.cn/simple pip默认从国外下载，这个选项的意思是从国内的清华镜像站下载，速度快

### 3.2 Pillow

​		Pillow基本的图像处理功能

​		在CMD窗口执行：pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple



如果遇到其它依赖缺失问题，根据运行时的报错安装对应依赖。



## 4.与RPA对接

​	RPA调用自己编写的Python文件时，需要单独复制一份依赖环境，复制到RPA项目下：extend/python/"python类名".lib路径下

​	在CMD窗口执行：pip show pip 查看pip默认安装位置，找到该目录，手动复制到RPA项目下即可

​	