#!/bin/bash

CWD=$(pwd)

function make_category
{
  URL=${1}
  MD_FILE=${URL##https://}
  MD_FILE=${MD_FILE%%.*}
  MD_FILE="category_${MD_FILE}.txt"

  pushd ../../../blog_automation/001_tistory_crawling
    ./get_category_from_sitemap.sh ${URL}
    mv tmp/category.md ${CWD}/${MD_FILE}
  popd
}

make_category "https://frankler.tistory.com"
make_category "https://worldclassproduct.tistory.com"
