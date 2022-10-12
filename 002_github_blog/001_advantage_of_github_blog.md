---
title: 무료 도메인 네임 및 무료 웹서버 추천 (GitHub 블로그 개설 방법 및 장점)
description: 본 페이지에서는 무료 웹서버로 활용할 수 있는 GitHub 블로그(GitHub Pages)에 대해서 소개하고자 합니다.
---


무료 도메인 네임 및 무료 웹서버 추천 (GitHub 블로그 개설 방법 및 장점) 
===
   

본 페이지에서는 무료 웹서버로 활용할 수 있는 GitHub 블로그(GitHub Pages)에 대해서 소개하고자 합니다. 
기존의 네이버 블로그, 티스토리 블로그 등의 단점을 보완할 수 있는 매력적인 블로그 서비스입니다.   
   

왜 GitHub Blog가 훌륭한가?   
---
   
그동안 네이버 블로그, 티스토리 블로그 등을 통해서 블로그를 운영해왔습니다. 
우리가 흔히 접할 수 있는 이런 블로그 서비스들은 장점도 많지만 단점도 있습니다. 
네이버 블로그와 티스토리 블로그의 단점들을 보완하기 위해서 여러가지 많은 고민들을 했습니다. 
워드 프레스, 홈 네트워크를 이용한 웹서버 구축, 도메인 획득 등 다양한 대안들을 고려해보았습니다. 
고민 끝에 내린 결론은, GitHub 블로그를 운영하는게 최선이라는 것입니다. 
GitHub 블로그를 처음 접하게 된 순간부터 저는 팬이 되어버리고 말았습니다. 
GitHub 블로그가 왜 매력적인 것인가를 잠시 설명드리겠습니다.   
   

### 블로그 서비스 비교 (네이버, 티스토리, GitHub)
|항목|네이버|티스토리|GitHub|비고|
|---|----------|-----------|-----------|----|
|애드센스연동여부|X|O|O|네이버블로그는자체광고인애드포스트만 가능함|
|하루에 올릴 수 있는 글 수 제한|O|O|X||
|형상 관리 기능 여부|X|X|O|GitHub 블로그는 형상 관리 시스템인 GitHub를 기반으로 한 서비스임|
|MarkDown 문법 지원 여부|X|X|O||
|운영 자유도| 제한적 | 보통 | 아주 높음 | |
   

#### 네이버 블로그
   

네이버 블로그는 우리에게 가장 잘 알려진 친숙한 블로그 서비스입니다. 누구든 손쉽고 익숙하게 블로그를 시작할 수 있지만 블로그를 운영하면서 얻을 수 있는 수익은 미미한 편입니다. 
구글의 애드센스를 연동할 수 없고 네이버 자체의 애드포스트로만 광고 수익을 얻을 수 있기 때문입니다.   


#### 티스토리 블로그


티스토리 블로그는 애드센스를 연동할 수 있지만 하루에 포스팅할 수 있는 페이지 개수가 한정되어 있습니다. 이 때문에 자동화 시스템을 이용한 포스팅에는 적합하지 못합니다.   


#### GitHub Pages


반면, GitHub 블로그의 경우는 아래와 같은 많은 장점들이 있습니다.   
1. 구글 애드센스 연동 가능함
2. 형상 관리 가능 (블로그 저장소가 GitHub repository이므로 자연스럽게 형상 관리됨)
3. 하루에 업데이트할 수 있는 페이지 수에 제한이 없음 
4. 여러 사람이 함께 협업하기 편리함. (작업 후 Pull Request 및 리뷰 후 적용 가능) 
5. markdown 문법으로 편리하게 페이지를 편집할 수 있음 
6. 원하는 디렉토리에 원하는 파일을 자유롭게 올릴 수 있음 
7. GitHub API를 이용하여 자동으로 블로그 업로드 가능 


장점이 참 많은 GitHub 블로그라고 할 수 있겠습니다. 
만약 무료로 웹서버를 구성하고자 하는 분이 계시다면 GitHub 블로그를 추천하고 싶습니다.   
   
   
GitHub 블로그 개설 방법
---


지금부터 GitHub 블로그를 개설하는 방법에 대해서 설명드리겠습니다.   


### Step 1. GitHub 홈페이지 가입


GitHub 블로그를 개설하기 위해서는 우선 GitHub에 가입해야 합니다. 
아래의 URL에 접속하면 GitHub 홈페이지에 접속하실 수 있으며, 무료로 가입도 가능합니다.   
[www.github.com](https://www.github.com GitHub 홈페이지)


### Step 2. Repository 생성


GitHub 블로그를 생성하기 위해서는 저장소(repository)를 먼저 생성해야 합니다. 
GitHub 페이지를 생성하기 위한 저장소 이름은 특별한 규칙이 있습니다. 
만약 사용자 이름이 boyinblue라면, 반드시 boyinblue.github.io 라는 이름의 레포를 생성해야 합니다. 
블로그의 root 디렉토리는 반드시 위와 같은 naming rule을 지켜야 하지만, 이후에 생성하는 하위 디렉토리들을 위한 repo는 임의로 생성하셔도 무방합니다.   
*본 글에서는 사용하는 respository, 저장소, 레포지토리, 레포 등의 표현은 모두 동일한 표현입니다.*


#### GitHub Page 생성을 위한 저장소 작명 규칙
|구분|규칙|
|----|-------------------------|
|id|boyinblue일 경우|
|repo name|boyinblue.github.io|
|URL|https://boyinblue.github.io|
   

GitHub 페이지 생성을 위한 네이밍 룰은 위와 같습니다. 
위의 규칙을 지키지 않을 경우 해당 페이지의 root 디렉토리를 사용할 수 없으므로 이 점을 유념하시기 바랍니다.   
   

#### Repository 생성을 위한 메뉴


GitHub Repository를 생성하기 위해서는 아래 메뉴로 들어가시면 됩니다.   
- Menu 
  - Your repositories
    - New   


#### Repository 생성을 위한 링크
   

혹은 간략하게 아래의 경로로 접속하셔도 됩니다.   


[GitHub 새 repository 생성](https://github.com/new GitHub 새 repository 생성)   
   

### Step 3. GitHub Pages 설정
   

Repositry를 생성하였다면 해당 Repository를 GitHub Pages로 설정할 차례입니다.   
   

#### GitHub Pages 설정을 위한 메뉴
   

아래의 경로의 메뉴로 접속하시면 GitHub Pages 설정을 위한 메뉴로 들어갈 수 있습니다.   
- Repository 
  - Settings
    - Pages   
   

### Step 4. GitHub Pages 접속
   

아래의 경로로 접속하시면 새로 생성한 GitHub Pages로 접속하실 수 있습니다.   
https://boyinblue.github.io   
물론 boyinblue.github.io는 보고 계시는 이 페이지의 주소이므로, 
boyinblue 부분을 GitHub ID로 바꿔서 입력하시면 되겠습니다.   


이상으로 GitHub 블로그(GitHub Pages)의 장점에 대해서 설명을 모두 마칩니다.   





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
