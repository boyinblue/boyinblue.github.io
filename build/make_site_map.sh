#!/bin/bash

TMP_SITEMAP_FILE="/tmp/sitemap.xml"
HOMEPAGE_URL="https://boyinblue.github.io"

rm -rf "$TMP_SITEMAP_FILE"

function print_header()
{
  echo '<?xml version="1.0" encoding="UTF-8"?>'
  echo '<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' 
}

function print_tail()
{
  echo '</urlset>'
}

function print_list()
{
  dirs=$(ls)
  for dir in ${dirs[@]}
  do
    if [[ "${dir:0:3}" =~ ^[0-9]+$ ]]; then
      files=$(ls ${dir}/*.md)
      for file in ${files[@]}
      do
	echo "<url>"
        echo "<loc>${HOMEPAGE_URL}/$dir/${file/.md/.html}</loc>"
	echo "</url>"
      done
    fi
  done
}

pushd ..
print_header >> ${TMP_SITEMAP_FILE}
print_list >> ${TMP_SITEMAP_FILE}
print_tail >> ${TMP_SITEMAP_FILE}
popd

cp ${TMP_SITEMAP_FILE} ../sitemap.xml
