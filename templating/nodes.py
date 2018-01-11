import html

class Node:
    def evaluate(self):
        pass
        # Returns a string

class TextNode(Node):
    """
    thisText = TextNode("Value of the thisText")

    thisText.evaluate()

    """
    def __init__(self, value):
        self.value = value

    def evaluate(self, context):
        return str(self.value)


class GroupNode(Node):
    def __init__(self):
        self.children = []

    def addChild(self, newNode):
        self.children.append(newNode)

    def evaluate(self, context):
        theString = ""
        for node in self.children:
            theString += node.evaluate(context)

        return theString

class PythonNode(Node):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, context):
        return html.escape(eval(self.expression, {}, context))


class IfNode(Node):
    def __init__(self, condition, child):
        self.condition = condition
        self.child = child

    def evaluate(self, context):
        if eval(self.condition):
            return self.child.evaluate(context)
        else:
            return ""




# class VariableNode(Node):
#     def __init__(self, expression):
#         self.expression = expression
#
#     def evaluate():
#         pass

class ForNode(Node):
    def __init__(self, variableName, iterable, child):
        self.variableName = variableName
        self.iterable = iterable
        self.child = child

    def evaluate(self, context):
        iterable = eval(self.iterable, {}, context)
        variableName = self.variableName
        newString = ""
        for item in iterable:
            context[variableName] = item
            newString += self.child.evaluate(context)

        return newString


            # {% for variableName in iterable %}
## TEST CODE
# ga = GroupNode()
#
# group = GroupNode()
# group.addChild(PythonNode("item"))
# group.addChild(PythonNode("item"))
# group.addChild(PythonNode("item"))
# forNode = ForNode("item", '["a", "b", "c"]', group)
#
# ga.addChild(forNode)
#
# ifNode = IfNode("1 == 0", TextNode("Hello!!!"))
# ga.addChild(ifNode)
# print(ga.evaluate({}))



test = """
<h1> This is a {{test}} </h1>
"""
mode = "string"

string = ""
nodeString = ""

nodeStack = GroupNode()

def processPython(nodeString):
    nodeStack.addChild(PythonNode(nodeString))

def processNode(nodeString):
    nodeStack.addChild(PythonNode(nodeString))

def endString():
    global string
    nodeStack.addChild(TextNode(string))
    string = ""

while test != "":
    print(test)
    print(mode)
    if mode == "string":
        if test[:2] == "{{":
            mode = "python"
            endString()
            test = test[2:]
        elif test[:2] == "{%":
            mode = "python"
            endString()
            test = test[2:]
        else:
            string += test[0]
            test = test[1:]
    elif node == "python":
        if test[:2] == "}}":
            mode = "string"
            test = test[2:]
            string = ""
            # Process Nodestring
            processPython(nodeString)
        else:
            nodeString += test[0]
            test = test[1:]

    elif node == "node":
        if test[:2] == "%}":
            mode = "string"
            test = test[2:]
            string = ""
            # Process Nodestring
            processNode(nodeString)
        else:
            nodeString += test[0]
            test = test[1:]

endString()
print(nodeStack.evaluate({"test": "Hello"}))
