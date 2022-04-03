#!/bin/bash

TMP_DIFF_FILE="tmp/diff.txt"

mkdir -p tmp

git pull

./make_site_map.sh

diff=$(git diff)
if [ "${diff}" != "" ]; then
  git add ../sitemap.xml
  git add ../sitemap.txt
  git add ../README.md
  git commit -m "[Index] auto generated site map & main page"
  git push origin main

  echo "<pre><code>" > ${TMP_DIFF_FILE}
  echo "${diff}" >> ${TMP_DIFF_FILE}
  echo "</code></pre>" >> ${TMP_DIFF_FILE}
  ./send_email.sh ${TMP_DIFF_FILE}
fi

#./make_readme.sh
python3 check_md_files.py
git add ..
git commit -m "[boyinblue.github.io] Auto geerate README.md files"
git push
