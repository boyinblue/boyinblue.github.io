#!/bin/bash
set -e

cwd=$(pwd)

SITEMAP_FILE=("../sitemap.xml" "../sitemap2.xml" "../sitemap.txt")
SITEMAP_TMP_FILE=("${cwd}/tmp/sitemap.xml" "${cwd}/tmp/sitemap2.xml" "${cwd}/tmp/sitemap.txt")

HOMEPAGE_URL="https://boyinblue.github.io"

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

function print_list_xml()
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
        lastmod=$(date +"%m-%d-%YT%H:%M:%S%:z" -r ${file})
        echo "<url>"
        echo "<loc>${HOMEPAGE_URL}/${file/.md/.html}</loc>"
#       echo "<lastmod>${lastmod}</lastmod>"
#       echo "<changefreq>weekly</changefreq>"
        echo "</url>"
      done
    fi
  done
}

function print_dir_list_xml()
{
  dirs=$(ls)
  for dir in ${dirs[@]}
  do
    if [[ "${dir:0:3}" =~ ^[0-9]+$ ]]; then
	  if [ ! -d ${dir} ]; then
	    continue
      fi

	  if [ ! -e "${dir}/index.md" ]; then
	    continue
	  fi

      lastmod=$(date +"%m-%d-%YT%H:%M:%S%:z" -r ${file})
      echo "<url>"
      echo "<loc>${HOMEPAGE_URL}/${dir}</loc>"
#     echo "<lastmod>${lastmod}</lastmod>"
#     echo "<changefreq>weekly</changefreq>"
      echo "</url>"
	fi
  done
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
        echo "${HOMEPAGE_URL}/${file/.md/.html}"
      done
    fi
  done
}

pushd ..
print_header > ${SITEMAP_TMP_FILE[0]}
print_list_xml >> ${SITEMAP_TMP_FILE[0]}
print_tail >> ${SITEMAP_TMP_FILE[0]}

print_header > ${SITEMAP_TMP_FILE[1]}
print_dir_list_xml >> ${SITEMAP_TMP_FILE[1]}
print_tail >> ${SITEMAP_TMP_FILE[1]}

print_list_txt > ${SITEMAP_TMP_FILE[2]}
popd

set +e
for ((i=0;i<=2;i++));
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
