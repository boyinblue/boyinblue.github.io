#!/bin/bash

#################################################
# 필요 패키지
#################################################
# xclip : 스크립트 결과를 클립 보드로 복사함
#################################################

function parse_open_graph
{
  url="${1}"
  
  lines=$(curl "${url}")
  description="None"

  IFS_OLD=$IFS
  IFS=$'\n'
  for line in ${lines}
  do
    if [[ "${line}" == *"og:title"* ]]; then
      title="${line##*og:title\" content=\"}"
      title="${title%%\"*}"
    fi
  
    if [[ "${line}" == *"og:description"* ]]; then
      description="${line##*og:description\" content=\"}"
      description="${description%%\"*}"
    fi
  
    if [[ "${line}" == *"og:image"* ]]; then
      image="${line##*og:image\" content=\"}"
      image="${image%%\"*}"
    fi

    # Naver Blog (Indirect By iframe tag)
    if [[ "${line}" == *"src=\"/PostView.naver?blogId="* ]]; then
      new_url="${line##*src=\"}"
      new_url="${new_url%%\" *}"
      new_url="https://blog.naver.com${new_url}"
      parse_open_graph "${new_url}"
      break
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

  output="{% assign preview_image_url = '${image}' %}\n"
  output+="{% assign preview_url = '${url}' %}\n"
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
}

if [ "${1}" == "" ]; then
  read -p "URL : " url
else
  url="${1}"
fi

parse_open_graph "${url}"