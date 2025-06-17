import networkx as nx
import matplotlib.pyplot as plt


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

nx.draw(G, with_labels=True, node_color='pink', node_size=2500, font_weight='bold')
plt.title("City Metro Network")
plt.show()

print(f"Number of stations (nodes): {G.number_of_nodes()}")
print(f"Number of connections (edges): {G.number_of_edges()}")
print("\nDegree of each station:")
for node, degree in G.degree():
    print(f"- {node}: {degree} connection(s)")

start = "Central"
end = "Stadium"

# BFS (shortest path)
bfs_path = nx.shortest_path(G, source=start, target=end)

# DFS (first depth path)
dfs_edges = list(nx.dfs_edges(G, source=start))
dfs_path = [start]
visited = {start}

for u, v in dfs_edges:
    if u in dfs_path and v not in visited:
        dfs_path.append(v)
        visited.add(v)
    if v == end:
        break

print("\nBFS path (shortest path):")
print(" -> ".join(bfs_path))

print("\nDFS path (first depth-found path):")
print(" -> ".join(dfs_path))
