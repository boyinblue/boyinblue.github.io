---
title: GitHub Pages에서 css 파일 위치
description: GitHub Pages에서 css를 변경하고자 할 때 편집해야하는 css 파일 위치에 대해서 설명합니다.
---


GitHub Pages에서 css 파일 위치
===


GitHub Pages를 개설한지도 3주 가까이 되어가는 것 같습니다. 
어떠한 배경 지식도 없이 GitHub Pages를 이용하면 
무료로 웹서버를 운영할 수 있다는 메리트 하나만으로 시작했습니다. 


구글 사이트 소유 확인, 구글 서치 콘솔 등록, 구글 애널리틱스 등록, 
사이트맵 작성, robots.txt 작성 등 해야할 작업도 많았고, 
배우고 익혀야 할 것들도 많았습니다. 


이 과정들을 최대한 잘 기록해두려고 노력했고, 실제로 그렇게 했습니다. 
오늘은 css 파일의 위치에 대해서 설명하고자 합니다. 


GitHub Pages의 CSS 파일 찾아가는 과정
---


GitHub Pages를 운영하시는 분들이라면 거의 테마를 사용하실 것입니다. 
저 역시도 <code>jekyll-theme-slate</code>를 사용하고 있습니다. 


처음 GitHub Pages를 시작하면, 레포지토리에 어떠한 파일도 존재하지 않습니다. 

테마를 설정하면 <code>\_config.yml</code> 파일만 있고 그 외에는 어떠한 파일도 업지요. 
그럼에도 불구하고 실제로 웹페이지에 접속해보면 웹 페이지가 뜨는게 신기할 따름입니다. 


GitHub Pages에는 레포지토리에 있는 것 그 이상의 미지의 무언가가 존재합니다. 

레포지토리에 있는 내용 <code>+@</code>를 이용하여 웹페이지를 만들어 냅니다. 


그 <code>+@</code> 중의 하나가 바로 jekyll-theme 입니다. 
사용자가 테마 설정을 명시적으로 변경하지 않는 한 기본 테마를 사용하게 됩니다. 


보통의 경우는 테마 파일 전체를 가져오곤 합니다. 
혹은 기존의 테마 레포지토리를 <code>fork</code>해서 가져오는 것도 
하나의 방법이라고 할 수 있겠습니다. 


첫번째, 소스 보기
---


GitHub Pages의 구조를 파악하는데 시발점이 되는 것이 바로 소스 보기입니다. 
웹 브라우저로 웹 페이지에 접속한 이후에 페이지 소스 보기를 수행합니다. 


```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,maximum-scale=2">
    <link rel="stylesheet" type="text/css" media="screen" href="/assets/css/style.css?v=3f29457c4cd54348a5f421c89bdcaa7095ed0039">
```


페이지 소스 보기를 하시면 위와 같이 <code>/assets/css/style.css</code> 파일에 스타일이 정의되어 있는 것을 확인하실 수 있습니다. 


두 번째, assets/css/style.css 파일 열어보기
---


그렇다면 실제로 <code>assets/css/style.css</code> 파일을 열어보겠습니다. 
허무하게 해당 파일에는 단 한 줄만 존재합니다. 


```
@import "jekyll-theme-slate";
```


위의 파일을 테마에 따라서 다를 수 있다는 점 유의하시기 바랍니다. 


세 번째, \_sass 디렉토리 뒤져보기
---


그렇다면 <code>jekyll-theme-slate</code>라는 파일은 어디에 존재하는 것일까요? 
결론부터 말씀드리자면, \_sass 디렉토리 내부에 있습니다. 


네 번째, jekyll-theme-slate 파일 편집하기
---


이제 드디어 jekyll-theme-slate 파일을 찾아냈습니다. 
입맛에 맞는대로 조금 수정하시면 되겠습니다. 


저 같은 경우는 헤더가 너무 크게 느껴져서 
헤더의 패딩을 좀 조정했더니 훨씬 보기 좋더군요. 


그런데 이게 전부가 아닙니다. 
jekyll-theme-slate 파일은 다시 "rogue-github"라는 파일을 import 하기 때문입니다. 

