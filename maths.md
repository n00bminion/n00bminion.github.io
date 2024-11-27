---
layout: default
title: Maths
---

<ul>
  {% for module in site.maths %}
    <li>
      <h2>{{ module.name }}</h2>
        <ul>
          {% for post in site.posts %}
            {% if post.code == module.code %}
              <li>
                <h4><a href="{{ post.url }}">{{ post.date | date: "%d %B %Y" }} - {{ post.title }}</a></h4>
              </li>
            {% endif %}
          {% endfor %}
        </ul>
    </li>
  {% endfor %}
</ul>