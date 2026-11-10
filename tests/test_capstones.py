"""Unit tests for Capstone Projects.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "Capstone-Projects" / "Project01-Mini-Database-Engine"))
sys.path.insert(0, str(REPO_ROOT / "Capstone-Projects" / "Project02-Hospital-Management"))
sys.path.insert(0, str(REPO_ROOT / "Capstone-Projects" / "Project03-ECommerce-Backend-Simulator"))
sys.path.insert(0, str(REPO_ROOT / "Capstone-Projects" / "Project04-Pathfinding-Visualizer"))

from mini_database_engine import MiniDatabaseEngine
from hospital_management import HospitalManagementSystem
from ecommerce_backend import ECommerceBackend
from pathfinding_visualizer import PathfindingVisualizer


class TestCapstoneProjects(unittest.TestCase):
    def test_mini_database(self):
        db = MiniDatabaseEngine("TestTable")
        id1 = db.create("DevA", "Backend", 50000.0)
        self.assertEqual(db.read(id1)["name"], "DevA")
        db.update(id1, salary=60000.0)
        self.assertEqual(db.read(id1)["salary"], 60000.0)
        self.assertEqual(len(db.query_by_salary(60000.0)), 1)
        db.delete(id1)
        self.assertIsNone(db.read(id1))
        self.assertEqual(len(db.query_by_salary(60000.0)), 0)

    def test_hospital_management(self):
        hosp = HospitalManagementSystem()
        hosp.admit_patient("Minor", 4)
        hosp.admit_patient("Critical", 1)
        # Critical patient should be treated first
        self.assertEqual(hosp.treat_next_patient(), "Critical")
        self.assertEqual(hosp.treat_next_patient(), "Minor")
        hosp.add_contact("P1", "P2")
        self.assertEqual(hosp.trace_contacts("P1"), {"P2"})

    def test_ecommerce_backend(self):
        ec = ECommerceBackend()
        ec.add_product(1, "Phone", 20000.0)
        ec.add_to_cart(1)
        oid = ec.checkout("Jayesh")
        self.assertEqual(oid, 1)
        order = ec.process_next_order()
        self.assertEqual(order["customer"], "Jayesh")

    def test_pathfinding_visualizer(self):
        grid = [[0, 0], [0, 0]]
        viz = PathfindingVisualizer(grid, (0, 0), (1, 1))
        bfs_path, _ = viz.visualize_bfs()
        self.assertEqual(len(bfs_path), 3)
        self.assertEqual(bfs_path[0], (0, 0))
        self.assertEqual(bfs_path[-1], (1, 1))


if __name__ == "__main__":
    unittest.main()
