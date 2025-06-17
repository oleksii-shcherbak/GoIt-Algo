# Task 2: DFS and BFS Pathfinding

This task implements two graph traversal algorithms — Depth-First Search (DFS) and Breadth-First Search (BFS) — to find a path from "Central" to "Stadium" in the metro network graph.

---

**BFS path:**
Central → North → University → Stadium

**DFS path:**
Central → East → Museum → University → Stadium

---

BFS explores the graph level by level. It found the shortest path to "Stadium" through "North" and "University", using only three steps. This is expected since BFS is designed to return the shortest path in an unweighted graph.

DFS, on the other hand, explores as deeply as possible along one branch before backtracking. It first followed "East", then "Museum", "University", and finally "Stadium", resulting in a longer but valid path.

This difference in results is due to the traversal strategy. BFS prioritizes minimal steps, while DFS returns the first valid path it discovers, which may not be optimal.
