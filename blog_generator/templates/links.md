# Link List

{% for link in links %}
## {{ link.title }}

<a href="{{ link.link }}" target="_blank">{{ link.link }}</a>

**Tags:**
{% for tag in link.tags %}
 - {{ tag -}}
{% endfor %}
{% if link.authors %}
**Authors:**
{% for author in link.authors %}
 - {{ author -}}
{% endfor %}
{% endif %}
<hr style="height:2px;border-width:0;color:gray;background-color:gray">
{% endfor %}
