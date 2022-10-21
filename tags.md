---
title: 테그들
permalink: /tags/
description: 이 사이트에서 제공하는 모든 테그들을 살펴봅니다.
category: menu
---
{% capture site_tags %}{% for tag in site.tags %}{{ tag | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
<!-- site_tags: {{ site_tags }} -->
{% assign tag_words = site_tags | split:',' | sort %}
<!-- tag_words: {{ tag_words }} -->

<div id="tags">
  <p>
  {% for tag in tag_words %}
  <a style="background-color: #0040ff; color: #fff; border-radius: 10px; padding: 3px 5px; font-size: 12px; font-weight: bold; text-decoration: none;" href="#{{ tag | cgi_escape }}">{{ tag }} {{ site.tags[tag] | size }}</a>
  {% endfor %}
  </p>

  {% for item in (0..site.tags.size) %}
    {% unless forloop.last %}
      {% capture this_word %}{{ tag_words[item] | strip_newlines }}{% endcapture %}
      <h2 id="{{ this_word | cgi_escape }}">{{ this_word }}</h2>
      <ul class="posts">
      {% for post in site.tags[this_word] %}
        {% if post.title != null %}
        <li itemscope><span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}" itemprop="datePublished">{{ post.date | date: "%B %d, %Y" }}</time></span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
        {% endif %}
      {% endfor %}
      </ul>
    {% endunless %}
  {% endfor %}
</div>
