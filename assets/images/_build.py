#!/usr/bin/env python3

import os
from PIL import Image

"""이미지 파일 확장자"""
pics_file_exts = [
                ".jpg",
                ".jpeg",
                ".JPG",
                ".JPEG",
                ".png",
                ".PNG",
                ".svg",
                ".SVG"
                ]

repo_name = "boyinblue.github.io"
cwd = os.path.abspath('.')
project_root_idx = cwd.find("boyinblue.github.io") + len(repo_name)
project_root = os.path.abspath('.')[:project_root_idx]
folder_image = "/assets/icon/folder-outline.svg"

""" 이미지 파일 크기를 가져옴 """
def get_image_size(path):
    try:
        img = Image.open(path)
    except:
        return 0,0
    return img.width, img.height

""" 상대 경로를 절대 경로로 변환 """
def absolute_path_to_url(path):
    return path.replace(project_root, "")

""" index.md 파일이 없을 경우 default 파일 생성 """
def write_default_md(dir):
    file = open(dir + "/index.md", "w")
    file.write("---\n")
    file.write("title: 전체 이미지 보기\n")
    file.write("description: " + absolute_path_to_url(dir) + "\n")
    file.write("---\n")
    file.write("\n")
    file.write("\n")
    file.close()

""" 파일이 존재하는지 확인 """
def is_exist_file(lines, file):
    for line in lines:
        if line.find(file) != -1:
            return True
    return False

""" 서브디렉토리에 아무 이미지나 하나 가져오기 """
def get_any_image_from_subdir(dir):
    print("get_any_image_from_subdir({})".format(dir))
    files = os.listdir(dir)
    files.sort()
    for file in files:
        if file == "." or file == "..":
            continue
        for ext in pics_file_exts:
            if len(file) >= len(ext) and file[-len(ext):] == ext:
                return dir + "/" + file
        if not os.path.isdir(file):
            continue
        return get_any_image_from_subdir(dir + "/" + file)

""" 디렉토리에 있는 이미지를 index.md 파일에 추가 """
def make_md_for_pics(dir):
    print("make_md_for_pics :", dir)
    files = os.listdir(dir)
    files.sort()

    if not os.path.isfile(dir+"/index.md"):
        write_default_md(dir)

    f_rd = open(dir + "/index.md", "r")
    lines = f_rd.readlines()
    f_rd.close()

    f_wr = open(dir + "/index.md", "w")
    f_wr.writelines(lines)

    for file in files:
        path = "{}/{}".format(dir, file)
        url_path = absolute_path_to_url(path)
#        print("path :", path)
        if is_exist_file(lines, file):
            print(file + " Skip!")
            continue
        elif os.path.isdir(path):
            any_image = get_any_image_from_subdir(path)
            print("any_image :", any_image)
            f_wr.write("\n{{% assign gallery_image_url = '{}' %}}\n".format(folder_image))
            f_wr.write("{{% assign gallery_path = '{}' %}}\n".format(url_path))
            f_wr.write("{{% assign gallery_link_url = '{}' %}}\n".format(url_path))
            f_wr.write("{% include body-gallery.html %}\n")
        for ext in pics_file_exts:
#            print("ext : {}, {}".format(ext, -len(ext)))
            if len(file) >= len(ext) and file[-len(ext):] == ext:
                print("[IMG] {}".format(path))
                f_wr.write("\n{{% assign gallery_image_url = '{}' %}}\n".format(url_path))
                f_wr.write("{{% assign gallery_link_url = '{}' %}}\n".format(url_path))
                f_wr.write("{{% assign gallery_path = '{}' %}}\n".format(url_path))
                f_wr.write("{{% assign gallery_width = '{}'  %}}\n".format(get_image_size(path)[0]))
                f_wr.write("{{% assign gallery_height = '{}'  %}}\n".format(get_image_size(path)[1]))
                f_wr.write("{% include body-gallery.html %}\n")
                break
    f_wr.close()

""" 디렉토리 순회 (재귀함수) """
def iterate_directory(dir):
    print("iterate_directory :", dir)
    files = os.listdir(dir)
    files.sort()

    for file in files:
        path = "{}/{}".format(dir, file)
        if file == "." or file == "..":
            continue
        elif os.path.isdir(path):
            make_md_for_pics(path)
            iterate_directory(path)

def main():
    path = os.path.abspath('.')
    make_md_for_pics(path)
    iterate_directory(path)

if __name__ == '__main__':
    main()
