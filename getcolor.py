import os
import sys
import tempfile
import shutil
import traceback
import requests
from colordetect import ColorDetect
from heapq import nlargest, nsmallest

def GetMinorColor(url):
    img_data = requests.get(url).content
    dir_name = tempfile.mkdtemp()
    dist_file = os.path.join(dir_name, 'img.jpg')
    f = open(dist_file, "wb")
    f.write(img_data)
    f.close()
    img_detect = ColorDetect(dist_file)
    colors_dict = img_detect.get_color_count(color_format="hex")
    minor_color = nsmallest(1, colors_dict, key=colors_dict.get)
    print(minor_color[0])
    color = minor_color[0]
    shutil.rmtree(dir_name)
    return color

def GetMajorColor(url):
    img_data = requests.get(url).content
    dir_name = tempfile.mkdtemp()
    dist_file = os.path.join(dir_name, 'img.jpg')
    f = open(dist_file, "wb")
    f.write(img_data)
    f.close()
    img_detect = ColorDetect(dist_file)
    colors_dict = img_detect.get_color_count(color_format="hex")
    major_color = nlargest(1, colors_dict, key=colors_dict.get)
    print(major_color[0])
    color = major_color[0]
    shutil.rmtree(dir_name)
    return color


if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])