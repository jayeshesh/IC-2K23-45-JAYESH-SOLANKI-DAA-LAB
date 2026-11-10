# Capstone Project 4: Pathfinding Visualizer

**Language:** Python 3.10+  
**Run:** `python Capstone-Projects/Project04-Pathfinding-Visualizer/pathfinding_visualizer.py`

## 1. Problem statement
Build a pathfinding visualizer comparing BFS, DFS, and Dijkstra on 2D obstacle grids, rendering ASCII trajectory maps and tracking node expansion metrics.

## 2. Approach
The grid is modeled as an implicit graph ($R \times C$). The visualizer benchmarks frontier exploration order, total nodes evaluated, and reconstructs the optimal shortest path from goal back to start.

## 3. Complexity analysis
| Algorithm | Time Complexity | Auxiliary Space | Path Guarantee |
|---|---:|---:|---|
| BFS | O(R \times C) | O(R \times C) | Optimal (Fewest Steps) |
| DFS | O(R \times C) | O(R \times C) | Sub-optimal |
| Dijkstra | O((RC) \log(RC)) | O(R \times C) | Optimal (Minimum Weight) |

## 4. Sample I/O
```text
=== BFS Grid Path Visualizer ===
Path Length: 9 steps | Nodes Explored: 15
S * * * .
# # # * #
. . * * .
. # # # *
. . . . G
```

## 5. Learning outcomes
Visualized graph search dynamics and verified the optimality properties of BFS and Dijkstra.
