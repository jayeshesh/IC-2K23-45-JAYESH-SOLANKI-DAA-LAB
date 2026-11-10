"""Unit tests for Unit 7: Graphs.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "Lab07-Graphs" / "Program01-Graph-Representations"))
sys.path.insert(0, str(REPO_ROOT / "Lab07-Graphs" / "Program02-BFS-DFS"))
sys.path.insert(0, str(REPO_ROOT / "Lab07-Graphs" / "Program03-Weighted-Graph-Dijkstra-Optional"))
sys.path.insert(0, str(REPO_ROOT / "Lab07-Graphs" / "Application-Social-Network-Graph"))
sys.path.insert(0, str(REPO_ROOT / "Lab07-Graphs" / "Application-Maze-Shortest-Path"))
sys.path.insert(0, str(REPO_ROOT / "Lab07-Graphs" / "Application-Course-Prerequisite-Tracker-Bonus"))
sys.path.insert(0, str(REPO_ROOT / "Lab07-Graphs" / "Application-Route-Planner"))

from graph_representations import GraphMatrix, GraphList
from bfs_dfs import bfs, dfs_recursive, dfs_iterative
from dijkstra import WeightedGraph
from social_network_graph import SocialNetworkGraph
from maze_solver import solve_maze_bfs
from course_prerequisite_tracker import topological_sort_kahn
from route_planner import NetworkAnalyzer


class TestGraphs(unittest.TestCase):
    def test_representations(self):
        gm = GraphMatrix(3)
        gm.add_edge(0, 1)
        self.assertTrue(gm.has_edge(0, 1))
        self.assertTrue(gm.has_edge(1, 0))
        self.assertFalse(gm.has_edge(0, 2))

        gl = GraphList()
        gl.add_edge("X", "Y")
        self.assertIn("Y", gl.get_neighbors("X"))
        self.assertIn("X", gl.get_neighbors("Y"))

    def test_traversals(self):
        g = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
        self.assertEqual(bfs(g, "A"), ["A", "B", "C"])
        self.assertEqual(dfs_recursive(g, "A"), ["A", "B", "C"])
        self.assertEqual(dfs_iterative(g, "A"), ["A", "B", "C"])

    def test_dijkstra(self):
        wg = WeightedGraph()
        wg.add_edge("A", "B", 1)
        wg.add_edge("B", "C", 2)
        wg.add_edge("A", "C", 10)
        dist, path = wg.get_shortest_path("A", "C")
        self.assertEqual(dist, 3)
        self.assertEqual(path, ["A", "B", "C"])

    def test_applications(self):
        # Social Network
        sn = SocialNetworkGraph()
        sn.add_friendship("A", "B")
        sn.add_friendship("B", "C")
        self.assertEqual(sn.get_friends_of_friends("A"), {"C"})

        # Maze Solver
        grid = [[0, 0], [1, 0]]
        self.assertEqual(solve_maze_bfs(grid, (0, 0), (1, 1)), [(0, 0), (0, 1), (1, 1)])

        # Topological Sort
        order = topological_sort_kahn(["A", "B"], [("A", "B")])
        self.assertEqual(order, ["A", "B"])

        # Network Analyzer
        na = NetworkAnalyzer()
        na.add_connection("A", "B")
        self.assertTrue(na.is_connected())


if __name__ == "__main__":
    unittest.main()
