"""Graph Representations (Adjacency Matrix and Adjacency List).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 7: Graphs (CO3)
"""

from typing import Dict, List, Set


class GraphMatrix:
    """Adjacency Matrix representation for an undirected/directed graph."""

    def __init__(self, num_vertices: int, directed: bool = False) -> None:
        self.V: int = num_vertices
        self.directed: bool = directed
        self.matrix: List[List[int]] = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight

    def has_edge(self, u: int, v: int) -> bool:
        return self.matrix[u][v] != 0

    def get_neighbors(self, u: int) -> List[int]:
        return [v for v in range(self.V) if self.matrix[u][v] != 0]


class GraphList:
    """Adjacency List representation for an undirected/directed graph."""

    def __init__(self, directed: bool = False) -> None:
        self.directed: bool = directed
        self.adj: Dict[str, List[str]] = {}

    def add_vertex(self, u: str) -> None:
        if u not in self.adj:
            self.adj[u] = []

    def add_edge(self, u: str, v: str) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def get_neighbors(self, u: str) -> List[str]:
        return self.adj.get(u, [])


def demo() -> None:
    gm = GraphMatrix(4)
    gm.add_edge(0, 1)
    gm.add_edge(0, 2)
    gm.add_edge(1, 3)
    print("Graph Matrix Neighbors of 0:", gm.get_neighbors(0))

    gl = GraphList()
    gl.add_edge("A", "B")
    gl.add_edge("A", "C")
    gl.add_edge("B", "D")
    print("Graph List Neighbors of A:", gl.get_neighbors("A"))


if __name__ == "__main__":
    demo()
