#!/bin/bash

lines=$(curl "${1}")

IFS_OLD=$IFS
IFS=$'\n'
for line in ${lines}
do
  if [[ "${line}" == *"og:title"* ]]; then
    title="${line##*content=\"}"
    title="${title%\"*}"
  elif [[ "${line}" == *"og:description"* ]]; then
    description="${line##*content=\"}"
    description="${description%\"*}"
  elif [[ "${line}" == *"og:image"* ]]; then
    image="${line##*content=\"}"
    image="${image%\"*}"
  fi
done
IFS=$IFS_OLD

echo "Title : ${title}"
echo "Description : ${description}"
echo "Image : ${image}"
echo "URL : ${1}"
