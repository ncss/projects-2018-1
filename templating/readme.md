# The Templating Language  

## Types of tags:
- expression
- include
- if
- for loop
- comments

## expression tags
An expression tag evaluates whatever is in-between the double curly braces. For example:
```
My first name is {{ first_name }}. My last name is {{ last_name }}.
```
With a context of {'first_name': 'John', 'last_name': 'Doe'}, this template renders to:
```
My first name is John. My last name is Doe.
```

## include tags
Include tags include (HAHA NO PUN INTENDED) content from another file. For example:
```
{% include knowledge.html %}
<p> are less liked than knowledge </p>
```
If the contents of knowledge.html are:
```
Lamborghinis
```
then this template renders to:
```
Lamborghinis
<p> are less liked than knowledge </p>
```

## if tag
Structure:
```
{% if CONDITION %} CONTENT {% end if %}
```
If CONDITION evaluates to TRUE, then CONTENT will be rendered, otherwise, it won't be rendered.

## for loop tag
Structure:
```
{% for varName in iterable %} CONTENT {% end for %}
```
The for loop can render CONTENT x amount of times. Using the expression tag mentioned previously,  
the varName can also be referenced. For example:
```
{% for i in range(11) %} {{i}} {% end for %}
```
will become:
```
0
1
2
3
4
5
6
7
8
9
10
```
Or, if iterable is a dictionary/list, the contents of iterable[varName] can also be accessed. For example,  
if we have a dictionary like:
```
data = {'user': 'James Curran', 'knowledge': 'infinite', 'repeatCounter': 3}
```
then
```
{% for key in data %} <p>{{ key + ': ' data[key] }}</p> {% end for %}
```
will render to:
```
<p>user: James Curran</p>
<p>knowledge: infinite</p>
<p>repeatCounter: 3</p>
```

## Comments

Comments look like this:
```
{# this won't be rendered #}
```
Even if you place code inside this comment tag, it will not be rendered.


## Enjoy!