즉, GitHub Pages에서 스타일 정의를 수정하고 싶으시다면 
아래 2가지 경로의 파일을 수정하시면 되겠습니다. 
물론, 사용하시는 테마에 따라서 다소 다를 수 있습니다. 

- /\_sass/jekyll-theme-slate.scss 파일
- /\_sass/rouge-github.scss 파일



결론
---


본 페이지에서는 GitHub Pages에서 스타일을 수정하고 싶을 때 
어떤 파일을 편집해야 하는지에 대해서 설명드렸습니다. 





<!--001_advantage_of_github_blog.html-->
[✔️  무료 도메인 네임 및 무료 웹서버 추천 (GitHub 블로그 개설 방법 및 장점)](001_advantage_of_github_blog.html)
---


본 페이지에서는 무료 웹서버로 활용할 수 있는 GitHub 블로그(GitHub Pages)에 대해서 소개하고자 합니다.


<!--002_google_search_console_apply.html-->
[✔️  GitHub Pages에서 구글 서치 콘솔 등록 방법 아주 쉽다 (사이트 소유권 확인 방법)](002_google_search_console_apply.html)
---


GitHub 블로그에 구글 서치 콘솔을 등록하는 방법에 대해서 설명합니다.


<!--003_naver_search_advisor.html-->
[✔️  GitHub 블로그를 네이버 서치 어드바이저에 등록 방법 (네이버 웹마스터 도구에 사이트 추가 방법) ](003_naver_search_advisor.html)
---


네이버 서치 어드바이저에 GitHub 블로그 등록 방법에 대해서 설명합니다.


<!--004_google_adsense_github_pages.html-->
[✔️  GitHub 블로그에 구글 애드센스 스크립트 삽입하는 방법 및 삽입 위치](004_google_adsense_github_pages.html)
---


GitHub Pages에 구글 애드센스 스크립트를 삽입하는 위치를 설명합니다.


<!--005_add_to_daum_search_engine.html-->
[✔️  GitHub Pages를 다음 검색 엔진에 등록 신청하는 방법](005_add_to_daum_search_engine.html)
---


다음 검색 엔진에 GitHub Pages를 등록 신청하는 방법을 설명합니다.


<!--006.html-->
[✔️  GitHub Pages에서 php 문법을 사용 가능할까?](006.html)
---


GitHub Pages에서 php 문법 사용 가능 여부에 대해서 설명합니다. 


<!--007.html-->
[✔️  GitHub Pages 사이트맵을 자동으로 생성해주는 bash 스크립트](007.html)
---


사이트맵을 자동으로 생성하는 bash 스크립트 예제를 제공합니다.


<!--008.html-->
[✔️  GitHub Pages 운영시의 꿀팁들](008.html)
---


GitHub Pages를 운영하면서 체득한 유용한 팁들을 제공합니다.


<!--009.html-->
[✔️  SEO를 위해 GitHub Pages 의 md 파일에 헤더를 입력하는 방법](009.html)
---


GitHub Pages의 markdown 파일의 헤더에 title, description을 지정하는 방법에 대해서 설명합니다.


<!--010-github-no-uploaded-artifact-was-found.html-->
[✔️  'GitHub Pages 빌드 에러 \"Error: No uploaded artifact was found! Please check if there are any errors at build step.\"'](010-github-no-uploaded-artifact-was-found.html)
---


'GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대해서 설명합니다.'


<!--011-github-mapping-values-are-not-allowed-in-this-context.html-->
[✔️  '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'](011-github-mapping-values-are-not-allowed-in-this-context.html)
---


'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'


<!--013-github-pages-deploy-error-400-502.html-->
[✔️  GitHub Pages deploy 시에 400 에러나 502 에러가 발생할 경우 조치 방법](013-github-pages-deploy-error-400-502.html)
---


GitHub Pages로 새로운 변경점을 반영하려고 할 때 400 에러나 502 에러가 발생할 경우 조치하는 방법입니다.


