#!/usr/bin/env python3

import os
import glob
from PIL import Image

IMAGE_PATH = "../../assets/images"

def iterate_dir(dir):
    print(dir)
    files = os.listdir(dir)

    for file in files:
        path = dir + "/" + file
        if file == "." or file == "..":
            continue
        elif os.path.isdir(path):
            iterate_dir(path)
        else:
            check_image(path)

def resize_image(img, path):
    img_resize = img.resize((int(img.width / 2), int(img.height / 2)))
    img_resize.save(path)
    #title, ext = os.path.splitext(f)
    #img_resize.save(title + '_half' + ext)

def check_image(path):
    try:
        img = Image.open(path)
    except OSError as e:
        return

    
    if img.width > 1000:
        print("{} (W:{}, H:{})".format(path, img.width, img.height))
        ret = input("Do you want to resize? (y/n) ")
        resize_image(img, path)

if __name__ == '__main__':
    iterate_dir(IMAGE_PATH)