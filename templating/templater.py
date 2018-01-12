from templating.nodes import *

from templating.Syntax import render_profiles
render = render_profiles
# "def render(originString, context):
#     mode = "string"
#     string = ""
#     nodeString = ""
#     nodeStack = GroupNode()
#
#     while originString != "":
#         if mode == "string":
#             if originString[:2] == "{{":
#                 mode = "python"
#                 nodeStack.addChild(TextNode(string))
#                 string = ""
#                 nodeString = ""
#                 originString = originString[2:]
#             else:
#                 string += originString[0]
#                 originString = originString[1:]
#         elif mode == "python":
#             if originString[:2] == "}}":
#                 mode = "string"
#                 originString = originString[2:]
#                 string = ""
#                 # Process Nodestring
#                 nodeStack.addChild(PythonNode(nodeString))
#             else:
#                 nodeString += originString[0]
#                 originString = originString[1:]
#
#     nodeStack.addChild(TextNode(string))
#     string = ""
#     return nodeStack.evaluate(context)
#
# # Group node parser -> Give a 'end node' and it will finish parsing when it hits that end node.
# # group node parser: give it a string, it will iterate over it detecting tags and adding anything it can, will call other parsers
# # for node parser:
# # if node parser
