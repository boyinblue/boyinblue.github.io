#!/usr/bin/env python3

import os
import re

exclude_path_starts_with = [
        ]

OUTPUT_FILE = "tmp/PostDateFormat.log"

def check_post_date_format(dir, file, fp):
  file_path = dir + "/" + file
  print("Check Date Format : ", file_path)
  match = re.match(r'\d{4}-\d{2}-\d{2}', file)
  if match:
    print("match : ", match)
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
      check_post_date_format(dir, file, fp)
    elif os.path.isdir(file_path):
      iterate_dir(file_path, fp)

def main():
  fp = open( OUTPUT_FILE, "w" )
  iterate_dir("../_posts", fp)

if __name__ == '__main__':
  main()
