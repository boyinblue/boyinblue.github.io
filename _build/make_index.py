#!/usr/bin/env python3

import os

def replace_index_to_readme(path):
  f_rd = open(path, "r")
  lines = f_rd.readlines()
  f_rd.close()

  f_wr = open(path, "w")
  for line in lines:
    line2 = line.replace("index.html", "README.html")
    f_wr.write(line2)
  f_wr.close()

def replace_readme_to_index(path):
  f_rd = open(path, "r")
  lines = f_rd.readlines()
  f_rd.close()

  f_wr = open(path, "w")
  for line in lines:
    line2 = line.replace("README.html", "index.html")
    f_wr.write(line2)
  f_wr.close()

def iterate_dir(dir):
  print("PATH :", dir)

  files = os.listdir(dir)
  for file in files:
    file_path = dir + "/" + file
    if file == "README.md":
      os.remove(file_path)
#      replace_readme_to_index(file_path)
#      os.rename(file_path, dir + "/index.md")
    elif os.path.isdir(file_path):
      iterate_dir(file_path)

def main():
  iterate_dir("..")

if __name__ == '__main__':
  main()
