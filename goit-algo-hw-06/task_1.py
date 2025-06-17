import networkx as nx
import matplotlib.pyplot as plt


# Undirected graph representing a real-world metro network
G = nx.Graph()

# Stations (nodes)
stations = [
    "Central", "North", "South", "East", "West",
    "Museum", "University", "Airport", "Stadium", "Park"
]

# Connections (edges)
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
