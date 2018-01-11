import re
import sys

def _parse_template(template,upto,parent):
  Toconcat = []
  for line in template:
     Toconcat.append(line.strip())
  Tree = "".join(Toconcat)
  for char in Tree:
    if char == "{":
      #Regex check function
      
  
def render_profiles(context):
  try:
    with open('html.txt') as f:
      tree = _parse_template(f.read(),0,None)
  except ParseError as e:
    #ncssbook_log.exception(e)
    return False
  else:
    #tree.render(sys.stdout,context)
    return True
      
render_profiles()       
  
