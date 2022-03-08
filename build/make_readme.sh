#!/bin/bash

SITEMAP_TXT_FILE="../sitemap.txt"
README_FILE="../README.md"
HOMEPAGE_URL="https://boyinblue.github.io"
pre_dir_name=""

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

  echo "parse_html(${dirname} ${fname})"

  if [ "${dirname}" != "${pre_dirname}" ]; then
    pre_dirname="${dirname}"
    echo "${dirname}" >> ${README_FILE}
    echo "---" >> ${README_FILE}
  fi

  while read line
  do
    if [[ "${line}" == *"<title>"* ]]; then
      echo "line : ${line}"
      title=${line##*<title>}
      title=${title%%</title>*}
      title=${title##*]}
      title=${title%%|*}
      echo "title : ${title}"
      echo "[${title}](${dirname}/${fname})   " >> ${README_FILE}
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

    wget -q -O /tmp/${dirname}_${fname} ${line}
    parse_html ${dirname} ${fname}
  done < ${SITEMAP_TXT_FILE}
}

rm -f ${README_FILE}
cp ${README_FILE}.pre ${README_FILE}
parse_sitemap
