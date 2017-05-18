# Python Meetup Athens

Schedule, code and other assets for Python Meetup Athens.


{% for meetup in meetups %}
## {{ meetup.name }}

**Ημέρα:** {{ meetup.when }} | **Μέρος:** {{ meetup.where }}

{{ meetup.description }}


## Presentations

{% for presentation in meetup.presentations %}
### {{ presentation.name }}

{{ presentation.description}}

**Παρουσιαστές:** {% for presenter in presentation.presenters -%}
    {{ presenter.name }} {% if presenter.github -%}
        [GitHub](https://github.com/{{ presenter.github }}) |
    {%- endif %}
    {% if presenter.website -%}
        [Website]({{ presenter.website }})  |
    {%- endif %}
    {%- if presenter.twitter -%}
        [Twitter](https://twitter.com/{{ presenter.twitter }}) |
    {%- endif %}
    {% if presenter.linkedin -%}
        [LinkedIn]({{ presenter.linkedin }})
    {%- endif %}
    {% if not loop.last %},{% endif %}
  {%- endfor %}

{% if presentation.slides %}
**Διαφάνειες:** [{{ presentation.slides }}]({{ presentation.code }})
{% endif %}
{% if presentation.code %}
**Κώδικας:** [{{ presentation.code }}]({{ presentation.code }})
{% endif %}
{% if presentation.otherlinks %}
**Άλλοι σύνδεσμοι:**
{% for link in presentation.otherlinks %}
 * [{{ link }}](link)
{% endfor %}
{% endif %}
{% endfor %}
{% if not loop.last %}
----
{% endif %}
{% endfor %}
