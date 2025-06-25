import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
from task_4 import build_heap_tree, add_edges

def generate_color(index, total, base_color="#1296F0"):
    """
    Generate a gradient color (in hex) from dark to light based on traversal order.

    Parameters:
        index (int): Current node's position in traversal.
        total (int): Total number of visited nodes.
        base_color (str): Base hex color (default is blue tone).

    Returns:
        str: Hex color string (e.g., '#4a6df0').
    """
    base = int(base_color[1:], 16)
    r = (base >> 16) & 0xFF
    g = (base >> 8) & 0xFF
    b = base & 0xFF

    factor = 0.4 + 0.6 * (index / max(total - 1, 1))  # Range: 0.4 to 1.0
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def bfs_coloring(root):
    """
    Perform Breadth-First Traversal and assign gradient colors to visited nodes.

    Parameters:
        root (Node): The root node of the binary tree.

    Returns:
        list: Ordered list of visited nodes.
    """
    queue = deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            # Enqueue left and right children
            queue.append(node.left)
            queue.append(node.right)

    # Assign colors in visitation order
    for i, node in enumerate(visited):
        node.color = generate_color(i, len(visited))
    return visited

def dfs_coloring(root):
    """
    Perform Depth-First Traversal using a stack and assign gradient colors.

    Parameters:
        root (Node): The root node of the binary tree.

    Returns:
        list: Ordered list of visited nodes.
    """
    stack = [root]
    visited = []

    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            # Push right first, so left is processed first
            stack.append(node.right)
            stack.append(node.left)

    for i, node in enumerate(visited):
        node.color = generate_color(i, len(visited))
    return visited

def draw_colored_tree(root, title):
    """
    Draw a binary tree with colored nodes using NetworkX and matplotlib.

    Parameters:
        root (Node): The root of the binary tree.
        title (str): Title of the plot.
    """
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [tree.nodes[n]['color'] for n in tree.nodes()]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes()}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Binary heap represented as a list
heap = [1, 3, 6, 5, 9, 8, 10, 13, 15]

# Build and visualize DFS traversal
root_dfs = build_heap_tree(heap)
dfs_coloring(root_dfs)
draw_colored_tree(root_dfs, "DFS Traversal Visualization")

# Build and visualize BFS traversal
root_bfs = build_heap_tree(heap)
bfs_coloring(root_bfs)
draw_colored_tree(root_bfs, "BFS Traversal Visualization")
