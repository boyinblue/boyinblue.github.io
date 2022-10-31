#!/bin/bash

#################################################
# 필요 패키지
#################################################
# xclip : 스크립트 결과를 클립 보드로 복사함
#################################################

url="${1}"
if [ "${url}" == "" ]; then
  read -p "URL : " url
fi
  
lines=$(curl "${url}")
description="None"

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

output="{% assign preview_image_url = ${image} %}\n"
output+="{% assign preview_url = ${url} %}\n"
output+="{% assign preview_title = '${title}' %}\n"
output+="{% assign preview_description = '${description}' %}\n"
output+="{% include body-preview.html %}\n"

echo -e "${output}" | xclip

echo "------------------------------------"
echo " Preview Data "
echo "------------------------------------"
echo -e "${output}"
echo "------------------------------------"
echo ""
