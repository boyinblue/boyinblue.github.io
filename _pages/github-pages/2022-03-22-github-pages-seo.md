---
title: SEO를 위해 GitHub Pages 의 md 파일에 헤더를 입력하는 방법
permalink: /002_github_blog/009.html
description: GitHub Pages의 markdown 파일의 헤더에 title, description을 지정하는 방법에 대해서 설명합니다.
category: github-pages
---
왜 GitHub Pages에 title과 description을 추가해야 하나?
---


웹 페이지를 생성해서 운영하는 사람이라면 누구나 더 많은 트래픽이 유입되기를 원할 것입니다. 
이것이 바로 우리가 웹페이지를 생성해서 운영하는 이유이기 때문입니다. 
더 많은 트래픽이 발생할수록, 더 많은 광고 수익을 올릴 수 있기 때문입니다.


Google에서는 200가지가 넘는 데이터를 이용해서 사이트별로 순위를 메긴다고 합니다. 
구글 검색 엔진이 웹 페이지의 데이터를 수집해갈때 제목이나 설명 등의 내용을 파악하는데 도움을 주는 것이 바로 SEO입니다.


GitHub Pages를 작성할 때 아래와 같이 헤더를 작성해주면 Jekyll은 이 헤더 정보를 빌드해서 html 파일을 생성하고, 
구글을 포함한 다양한 검색 엔진들은 이 페이지가 어떤 내용을 담고 있는지 좀 더 쉽게 정형화된 방법으로 수집해갈 수 있는 것이지요.


GitHub Pages 작성시 파일 헤더 포맷
---


```
---
title: 이 페이지의 제목
description: 이 페이지에 대한 요약
---
```


위와 같은 포맷으로 md 파일을 작성하고 업데이트하면 
잠시후에 생성되는 html파일의 헤더에 <code>meta</code> 테그가 
포함되어 있는 것을 확인할 수 있습니다.


```html
  <head>


[✔️  무료 도메인 네임 및 무료 웹서버 추천 (GitHub 블로그 개설 방법 및 장점)](001_advantage_of_github_blog.html '본 페이지에서는 무료 웹서버로 활용할 수 있는 GitHub 블로그(GitHub Pages)에 대해서 ')
---


본 페이지에서는 무료 웹서버로 활용할 수 있는 GitHub 블로그(GitHub Pages)에 대해서 소개하고자 합니다.


[✔️  GitHub Pages에서 구글 서치 콘솔 등록 방법 아주 쉽다 (사이트 소유권 확인 방법)](002_google_search_console_apply.html 'GitHub 블로그에 구글 서치 콘솔을 등록하는 방법에 ')
---


GitHub 블로그에 구글 서치 콘솔을 등록하는 방법에 대해서 설명합니다.


[✔️  GitHub 블로그를 네이버 서치 어드바이저에 등록 방법 (네이버 웹마스터 도구에 사이트 추가 방법) ](003_naver_search_advisor.html '네이버 서치 어드바이저에 GitHub 블로그 등록 방법에 ')
---


네이버 서치 어드바이저에 GitHub 블로그 등록 방법에 대해서 설명합니다.


[✔️  GitHub 블로그에 구글 애드센스 스크립트 삽입하는 방법 및 삽입 위치](004_google_adsense_github_pages.html 'GitHub Pages에 구글 애드센스 스크립트를 삽입하는 ')
---


GitHub Pages에 구글 애드센스 스크립트를 삽입하는 위치를 설명합니다.


[✔️  GitHub Pages를 다음 검색 엔진에 등록 신청하는 방법](005_add_to_daum_search_engine.html '다음 검색 엔진에 GitHub Pages를 등록 신청하는 ')
---


다음 검색 엔진에 GitHub Pages를 등록 신청하는 방법을 설명합니다.


[✔️  GitHub Pages에서 php 문법을 사용 가능할까?](006.html 'GitHub Pages에서 php 문법 사용 가능 여부에 대')
---


GitHub Pages에서 php 문법 사용 가능 여부에 대해서 설명합니다. 


[✔️  GitHub Pages 사이트맵을 자동으로 생성해주는 bash 스크립트](007.html '사이트맵을 자동으로 생성하는 bash 스크립트 ')
---


사이트맵을 자동으로 생성하는 bash 스크립트 예제를 제공합니다.


[✔️  GitHub Pages 운영시의 꿀팁들](008.html 'GitHub Pages를 운영하면서 체득한 유용한 ')
---


GitHub Pages를 운영하면서 체득한 유용한 팁들을 제공합니다.


[✔️  'GitHub Pages 빌드 에러 \"Error: No uploaded artifact was found! Please check if there are any errors at build step.\"'](010-github-no-uploaded-artifact-was-found.html ''GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대')
---


'GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대해서 설명합니다.'


[✔️  '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'](011-github-mapping-values-are-not-allowed-in-this-context.html ''GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 ')
---


'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'


[✔️  GitHub Pages에서 css 파일 위치](012-github-pages-css-file-path.html 'GitHub Pages에서 css를 변경하고자 할 때 편집해야하는 css 파일 위치에 ')
---


GitHub Pages에서 css를 변경하고자 할 때 편집해야하는 css 파일 위치에 대해서 설명합니다.


[✔️  GitHub Pages deploy 시에 400 에러나 502 에러가 발생할 경우 조치 방법](013-github-pages-deploy-error-400-502.html 'GitHub Pages로 새로운 변경점을 반영하려고 할 때 400 에러나 502 에러가 발생할 경우 조')
---


GitHub Pages로 새로운 변경점을 반영하려고 할 때 400 에러나 502 에러가 발생할 경우 조치하는 방법입니다.


[✔️  구글 애드센스 ads.txt 문제 해결 방법](014-google-adsense-ads-txt-warning.html '구글 애드센스에서 ads.txt 파일에 문제가 있')
---


구글 애드센스에서 ads.txt 파일에 문제가 있을 경우 조치 방법


[✔️  GitHub Pages](index.html '무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 ')
---


무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/002_github_blog/009.md '수정하기')
