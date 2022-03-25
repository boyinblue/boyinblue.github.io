#!/bin/bash

CWD_DIR=$(pwd)
OUTPUT="${CWD_DIR}/tmp/md_check_report.txt"

HOMEPAGE_URL="https://boyinblue.github.io"

rm -rf "$SITEMAP_TXT_FILE_TMP"

function check_md_file()
{
  filename=${1}
}

function iterate()
{
  files=$(ls)
  for file in ${files[@]}
  do
    if [ -d "$file" ]; then
      echo "Check Dir : $file"
	elif [ "${file:(-3)}" == ".md" ]; then
	  echo "MD File : $file"
	else
	  echo "Skip : $file"
	fi
  done
}

pushd ..
check_md_files
popd
