# god regex code
# the string returned in each regex match (accessed through groups(1), groups(2)...) is indicated in CAPS LOCK in the comment above the regex
# e.g. match = re.match(r'^\s*include\s+(\w+\.\w+)\s*$', 'include header.html')
# groups(1) will be header.html

# regex for {% include PATH %}
r'\s*include\s+(\w+\.\w+)\s*'

# regex for {% if PREDICATE %}
r'\s*if\s+(.+)\s*'

# regex for {% else %}
r'\s*else\s*'

# regex for {% end if %}
r'\s*end\s+if\s*'

# regex for {% for DEST in SRC %}
r'\s*for\s+(.+)\s+in\s+(.+)\s*'

# regex for {% end for %}
r'\s*end\s+for\s*'

# regex for a unary statement
r'{%(.+)%}'
