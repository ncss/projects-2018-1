import re
import sys

regexes = {}
           
def _parse_template(template):
  toconcat = []
  matches = []
  x = False
  for line in template:
     toconcat.append(line.strip())
  Tree = "".join(toconcat)
  for char in Tree:
    if x == True and char != "}":
      s += char
    if char == "}":
      matches.append(s)
      x = False
    if char == "{":
      s = ''
      x = True
  # finished scanning all characters
  # if x is still true, then an ending curly brace hasn't ended
  if x == True:
    raise ParseError
    
  for item in matches:
    for regex in regexes:
      if bool(re.match(regexes[regex],item)) == False:
        raise ParseError
  return 
      
  
def render_profiles(context):
  try:
    with open('html.txt') as f:
      tree = _parse_template(f.read())
  except ParseError as e:
    #ncssbook_log.exception(e)
    return False
  else:
    #tree.render(sys.stdout,context)
    return True
      
render_profiles()       
  
