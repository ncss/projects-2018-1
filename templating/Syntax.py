import re
import sys
from templating.nodes import *
from templating.regex import *
#from nodes import *
#from regex import *

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
            else:
                continue
            if endNode:
                if endNode == 'for' and regex == 'endFor':
                    return tree
                # TODO if
            if regex == 'include':
                filename = match.group(2)
                with open(filename) as f:
                    f = f.read()
                    tree.addChild(generateTree(f))
            elif regex == 'expr':
                tree.addChild(PythonNode(match.group(1)))
            elif regex == 'for':
                print(match.groups())
                tree.addChild(ForNode(match.group(1), match.group(2), generateTree(template, 'for')))
    return tree

def render_profiles(template, context):
    tree = generateTree(template)
    return tree.evaluate(context)
