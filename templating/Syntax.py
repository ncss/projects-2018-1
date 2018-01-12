import re
import sys
import nodes
import regex


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

def group_parse(template,context,endNode = None):
    tree = GroupNode()
    nodeType = "string"
    index = 0
    currentNode = None
    while template != "":
        # determine nodeType of currentNode
        if template[0] == "{":
            nodeType = "template"
        else:
            nodeType = "string"
        # extract current  node
        if nodeType == "string":
            nodeContent = ""
            # if current node is a text node
            while template[0] != "{":
                nodeContent += template[0]
                template = template[1:]
            tree.addChild(TextNode(nodeContent))
        else:
            nodeContent = ""
            numBraces = 0
            while template[0] != "}":
                if template[0] == "{":
                    numBraces += 1
                nodeContent += template[0]
                template = template[1]
            nodeContent += template[:numBraces]
            template = template[numBraces:]
    return tree





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
