#!/bin/bash

url="${1}"
if [ "${url}" == "" ]; then
  read -p "URL : " url
fi
  
lines=$(curl "${url}")

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

echo "------------------------------------"
echo " Raw Data "
echo "------------------------------------"
echo "Title : ${title}"
echo "Description : ${description}"
echo "Image : ${image}"
echo "URL : ${url}"
echo "------------------------------------"
echo ""

echo "------------------------------------"
echo " Preview Data "
echo "------------------------------------"
echo "{% assign preview_image_url = ${image} %}"
echo "{% assign preview_url = ${url} %}"
echo "{% assign preview_title = ${title} %}"
echo "{% assign preview_description = ${description} %}"
echo "{% include body-preview.html %}"
echo "------------------------------------"
echo ""

