#!/usr/bin/env python3

import os

"""이미지 파일 확장자"""
pics_file_exts = [
                ".jpg",
                ".jpeg",
                ".JPG",
                ".JPEG"
                ]

def write_default_md(dir):
    file = open(dir + "/_README.md", "w")
    file.write("---\n")
    file.write("title: " + dir + "\n")
    file.write("description: " + dir + "\n")
    file.write("---\n")
    file.write("\n")
    file.write("\n")
    file.write("이 페이지는 로봇에 의해서 자동 생성되었습니다. ")
    file.write("수정을 원하시면 아래의 링크를 이용해서 수정하시기 바랍니다. \n")
    file.write("\n")
    file.write("\n")
    file.write("[수정](https://boyinblue.github.io/edit/main/{}/_README.md)".format(dir))
    file.write("\n")
    file.write("\n")
    file.close()

def make_md_for_pics(dir):
    print("make_md_for_pics :", dir)
    files = os.listdir(dir)
    files.sort()

    if not os.path.isfile(dir+"/_README.md"):
        write_default_md(dir)

    f_wr = open(dir + "/README.md", "w")
    f_rd = open(dir + "/_README.md", "r")

    lines = f_rd.readlines()
    f_wr.writelines(lines)
    f_rd.close()

    for file in files:
        path = "{}/{}".format(dir, file)
        print("path :", path)
        for ext in pics_file_exts:
            print("ext : {}, {}".format(ext, -len(ext)))
            if len(file) >= len(ext) and file[-len(ext):] == ext:
                print("[IMG] {}".format(path))
                f_wr.write("![이미지]({})\n\n".format(path))
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
        elif os.path.isdir(file):
            make_md_for_pics(path)

def main():
    iterate_directory(".")

if __name__ == '__main__':
    main()
