# How to use the templating language


'''html
<h1>This is a string</h1>

<ul>
{% for item in range(10) %}
  <li>{{item}}</li>
{% endfor}
</ul>
