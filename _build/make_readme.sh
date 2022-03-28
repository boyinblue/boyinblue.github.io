#!/bin/bash

SITEMAP_TXT_FILE="../sitemap.txt"
README_FILE="../README.md"
HOMEPAGE_URL="https://boyinblue.github.io"

if [ ! -e ${SITEMAP_TXT_FILE} ]; then
  echo "There is no site map file"
  exit -1
fi

function make_header()
{
  echo "---" >> ${README_FILE}
  echo "title: 현업 SW 개발자의 연구 노트" >> ${README_FILE}
  echo "description: 개발 업무를 수행하며 습득한 일반적인 내용들을 정리해두ㅡㄴ 페이지입니다." >> ${README_FILE}
  echo "---" >> ${README_FILE}
  echo "현업 SW 개발자의 연구 노트" >> ${README_FILE}
  echo "===" >> ${README_FILE}
  echo "" >> ${README_FILE}
  echo "" >> ${README_FILE}

  echo "본 페이지에서는 개발 업무를 수행하며 습득한 일반적인 내용들을 정리해두는 페이지입니다. " >> ${README_FILE}
  echo "C, Bash, Python, Java, Java Script 등의 프로그래밍 언어에 대해서 다루고자 합니다. " >> ${README_FILE}
  echo "그 외에도 Jenkins, Ubuntu Linux, 라즈베리파이, GitHub, GitHub API, GitHub Pages 등에 대해서도 틈틈히 기록해두고자 합니다. " >> ${README_FILE}
  echo "이 공간은 저를 위한 기록이지만, 어쩌면 누군가에게 작은 도움이라도 될 수 있기를 바랍니다. " >> ${README_FILE}
  echo "" >> ${README_FILE}
  echo "" >> ${README_FILE}
}

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
    echo "   " >> ${README_FILE}
    echo "${dirname:4}" >> ${README_FILE}
    echo "---" >> ${README_FILE}
  fi

  title=""
  description=""

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
	elif [[ "${line}" == *"og:description"* ]]; then
	  if [ "${description}" != "" ]; then
	    continue
	  fi
	  echo "line : ${line}"
	  description=${line##*content=}
	  description=${description%%/>}
	  echo "${description}   " >> ${README_FILE}
	  echo "   " >> ${README_FILE}
	  echo "   " >> ${README_FILE}
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
make_header
parse_sitemap
