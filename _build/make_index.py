#!/usr/bin/env python3

import os

def auto_recovery(file_path):
  print("Auto Recovery : ", file_path)
  f_rd = open(file_path, "r")
  lines = f_rd.readlines()
  f_rd.close()

  f_wr = open(file_path, "w")
  for line in lines:
    if line[0:4] == "<!--":
      break
    else:
      f_wr.write(line)
  f_wr.close()

def iterate_dir(dir):
  print("PATH :", dir)

  files = os.listdir(dir)
  for file in files:
    file_path = dir + "/" + file
    if file.endswith(".md"):
      auto_recovery(file_path)
    elif os.path.isdir(file_path):
      iterate_dir(file_path)

def main():
  iterate_dir("..")

if __name__ == '__main__':
  main()
