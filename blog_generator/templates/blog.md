**Date**: {{ blog_data.date.strftime('%Y-%m-%d') }}

**Tags:**
{% for category in blog_data.categories %}
- {{ category -}}
  {% endfor %}

<hr>

{{ blog_data.content }}
