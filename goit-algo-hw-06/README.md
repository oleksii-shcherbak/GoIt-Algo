# Task 2: DFS and BFS Pathfinding

This task implements two graph traversal algorithms — Depth-First Search (DFS) and Breadth-First Search (BFS) — to find a path from "Central" to "Stadium" in the metro network graph.

---

**BFS path:**
Central → West → Park → Stadium

**DFS path:**
Central → North → University → Museum → East → Stadium

---

Both paths are valid but differ in length and structure due to the nature of the algorithms.

BFS explores the graph level by level. It found the shortest path to "Stadium" in just three steps, going through "West" and "Park". This is expected, as BFS is designed to return the shortest path (by number of edges) in an unweighted graph.

DFS, on the other hand, explores as deeply as possible before backtracking. It followed a longer route through "North", "University", "Museum", and "East" before reaching "Stadium". This path is valid but not the most efficient. DFS does not guarantee the shortest path, especially when multiple paths exist.

The difference in output is caused by the order of node exploration. BFS ensures minimal steps, while DFS follows the first discovered complete path regardless of length.
