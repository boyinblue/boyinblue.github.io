---
layout: post-with-tag
title: 테스트 페이지
description: GitHub Pages의 Jekyll Liquid의 변수들을 확인하는 테스트 페이지입니다.
category:
- GitHub
tags:
- GitHub
- Blog
---


|Variable|Value|Note|
|---|---|---|
|site.title|{{ site.title }}|  |
|site.description|{{ site.description }}|  |
|site.url|{{ site.url }}|  |
|site.permalink|{{ page.permalink }}|  |
|site.baseurl|{{ site.baseurl }}|  |


|site.category|{{ site.category }}|  |
|site.categories|{% for cate in site.categories %}{{ cate | first }} {% endfor %}|  |
|site.categories[diary]|{{ site.categories[diary] }}|  |


|site.tags|{% for tag in site.tags %}{{ tag | first }} {% endfor %}|  |
|site.tag|{{ site.tag }}|  |
|site.posts|생략|모든 포스트들이 나옴|


|Variable|Value|Note|
|---|---|---|
{% for github in site.github %}|site.github.{{ github | first }}|  |  |{% endfor %}
|site.github.repository_url|{{ site.github.repository_url }}|  |


|Variable|Value|Note|
|---|---|---|
|page.title|{{ page.title }}|  |
|page.description|{{ page.description }}|  |
|page.layout|{{ page.layout }}|  |
|page.published|{{ page.published }}|  |
|page.url|{{ page.url }}|  |
|page.permalink|{{ page.permalink }}|  |
|page.baseurl|{{ page.baseurl }}|  |
|page.category|{{ page.category }}|  |
|page.categories|{{ page.categories }}|  |
|page.tags|{{ page.tags }}|  |
|page.dir|{{ page.dir }}|  |
|page.name|{{ page.name }}|  |
|page.path|{{ page.path }}|  |
|page.content|생략|콘텐츠가 너무 많이 나옴|
