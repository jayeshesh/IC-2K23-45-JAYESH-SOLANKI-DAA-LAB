"""Route Planner and Network Connectivity Analyzer.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 7: Graphs (CO3) Application
"""

from typing import Dict, List, Set


class NetworkAnalyzer:
    """Analyzes network connectivity, bridges, and critical communication paths."""

    def __init__(self) -> None:
        self.adj: Dict[str, Set[str]] = {}

    def add_connection(self, u: str, v: str) -> None:
        if u not in self.adj:
            self.adj[u] = set()
        if v not in self.adj:
            self.adj[v] = set()
        self.adj[u].add(v)
        self.adj[v].add(u)

    def is_connected(self) -> bool:
        """Check if all nodes in the network can communicate."""
        if not self.adj:
            return True
        start = next(iter(self.adj))
        visited: Set[str] = set()
        queue = [start]
        visited.add(start)

        while queue:
            curr = queue.pop(0)
            for neighbor in self.adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == len(self.adj)

    def find_all_routes(self, source: str, destination: str, visited: Set[str] = None) -> List[List[str]]:
        """Find all simple non-cyclic paths between two nodes using backtracking DFS."""
        if visited is None:
            visited = set()
        if source == destination:
            return [[destination]]
        if source not in self.adj:
            return []

        visited.add(source)
        paths: List[List[str]] = []

        for neighbor in self.adj[source]:
            if neighbor not in visited:
                sub_paths = self.find_all_routes(neighbor, destination, visited.copy())
                for sp in sub_paths:
                    paths.append([source] + sp)

        return paths


def demo() -> None:
    na = NetworkAnalyzer()
    na.add_connection("Server1", "RouterA")
    na.add_connection("RouterA", "RouterB")
    na.add_connection("RouterB", "Database")
    na.add_connection("RouterA", "Database")  # Redundant backup path

    print("Is Entire Network Fully Connected?", na.is_connected())
    routes = na.find_all_routes("Server1", "Database")
    print(f"Discovered {len(routes)} distinct redundant routes:")
    for r in routes:
        print(" ", " -> ".join(r))


if __name__ == "__main__":
    demo()
