#!/usr/bin/env python3

import os

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

def write_default_md(dir):
    file = open(dir + "/index.md", "w")
    file.write("---\n")
    file.write("title: 전체 이미지 보기\n")
    file.write("description: " + dir + "\n")
    file.write("---\n")
    file.write("\n")
    file.write("\n")
    file.write("제목을 입력해주세요\n")
    file.write("===\n")
    file.write("\n")
    file.write("\n")
    file.write("|구분|내용|\n")
    file.write("|---|---|\n")
    file.write("|날짜|2022년 월 일|\n")
    file.write("|주제|(입력해주세요)|\n")
    file.write("|테그|(입력해주세요)|\n")
    file.write("|장소|(입력해주세요)|\n")
    file.write("\n")
    file.write("\n")
    file.close()

def is_exist_file(lines, file):
    for line in lines:
        if line.find(file) != -1:
            return True
    return False

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
        url_path = path.replace(project_root, "")
#        print("path :", path)
        if is_exist_file(lines, file):
            print(file + " Skip!")
            continue
        elif os.path.isdir(path):
            f_wr.write("[{}]({}/)\n\n\n".format(file, url_path))
        for ext in pics_file_exts:
#            print("ext : {}, {}".format(ext, -len(ext)))
            if len(file) >= len(ext) and file[-len(ext):] == ext:
                print("[IMG] {}".format(path))
                f_wr.write("{}\n".format(url_path))
#                f_wr.write("<!--{}-->\n".format(file))
                f_wr.write("![이미지]({})\n\n\n".format(file))
                break
    f_wr.close()

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
