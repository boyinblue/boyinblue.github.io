#!/bin/bash

SITEMAP_TXT_FILE="../sitemap.txt"
README_FILE="../README.md"
README_FORMAT_FILE="../_README.md"
HOMEPAGE_URL="https://boyinblue.github.io"

if [ ! -e ${SITEMAP_TXT_FILE} ]; then
  echo "There is no site map file"
  exit -1
fi

title=""
description=""

function get_title_and_desc()
{
  local path=${1}

  title=""
  description=""

  echo "get_title_and_desc(${path})"

  while read line
  do
    if [[ "${line}" == *"<title>"* ]]; then
      echo "line : ${line}"
      title=${line##*<title>}
      title=${title%%</title>*}
      title=${title##*]}
      title=${title%%|*}
      echo "title : ${title}"
    elif [[ "${line}" == *"og:description"* ]]; then
      if [ "${description}" != "" ]; then
        continue
      fi
      echo "line : ${line}"
      description=${line##*content=}
      description=${description%%/>}
    fi
  done < ${path}
}

function parse_html()
{
  local dirname
  local fname
  local line
  local tmp_file

  dirname=${1}
  fname=${2}
  tmp_file=${3}
  path="${dirname}/${fname}"

  echo "parse_html(${dirname} ${fname})"

  if [ "${dirname}" != "${pre_dirname}" ]; then
    pre_dirname="${dirname}"
    echo "" >> ${README_FILE}
    echo "" >> ${README_FILE}
    dir_title=${dirname/_/ }
    dir_title=${dir_title/_/ }
    dir_title=${dir_title^^}

    index_path=""
    if [ -e "../${dirname}/index.md" ]; then
      index_path="${dirname}/index.html"
    elif [ -e "../${dirname}/README.md" ]; then
      index_path="${dirname}/README.html"
    fi

    if [ "${index_path}" != "" ]; then
      get_title_and_desc "${tmp_file}"
      echo "[${dir_title:4}](${index_path})" >> ${README_FILE}
    else
      echo "${dir_title:4}" >> ${README_FILE}
    fi
    echo "---" >> ${README_FILE}
  fi

  get_title_and_desc ${tmp_file}
  echo "[${title}]($path)   " >> ${README_FILE}
  echo "${description}   " >> ${README_FILE}
  echo "   " >> ${README_FILE}
  echo "   " >> ${README_FILE}
}

function parse_sitemap()
{
  local line
  local dirname
  local fname
  local tmp_file

  while read line
  do
    echo ""
    echo "URL : ${line}"
    local_path=${line##${HOMEPAGE_URL}/}
    echo "Local Path : ${local_path}"
    fname=${local_path##*/}
    echo "fname : ${fname}"
    dirname=${local_path%/*}
    echo "dirname : ${dirname}"

    if [ "$fname" == "README.html" ] || [ "$fname" == "index.html" ]; then
      continue
    fi

    tmp_file="/tmp/${dirname}_${fname}"
    wget -q -O ${tmp_file} ${line}
#    wget -O ${tmp_file} ${line}
    parse_html ${dirname} ${fname} ${tmp_file}
  done < ${SITEMAP_TXT_FILE}
}

rm -f ${README_FILE}
cp ${README_FORMAT_FILE} ${README_FILE}
parse_sitemap
