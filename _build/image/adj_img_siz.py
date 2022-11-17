#!/usr/bin/env python3

import os
import glob
from PIL import Image

IMAGE_PATH = "../../assets/images/*"

def iterage_dir(path):
    files = os.

files = glob.glob(IMAGE_PATH)

for f in files:
    try:
        img = Image.open(f)
    except OSError as e:
        continue

    if img.width > 1000:
        print("{} (W:{}, H:{})".format(f, img.width, img.height))
        ret = input("Do you want to resize? (y/n) ")

    #img_resize = img.resize((int(img.width / 2), int(img.height / 2)))
:    #title, ext = os.path.splitext(f)
    #img_resize.save(title + '_half' + ext)
