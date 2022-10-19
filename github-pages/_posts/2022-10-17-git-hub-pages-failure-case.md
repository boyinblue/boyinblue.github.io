---
title: 깃허브 블로그 실패 사례
description: GitHub Pages로 6개월동안 삽질하고 깨닫게 된 것들
category: github-pages
tags:
- GitHub Pages
- Jekyll
---


깃허브 블로그 실패 사례
===


GitHub Pages를 개설한지 16일만에 구글 애드센스 승인을 받았습니다. 
자신감을 가지고 6개월동안 블로그를 운영했습니다. 
그간의 노력들이 삽질에 불과했다는 것을 깨달았습니다. 


현타 포인트
---


가장 현타가 오는 부분은 Jekyll입니다. 


> 제킬! 지킬을 지켜야 했어! 


Jekyll이 무엇인지 모르고 일단 찍먹해봤었기 때문에 
그것이 제공하는 다양한 기능과 편리함을 이용하지 못했습니다. 


가장 대표적인 부분이 사이트맵 파일을 생성하는 것에 있었습니다. 
자동으로 사이트맵 파일을 생성할 수 있는 방법이 있었음에도 불구하고, 
저는 제가 직접 쉘 스크립트를 작성해서 xml 파일을 생성했었습니다. 


포스트 작성시에 지켜야 하는 규칙
---


`_posts/` 디렉토리에 `YYYY-MM-DD'로 시작하는 
파일명으로 md 파일을 작성해야 합니다. 


- '_posts'
  - 2022-10-17-github-현타.md
  - 2022-10-18-내일작성할블로그.md


이 규칙을 지키지 않으면 Jekyll에서 기본적으로 제공하는 
사이트 맵 자동화 기능, feed.xml 파일 자동화 기능을 사용할 수 없습니다. 


왜냐하면 지킬에서 참조하는 site.posts 변수는 
_posts 디렉토리 안에 있는 파일들을 이용하기 때문입니다. 


카테고리 분류를 하고 싶다면?
---


만약, 카테고리 기능을 이용하고 싶다면, 
'_posts' 디렉토리 안에 카테고리 키워드를 입력하면 됩니다. 


예를들면, Blog라는 카테고리를 이용하고 싶다면, 
아래와 같은 디렉토리 구조로 파일을 업로드하면 됩니다. 


- '_posts'
  - Blog
    - 2022-10-17-github-현타.md
    - 2022-10-18-내일작성할블로그.md


포스트에 테그를 입력하고 싶다면?
---


포스트에 테그를 입력하고 싶다면, Front Matter에 Tags를 입력하면 됩니다. 


만약, 'Blog' 테그와 'Diary' 테그를 추가하고 싶다면, 
아래처럼 Front Matter를 입력하면 됩니다. 


```yaml
---
title: 제목을 입력합니다.
description: 포스트를 잘 나타내는 설명을 입력합니다.
tags:
- Blog
- Diary
---


모든 포스트에 대한 링크를 표시하려면
---


만약 모든 포스트에 대한 링크를 표기하려면 
아래와 같은 Liquid 문법을 활용하시면 됩니다. 


```html
<ul>
  \{\% for post in site.posts \%\}
    <li>
      <a href="\{\{ post.url \}\}">[\{\{ post.date \}\}] \{\{ post.title \}\}</a>
    </li>
 \{\% endfor \%\}
</ul>


포스트 개수를 한정해서 링크를 표시하려면
---


위와 같이 모든 포스트 링크를 출력하게 되면, 
엄청나게 많은 포스트의 링크가 출력되게 됩니다. 


그래서 3개, 5개, 10개 정도만 출력할 필요가 생깁니다. 
이 때는 '\{\%' 구문에 'limit:3'처럼 개수를 한정하면 됩니다. 


```html
<ul>
  \{\% for post in site.posts limit:3 \%\}
    <li>
      <a href="\{\{ post.url \}\}">[\{\{ post.date \}\}] \{\{ post.title \}\}</a>
    </li>
 \{\% endfor \%\}
</ul>


페이지에 작성된 테그들을 표시하려면
---


만약, 페이지에 작성된 테그들을 표시하려면
아래와 같은 Liquid 문법을 활용하시면 됩니다. 


```
<!-- tags -->
\{\% for tag in page.tags \%\}
  #️⃣\{\{ tag \}\}
\{\% endfor \%\}
```


도움이 되는 링크들
---


아래의 링크에 접속하면 Jekyll이 빌드시에 규칙을 알아볼 수 있습니다. 
Jekyll을 통해서 서비스되는 콘텐츠들은 2종류로 구분할 수 있습니다. 


하나는 'pages'이고, 나머지 하나는 'posts' 입니다. 
'pages'는 고정적인 페이지를 의미하고, 
'posts'는 그때그때 작성하는 블로그 같은 개념입니다. 


예를 들면, 블로그에 대한 소개나 저자에 대한 소개는 
'pages'으로 작성하면 좋고, 
매일 작성하는 일기는 'posts' 형식으로 작성을 하시면 됩니다. 


### 페이지 작성 관련
[https://jekyllrb.com/docs/pages/](https://jekyllrb.com/docs/pages/)


### 포스트 작성 관련
[https://jekyllrb.com/docs/posts/](https://jekyllrb.com/docs/posts/)


### Liquid 문법 관련
[https://shopify.github.io/liquid/](https://shopify.github.io/liquid/)


이상입니다. 
