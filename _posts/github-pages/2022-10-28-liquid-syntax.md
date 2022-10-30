---
title: GitHub Pages Jekyll Liquid 문법 정리
description: GitHub Pages Jekyll Liquid 문법 정리
category: github-pages
image: https://shopify.github.io/liquid/images/icons/water-drop-64x.png
---

필터
---


#### abs (절대값 구하기)


절대값을 구하는 필터


```
{% raw %}
{{ -17 | abs }}
{{ 4 | abs }}
{% endraw %}
```


```
{{ -17 | abs }}
{{ 4 | abs }}
```


#### newline_to_br (개행을 br 테그로 변환)
---
개행을 br 테그로 변환


```
{% raw %}
{% capture string_with_newlines %}
Hello
there
{% endcapture %}
{% endraw %}
```


```
{% capture string_with_newlines %}
Hello
there
{% endcapture %}

{{ string_with_newlines | newline_to_br }}
```


#### strip_html (html 테그 제거)


HTML 테그를 제거하는 필터


---
{% raw %}
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
{% endraw %}

{{ string_with_newlines | newline_to_br }}
---


```
Have you read Uiysses?
```


참고할만한 페이지
---


{% assign preview_title = "Liquid template language" %}
{% assign preview_description = "Documentation for the Liquid template language, created by Shopify." %}
{% assign preview_image_url = "https://shopify.github.io/liquid/images/icons/water-drop-64x.png" %}
{% assign preview_url = "http://shopify.github.io/liquid/" %}
{% include body-preview.html %}
