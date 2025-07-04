import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    """
    Represents a node in a binary tree with a unique ID and optional color for visualization.
    """
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Unique ID for visualization


def build_heap_tree(arr, i=0):
    """
    Recursively builds a binary tree from a list `arr` interpreted as a binary heap.

    Parameters:
        arr (list): List of values representing a binary heap.
        i (int): Current index in the list.

    Returns:
        Node: Root of the binary tree.
    """
    if i >= len(arr):
        return None
    node = Node(arr[i])
    node.left = build_heap_tree(arr, 2 * i + 1)
    node.right = build_heap_tree(arr, 2 * i + 2)
    return node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Recursively adds nodes and edges to the NetworkX graph for visualization.

    Parameters:
        graph (nx.DiGraph): Graph object being built.
        node (Node): Current node being processed.
        pos (dict): Positions for node layout.
        x, y (float): Coordinates for node placement.
        layer (int): Current depth level in the tree.

    Returns:
        nx.DiGraph: Updated graph with added nodes and edges.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    """
    Draws the binary tree using NetworkX and matplotlib.

    Parameters:
        tree_root (Node): The root of the binary tree.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

if __name__ == "__main__":
    # Binary heap represented as a list
    heap = [1, 3, 6, 5, 9, 8, 10, 13, 15]

    # Build binary tree from heap array
    root = build_heap_tree(heap)

    # Visualize the binary tree
    draw_tree(root)
