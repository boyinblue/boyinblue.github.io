---
title: 카테고리
permalink: /category/
description: 이 사이트에서 제공하는 모든 카테고리들을 살펴봅니다.
category: menu
---

<div id="categories">
  <p>
  {% for cath in site.categories %}
  {% assign cath_name = cath | first %}
  <a style="background-color: #0040ff; color: #fff; border-radius: 10px; padding: 3px 5px; font-size: 12px; font-weight: bold; text-decoration: none;" href="#{{ cath_name }}">{{ cath_name }} {{ site.categories[cath_name] | size }}</a>
  {% endfor %}
  </p>

  {% for cath in site.categories %}
    {% assign cath_name = cath | first %}
    <h2 id="{{ cath_name }}">{{ cath_name }}</h2>
    {% for post in site.categories[cath_name] %}
      {% if post.image.path %}
        {% assign image_url = post.image.path %}
      {% elsif post.image %}
        {% assign image_url = post.image %}
      {% else %}
        {% assign image_url = site.image.path %}
      {% endif %}
      {% assign url = post.url %}
      {% assign description = post.description %}
      {% assign post_date = post.date %}
      {% include body-preview.html url=url image_url=image_url title=post.title description=description post_date=post_date %}
    {% endfor %}      
  {% endfor %}

  <h2 id="미분류">미분류</h2>
  {% for post in site.posts %}
    {% if post.category %}
      {% continue %}
    {% endif %}
    {% if post.image.path %}
      {% assign image_url = {{ post.image.path }} %}
    {% elsif post.image %}
      {% assign image_url = {{ post.image }} %}
    {% else %}
      {% assign image_url = {{ site.image.path }} %}
    {% endif %}
    {% assign url = post.url %}
    {% assign title = post.title %}
    {% assign description = post.description %}
    {% assign post_date = post.date %}
    {% include body-preview.html url=url image_url=image_url title=title description=description post_date=post_date %}
  {% endfor %}
</div>