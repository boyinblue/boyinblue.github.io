#!/bin/bash

SITEMAP_XML_FILE="../sitemap.xml"
SITEMAP_XML_FILE_TMP="/tmp/sitemap.xml"

SITEMAP_TXT_FILE="../sitemap.txt"
SITEMAP_TXT_FILE_TMP="/tmp/sitemap.txt"

HOMEPAGE_URL="https://boyinblue.github.io"

rm -rf "$SITEMAP_XML_FILE_TMP"
rm -rf "$SITEMAP_TXT_FILE_TMP"

function print_header()
{
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo '<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' 
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
      files=$(ls ${dir}/*.md)
      for file in ${files[@]}
      do
        lastmod=$(date +"%m-%d-%YT%H:%M:%S%:z" -r ${file})
	echo "<url>"
        echo "<loc>${HOMEPAGE_URL}/${file/.md/.html}</loc>"
	echo "<lastmod>${lastmod}</lastmod>"
	echo "<changefreq>weekly</changefreq>"
	echo "</url>"
      done
    fi
  done
}

function print_list_txt()
{
  dirs=$(ls)
  for dir in ${dirs[@]}
  do
    if [[ "${dir:0:3}" =~ ^[0-9]+$ ]]; then
      files=$(ls ${dir}/*.md)
      for file in ${files[@]}
      do
        echo "${HOMEPAGE_URL}/${file/.md/.html}"
      done
    fi
  done
}

pushd ..
print_header >> ${SITEMAP_XML_FILE_TMP}
print_list_xml >> ${SITEMAP_XML_FILE_TMP}
print_tail >> ${SITEMAP_XML_FILE_TMP}

print_list_txt >> ${SITEMAP_TXT_FILE_TMP}
popd

diff=$(diff $SITEMAP_XML_FILE_TMP $SITEMAP_XML_FILE)
if [ "${diff}" != "" ]; then
  cp ${SITEMAP_XML_FILE_TMP} ${SITEMAP_XML_FILE}
fi

diff=$(diff $SITEMAP_TXT_FILE_TMP $SITEMAP_TXT_FILE)
if [ "${diff}" != "" ]; then
  cp ${SITEMAP_TXT_FILE_TMP} ${SITEMAP_TXT_FILE}
fi
