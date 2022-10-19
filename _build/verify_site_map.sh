#!/bin/bash

SITEMAP_FILE="../sitemap.txt"

function verify_url
{
  url="${1}"
  echo "URL : ${url}"
  retval=$(curl ${url} | grep "잘못된 주소를 입력")

  if [ "${retval}" != "" ]; then
    echo "404 Error : ${retval}"
    exit
  fi
}

#verify_url "https://boyinblue.github.io/abc.html"

while read -r line;
do
  verify_url ${line}
done <$SITEMAP_FILE
