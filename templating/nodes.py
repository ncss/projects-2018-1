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
        return html.escape(eval(self.expression))

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
        iterable = list(self.iterable)
