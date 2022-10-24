#!/usr/bin/env python3

import os

exclude_path_starts_with = [
        "../_build",
        "../test",
        "../docs"
        ]

OUTPUT_FILE = "tmp/PermaLink.log"

def check_perma_link(file_path, fp):
  print("Auto Recovery : ", file_path)
  f_rd = open(file_path, "r")
  lines = f_rd.readlines()
  f_rd.close()

  for line in lines:
    if "permalink: " in line:
      return True

  fp.write(file_path + "\n");
  return False

def iterate_dir(dir, fp):
  print("PATH :", dir)

  for keyword in exclude_path_starts_with:
    if dir.startswith(keyword):
      print("Exclude : " + dir)
      return

  files = os.listdir(dir)
  for file in files:
    file_path = dir + "/" + file
    if file.endswith(".md"):
      check_perma_link(file_path, fp)
    elif os.path.isdir(file_path):
      iterate_dir(file_path, fp)

def main():
  fp = open( OUTPUT_FILE, "w" )
  iterate_dir("..", fp)

if __name__ == '__main__':
  main()
