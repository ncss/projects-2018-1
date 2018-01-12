import re
import sys
from nodes import *
from regex import *

def isValidTemplate(template):
  toconcat = []
  matches = []
  x = False
  for line in template:
     toconcat.append(line.strip())
  tree = "".join(toconcat)
  for char in tree:
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
    raise TypeError

  for item in matches:
    for regex in regexes:
      if bool(re.match(regexes[regex],item)) == False:
        raise TypeError
  return True

def generateTree(template, endNode = None):
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
            while len(template) and template[0] != "{" :
                nodeContent += template[0]
                if len(template) > 1:
                    template = template[1:]
                else:
                    template = ""
            tree.addChild(TextNode(nodeContent))
        else:
            nodeContent = ""
            numBraces = 0
            while len(template) and template[0] != "}":
                if template[0] == "{":
                    numBraces += 1
                nodeContent += template[0]
                if len(template) > 1:
                    template = template[1:]
                else:
                    template = ""
            nodeContent += template[:numBraces]
            template = template[numBraces:]
            for regex in regexes:
                match = re.search(regexes[regex], nodeContent)
                if match:
                    break
            if regex == 'include':
                filename = match.group(2)
                with open(filename) as f:
                    f = f.read()
                    tree.addChild(generateTree(f))
            elif regex == 'expr':
                tree.addChild(PythonNode(match.group(1)))
            else:
                raise TypeError
    return tree




def render_profiles(context, file):
  try:
    with open(file) as f:
      f = f.read()
      tree = generateTree(f)
      print(tree.evaluate(context))
  except TypeError as e:
    #ncssbook_log.exception(e)
    return False
  else:
    #tree.render(sys.stdout,context)
    return True

render_profiles({'desu': 'world!!'}, 'html.txt')
