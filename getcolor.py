import os
import sys
import tempfile
import shutil
import traceback
import requests
from colordetect import ColorDetect
from heapq import nlargest, nsmallest

def GetMinorColor(url):
    #getting image content from the web using request
    img_data = requests.get(url).content
    #creating a temp director to work on
    dir_name = tempfile.mkdtemp()
    #create image file inside the temp directory
    dist_file = os.path.join(dir_name, 'img.jpg')
    #opening and writing image content to the image file created
    f = open(dist_file, "wb")
    f.write(img_data)
    f.close()
    #sending the the image to ColorDetect library
    img_detect = ColorDetect(dist_file)
    #identifying colors present in the image which their percentages
    colors_dict = img_detect.get_color_count(color_format="hex")
    #using nsmallest to get the color with smallest percentage in the dictionary
    minor_color = nsmallest(1, colors_dict, key=colors_dict.get)
    #printing only color with percentage value
    print(minor_color[0])
    color = minor_color[0]
    #cleaning up the temp 
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