"""Capstone Project 4: Pathfinding Visualizer.

Compares and visualizes BFS, DFS, and Dijkstra on 2D grid mazes with step-by-step ASCII terminal rendering.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import heapq
from typing import Dict, List, Optional, Set, Tuple


class PathfindingVisualizer:
    """Visualizes grid search pathfinding algorithms (BFS, DFS, Dijkstra)."""

    def __init__(self, grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> None:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = start
        self.goal = goal

    def visualize_bfs(self) -> Tuple[Optional[List[Tuple[int, int]]], int]:
        queue = [self.start]
        visited: Set[Tuple[int, int]] = {self.start}
        parent: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {self.start: None}
        nodes_explored = 0

        while queue:
            curr = queue.pop(0)
            nodes_explored += 1
            if curr == self.goal:
                break
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr[0] + dr, curr[1] + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        parent[(nr, nc)] = curr
                        queue.append((nr, nc))

        return self._reconstruct_path(parent), nodes_explored

    def visualize_dijkstra(self) -> Tuple[Optional[List[Tuple[int, int]]], int]:
        pq: List[Tuple[float, Tuple[int, int]]] = [(0.0, self.start)]
        distances: Dict[Tuple[int, int], float] = {self.start: 0.0}
        parent: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {self.start: None}
        nodes_explored = 0

        while pq:
            curr_dist, curr = heapq.heappop(pq)
            nodes_explored += 1
            if curr == self.goal:
                break
            if curr_dist > distances[curr]:
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr[0] + dr, curr[1] + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 0:
                    weight = 1.0
                    new_dist = curr_dist + weight
                    if (nr, nc) not in distances or new_dist < distances[(nr, nc)]:
                        distances[(nr, nc)] = new_dist
                        parent[(nr, nc)] = curr
                        heapq.heappush(pq, (new_dist, (nr, nc)))

        return self._reconstruct_path(parent), nodes_explored

    def _reconstruct_path(self, parent: Dict[Tuple[int, int], Optional[Tuple[int, int]]]) -> Optional[List[Tuple[int, int]]]:
        if self.goal not in parent:
            return None
        path = []
        curr: Optional[Tuple[int, int]] = self.goal
        while curr:
            path.append(curr)
            curr = parent[curr]
        return path[::-1]

    def render_grid(self, path: Optional[List[Tuple[int, int]]]) -> str:
        path_set = set(path) if path else set()
        lines = []
        for r in range(self.rows):
            row_chars = []
            for c in range(self.cols):
                if (r, c) == self.start:
                    row_chars.append("S")
                elif (r, c) == self.goal:
                    row_chars.append("G")
                elif (r, c) in path_set:
                    row_chars.append("*")
                elif self.grid[r][c] == 1:
                    row_chars.append("#")
                else:
                    row_chars.append(".")
            lines.append(" ".join(row_chars))
        return "\n".join(lines)


def demo() -> None:
    # 0 = open, 1 = wall
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    start = (0, 0)
    goal = (4, 4)

    viz = PathfindingVisualizer(grid, start, goal)
    bfs_path, bfs_explored = viz.visualize_bfs()
    dijk_path, dijk_explored = viz.visualize_dijkstra()

    print("=== BFS Grid Path Visualizer ===")
    print(f"Path Length: {len(bfs_path)} steps | Nodes Explored: {bfs_explored}")  # type: ignore
    print(viz.render_grid(bfs_path))

    print("\n=== Dijkstra Grid Path Visualizer ===")
    print(f"Path Length: {len(dijk_path)} steps | Nodes Explored: {dijk_explored}")  # type: ignore


if __name__ == "__main__":
    demo()
