import re
import sys
from templating.nodes import *
from templating.regex import *
#from nodes import *
#from regex import *

class TemplateTree:
    def __init__(self,template):
        self.template = template

    def generateTree(self,endNode = None):
        tree = GroupNode()
        nodeType = "string"
        index = 0
        currentNode = None
        while self.template != "":
            # determine nodeType of currentNode
            if self.template[0] == "{":
                nodeType = "template"
            else:
                nodeType = "string"
            # extract current  node
            if nodeType == "string":
                nodeContent = ""
                # if current node is a text node
                while len(self.template) and self.template[0] != "{" :
                    nodeContent += self.template[0]
                    if len(self.template) > 1:
                        self.template = self.template[1:]
                    else:
                        self.template = ""
                tree.addChild(TextNode(nodeContent))
            else:
                nodeContent = ""
                numBraces = 0
                while len(self.template) and self.template[0] != "}":
                    if self.template[0] == "{":
                        numBraces += 1
                    nodeContent += self.template[0]
                    if len(self.template) > 1:
                        self.template = self.template[1:]
                    else:
                        self.template = ""
                nodeContent += self.template[:numBraces]
                self.template = self.template[numBraces:]
                for regex in regexes:
                    match = re.search(regexes[regex], nodeContent)
                    if match:
                        break
                else:
                    continue
                if endNode:
                    if endNode == 'for' and regex == 'endfor':
                        return tree
                    # TODO if
                if regex == 'include':
                    filename = match.group(2)
                    with open(filename) as f:
                        f = f.read()
                        tree.addChild(TemplateTree(f).generateTree())
                elif regex == 'expr':
                    tree.addChild(PythonNode(match.group(1)))
                elif regex == 'for':
                    print(match.groups())
                    tree.addChild(ForNode(match.group(1), match.group(2), self.generateTree('for')))
        return tree


def render_profiles(template, context):
    tree = TemplateTree(template).generateTree()
    print(tree)
    return tree.evaluate(context)

if __name__ == "__main__":
    with open('sample.html') as f:
        f = f.read()
        render_profiles(f, {})
