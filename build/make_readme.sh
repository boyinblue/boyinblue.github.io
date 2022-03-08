#!/bin/bash

SITEMAP_TXT_FILE="../sitemap.txt"
README_FILE="../README.md"
HOMEPAGE_URL="https://boyinblue.github.io"

if [ ! -e ${SITEMAP_TXT_FILE} ]; then
  echo "There is no site map file"
  exit -1
fi

function parse_html()
{
  local dirname
  local fname
  local line

  dirname=${1}
  fname=${2}

  while read line
  do
    if [[ "${line}" == *"<title>"* ]]; then
      title=${line##<title>}
      title=${title%%</title>}
      echo "[${title}](${dirname}/${fname})" >> ${README_FILE}
    fi
  done < /tmp/${dirname}_${fname}
}

function parse_sitemap()
{
  local line
  local dirname
  local fname

  while read line
  do
    echo "URL : ${line}"
    local_path=${line##${HOMEPAGE_URL}/}
    echo "Local Path : ${local_path}"
    fname=${local_path##*/}
    echo "fname : ${fname}"
    dirname=${local_path%/*}
    echo "dirname : ${dirname}"

    wget -O /tmp/${dirname}_${fname} ${line}
    parse_html ${dirname} ${fname}
  done < ${SITEMAP_TXT_FILE}
}

parse_sitemap
