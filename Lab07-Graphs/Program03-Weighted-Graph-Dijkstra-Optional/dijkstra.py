"""Weighted Graph and Dijkstra's Shortest Path Algorithm (Optional / Advanced).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 7: Graphs (CO3)
"""

import heapq
from typing import Dict, List, Optional, Tuple


class WeightedGraph:
    """Weighted graph supporting Dijkstra's single-source shortest path algorithm."""

    def __init__(self, directed: bool = False) -> None:
        self.directed: bool = directed
        self.adj: Dict[str, List[Tuple[str, float]]] = {}

    def add_edge(self, u: str, v: str, weight: float) -> None:
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def dijkstra(self, source: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
        """Compute shortest distances and predecessors from source using min-heap."""
        distances: Dict[str, float] = {v: float("inf") for v in self.adj}
        predecessors: Dict[str, Optional[str]] = {v: None for v in self.adj}
        distances[source] = 0.0

        # Min-heap stores (dist, vertex)
        pq: List[Tuple[float, str]] = [(0.0, source)]

        while pq:
            curr_dist, u = heapq.heappop(pq)
            if curr_dist > distances[u]:
                continue

            for v, weight in self.adj.get(u, []):
                new_dist = curr_dist + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    predecessors[v] = u
                    heapq.heappush(pq, (new_dist, v))

        return distances, predecessors

    def get_shortest_path(self, source: str, target: str) -> Tuple[float, List[str]]:
        """Reconstruct the optimal path and total distance between source and target."""
        distances, predecessors = self.dijkstra(source)
        if distances[target] == float("inf"):
            return float("inf"), []
        path = []
        curr: Optional[str] = target
        while curr:
            path.append(curr)
            curr = predecessors[curr]
        return distances[target], path[::-1]


def demo() -> None:
    wg = WeightedGraph()
    wg.add_edge("Indore", "Bhopal", 195)
    wg.add_edge("Indore", "Ujjain", 55)
    wg.add_edge("Ujjain", "Bhopal", 185)
    wg.add_edge("Bhopal", "Jabalpur", 310)
    wg.add_edge("Indore", "Khandwa", 130)

    dist, path = wg.get_shortest_path("Indore", "Jabalpur")
    print(f"Shortest path from Indore to Jabalpur: {' -> '.join(path)}")
    print(f"Total distance: {dist} km")


if __name__ == "__main__":
    demo()
