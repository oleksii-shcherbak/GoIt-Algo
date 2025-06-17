import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

stations = [
    "Central", "North", "South", "East", "West",
    "Museum", "University", "Airport", "Stadium", "Park"
]

# Weighted connections (for Task 3)
connections = [
    ("Central", "North", 4),
    ("Central", "South", 2),
    ("Central", "East", 3),
    ("Central", "West", 6),
    ("North", "University", 3),
    ("South", "Airport", 5),
    ("East", "Museum", 2),
    ("West", "Park", 4),
    ("Museum", "University", 1),
    ("Stadium", "Park", 2),
    ("University", "Stadium", 3)
]

G.add_nodes_from(stations)
G.add_weighted_edges_from(connections)

pos = nx.spring_layout(G, seed=42)  # use fixed layout for consistency

plt.figure(figsize=(10, 7))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='pink',
    node_size=2500,
    font_weight='bold'
)

# Draw edge weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("City Metro Network with Edge Weights")
plt.show()

print(f"Number of stations (nodes): {G.number_of_nodes()}")
print(f"Number of connections (edges): {G.number_of_edges()}")
print("\nDegree of each station:")
for node, degree in G.degree():
    print(f"- {node}: {degree} connection(s)")

start = "Central"
end = "Stadium"

# BFS (shortest path by number of hops)
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

print("\nBFS path (shortest path by edges):")
print(" -> ".join(bfs_path))

print("\nDFS path (first depth-found path):")
print(" -> ".join(dfs_path))

# Dijkstra's algorithm for shortest path with weights
print("\nShortest paths using Dijkstra's algorithm (with weights):")

# Compute and display shortest path from each station to all others
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
all_shortest_lengths = dict(nx.all_pairs_dijkstra_path_length(G))

for src in stations:
    print(f"\nFrom {src}:")
    for dst in stations:
        if src != dst:
            path = all_shortest_paths[src][dst]
            distance = all_shortest_lengths[src][dst]
            print(f" - to {dst}: {' -> '.join(path)} (distance: {distance})")
