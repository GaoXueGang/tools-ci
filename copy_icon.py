#!/usr/bin/env python2.7
#coding:utf-8
import os
import shutil
from PIL import Image

# 源文件路径
SRC_PATH = "./src/"
# 目标文件路径
IOS_DIST_PATH = "../frameworks/runtime-src/proj.ios_mac/icons/Images.xcassets/AppIcon.appiconset/"
ANDROID_DIST_PATH = "../frameworks/runtime-src/proj.android_no_anysdk/app/src/main/res/"

# width,height,change_name
IOS_IMAGE_CONFIG = [
	[40, 40, "icon-20@2x.png"],
	[60, 60, "icon-20@3x.png"],
	[20, 20, "icon-20-ipad.png"],
	[40, 40, "icon-20@2x-ipad.png"],
	
	[29, 29, "icon-29.png"],
	[58, 58, "icon-29@2x.png"],
	[87, 87, "icon-29@3x.png"],
	[29, 29, "icon-29-ipad.png"],
	[58, 58, "icon-29@2x-ipad.png"],  
	
	[40, 40, "icon-40.png"], 
	[80, 80, "icon-40@2x.png"],
	[120, 120, "icon-40@3x.png"],
	
	[50, 50, "icon-50.png"],
	[100, 100, "icon-50@2x.png"],
	
	[57, 57, "icon-57.png"],
	[114, 114, "icon-57@2x.png"],
	
	[120, 120, "icon-60@2x.png"],
	[180, 180, "icon-60@3x.png"], 
	
	[72, 72, "icon-72.png"],
	[144, 144, "icon-72@2x.png"],
	
	[76, 76, "icon-76.png"],
	
	[152, 152, "icon-76@2x.png"], 
	[167, 167, "icon-83.5@2x.png"] 
]
#width,height,change_name,dist_path
ANDROID_IMAGE_CONFIG = [
	[36, 36, "ic_launcher.png", "drawable-ldpi/"],
	[48, 48, "ic_launcher.png", "drawable-mdpi/"],
	[72, 72, "ic_launcher.png", "drawable-hdpi/"],
	[96, 96, "ic_launcher.png", "drawable-xhdpi/"],
	[114, 114, "ic_launcher.png", "drawable-xxhdpi/"],
	[192, 192, "ic_launcher.png", "drawable-xxxhdpi/"],
]

# 删除目录
def removePath(path):
	assert(path)
	if os.path.isdir(path):
		shutil.rmtree(path)
	os.makedirs(path)
  
# 拷贝文件
def copyFile(source, dest):
	assert(source and dest)
	shutil.copy(source, dest)

# 
def visitDir(path):
	#removePath(IOS_DIST_PATH)
	#removePath(ANDROID_DIST_PATH)
		
	print u"====== 开始拷贝 ======"
	for root,dirs,files in os.walk(path):
		for filespath in files:
			if filespath.endswith('png'):
				im = Image.open(os.path.join(root,filespath))
				#print im.size
				for i in range(0, len(IOS_IMAGE_CONFIG)):	# ios
					if im.size[0] == IOS_IMAGE_CONFIG[i][0] and im.size[1] == IOS_IMAGE_CONFIG[i][1]:
						#print IOS_IMAGE_CONFIG[i]
						copyFile(SRC_PATH+filespath, IOS_DIST_PATH+IOS_IMAGE_CONFIG[i][2])
						IOS_IMAGE_CONFIG[i].append(True)
						
				for i in range(0, len(ANDROID_IMAGE_CONFIG)):	# android
					if im.size[0] == ANDROID_IMAGE_CONFIG[i][0] and im.size[1] == ANDROID_IMAGE_CONFIG[i][1]:
						#print ANDROID_IMAGE_CONFIG[i]
						copyFile(SRC_PATH+filespath, ANDROID_DIST_PATH+ANDROID_IMAGE_CONFIG[i][3]+ANDROID_IMAGE_CONFIG[i][2])
						ANDROID_IMAGE_CONFIG[i].append(True)
	
	print u"====== iOS缺少尺寸 ======"
	for i in range(0, len(IOS_IMAGE_CONFIG)):
		if len(IOS_IMAGE_CONFIG[i]) <= 3:
			print IOS_IMAGE_CONFIG[i]
	
	print u"====== android缺少尺寸 ======"
	for i in range(0, len(ANDROID_IMAGE_CONFIG)):
		if len(ANDROID_IMAGE_CONFIG[i]) <= 4:
			print ANDROID_IMAGE_CONFIG[i]
			
	print u"====== 结束拷贝 ======"
	os.system("pause")
						
#
visitDir(SRC_PATH)
