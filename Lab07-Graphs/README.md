# Lab 07 – Graphs

**Course:** IC-307D | Data Structures and Algorithms Lab  
**Unit:** Unit 7: Graphs (CO3)  
**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Language:** Python 3.10+

---

## 1. Unit Overview
Unit 7 implements fundamental graph representations, network traversals, and shortest-path optimization algorithms:
- **Program 01:** Graph Representations (Adjacency Matrix vs. Adjacency List)
- **Program 02:** BFS & DFS Traversals (Queue-based BFS, Recursive DFS, and Stack-based Iterative DFS)
- **Program 03:** Weighted Graphs & Dijkstra's Algorithm (Priority queue min-heap single-source shortest path)
- **Application 01:** Social Network / Friendship Graph (2-hop friends-of-friends & connected components)
- **Application 02:** Maze Solver (Grid graph modeling with BFS optimal path reconstruction)
- **Application 03:** Course Prerequisite Tracker (Topological sort using Kahn's algorithm with cycle detection)
- **Application 04:** Route Planner & Network Connectivity Analyzer (Backtracking simple route enumeration)

---

## 2. Directory Structure
```text
Lab07-Graphs/
├── Program01-Graph-Representations/
│   ├── graph_representations.py
│   └── README.md
├── Program02-BFS-DFS/
│   ├── bfs_dfs.py
│   └── README.md
├── Program03-Weighted-Graph-Dijkstra-Optional/
│   ├── dijkstra.py
│   └── README.md
├── Application-Social-Network-Graph/
│   ├── social_network_graph.py
│   └── README.md
├── Application-Maze-Shortest-Path/
│   ├── maze_solver.py
│   └── README.md
├── Application-Course-Prerequisite-Tracker-Bonus/
│   ├── course_prerequisite_tracker.py
│   └── README.md
├── Application-Route-Planner/
│   ├── route_planner.py
│   └── README.md
├── reflection.md
└── README.md
```

---

## 3. Execution Instructions
Run from repository root:
```bash
python Lab07-Graphs/Program01-Graph-Representations/graph_representations.py
python Lab07-Graphs/Program02-BFS-DFS/bfs_dfs.py
python Lab07-Graphs/Program03-Weighted-Graph-Dijkstra-Optional/dijkstra.py
python Lab07-Graphs/Application-Social-Network-Graph/social_network_graph.py
python Lab07-Graphs/Application-Maze-Shortest-Path/maze_solver.py
python Lab07-Graphs/Application-Course-Prerequisite-Tracker-Bonus/course_prerequisite_tracker.py
python Lab07-Graphs/Application-Route-Planner/route_planner.py
```

Run test suite:
```bash
python -m unittest tests/test_unit7.py
```
