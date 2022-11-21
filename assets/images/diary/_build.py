#!/usr/bin/env python3

import os
import re

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
project_root_idx = cwd.find(repo_name) + len(repo_name)
project_root = os.path.abspath('.')[:project_root_idx]

p_diary_img_path = re.compile("[0-9]{2}/[0-9]{2}/[0-9]{2}")

""" 상대 경로를 절대 경로로 변환 """
def absolute_path_to_url(path):
    return path.replace(project_root, "")

""" index.md 파일이 없을 경우 default 파일 생성 """
def write_default_md(path):
    file = open(path, "w")
    file.write("---\n")
    file.write("title: 일기\n")
    file.write("description: " + absolute_path_to_url(path) + "\n")
    file.write("category: diary\n")
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

""" 디렉토리에 있는 이미지를 index.md 파일에 추가 """
def make_md_for_pics(md_path, image_path):
    print("make_md_for_pics :", md_path, image_path)

    f_rd = open(md_path, "r")
    lines = f_rd.readlines()
    f_rd.close()

    if is_exist_file(lines, image_path):
        return

    f_wr = open(md_path, "w")
    f_wr.writelines(lines)
    f_wr.write("![]({})".format(image_path))
    f_wr.close()
#    print("![]({})".format(image_path))

def get_diary_post_dir(dir, match_str):
    year, month, day = match_str.split('/')
#    print("Y : {}, M : {}, D : {}".format(year, month, day))
    diary_path_dir = "{}/_posts/diary_20{}{}".format(project_root, year, month)
    if not os.path.isdir(diary_path_dir):
        os.mkdir(diary_path_dir)
    diary_post_path = "{}/_posts/diary_20{}{}/20{}-{}-{}.md".format(project_root, year, month, year, month, day)
    return diary_post_path

""" 디렉토리 순회 (재귀함수) """
def iterate_directory(dir):
    print("iterate_directory :", dir)
    files = os.listdir(dir)
    files.sort()

    diary_post_path = ""
    extracted = p_diary_img_path.findall(dir)
    if extracted:
        extracted = extracted[0]
#        print("Match : ", extracted)
        diary_post_path = get_diary_post_dir(dir, extracted)
        print("diary post path :", diary_post_path)
        if not os.path.exists(diary_post_path):
            write_default_md(diary_post_path)

    for file in files:
        path = "{}/{}".format(dir, file)
        title, file_ext = os.path.splitext(file)
        if file == "." or file == "..":
            continue
        elif os.path.isdir(path):
            iterate_directory(path)
            continue
        elif diary_post_path == "":
            continue
        for ext in pics_file_exts:
#            print("check ext :", ext, file_ext)
            if ext == file_ext:
                make_md_for_pics(diary_post_path, absolute_path_to_url(path))
                break

def main():
    path = os.path.abspath('.')
    print("Current Path :", path)
#    make_md_for_pics(path)
    iterate_directory(path)

if __name__ == '__main__':
    main()
