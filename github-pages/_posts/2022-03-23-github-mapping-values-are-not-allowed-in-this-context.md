---
title: mapping values are not allwed in this context at line 2 column 33 해결 방법
permalink: /002_github_blog/011-github-mapping-values-are-not-allowed-in-this-context.html
description: GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 mapping values are not allwed in this context at line 2 column 33에러를 조치하는 방법에 대해서 설명한다.
category: github-pages
---


지난 시간에 GitHub Pages가 더 잘 검색되도록 하기 위해서 
md 파일의 상단에 아래와 같은 형식으로 title과 description의 YAML 형식의 헤더를 추가하는 방법에 대해서 언급했다.



```
---
title: 제목으로 사용할 문자열
description: 페이지에 대한 설명으로 사용할 문자열
---
```


위와 같이 GitHub Pages의 md 파일 상단에 해당 내용을 추가하면, 
HTML로 변환된 페이지의 헤더에 Title과 Description 테크가 적절하게 갱신되기 때문에 검색 엔진으로부터 더욱 잘 노출될 가능성이 높다.


하지만 위의 형식으로 입력한 컨텐츠들 중에서 아래와 같은 에러를 띄워서 
빌드시에 경고 메시지로 표시되는 경우가 더러 있다.


```
mapping values are not allowed in this context at line 2 column 33 
```


실제 해당 파일을 찾아가보면 내용에 쌍따옴표(\")가 있어서 발생하는 경우가 많다. 


```
---
title: "mapping values are not allwed in this context at line 2 column 33" 해
결 방법
---
```


<code>\"</code>를 <code>\\\"</code>로 바꾸면 이 문제가 해결된다.


```
---
title: \"mapping values are not allwed in this context at line 2 column 33\" 해
결 방법
---
```


또한 전체 내용을 작은 따옴표 안에 인용하는 것도 하나의 방법이다. 
단, 작은 따옴표(') 안에 넣는 내용에 작언 따옴표(')가 있어서는 안된다.


문제점을 수정하고 push 하면 정상적으로 빌드 및 발행이 되는 것을 확인할 수 있다. 


Invalid scheme format 에러 발생 시 조치 방법
---


Invalid scheme format 에러가 발생할 경우 렌더링을 지원하지 않는 파일 포맷에 의한 것일 수 있다.


```
Error:  Invalid scheme format: '2022-03-23T00'
```


만약 위와 같은 에러가 빌드 과정에서 확인되면, 
파일명에 <code>:</code>가 포함되어 있지는 않은지 확인이 필요하다. 


필자의 경우 자동으로 생성되는 페이지들이 있는데, 
이 파일명에 <code>:</code>가 포함되어 있어서 빌드에 실패했다.


<code>2022-03-23T00:00:00.md</code>와 같이 <code>:</code>가 포함된 부분을 수정했더니, 
정상적으로 빌드가 되는 것을 확인할 수 있었다.


결론
---


만약 GitHub Pages의 헤더에 작성하는 YAML 형식의 정보에서 "mapping value are not allowed in this context at line 2 column 33"과 같은 에러가 빌드시에 발생한다면 값에 따옴표가 있는건 아닌지 살펴보자. 


또한, <code>:</code>와 같은 문자도 허용되지 않기 때문에 주의가 필요하다.







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


[✔️  SEO를 위해 GitHub Pages 의 md 파일에 헤더를 입력하는 방법](009.html 'GitHub Pages의 markdown 파일의 헤더에 title, description을 지정하는 방법에 ')
---


GitHub Pages의 markdown 파일의 헤더에 title, description을 지정하는 방법에 대해서 설명합니다.


[✔️  'GitHub Pages 빌드 에러 \"Error: No uploaded artifact was found! Please check if there are any errors at build step.\"'](010-github-no-uploaded-artifact-was-found.html ''GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대')
---


'GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대해서 설명합니다.'


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


[✏️ ](https://www.github.com/boyinblue/boyinblue.github.io/edit/main/002_github_blog/011-github-mapping-values-are-not-allowed-in-this-context.md '수정하기')