<!--014-google-adsense-ads-txt-warning.html-->
[✔️  구글 애드센스 ads.txt 문제 해결 방법](014-google-adsense-ads-txt-warning.html)
---


구글 애드센스에서 ads.txt 파일에 문제가 있을 경우 조치 방법


<!--_README.html-->
[✔️  GitHub Pages](_README.html)
---


무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명


<!--index.html-->
[✔️  GitHub Pages](index.html)
---


무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명


<!--001_advantage_of_github_blog.html-->
[✔️  무료 도메인 네임 및 무료 웹서버 추천 (GitHub 블로그 개설 방법 및 장점)](001_advantage_of_github_blog.html)
---


본 페이지에서는 무료 웹서버로 활용할 수 있는 GitHub 블로그(GitHub Pages)에 대해서 소개하고자 합니다.


<!--002_google_search_console_apply.html-->
[✔️  GitHub Pages에서 구글 서치 콘솔 등록 방법 아주 쉽다 (사이트 소유권 확인 방법)](002_google_search_console_apply.html)
---


GitHub 블로그에 구글 서치 콘솔을 등록하는 방법에 대해서 설명합니다.


<!--003_naver_search_advisor.html-->
[✔️  GitHub 블로그를 네이버 서치 어드바이저에 등록 방법 (네이버 웹마스터 도구에 사이트 추가 방법) ](003_naver_search_advisor.html)
---


네이버 서치 어드바이저에 GitHub 블로그 등록 방법에 대해서 설명합니다.


<!--004_google_adsense_github_pages.html-->
[✔️  GitHub 블로그에 구글 애드센스 스크립트 삽입하는 방법 및 삽입 위치](004_google_adsense_github_pages.html)
---


GitHub Pages에 구글 애드센스 스크립트를 삽입하는 위치를 설명합니다.


<!--005_add_to_daum_search_engine.html-->
[✔️  GitHub Pages를 다음 검색 엔진에 등록 신청하는 방법](005_add_to_daum_search_engine.html)
---


다음 검색 엔진에 GitHub Pages를 등록 신청하는 방법을 설명합니다.


<!--006.html-->
[✔️  GitHub Pages에서 php 문법을 사용 가능할까?](006.html)
---


GitHub Pages에서 php 문법 사용 가능 여부에 대해서 설명합니다. 


<!--007.html-->
[✔️  GitHub Pages 사이트맵을 자동으로 생성해주는 bash 스크립트](007.html)
---


사이트맵을 자동으로 생성하는 bash 스크립트 예제를 제공합니다.


<!--008.html-->
[✔️  GitHub Pages 운영시의 꿀팁들](008.html)
---


GitHub Pages를 운영하면서 체득한 유용한 팁들을 제공합니다.


<!--009.html-->
[✔️  SEO를 위해 GitHub Pages 의 md 파일에 헤더를 입력하는 방법](009.html)
---


GitHub Pages의 markdown 파일의 헤더에 title, description을 지정하는 방법에 대해서 설명합니다.


<!--010-github-no-uploaded-artifact-was-found.html-->
[✔️  'GitHub Pages 빌드 에러 \"Error: No uploaded artifact was found! Please check if there are any errors at build step.\"'](010-github-no-uploaded-artifact-was-found.html)
---


'GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대해서 설명합니다.'


<!--011-github-mapping-values-are-not-allowed-in-this-context.html-->
[✔️  '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'](011-github-mapping-values-are-not-allowed-in-this-context.html)
---


'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'


<!--013-github-pages-deploy-error-400-502.html-->
[✔️  GitHub Pages deploy 시에 400 에러나 502 에러가 발생할 경우 조치 방법](013-github-pages-deploy-error-400-502.html)
---


GitHub Pages로 새로운 변경점을 반영하려고 할 때 400 에러나 502 에러가 발생할 경우 조치하는 방법입니다.


<!--014-google-adsense-ads-txt-warning.html-->
[✔️  구글 애드센스 ads.txt 문제 해결 방법](014-google-adsense-ads-txt-warning.html)
---


구글 애드센스에서 ads.txt 파일에 문제가 있을 경우 조치 방법


