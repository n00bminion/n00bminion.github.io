---
layout: category
title: Maths
---

<ul style="list-style-type: none;">
  {% for module in site.maths %}
    <li>
      <h2><a href="{{ module.url }}">{{ module.name }}</a></h2>
        <ul style="list-style-type: none;">

          {% assign post_counter = 0 %}

          {% for post in site.posts %}
            {% if post.code == module.code %}
              {% assign post_counter = post_counter | plus: 1 %}
              <li>
                <h4>{{post_counter}}. <a href="{{ post.url }}">{{ post.title }}</a></h4>
              </li>
            {% endif %}

            {% if post_counter == 3 %}
              {% assign post_counter = 0 %}
              {% break %}
            {% endif %}

          {% endfor %}
        </ul>
    </li>
  {% endfor %}
</ul>