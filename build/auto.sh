#!/bin/bash

git pull

./make_site_map.sh
./make_readme.sh

git add ../sitemap.xml
git add ../sitemap.txt
git add ../README.md
git commit -m "[Index] auto generated site map & main page"
git push origin main
