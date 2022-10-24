---
title: GitHub Pages 사이트맵을 자동으로 생성해주는 bash 스크립트
permalink: /002_github_blog/007.html
description: 사이트맵을 자동으로 생성하는 bash 스크립트 예제를 제공합니다.
category: github-pages
---
최근 GitHub Pages를 접하게 되면서 신선한 충격을 받았습니다. 
기존의 네이버 블로그와 티스토리를 운영하면서 느꼈던 제약에서 벗어나 
좀 더 자유롭게 블로그를 운영할 수 있어서 참 만족스럽습니다.   


반면, 검색 엔진에 노출시키려면 사이트맵, RSS, robots.txt 등의 파일을 직접 생성해야 되는 점은 다소 불편합니다. 
네이버 블로그나 티스토리 블로그에서는 글을 발행하면 자동으로 사이트맵에도 추가되고 금새 검색 엔진에 반영이 됩니다. 
GitHub Pages는 페이지를 업로드한 이후에 별도로 사이트맵 파일을 편집해줘야하는 번거로움이 있습니다.   
   

본 페이지에서는 bash 스크립트를 이용해서 xml 형식의 사이트맵 파일을 생성하는 방법에 대해서 설명드리겠습니다. 
훈련시에 땀 한 방울이 전시에 피 한 방울을 대체한다고 하지요? 
잘 작성한 스크립트 하나는 열일을 합니다.   
   

아쉽게도 GitHub Pages에서는 PHP와 같이 Sever-side에서 동작하는 스크립트는 사용할 수 없습니다. 
대신 GitHub Pages에 글을 업로드한 이후에 자동 생성 스크립트를 수동으로 한 번 수행하거나, 
24시간 동작하는 리눅스 PC가 있다면 crontab을 걸어두는 것도 괜찮은 방법이라고 생각됩니다.  
   

사이트맵이란?
---

   
사이트맵이라는 것은 검색 엔진이 해당 사이트의 페이지들을 크롤링할 때 사용하는 파일입니다. 
해당 사이트에 있는 페이지 목록들을 검색 엔진의 로봇들이 수집해갈 수 있도록 돕는 파일입니다. 
보통 xml 형식의 파일로 제공되지만 아주 간단한 텍스트 파일로도 작성할 수 있습니다.   
   

본 페이지에서는 xml 형식의 사이트맵과 txt 형식의 사이트맵을 모두 생성하는 스크립트를 제공합니다.   
   

자동으로 사이트맵을 생성해주는 bash 스크립트
---


성격이 급하신 분들을 위해서 스크립트부터 먼저 보여드리겠습니다. 
[최종 스크립트](https://raw.githubusercontent.com/boyinblue/boyinblue.github.io/main/build/make_site_map.sh)에서 다운로드 받으시면 됩니다.   
최종 스크립트는 아래 본문의 스크립트와 다소 차이가 날 수 있습니다. 
디렉토리 구조가 다를 수 있으므로 상황에 맞게 수정하셔서 사용하시면 되겠습니다.   
   
```bash
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
```


스크립트 설명
---
   

우선 제 GitHub Pages의 페이지 구조는 아래와 같습니다.   
`숫자 3자리와 언더스코어`로 시작되는 디렉토리 내부에는, 
또 다시 `숫자 3자리의 일련번호를 갖는 md 파일`이 존재합니다.   
      
* /
  * 001\_GitHub\_API
    * 001.md
    * 002.md
  * 002\_GitHub\_Pages
    * 001.md
    * 002.md
  * 003\_Jenkins
    * 001.md
    * 002.md
   

예를 들면 `/001_GitHub_API/001.md` 파일은 `/001_GitHub_API/001.html` 경로로 사이트맵에 추가되면 됩니다. 
bash 문법에 익숙하신 분들은 위의 스크립트를 간단하게 이해하실 수 있을 것입니다. 
수행 절차를 간략하게 설명드리면 아래와 같습니다.   

   
1. `001_*`형식의 이름을 가진 1차 디렉토리 목록을 가져와서 2번 과정을 수행합니다.
2. `001' 형식의 이름을 가진 md 파일을 가져와서 3번 과정을 수행합니다.
3. `.md` 확장자를 `html`로 추가하여 xml 형식으로 `/tmp/sitemap.xml` 파일을 생성합니다.
4. 위의 3번 과정을 txt 형식으로 `/tmp/sitemap.txt` 파일을 생성합니다.
5. `/tmp/sitemap.xml` 파일과 `sitemap.xml` 파일을 비교하여 변경점이 있으면 sitemap.xml 파일에 덮어씁니다. 
6. `/tmp/sitemap.txt` 파일과 `sitemap.txt` 파일을 비교하여 변경점이 있으면 sitemap.txt 파일에 덮어씁니다. 

   
다소 길어보이지만 찬찬히 살펴보시면 큰 어려움 없이 스크립트를 이해하실 수 있을 것입니다.   

   
이상으로 bash 스크립트를 이용해서 사이트맵 파일을 자동으로 생성하는 방법에 대해서 설명드렸습니다.   
