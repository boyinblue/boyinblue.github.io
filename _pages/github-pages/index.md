---
title: GitHub Pages
permalink: /002_github_blog/index.html
description: 무료로 사용할 수 있는 정적 웹서버인 GitHub Pages 개설 및 운영 방법 설명
category: github-pages
tags:
- GitHub
- GitHub Pages
---
저는 네이버 블로그, 티스토리 블로그 등을 오랫동안 운영해 왔습니다. 
해당 서비스를 이용하면 누구든 편하게 글을 작성하고 발행할 수 있습니다. 


우선 GitHub Pages와 네이버 블로그, 티스토리 블로그를 비교해보겠습니다.


네이버 블로그, 티스토리 블로그의 장점
---


GitHub Pages 대비 네이버 블로그와 티스토리 블로그의 장점은 아래와 같습니다.
1. 누구든 손쉽게 블로그를 작성하고 발생할 수 있음.
2. 블로그를 작성하면 네이버나 다음에서 금방 유입됨.
3. 사이트맵이나 RSS 피드 작성이 필요 없음.
4. SEO에 대해서 크게 신경쓸 필요 없음.
5. robots.txt, .htaccess 파일 등을 생성할 필요가 없음.


네이버 블로그, 티스토리 블로그의 단점
---


반면, 네이버 블로그와 티스토리는 아래와 같은 제약사항들이 존재합니다. 
1. 하루에 발행할 수 있는 글의 개수가 제한됨.
2. 정해진 형식의 파일 이외의 다른 파일은 업로드 불가함.
3. 구글 애드센스를 달 수 없음 (네이버 블로그)
4. 웹서버나 웹페이지를 커스터마이징(customizing)하기 어려움


GitHub Pages의 장점
---


네이버 블로그나 티스토리 블로그의 단점이 곧 GitHub Pages의 장점입니다.
1. 원하는대로 페이지를 구성할 수 있고 자유도가 높음.
2. 구글 애드센스를 달 수 있음.
3. 하루에 발행할 수 있는 글의 수에 제한이 없음.
4. 어떠한 형식의 파일이든 자유롭게 업로드할 수 있음.
5. GitHub Repositoy 베이스이므로 협업 및 히스토리 관리가 용이함.
6. 무료 웹서버이므로 웹서버 및 도메인 네임 비용이 불필요함.
7. markdown 문법으로 손쉽고도 깔끔하게 웹페이지 작성이 가능함.


GitHub Pages의 단점
---


GitHub Pages는 장점이 상당히 많지만 단점도 있습니다. 
1. 처음 접하는 사람은 개설 및 글 발행이 조금 어려울 수 있음.
2. 정적 페이지만 지원하므로 PHP 등의 문법은 사용이 불가능함.
3. 사이트맵, robots.txt, .htaccess 등의 파일을 직접 작성해야 함.


GitHub Pages로 만든 사이트들
---


|사이트|GitHub Repo|비고|
|---|---|---|
|[peterroelants.github.io](https://peterroelants.github.io)|[Repo](https://github.com/peterroelants/peterroelants.github.io)|테그 활용 방법|
|[blog.lanyonm.org](https://blog.lanyonm.org)|[Repo](https://github.com/lanyonm/lanyonm.github.io)|테그 활용 방법|
|[ansohxxn.github.io](https://ansohxxn.github.io)|[Repo](https://github.com/ansohxxn/ansohxxn.github.io)|디자인|
|[devinlife.github.io](https://devinlife.github.io)|[Repo](https://github.com/devinlife/devinlife.github.io)|   |
|[feel5ny.github.io](https://feel5ny.github.io)|[Repo](https://github.com/feel5ny/feel5ny.github.io)   |


Theme 페이지
---


|Theme|GitHub Repo|Sample Page|
|---|---|---|
|jekyll-theme-slate|[https://github.com/pages-themes/slate](https://github.com/pages-themes/slate)|[https://pages-themes.github.io/slate/](https://pages-themes.github.io/slate)|


도움되는 사이트들
---


|URL|비고|
|---|---|
|[https://jekyllrb.com/](https://jekyllrb.com/)|Jekyll에 대한 내용이 잘 정리된 페이지다. |
|- [https://jekyllrb.com/docs/pages/](https://jekyllrb.com/docs/pages/)|페이지 구조|
|- [https://jekyllrb.com/docs/posts/](https://jekyllrb.com/docs/posts/)|포스트 구조|
|- [https://jekyllrb.com/docs/includes/](https://jekyllrb.com/docs/includes/)|include 구문 설명|
|[https://shopify.github.io/liquid/](https://shopify.github.io/liquid/)|Liquid 문법에 대해서 살펴볼 수 있는 페이지다.|
|[https://jekyll.github.io/jekyll-seo-tag/advanced-usage/#customizing-image-output](https://jekyll.github.io/jekyll-seo-tag/advanced-usage/#customizing-image-output)|SEO에 대한 내용이 풍부하다.|


내가 작성한 글들
---


{% assign category="github-pages" %}
{% include body-category.html %}