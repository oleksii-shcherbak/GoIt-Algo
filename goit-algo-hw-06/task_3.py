import networkx as nx
import matplotlib.pyplot as plt
import heapq


G = nx.Graph()

stations = [
    "Central", "North", "South", "East", "West",
    "Museum", "University", "Airport", "Stadium", "Park"
]

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

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color='pink', node_size=2500, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("City Metro Network with Edge Weights")
plt.show()

print(f"Number of stations (nodes): {G.number_of_nodes()}")
print(f"Number of connections (edges): {G.number_of_edges()}")
print("\nDegree of each station:")
for node, degree in G.degree():
    print(f"- {node}: {degree} connection(s)")

def dijkstra(graph, start):
    """
    Calculate shortest paths from start node to all other nodes using Dijkstra's algorithm.
    """
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    # Build final paths
    paths = {}
    for target in graph.nodes:
        if distances[target] == float('inf'):
            paths[target] = None
        else:
            path = []
            node = target
            while node is not None:
                path.insert(0, node)
                node = previous[node]
            paths[target] = path

    return distances, paths

print("\nShortest paths using manual Dijkstra's algorithm:")

# Calculate shortest paths from each station
for src in stations:
    distances, paths = dijkstra(G, src)
    print(f"\nFrom {src}:")
    for dst in stations:
        if src != dst:
            path = paths[dst]
            dist = distances[dst]
            if path is not None:
                print(f" - to {dst}: {' -> '.join(path)} (distance: {dist})")
            else:
                print(f" - to {dst}: No path found")
