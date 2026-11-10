# Graph Representations (Adjacency Matrix and Adjacency List)

**Language:** Python 3.10+  
**Run:** `python Lab07-Graphs/Program01-Graph-Representations/graph_representations.py`

## 1. Problem statement
Implement and compare the two fundamental graph representations: dense Adjacency Matrix ($V \times V$) and sparse Adjacency List ($V + E$).

## 2. Approach
- **Adjacency Matrix:** 2D grid storing connection weights. Edge query `has_edge(u, v)` is instant $O(1)$ time, but consumes $O(V^2)$ memory.
- **Adjacency List:** Hash map of lists storing neighbor vertices. Consumes space proportional to edges $O(V + E)$, making it optimal for sparse topologies.

## 3. Complexity comparison
| Representation | Storage Space | Add Edge | Check Edge (u, v) | Iterate Neighbors of u |
|---|---:|---:|---:|---:|
| Adjacency Matrix | O(V^2) | O(1) | O(1) | O(V) |
| Adjacency List | O(V + E) | O(1) | O(deg(u)) | O(deg(u)) |

## 4. Sample I/O
```text
Graph Matrix Neighbors of 0: [1, 2]
Graph List Neighbors of A: ['B', 'C']
```

## 5. Real-life application
Dense road traffic grid modeling (matrix) vs large-scale social networks and the internet web graph (adjacency list).
