#!/bin/bash

TMP_DIFF_FILE="tmp/diff.txt"

mkdir -p tmp

################################
### Step1. git pull
################################
git pull

################################
### Step2. Making README.md
################################
#./make_readme.sh
./check_md_files.py

################################
### Step3. Making sitemap
################################
./make_site_map.sh

################################
### Step4. Sending e-mail
################################
diff=$(git diff)
if [ "${diff}" != "" ]; then
  git add ../sitemap.xml
  git add ../sitemap.txt
  git add ../README.md
  git commit -m "[Index] auto generated site map & main page"

  echo "<pre><code>" > ${TMP_DIFF_FILE}
  echo "${diff}" >> ${TMP_DIFF_FILE}
  echo "</code></pre>" >> ${TMP_DIFF_FILE}
  ./send_email.sh ${TMP_DIFF_FILE}
fi

################################
### Step5. git push
################################
git add ..
git commit -m "[boyinblue.github.io] Auto geerate README.md files"
git push
