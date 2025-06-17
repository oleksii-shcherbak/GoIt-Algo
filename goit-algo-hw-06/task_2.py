import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


G = nx.Graph()

stations = [
    "Central", "North", "South", "East", "West",
    "Museum", "University", "Airport", "Stadium", "Park"
]

connections = [
    ("Central", "North"),
    ("Central", "South"),
    ("Central", "East"),
    ("Central", "West"),
    ("North", "University"),
    ("South", "Airport"),
    ("East", "Museum"),
    ("West", "Park"),
    ("Museum", "University"),
    ("Stadium", "Park"),
    ("University", "Stadium")
]

G.add_nodes_from(stations)
G.add_edges_from(connections)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 7))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='pink',
    node_size=2500,
    font_weight='bold'
)
plt.title("City Metro Network")
plt.show()

print(f"Number of stations (nodes): {G.number_of_nodes()}")
print(f"Number of connections (edges): {G.number_of_edges()}")
print("\nDegree of each station:")
for node, degree in G.degree():
    print(f"- {node}: {degree} connection(s)")

def bfs(graph, start, target):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == target:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in sorted(graph.neighbors(node)):  # sorted for stable order
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
    return None

def dfs(graph, start, target):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == target:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(sorted(graph.neighbors(node))):  # reversed(sorted) for deep-first order
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
    return None

start = "Central"
end = "Stadium"

bfs_path = bfs(G, start, end)
dfs_path = dfs(G, start, end)

print("\nBFS path (shortest path by edges):")
print(" -> ".join(bfs_path))

print("\nDFS path (first depth-found path):")
print(" -> ".join(dfs_path))