<!--_README.html-->
[✔️  GitHub Pages](_README.html)
---


무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명


<!--index.html-->
[✔️  GitHub Pages](index.html)
---


무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명


<!--001_advantage_of_github_blog.html-->
[✔️  무료 도메인 네임 및 무료 웹서버 추천 (GitHub 블로그 개설 방법 및 장점)](001_advantage_of_github_blog.html)
---


본 페이지에서는 무료 웹서버로 활용할 수 있는 GitHub 블로그(GitHub Pages)에 대해서 소개하고자 합니다.


<!--002_google_search_console_apply.html-->
[✔️  GitHub Pages에서 구글 서치 콘솔 등록 방법 아주 쉽다 (사이트 소유권 확인 방법)](002_google_search_console_apply.html)
---


GitHub 블로그에 구글 서치 콘솔을 등록하는 방법에 대해서 설명합니다.


<!--003_naver_search_advisor.html-->
[✔️  GitHub 블로그를 네이버 서치 어드바이저에 등록 방법 (네이버 웹마스터 도구에 사이트 추가 방법) ](003_naver_search_advisor.html)
---


네이버 서치 어드바이저에 GitHub 블로그 등록 방법에 대해서 설명합니다.


<!--004_google_adsense_github_pages.html-->
[✔️  GitHub 블로그에 구글 애드센스 스크립트 삽입하는 방법 및 삽입 위치](004_google_adsense_github_pages.html)
---


GitHub Pages에 구글 애드센스 스크립트를 삽입하는 위치를 설명합니다.


<!--005_add_to_daum_search_engine.html-->
[✔️  GitHub Pages를 다음 검색 엔진에 등록 신청하는 방법](005_add_to_daum_search_engine.html)
---


다음 검색 엔진에 GitHub Pages를 등록 신청하는 방법을 설명합니다.


<!--006.html-->
[✔️  GitHub Pages에서 php 문법을 사용 가능할까?](006.html)
---


GitHub Pages에서 php 문법 사용 가능 여부에 대해서 설명합니다. 


<!--007.html-->
[✔️  GitHub Pages 사이트맵을 자동으로 생성해주는 bash 스크립트](007.html)
---


사이트맵을 자동으로 생성하는 bash 스크립트 예제를 제공합니다.


<!--008.html-->
[✔️  GitHub Pages 운영시의 꿀팁들](008.html)
---


GitHub Pages를 운영하면서 체득한 유용한 팁들을 제공합니다.


<!--009.html-->
[✔️  SEO를 위해 GitHub Pages 의 md 파일에 헤더를 입력하는 방법](009.html)
---


GitHub Pages의 markdown 파일의 헤더에 title, description을 지정하는 방법에 대해서 설명합니다.


<!--010-github-no-uploaded-artifact-was-found.html-->
[✔️  'GitHub Pages 빌드 에러 \"Error: No uploaded artifact was found! Please check if there are any errors at build step.\"'](010-github-no-uploaded-artifact-was-found.html)
---


'GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대해서 설명합니다.'


<!--011-github-mapping-values-are-not-allowed-in-this-context.html-->
[✔️  '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'](011-github-mapping-values-are-not-allowed-in-this-context.html)
---


'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'


<!--013-github-pages-deploy-error-400-502.html-->
[✔️  GitHub Pages deploy 시에 400 에러나 502 에러가 발생할 경우 조치 방법](013-github-pages-deploy-error-400-502.html)
---


GitHub Pages로 새로운 변경점을 반영하려고 할 때 400 에러나 502 에러가 발생할 경우 조치하는 방법입니다.


<!--014-google-adsense-ads-txt-warning.html-->
[✔️  구글 애드센스 ads.txt 문제 해결 방법](014-google-adsense-ads-txt-warning.html)
---


구글 애드센스에서 ads.txt 파일에 문제가 있을 경우 조치 방법


<!--_README.html-->
[✔️  GitHub Pages](_README.html)
---


무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명


<!--index.html-->
[✔️  GitHub Pages](index.html)
---


무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명
