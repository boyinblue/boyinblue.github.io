---
title: jekyll-paginate 플러그인을 사용해서 페이지 나누기
description: GitHub Pages에서 페이지를 나누는 방법 설명
category: github-pages
image: /assets/images/github-pages/paginator-example.png
---

웹사이트들 중에는 여러 페이지 목록을 숫자로 나눠서 표기하는 경우가 많다. 
`GitHub Pages`에서는 `jekyll-paginate` 플러그인을 통해서 
페이지를 나눠서 표시하는 기능을 제공한다. 


요약
---


GitHub Pages에서 jekyll-paginate 플러그인을 사용하려면 
아래 2개 파일을 편집하면 된다. 


### _config.yml 파일 편집


```
plugins:
  - jekyll-paginate
paginate: 5
paginate_path: "/blog/page:num"
```


### /index.html 파일 편집


```
---
layout: null
---
{% raw %}
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{% for post in site.posts %}
 {% unless post.published == false %}
 <url>
   <loc>{{ site.url }}{{ post.url }}</loc>
   {% if post.sitemap.lastmod %}
     <lastmod>{{ post.sitemap.lastmod | date: "%Y-%m-%d" }}</lastmod>
   {% elsif post.date %}
     <lastmod>{{ post.date | date_to_xmlschema }}</lastmod>
   {% else %}
     <lastmod>{{ site.time | date_to_xmlschema }}</lastmod>
   {% endif %}
   {% if post.sitemap.changefreq %}
     <changefreq>{{ post.sitemap.changefreq }}</changefreq>
   {% else %}
     <changefreq>monthly</changefreq>
   {% endif %}
   {% if post.sitemap.priority %}
     <priority>{{ post.sitemap.priority }}</priority>
   {% else %}
     <priority>0.5</priority>
   {% endif %}
 </url>
 {% endunless %}
{% endfor %}
 </urlset>
{% endraw %}
```


변수
---


|변수|용도|비고|
|---|---|---|
|site.paginate_path|pagenate 된 페이지들이 서비스될 경로|   |
|paginator.page|페이지 번호|   |
|paginator.per_page|페이지 별로 표시될 포스트 개수|   |
|paginator.posts|이 페이지에 포함된 포스트들|   |
|paginator.total_posts|전체 포스트 개수|   |
|paginator.total_pages|전체 페이지 개수|   |
|paginator.previous_path|이전 페이지 번호|   |
|paginator.previous_page_path|이전 페이지 경로|   |
|paginator.next_page|다음 페이지 번호
|paginator.next_page_path|다음 페이지 경로|   |


제약사항
---


[x] paginate를 이용하기 위해서는 반드시 /index.html 파일만 가능하다. 
[x] permalink를 이용해서는 안 된다. 
[x] md 파일이 아닌 html 형식의 파일만 이용 가능하다. 


트러블 슈팅
---


### index.html 파일을 찾지 못하는 경우


#### 문제 현상
Pagination: Pagination is enabled, but I couldn't find an index.html page to use as the pagination template. Skipping pagination.


#### 원인
만약 Build 시에 위와 같은 에러가 발생했다면, 
index.html 파일을 찾지 못해서다. 


#### 대책
반드시 루트 경로에 index.html 파일을 작성해야 한다. 


참고할 만한 페이지
---


{% assign preview_image_url = https://jekyllrb.com/img/jekyll-og.png %}
{% assign preview_url = http://jekyllrb.com/docs/pagination/ %}
{% assign preview_title = Pagination %}
{% assign preview_description = "With many websites — especially blogs — it’s very common to break the main listing of posts up into smaller lists and display them over multiple pages. Jekyll offers a pagination plugin, so you can automatically generate the appropriate files and folders you need for paginated listings." %}
{% include body-preview.html %}

[http://jekyllrb.com/docs/pagination](http://jekyllrb.com/docs/pagination)


이상입니다. 
