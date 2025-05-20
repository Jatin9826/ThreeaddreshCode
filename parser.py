class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

precedence = {'+':1, '-':1, '*':2, '/':2, '>':0, '<':0, '>=':0, '<=':0, '=':0}

def to_postfix(tokens):
    output, stack = [], []
    for token in tokens:
        if token.isalnum() or token.isidentifier():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def build_ast(postfix):
    stack = []
    for token in postfix:
        if token.isalnum() or token.isidentifier():
            stack.append(ASTNode(token))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(ASTNode(token, left, right))
    return stack[0]

from graphviz import Digraph

def visualize_ast(node, graph=None, count=[0]):
    if graph is None:
        graph = Digraph()
    nid = str(count[0])
    graph.node(nid, node.value)
    count[0] += 1

    if node.left:
        lid = visualize_ast(node.left, graph, count)
        graph.edge(nid, lid)
    if node.right:
        rid = visualize_ast(node.right, graph, count)
        graph.edge(nid, rid)

    return nid if graph else graph

def save_ast_image(ast, filename='ast'):
    graph = Digraph()
    visualize_ast(ast, graph)
    graph.render(filename, format='png', cleanup=True)