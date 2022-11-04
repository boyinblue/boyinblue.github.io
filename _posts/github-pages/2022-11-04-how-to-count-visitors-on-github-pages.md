---
title: GitHub Pages에 방문자수 카운터 표시하는 방법 (feat. hits.sh)
description: 깃허브 페이지스 블로그에 방문자수 카운터 표시하는 방법
category: github-pages
image: /assets/images/github-pages/how-to-count-visitors-of-github-pages.png
---

GitHub Pages는 분명히 아주 매력적인 무료 웹호스팅 서비스이다. 
markdown 문법으로 시원시원하게 글을 작성할 수 있고, 
구글 애드센스를 연동하여 수익형 블로그로 만들 수 있다. 
장점을 이야기하자면 너무 많아서 손가락이 아프다. 


단점도 몇 가지 있다. 
정적인 웹서버이기 때문에 방문자수를 카운트가 불가하다. 
이를 해결하기 위해서는 카운터 서비스를 이용하면 된다. 


본 페이지에서는 GitHub Pages에 사용할 수 있는 카운터 서비스를 소개한다. 
- hits.sh 카운터


hits.sh 이용
---

구글에서 GitHub Pages에 카운터를 다는 방법을 검색하다가 만족스러운 무료 서비스를 찾았다. 

### 장점
- 깔끔한 디자인
- 가입 필요 없이 손쉽게 사용 가능
- 무료 서비스

### 단점
- 페이지를 로딩할때마다 방문자수가 증가한다.

유일한 단점은 한 사람이 여러번 방문해도 카운터가 증가한다는 것이다. 
실제 사용자수보다 훨씬 더 많은 방문자수가 표시된다. 

### 사용 방법
![hits.sh 카운터 서비스 이용 방법](/assets/images/github-pages/how-to-count-visitors-of-github-pages.png 'hits.sh 카운터 서비스 이용 방법')

1. hits.sh 홈페이지에 방문한다. 
2. 블로그 주소를 입력한다.
3. 자동으로 생성된 HTML 테그를 적당한 곳에 활용한다. 

### 홈페이지
{% assign preview_image_url = 'https://hits.sh/og-img-1200x630.png' %}
{% assign preview_url = 'https://hits.sh/' %}
{% assign preview_title = 'Hits' %}
{% assign preview_description = 'Hit Counter for Your GitHub or Any Kind of Websites You Want' %}
{% include body-preview.html %}

### 관련 페이지
{% assign preview_image_url = 'https://blog.silentsoft.org/static/images/twitter-card.png' %}
{% assign preview_url = 'https://blog.silentsoft.org/archives/192' %}
{% assign preview_title = 'GitHub, 블로그에 방문자 카운터를 달아보자' %}
{% assign preview_description = 'GitHub 프로필이나 레파지토리, 블로그 등을 방문하다 보면 종종 방문자 카운터가 달린 것을 종종 볼 수 있다.' %}
{% include body-preview.html %}

