import heapq

class Graph:
    def __init__(self):
        """
        Initializes an empty graph using an adjacency list.
        """
        self.graph = {}

    def add_edge(self, u, v, weight):
        """
        Adds a directed edge from u to v with the given weight.
        For an undirected graph, add_edge(v, u, weight) should also be called.
        """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def get_neighbors(self, u):
        """
        Returns a list of (neighbor, weight) tuples for a given vertex u.
        """
        return self.graph.get(u, [])

    def get_all_vertices(self):
        """
        Returns a set of all vertices in the graph.
        """
        vertices = set(self.graph.keys())
        for u in self.graph:
            for v, _ in self.graph[u]:
                vertices.add(v)
        return vertices

def dijkstra(graph: Graph, start_vertex):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a start_vertex
    to all other vertices in a weighted graph.

    Args:
        graph: An instance of the Graph class.
        start_vertex: The starting vertex for path computation.

    Returns:
        A tuple:
        - distances: A dictionary where keys are vertices and values are their
                     shortest distances from the start_vertex.
        - predecessors: A dictionary where keys are vertices and values are their
                        predecessor in the shortest path. Can be used to reconstruct paths.
    """
    distances = {vertex: float('inf') for vertex in graph.get_all_vertices()}
    distances[start_vertex] = 0
    predecessors = {vertex: None for vertex in graph.get_all_vertices()}

    # Priority queue stores tuples of (distance, vertex)
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we've already found a shorter path to current_vertex, skip
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight

            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, start_vertex, end_vertex):
    """
    Reconstructs the shortest path from start_vertex to end_vertex
    using the predecessors dictionary.
    """
    path = []
    current = end_vertex
    while current is not None:
        path.insert(0, current)
        if current == start_vertex:
            break
        current = predecessors[current]
    if path[0] == start_vertex:
        return path
    else:
        return [] # No path found

if __name__ == "__main__":
    # Create a graph
    g1 = Graph()
    g1.add_edge('A', 'B', 4)
    g1.add_edge('A', 'C', 2)
    g1.add_edge('B', 'E', 3)
    g1.add_edge('C', 'D', 2)
    g1.add_edge('C', 'F', 4)
    g1.add_edge('D', 'E', 3)
    g1.add_edge('D', 'F', 1)
    g1.add_edge('E', 'G', 1)
    g1.add_edge('F', 'G', 1)

    print("Graph created:")
    for vertex in g1.get_all_vertices():
        neighbors = g1.get_neighbors(vertex)
        if neighbors:
            print(f"  {vertex}: {neighbors}")

    start_node = 'A'
    print(f"\nRunning Dijkstra's algorithm from start node: {start_node}")
    shortest_distances, path_predecessors = dijkstra(g1, start_node)

    print("\nShortest distances from starting node 'A':")
    for vertex, distance in shortest_distances.items():
        if distance == float('inf'):
            print(f"  To {vertex}: Unreachable")
        else:
            print(f"  To {vertex}: {distance}")

    print("\nPaths reconstructed:")
    for target_node in g1.get_all_vertices():
        if target_node != start_node:
            path = reconstruct_path(path_predecessors, start_node, target_node)
            if path:
                print(f"  Path from {start_node} to {target_node}: {' -> '.join(path)}")
            else:
                print(f"  No path from {start_node} to {target_node}")
