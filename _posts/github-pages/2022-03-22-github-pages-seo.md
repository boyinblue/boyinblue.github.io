---
title: SEO를 위해 GitHub Pages 의 md 파일에 헤더를 입력하는 방법
permalink: /002_github_blog/009.html
description: GitHub Pages의 markdown 파일의 헤더에 title, description을 지정하는 방법에 대해서 설명합니다.
category: github-pages
image: /assets/images/github-pages/logo.png
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
```
