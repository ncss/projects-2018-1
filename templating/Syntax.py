import re
import sys
# from templating.nodes import *
# from templating.regex import *
from .nodes import *
from .regex import *

class TemplateSyntaxError(BaseException):
    pass

class TemplateTree:
    def __init__(self, template):
        self.template = re.sub(r'{#.*?#}', '', template, flags=re.S)

    def generateTree(self, endNode = None):
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
                    raise TemplateSyntaxError('Unknown tag: {}'.format(nodeContent))
                if endNode == 'for':
                    if regex == 'endfor':
                        return tree
                    elif regex == 'endif':
                        raise TemplateSyntaxError('Wrong closing tag. Expected for, got if.')
                if endNode == 'if':
                    if regex == 'endif':
                        return tree
                    elif regex == 'endfor':
                        raise TemplateSyntaxError('Wrong closing tag. Expected if, got for.')
                if (regex == 'endif' or regex =='endfor') and endNode is None:
                    raise TemplateSyntaxError('Attempted to close an unopened tag ({}).'.format(regex))
                if regex == 'include':
                    filename = match.group(2)
                    with open(filename) as f:
                        f = f.read()
                        tree.addChild(TemplateTree(f).generateTree())
                elif regex == 'expr':
                    tree.addChild(PythonNode(match.group(1)))
                elif regex == 'for':
                    tree.addChild(ForNode(match.group(1), match.group(2), self.generateTree('for')))
                elif regex == 'if':
                    tree.addChild(IfNode(match.group(1), self.generateTree('if')))
        if endNode:
            raise TemplateSyntaxError('Missing closing tag: {}'.format(endNode))
        return tree


def render_profiles(template, context):
    tree = TemplateTree(template).generateTree()
    return tree.evaluate(context)
