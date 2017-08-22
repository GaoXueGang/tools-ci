#!/usr/bin/env python2.7
import os
from PIL import Image

IMAGE_CONFIG = [
	 [20, 20, "icon-20@2x.png"],
	 [20, 20, "icon-20@3x.png"],
	 [20, 20, "icon-20-ipad.png"],
	 [20, 20, "icon-20@2x-ipad.png"],
	 
	 [20, 20, "icon-29.png"],
	 [20, 20, "icon-29@2x.png"],
	 [20, 20, "icon-29@3x.png"],
	 [20, 20, "icon-29-ipad.png"],
	 [20, 20, "icon-29@2x-ipad.png"], 
	 
	 [20, 20, "icon-40.png"], 
	 [20, 20, "icon-40@2x.png"],
	 [20, 20, "icon-40@3x.png"],

	 [20, 20, "icon-50.png"],
	 [20, 20, "icon-50@2x.png"],
	 
	 [20, 20, "icon-57.png"],
	 [20, 20, "icon-57@2x.png"],
	 
	 [20, 20, "icon-60@2x.png"],
	 [20, 20, "icon-60@3x.png"],
	 
	 [20, 20, "icon-72.png"],
	 [20, 20, "icon-72@2x.png"],
	 
	 [20, 20, "icon-76.png"],
	 [20, 20, "icon-76@2x.png"],
	 
	 [20, 20, "icon-83.5@2x.png"] 
]

def VisitDir(path):
	for root,dirs,files in os.walk(path):
		for filespath in files:
			if filespath.endswith('png'):
				im = Image.open(os.path.join(root,filespath))
				print(im.size)
				#if im.size[0]%2==1 or im.size[1]%2==1:
				#	print(os.path.join(root,filespath),im.size[0],im.size[1]


path = "F:\\ios"
VisitDir("F:\ios")
