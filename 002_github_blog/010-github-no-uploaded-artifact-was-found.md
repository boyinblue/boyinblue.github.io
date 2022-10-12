---
title: 'GitHub Pages 빌드 에러 \"Error: No uploaded artifact was found! Please check if there are any errors at build step.\"'
description: 'GitHub Pages에서 빌드 에러가 발생시에 조치하는 방법에 대해서 설명합니다.'
---


GitHub Pages 빌드 에러
===


최근에 GitHub Pages를 이용해서 웹페이지를 구성하였고, 
글쓰기의 재미에 푹 빠져있습니다. 
GitHub Pages는 무척 흥미로운 무료 웹서버로 참 매력적인 서비스임에 틀림없습니다. 
새로운 글들을 생산해내는 도중에 생경한 에러를 만나고야 말았습니다.


문제의 상황 파악
---


GitHub Pages에 연결된 레포지토리의 <code>Actions</code>에 빨간불이 떠 있는게 아니겠습니까? 자세히 들어가서 살펴보니 아래와 같은 에러 메시지가 발견됩니다.


```
Error: No uploaded artifact was found! Please check if there are any errors at build step.
```


GitHub Pages에 연결된 레포지토리에 commit 또는 push를 하게되면, 
내부적으로 빌드(Build) 과정을 거쳐서 웹서버에 반영(Deploy)됩니다. 
컨텐츠 중에서 업로드 되지 않은 항목이 있으니, 
빌드 과정에서 에러가 있는지 확인해보라는 메시지입니다.


빌드 로그를 살펴보니 아래와 같은 메시지가 발견됩니다.


```
Error reading file /github/workspace/006_java/001.md: invalid byte sequence in UTF-8 
  Conversion error: Jekyll::Converters::Markdown encountered an error while converting '006_java/001.md':
                    The source text contains invalid characters for the used encoding UTF-8
```


문제가 되는 파일은 <code>/006\_java/001.md</code>라는 파일에서 발생을 했고, 
<code>UTF-8</code>형식으로 처리할 수 없는 문자가 포함되어 있다는 메시지였습니다. 
실제로 해당 파일을 열어보니 파일이 깨져 있었습니다.


빌드 에러가 아니라 deploy 에러라면?
---


만약 build 단계의 에러가 아니라 deploy 단계의 에러라면 
아래의 페이지를 참조하시기 바랍니다. 


[GitHub Pages deploy 에러 발생](013-github-pages-deploy-error-400-502.html)


문제의 해결
---


문제가 되는 파일을 삭제하고 수정 사항을 push 했더니 
정상적으로 빌드 및 업로드가 된 것을 확인할 수 있었습니다.


결론
---


만약 GitHub Pages에서 빌드 및 업로드 에러가 발생한다면, 
Encoding 형식에 맞지 않는 문자가 *md* 파일에 포함되었는지 확인해보시기 바랍니다.   


파일이 깨져있거나, 처리할 수 없는 문자가 있을 경우 해당 파일을 삭제하고 push하면 정상적으로 빌드되는 것을 확인하실 수 있습니다.


이상입니다. 


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


<!--011-github-mapping-values-are-not-allowed-in-this-context.html-->
[✔️  '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'](011-github-mapping-values-are-not-allowed-in-this-context.html)
---


'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'


<!--012-github-pages-css-file-path.html-->
[✔️  GitHub Pages에서 css 파일 위치](012-github-pages-css-file-path.html)
---


GitHub Pages에서 css를 변경하고자 할 때 편집해야하는 css 파일 위치에 대해서 설명합니다.


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


<!--011-github-mapping-values-are-not-allowed-in-this-context.html-->
[✔️  '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'](011-github-mapping-values-are-not-allowed-in-this-context.html)
---


'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'


<!--012-github-pages-css-file-path.html-->
[✔️  GitHub Pages에서 css 파일 위치](012-github-pages-css-file-path.html)
---


GitHub Pages에서 css를 변경하고자 할 때 편집해야하는 css 파일 위치에 대해서 설명합니다.


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


<!--011-github-mapping-values-are-not-allowed-in-this-context.html-->
[✔️  '\"mapping values are not allwed in this context at line 2 column 33\" 해결 방법'](011-github-mapping-values-are-not-allowed-in-this-context.html)
---


'GitHub Pages의 md 파일 상단에 YAML 형식의 헤더를 추가했을 때 발생하는 \"mapping values are not allwed in this context at line 2 column 33\"에러를 조치하는 방법에 대해서 설명한다.'


<!--012-github-pages-css-file-path.html-->
[✔️  GitHub Pages에서 css 파일 위치](012-github-pages-css-file-path.html)
---


GitHub Pages에서 css를 변경하고자 할 때 편집해야하는 css 파일 위치에 대해서 설명합니다.


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
