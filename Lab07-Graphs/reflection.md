# Unit 7 Reflection – Graphs

**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Course:** IC-307D | Data Structures and Algorithms Lab

## 1. What was learned
- Balancing space-time trade-offs between Adjacency Matrix ($O(V^2)$ storage, $O(1)$ edge query) and Adjacency List ($O(V+E)$ storage, optimal for sparse topologies).
- Leveraging BFS for unweighted shortest paths and Dijkstra's algorithm with min-heaps for non-negative weighted graphs.
- Detecting dependency cycles and linearizing task DAGs using Kahn's topological sort.

## 2. Difficulties encountered
- Ensuring Dijkstra correctly relaxes edges without infinite loops on cyclic graphs by strictly comparing extracted distances with recorded best distances.
- Backtracking state management when enumerating all simple paths in route planning to avoid cycle deadlocks.

## 3. Optimizations applied
- Used `heapq` binary min-heap for Dijkstra, reducing time from $O(V^2)$ to $O((V+E)\log V)$.
- Used sets for $O(1)$ visited membership checks in BFS/DFS.
