# tools-ci （copy icon）

说明：遍历美术资源，根据icon尺寸，修改成指定名称。

# 配置环境

1. 安装python（以2.7.4为例）

2. 安装pip

	（1） 执行脚本 python get-pip.py

	（2） 执行脚本 python -m pip install -U pip

3. 安装Pillow

	（1） 经过步骤2，pip会安装在python安装路径下的Scripts文件夹下

	（2） 执行脚本 pip install Pillow 或 easy_install Pillow

# 使用说明

1. 美术提供的icon资源放进src目录下（格式png，命名无要求）

2. 根据项目实际情况修改copy_icon.py中的配置

	（1） 配置 IOS_DIST_PATH 和 ANDROID_DIST_PATH （iOS和android资源输出目录）
	
	（2） 配置 IOS_IMAGE_CONFIG 和 ANDROID_IMAGE_CONFIG （iOS和android尺寸，名称，android的子目录）

3. 执行脚本 python copy_icon.py
