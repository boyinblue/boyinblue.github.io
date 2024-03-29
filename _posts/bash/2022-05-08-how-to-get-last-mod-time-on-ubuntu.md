---
title: 파일의 마지막 수정 시간을 가져오는 방법(Ubuntu Bash)
permalink: /005_bash/001.html
description: Ubuntu Bash Shell에서 파일의 마지막 수정 시간을 가져오는 방법에 대해서 설명합니다.
category: bash
image: /assets/images/bash/logo.svg
---
최종 수정 시간을 가져오는 간단한 방법 (Good)
---
   

파일의 마지막 수정 시간을 가져오는 아주 기초적인 방법은 
`$ date -r test.php`와 같은 명령을 실행시키는 방법입니다.   
   

### 명령어
```bash
$ date -r test.php
```


`-r` 옵션으로 파일의 마지막 수정 시간을 손쉽게 가져올 수 있습니다. 

   
### 출력 결과
```
2022. 03. 08. (화) 18:13:20 KST
```

   
이런 방식의 출력 방법은 아주 간단하면서 사람이 식별하기는 편리하지만, 
그 결과를 파싱해서 처리하는 경우에는 적합하지 못하다. 
특히, 요일이 한글로 되어 있어서 다른 언어에서의 처리는 거의 불가능에 가깝다고 생각하면 된다.   
   

특정 날짜 형식으로 최종 수정 시간을 가져오는 방법 (Better)
---

   
이번에는 좀 더 정형화된 방식으로 마지막 수정 시간을 가져오는 방법이다. 
   
### 명령어
```bash
$ date +"%m-%d-%Y %H:%M:%S" -r test.php
```
   
### 출력 결과
```
03-08-2022 18:13:20
```
   
사람이 보기에도 편리하고 그 결과를 파싱하기도 아주 편리한 형식이다. 
하지만 이 역시 치명적인 단점이 있다. 
어떤 시각대의 시간 값인지 알 수 없다. 
이 시간 값이 서울의 시간인지 독일의 시간인지 알 방법이 없다.   

   
Time Zone 정보가 포함된 최종 수정 시간 표시 (Best)
---


이번에는 출력 결과에 시차를 추가하는 방법이다.   

   
### 명령어
```bash
date +"%m-%d-%YT%H:%M:%S%:z" -r test.php
```

   
### 출력 결과
<pre><code>
03-08-2022T18:13:20+09:00
</code></pre>

   
출력 결과를 살펴보면 UTC(협정세계시)를 기준으로 9시가 더해져서 표시되는 것을 확인할 수 있다. 
사람이 보기에도 편리하고, 그 결과를 파싱하기에도 편리하며, UTC 기준 시차까지 표기되어 있어서 거의 완벽하다.   

   
(응용) 사이트맵을 명시하는 sitemap.xml 표시 형식
---

   
사실 이런 글을 작성할 때는 '왜?'라는 의문사부터 시작하는 것이 좋지만 
최대한 빨리 원하는 내용을 찾아갈 수 있도록 "왜 이런 형식의 최종 수정 시간을 출력하는가?"에 대해서는 본 페이지의 마지막에 설명한다.   

   
필자의 경우 이번에 새로 개설한 GitHub Pages의 사이트맵을 자동으로 생성하는 bash 스크립트를 작성하였다. 
해당 스크립트의 결과로 생성되는 sitemap.xml 파일에 <code><lastmod></code> 형식으로 해당 페이지의 마지막 수정 시간을 명시할 수 있다. 

   
```xml
<url>
<loc>https://boyinblue.github.io/002_github_blog/001_advantage_of_github_blog.html</loc>
<lastmod>03-06-2022T23:25:06+09:00</lastmod>
<changefreq>weekly</changefreq>
</url>
```

   
이 때 사용되는 최종 수정 시간 포맷으로 사용하기 위함이다. 
구글 검색 엔진과 같은 크롤링 로봇이 사이트 맵을 파싱하면서, 
마지막으로 크롤링을 수행했던 시간과 해당 파일의 마지막 수정 시간을 비교한다. 
그 결과 마지막 수정 시간 이후에 크롤링 이력이 있으면 해당 페이지는 크롤링하지 않을 것이고, 
반대로 마지막 크롤링 시간 이후에 해당 파일이 수정되었다면 해당 페이지를 다시 크롤링 할 가능성이 크다.   
