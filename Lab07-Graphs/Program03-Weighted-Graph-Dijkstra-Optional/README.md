# Weighted Graph and Dijkstra's Shortest Path Algorithm

**Language:** Python 3.10+  
**Run:** `python Lab07-Graphs/Program03-Weighted-Graph-Dijkstra-Optional/dijkstra.py`

## 1. Problem statement
Find the single-source shortest path in a weighted non-negative directed/undirected graph using Dijkstra's greedy algorithm with a priority queue (min-heap).

## 2. Approach
Maintain a table of tentative distances from the source, initializing all to $\infty$ and source to 0. A binary min-heap extracts the closest unvisited vertex $u$, relaxing all outgoing edges $(u, v)$ where $\text{dist}[u] + w < \text{dist}[v]$.

## 3. Complexity analysis
| Metric | Value |
|---|---:|
| Time Complexity | O((V + E) \log V) |
| Auxiliary Space | O(V) |

## 4. Sample I/O
```text
Shortest path from Indore to Jabalpur: Indore -> Bhopal -> Jabalpur
Total distance: 505.0 km
```

## 5. Real-life application
GPS navigation road networks (Google Maps, OSRM), internet packet IP routing protocols (OSPF, IS-IS).
