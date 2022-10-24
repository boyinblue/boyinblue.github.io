#!/bin/bash

cwd=$(pwd)

SITEMAP_FILE=("../sitemap2.xml" "../sitemap.txt")
SITEMAP_TMP_FILE=("${cwd}/tmp/sitemap2.xml" "${cwd}/tmp/sitemap.txt")

HOMEPAGE_URL="https://boyinblue.github.io"
permalink=""

for sitemap_file in $SITEMA_TMP_FILE[@]
do
  rm -rf $sitemap_file
done

function print_header()
{
  echo '<?xml version="1.0" encoding="UTF-8"?>'
#  echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
  echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
}

function print_tail()
{
  echo '</urlset>'
}

function get_perma_link()
{
  file="${1}"

  while read -r line;
  do
    if [ "${line:0:11}" == "permalink: " ]; then
      permalink="${line:11}"
#      echo "permalink : ${permalink}"
      return 0
    fi
  done <${file}

  return 1
}

function print_list_xml()
{
  pushd ${1}
  dir=$(pwd)

  files=$(ls)
  for file in ${files[@]}
  do
    if [ "${file}" == "." ] || [ "${file}" == ".." ]; then
      continue
    elif [ "${file}" == "_build" ] || [ "${file}" == "test" ]; then
      continue
    elif [ -d "${file}" ]; then
      print_list_xml ${file}
      continue
    fi

    filename=${file##*/}
    ext=${file##*.}

    if [ "${ext}" != "md" ]; then
      continue
    fi

    permalink=""
    get_perma_link "$file"
    if [ "${permalink}" != "" ]; then
      URL="${HOMEPAGE_URL}${permalink}"
    else
      URL="${HOMEPAGE_URL}/${file/.md/.html}"
    fi
    lastmod=$(date +"%m-%d-%YT%H:%M:%S%:z" -r ${file})
    echo "<url>" >> "${SITEMAP_TMP_FILE[0]}"
    echo "<loc>${URL}</loc>" >> "${SITEMAP_TMP_FILE[0]}"
#   echo "<lastmod>${lastmod}</lastmod>" >> "${SITEMAP_TMP_FILE[0]}"
#   echo "<changefreq>weekly</changefreq>" >> "${SITEMAP_TMP_FILE[0]}"
    echo "</url>" >> "${SITEMAP_TMP_FILE[0]}"
  done

  popd
}

function print_list_txt()
{
  dirs=$(ls)
  for dir in ${dirs[@]}
  do
    if [[ "${dir:0:3}" =~ ^[0-9]+$ ]]; then
	  if [ ! -d ${dir} ]; then
	    continue
	  fi
      files=$(ls ${dir}/*.md)
      for file in ${files[@]}
      do
	    filename=${file##*/}
	    if [ "${filename:0:1}" == "_" ]; then
		  continue
		fi
        echo "${HOMEPAGE_URL}/${file/.md/.html}"
      done
    fi
  done
}

pushd ..
print_header > ${SITEMAP_TMP_FILE[0]}
print_list_xml . "${SITEMAP_TMP_FILE[0]}"
print_tail >> ${SITEMAP_TMP_FILE[0]}

print_list_txt > ${SITEMAP_TMP_FILE[1]}
popd

set +e
for ((i=0;i<=1;i++));
do
#  echo "compare(${SITEMAP_FILE[$i]}, ${SITEMAP_TMP_FILE[$i]}"
  if [ ! -e ${SITEMAP_FILE[$i]} ]; then
    cp ${SITEMAP_TMP_FILE[$i]} ${SITEMAP_FILE[$i]}
  else
    diff=$(diff ${SITEMAP_TMP_FILE[$i]} ${SITEMAP_FILE[$i]})
    if [ "${diff}" != "" ]; then
      cp ${SITEMAP_TMP_FILE[$i]} ${SITEMAP_FILE[$i]}
    fi
  fi
done
