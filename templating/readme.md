# The Templating Language



Normal HTML can be used.
```html
<h1>This is a string</h1>
```

In addition, common python constructs can be used as well. This includes reading variables, for loops, if state
```html
<ul>
{% for item in range(10) %}
  <li>{{item}}</li>
{% endfor}
</ul>'''
