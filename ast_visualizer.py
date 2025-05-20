from graphviz import Digraph

def visualize_ast(node, graph=None, parent=None):
    if graph is None:
        graph = Digraph()
        graph.node('0', type(node).__name__)
        parent = '0'
    node_id = str(id(node))
    graph.node(node_id, type(node).__name__)

    if parent:
        graph.edge(parent, node_id)

    if hasattr(node, 'statements'):
        for stmt in node.statements:
            visualize_ast(stmt, graph, node_id)
    if hasattr(node, 'condition'):
        visualize_ast(node.condition, graph, node_id)
    if hasattr(node, 'then_stmt'):
        visualize_ast(node.then_stmt, graph, node_id)
    if hasattr(node, 'else_stmt') and node.else_stmt:
        visualize_ast(node.else_stmt, graph, node_id)
    if hasattr(node, 'body'):
        visualize_ast(node.body, graph, node_id)
    if hasattr(node, 'left'):
        visualize_ast(node.left, graph, node_id)
    if hasattr(node, 'right'):
        visualize_ast(node.right, graph, node_id)
    if hasattr(node, 'expr'):
        visualize_ast(node.expr, graph, node_id)
    return graph
