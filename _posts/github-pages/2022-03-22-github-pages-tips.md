---
title: GitHub Pages 운영시의 꿀팁들
permalink: /002_github_blog/008.html
description: GitHub Pages를 운영하면서 체득한 유용한 팁들을 제공합니다.
category: github-pages
image: /assets/images/github-pages/logo.png
---
GitHub Pages를 이용해서 웹페이지를 운영하기 시작한지 2주가 좀 지났습니다. 
처음에는 전혀 개념을 잡지 못해서 제법 시간과 노력이 필요했습니다. 
GitHub에는 익숙한 SW 개발자이지만 jekyll이 어떻게 빌드되고 웹페이지가 생성되는지 파악하는데 제법 시간이 소요되었습니다. 
본 페이지에선 그 동안 GitHub Pages를 생성하면서 알게된 소소한 꿀팁들을 기록해두고자 합니다. 


Jekyll 빌드란?
---


저는 네이버 블로그, 티스토리 블로그, 직접 웹서버 운영 등을 모두 해봤습니다. 
하지만 Jekyll이 무엇인지에 대한 개념은 전혀 없었기 때문에, 
GitHub Pages를 어떻게 작서해야 하는지에 대한 개념이 전혀 없었습니다.   


### README.md 파일은 자동으로 index.html로 빌드됨


가장 기본적인 Jekyll 빌드 과정에 대해서 설명을 드리자면, 
README.md 파일을 작성하면 잠시후 빌드 과정을 거쳐서 index.html 파일이 생성됩니다. 
GitHub Pages에 익숙하지 않으신 분들은 Repository에 index.html 파일이 없는데 어떻게 index.html로 접속이 되는지 뇌의 회로가 정지되는 듯한 느낌을 느낄 수 있겠습니다.


### md 확장자를 가진 파일은 자동으로 html 파일로 빌드됨


방금 READMD.md 파일이 존재하면 자동으로 index.html 파일을 생성시킨다는 것을 알 수 있습니다. 
그렇다면 다른 페이지들은 어떻게 작성하면 될까요? 
그냥 md 파일을 작성해서 GitHub에 push되면 자동으로 html 파일이 생성되게 됩니다. 
즉. abc.md 파일을 작성해서 GitHub Pages에 업데이트하셨다면 잠시 후에 abc.html 파일이 생성되어서 게시가 가능하다는 것을 알 수 있습니다.


즉, GitHub repository에 있는 파일들을 기반으로 html 파일들이 생성되고, 웹서버에서 해당 파일들을 서비스할 수 있게 됩니다. 


|repisotory|Web Server|비고|
|--|--|--|
|/README.md|/README.md|README.md 파일을 repo에도 있고 웹서버에도 있음|
||/index.html|/README.md 파일에 의해서 생성된 index.html 파일은 웹서버에만 존재|
|/abc.md|/abc.md|md 확장자의 파일은 repo에도 존재하고 웹서버에도 존재함|
||/abc.html|md 파일에 의해서 생성된 html 파일은 웹서버에만 존재함|
|/\_include/sample.html||\_로 시작되는 디렉토리는 빌드되지 않음|


### 빌드되지 않도록 지정해주는 방법


Jekyll은 특정한 디렉토리나 파일들은 빌드하지 않습니다.


아래와 같이 작명된 디렉토리나 파일은 Jekyll이 빌드하지 않습니다. 
만약, Jekyll이 빌드하지 않도록 하고 싶다면 아래와 같이 설정해보시기 바랍니다.


1. <code>/node\_modules</code> 혹은 <code>/vendor</code> 디렉토리
2. <code>\_</code> 혹은 <code>.</code> 혹은 <code>#</code>로 시작하는 디렉토리나 파일들
3. <code>\~</code>로 끝나는 파일들
4. 설정 파일에서 <code>exclude</code>로 지정된 디렉토리나 파일들


반대로 위와 같이 작명된 디렉토리나 파일들 중에서 빌드되도록 지정하고 싶다면, 
<code>include</code> 설정을 환경 설정 파일에 추가하시면 됩니다.


### 만약 Jekyll 빌드를 원치 않을 경우


만약 GitHub Pages 전체를 Jekyll 빌드되지 않도록 하고 싶다면 
<code>.nojekyll</code> 파일을 루트 디렉토리에 생성하면 됩니다. 
파일 내용은 상관 없습니다. 