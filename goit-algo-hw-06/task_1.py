import networkx as nx
import matplotlib.pyplot as plt


# Create an undirected graph to represent the metro network
G = nx.Graph()

# Define metro stations as nodes
stations = [
    "Central", "North", "South", "East", "West",
    "Museum", "University", "Airport", "Stadium", "Park"
]

# Add nodes to the graph
G.add_nodes_from(stations)

# Define metro connections as edges (station-to-station links)
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

# Add edges to the graph
G.add_edges_from(connections)

# Create a layout for the nodes (spring layout for better visualization)
pos = nx.spring_layout(G, seed=42)

# Draw the graph
plt.figure(figsize=(10, 7))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='pink',
    node_size=1500,
    font_size=12,
    font_weight='bold',
    edge_color='gray'
)
plt.title("City Metro Transportation Network")
plt.show()

# Number of nodes (stations)
num_nodes = G.number_of_nodes()
print(f"Number of stations (nodes): {num_nodes}")

# Number of edges (connections)
num_edges = G.number_of_edges()
print(f"Number of connections (edges): {num_edges}")

# Degree of each node (station)
print("\nDegree of each station:")
for node, degree in G.degree():
    print(f" - {node}: {degree} connection(s)")

start = "Central"
end = "Stadium"

# BFS (Breadth-First Search) gives the shortest path in terms of number of edges
bfs_path = nx.shortest_path(G, source=start, target=end)

# DFS (Depth-First Search) explores deeply and may not return the shortest path
# Use dfs_edges to reconstruct a path manually
dfs_edges = list(nx.dfs_edges(G, source=start))
dfs_path = [start]
for u, v in dfs_edges:
    if dfs_path[-1] == u:
        dfs_path.append(v)
    elif u in dfs_path:
        dfs_path.append(v)
    if v == end:
        break

print("\nDFS path from Central to Stadium:")
print(" -> ".join(dfs_path))

print("\nBFS path from Central to Stadium:")
print(" -> ".join(bfs_path))

print("\nExplanation:")
print("BFS (Breadth-First Search) explores all neighboring stations level by level,")
print("so it always finds the shortest path in terms of number of connections.")
print("DFS (Depth-First Search) goes as deep as possible into one branch before backtracking,")
print("which can result in longer or suboptimal paths depending on the node visitation order.")
print("Therefore, BFS is typically better for shortest path problems in unweighted graphs.")
