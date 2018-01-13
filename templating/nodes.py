import html

def indent(s):
    return ('  ' + s.replace('\n', '\n  '))[:-2]
    # return s

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

    def __str__(self):
        # print(repr(self.value))
        s = self.value.replace('\n', '\\n')
        if len(s) < 20:
            return '\'' + s + '\'\n'
        else:
            return '\'' + s[:10] + '...' + s[-10:] + '\'\n'

    def evaluate(self, context):
        return str(self.value)


class GroupNode(Node):
    def __init__(self):
        self.children = []

    def __str__(self):
        result = 'Groupnode\n'
        # print(self.children)
        for node in self.children:
            result += indent(str(node))
            # print(str(node))
        return result

    def addChild(self, newNode):
        self.children.append(newNode)

    def evaluate(self, context):
        theString = ""
        for node in self.children:
            theString += node.evaluate(context)

        return theString

class PythonNode(Node):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value + '\n'

    def evaluate(self, context):
        return html.escape(str(eval(self.value, {}, context)))


class IfNode(Node):
    def __init__(self, condition, child):
        self.condition = condition
        self.child = child

    def evaluate(self, context):
        if eval(self.condition, {}, context):
            return self.child.evaluate(context)
        else:
            return ""

class ForNode(Node):
    def __init__(self, variableName, iterable, child):
        self.variableName = variableName
        self.iterable = iterable
        self.child = child

    def __str__(self):
        return 'for {} in {}'.format(self.variableName, self.iterable) + str(self.child)

    def evaluate(self, context):
        iterable = eval(self.iterable, {}, context)
        variableName = self.variableName
        newString = ""
        for item in iterable:
            context[variableName] = item
            newString += self.child.evaluate(context)

        return newString

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
