"""Maze Solver and Shortest Path Navigator (Grid as Graph).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 7: Graphs (CO3) Application
"""

from typing import List, Optional, Tuple


def solve_maze_bfs(
    grid: List[List[int]],
    start: Tuple[int, int],
    goal: Tuple[int, int],
) -> Optional[List[Tuple[int, int]]]:
    """Find the shortest path in a 2D binary maze (0 = open, 1 = wall) using BFS."""
    rows, cols = len(grid), len(grid[0])
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None

    queue: List[Tuple[int, int]] = [start]
    visited = {start}
    parent = {start: None}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        r, c = queue.pop(0)
        if (r, c) == goal:
            # Reconstruct path
            path = []
            curr: Optional[Tuple[int, int]] = goal
            while curr:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    return None


def demo() -> None:
    # 0 = open path, 1 = obstacle
    maze = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0],
    ]
    start = (0, 0)
    goal = (3, 3)
    path = solve_maze_bfs(maze, start, goal)
    print("Maze Shortest Path from (0,0) to (3,3):")
    print(path)


if __name__ == "__main__":
    demo()
