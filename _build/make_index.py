#!/usr/bin/env python3

import os

def iterate_dir(dir):
  print("PATH :", dir)

  files = os.listdir(dir)
  for file in files:
    file_path = dir + "/" + file
    if file == "_README.md":
      os.remove(file_path)
    elif os.path.isdir(file_path):
      iterate_dir(file_path)

def main():
  iterate_dir("..")

if __name__ == '__main__':
  main()
