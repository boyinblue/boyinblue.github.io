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
      <a href="{{ post.url }}">
        {% if post.image.path %}
          {% assign image_url = post.image.path %}
        {% elsif post.image %}
          {% assign image_url = post.image %}
        {% else %}
          {% assign image_url = site.image.path %}
        {% endif %}
        <div style="height: 300; border-radius: 3px;">
          <div style="width: 20%; float: left; margin: 2px; height: 100%;">
            <img style="border-radius: 20px;" src="{{ image_url }}" width=100%>
          </div>
          <div style="float: right; margin: 10px 0 10px 0; width: 75%; height: 100%; overflow: hidden">
            <h3 style="overflow: hidden">{{ post.title }}</h3>
            <pre style="overflow: hidden">{{ post.description }}</pre>
            ({{ post.date | date: "%Y-%m-%d" }} 작성)<br>
          </div>
          <div style="clear: both; width: 0">
          </div>
        </div>
      </a>
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
    <a href="{{ post.url }}">
      <div style="height: 300; border-radius: 3px;">
        <div style="width: 20%; float: left; margin: 2px; height: 100%">
          <img style="border-radius: 20px;" src="{{ image_url }}" width=100%>
        </div>
      
        <div style="float: right; margin: 10px 0 10px 0; width: 75%; height: 100%; overflow: hidden">
          <h3 style="overflow: hidden">{{ post.title }}</h3>
          <pre style="overflow: hidden">{{ post.description }}</pre>
          ({{ post.date | date: "%Y-%m-%d" }} 작성)<br>
        </div>
      
        <div style="clear: both; width: 0">
        </div>
      </div>
    </a>
{% endfor %}
</div>
