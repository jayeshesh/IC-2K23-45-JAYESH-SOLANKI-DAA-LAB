"""BFS and DFS Graph Traversals (Recursive and Iterative).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 7: Graphs (CO3)
"""

from typing import Dict, List, Set


def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """Breadth-First Search traversal using a queue."""
    visited: Set[str] = {start}
    queue: List[str] = [start]
    order: List[str] = []

    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order


def dfs_recursive(graph: Dict[str, List[str]], start: str, visited: Set[str] = None) -> List[str]:
    """Depth-First Search recursive traversal."""
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order


def dfs_iterative(graph: Dict[str, List[str]], start: str) -> List[str]:
    """Depth-First Search iterative traversal using a stack."""
    visited: Set[str] = set()
    stack: List[str] = [start]
    order: List[str] = []

    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            order.append(u)
            # Push in reverse to preserve alphabetical order
            for v in reversed(graph.get(u, [])):
                if v not in visited:
                    stack.append(v)
    return order


def demo() -> None:
    g = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print("BFS Order:        ", bfs(g, "A"))
    print("DFS Recursive:    ", dfs_recursive(g, "A"))
    print("DFS Iterative:    ", dfs_iterative(g, "A"))


if __name__ == "__main__":
    demo()
