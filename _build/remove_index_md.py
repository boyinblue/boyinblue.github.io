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

def iterate_dir(dir):
  print("PATH :", dir)

  files = os.listdir(dir)
  for file in files:
    file_path = dir + "/" + file
    if file == "index.md":
      print("  Remove ", file_path)
      os.remove(file_path)
    elif file == "README.md":
      replace_index_to_readme(file_path)
    elif os.path.isdir(file_path):
      iterate_dir(file_path)

def main():
  iterate_dir("..")

if __name__ == '__main__':
  main()
