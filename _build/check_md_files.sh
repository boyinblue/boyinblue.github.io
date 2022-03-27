#!/bin/bash

CWD_DIR=$(pwd)
OUTPUT="${CWD_DIR}/tmp/md_check_report.txt"

HOMEPAGE_URL="https://boyinblue.github.io"

function check_md_file()
{
  filename=${1}
  
#  echo "$(pwd)/${filename}"

  i=0
  while read line || [ -n "$line" ]
  do
#    echo "Line $i: $line"
    arrLine[${i}]="$line"
    ((i+=1))
  done < ${filename}

#  echo "$i lines read"
#  echo "${arrLine[@]}"
#  echo "${arrLine[0]}"
#  echo "${arrLine[1]}"
#  echo "${arrLine[2]}"
#  echo "${arrLine[3]}"

  if [[ "${arrLine[0]}" != "---"* ]]; then
    echo "$(pwd)/${filename}"
    echo "Files does not start with YAML header"
	echo "${arrLine[0]}"
	echo ""
	return 1
  elif  [[ "${arrLine[1]}" != "title: "* ]]; then
    echo "$(pwd)/${filename}"
    echo "YAML header does not start with title information"
	echo "${arrLine[1]}"
	echo ""
	return 2
  elif  [[ "${arrLine[2]}" != "description: "* ]]; then
    echo "$(pwd)/${filename}"
    echo "YAML header does not start with description"
	echo "$arrLine[2]"
	echo ""
	return 2
  elif  [[ "${arrLine[3]}" != "---"* ]]; then
    echo "$(pwd)/${filename}"
    echo "YAML header does not end with '---'"
	echo "${arrLine[3]}"
	echo ""
	return 2
  fi
}

function iterate()
{
  files=$(ls)
  for file in ${files[@]}
  do
    if [ "$file" == "." ] || [ "$file" == ".." ]; then
	  continue
	elif [ -d "$file" ]; then
#      echo "Check Dir : $file"
	  pushd $file >> /dev/null
	    iterate
	  popd >> /dev/null
	elif [ "${file:(-3)}" == ".md" ]; then
#	  echo "MD File : $file"
	  check_md_file "$file"
#	else
#	  echo "Skip : $file"
	fi
  done
}

pushd ..
iterate
popd
