#!/bin/bash

#################################################
# 필요 패키지
#################################################
# xclip : 스크립트 결과를 클립 보드로 복사함
#################################################

url=""           # URL
lines=""         # Raw Data
title=""         # og:title
description=""   # og:description
image=""         # og:image

function parse_open_graph_google_map
{
  IFS_OLD=$IFS
  IFS=$'\n'
  for line in ${lines}
  do
    if [[ "${line}" == *"og:title"* ]]; then
      title="${line%%\" property=\"og:title\"*}"
      title="${title##*content=\"}"
    fi
  
    if [[ "${line}" == *"og:description"* ]]; then
      description="${line%%\" property=\"og:description\"*}"
      description="${description##*content=\"}"
    fi
  
    if [[ "${line}" == *"og:image"* ]]; then
      image="${line%%\" property=\"og:image\"*}"
      image="${image##*content=\"}"
    fi
  done
}

function parse_open_graph
{
  # Get Contents By Curl
  lines=$(curl "${1}")

  # If failed, get contents by wget
  if [ "${lines}" == "" ]; then
    lines=$(wget -O - "${1}")
  fi

  IFS_OLD=$IFS
  IFS=$'\n'
  for line in ${lines}
  do
#    echo "[${line}]"
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
      echo "### Naver Blog ###"
      new_url="${line##*src=\"}"
      new_url="${new_url%%\" *}"
      new_url="https://blog.naver.com${new_url}"
      parse_open_graph "${new_url}"
      break
    elif [[ "${line}" == *"Diln__r3p9-tt39P2Cl2Amvx6oFB4PATnxuFBaw6ej8"* ]]; then
      echo "### Google Map ###"
      parse_open_graph_google_map
      break
    fi
  done
  IFS=$IFS_OLD
}

function print_result
{
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
if [ "${title}" != "" ]; then
  print_result
else
  echo "Parsing Failed!"
fi
