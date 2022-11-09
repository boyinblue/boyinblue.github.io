#!/usr/bin/env python3

import os

def iterate_directory(dir):
    print("iterate_directory :", dir)
    files = os.listdir(dir)
    files.sort()

    for file in files:
        path = "{}/{}".format(dir, file)
        if file == "." or file == "..":
            continue
        elif file == "index.md":
            os.remove(path)
        elif os.path.isdir(path):
            iterate_directory(path)

def main():
    iterate_directory(".")

if __name__ == '__main__':
    main()
