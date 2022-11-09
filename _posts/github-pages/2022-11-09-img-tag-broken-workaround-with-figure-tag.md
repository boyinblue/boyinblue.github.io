---
title: GitHub Pages Jekyll Liquid에서 for 반복문에 의해 img 테그가 깨지는 현상
description: How to workaround image tag escape problem.
category: github-pages
image: /assets/images/github-pages/logo.png
---

GitHub Pages를 이용해서 본 웹페이지를 운영하고 있다. 
Jekyll은 내부적으로 Liquid 문법을 이용하고 있다. 
for 반복문과 img 테그를 조합해서 미리 보기 기능을 구현했다. 
이유는 알 수 없지만 img 테그가 깨지는 문제가 발생했다. 
이 문제점에 대해서 근본 원인은 알 수 없지만, workaround는 있다. 


문제 내용 설명
---

아래는 최근 포스트 5개의 이미지를 보여준다.

### 코드
```
{% raw %}
{%- for post in site.posts limit:5 %}
  {%- if post.image %}
    <img style="border-radius: 20px;" src="{{ post.image }}"><br />
  {% endif %}
{% endfor %}
{% endraw %}
```

### 또 다른 코드
```
{%- for post in site.posts limit:5 %}
  {%- if post.image %}
    <a href="{{ post.url }}"><img style="border-radius: 20px;" src="{{ post.image }}"></a><br />
  {% endif %}
{% endfor %}
```

### 실행 결과
```
{%- for post in site.posts limit:5 %}
  {%- if post.image %}
    <img style="border-radius: 20px;" src="{{ post.image }}"><br />
  {% endif %}
{% endfor %}
```

실제로 생성되는 html 코드를 보면 `<img>` 부분이 `%ltmg>`로 깨진 것을 확인할 수 있다. 

근본 해결 방법
---

이 문제의 근본 원인은 아직 모른다. 
하지만 workaround 방법은 존재한다. 


임시 조치 방법
---

`<img>` 테그에 `<figure>` 테그를 씌우면 테그가 깨지는 문제를 회피할 수 있다. 

```
{% raw %}
{%- for post in site.posts limit:5 %}
  {%- if post.image %}
    <figure><img style="border-radius: 20px;" src="{{ post.image }}"></figure><br />
  {% endif %}
{% endfor %}
{% endraw %}
```


요약
---
만약 Jekyll에서 img 테그가 깨지는 문제가 발생한다면, 
firure 테그를 img 테그에 씌우면 해결된다. 

