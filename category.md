---
title: 카테고리
permalink: /category/
description: 이 사이트에서 제공하는 모든 카테고리들을 살펴봅니다.
---


카테고리
===


본 페이지에서는 카테고리별 글 목록을 보여줍니다. 


{% capture site_caths %}{% for cath in site.categories %}{{ cath | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
<!-- site_cates: {{ site_cates }} -->
{% assign cath_words = site_caths | split:',' | sort %}
<!-- cath_words: {{ cath_words }} -->

<div id="categories">
  <p>
  {% for cath in cath_words %}
  <a style="background-color: #0040ff; color: #fff; border-radius: 10px; padding: 3px 5px; font-size: 12px; font-weight: bold; text-decoration: none;" href="#{{ cath | cgi_escape }}">{{ cath }} {{ site.categories[cath] | size }}</a>
  {% endfor %}
  </p>

  {% for item in (0..site.categories.size) %}
    {% unless forloop.last %}
      {% capture this_word %}{{ cath_words[item] | strip_newlines }}{% endcapture %}
      <h2 id="{{ this_word | cgi_escape }}">{{ this_word }}</h2>
      <ul class="posts">
      {% for post in site.categories[this_word] %}
        {% if post.title != null %}
        <li itemscope><span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%B %d, %Y" }}</time></span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
        {% endif %}
      {% endfor %}
      </ul>
    {% endunless %}
  {% endfor %}
</div>
