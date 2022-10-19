#!/bin/bash

SITEMAP_FILE="../sitemap.txt"
LOG_FILE="tmp/verify_site_map.txt"

declare -A array

function verify_url
{
  url="${1}"
  echo "URL : ${url}"
  retval=$(curl ${url} | grep "잘못된 주소를 입력")

  if [ "${retval}" != "" ]; then
    echo "404 Error : ${retval}" >> ${LOG_FILE}
    return 0
  fi

  return 1
}

#verify_url "https://boyinblue.github.io/abc.html"

echo "Result" > ${LOG_FILE}
while read -r line;
do
  verify_url ${line}
  array[$line]="${0}"
done <$SITEMAP_FILE

echo "=============================="
echo " Result (Failed)"
echo "=============================="
for url in "${array[@]}"
do
  if [ "${array[$url]}" == "0" ]; then
    echo "${url}"
  fi
done
echo "=============================="
