"""Unit tests for Unit 2 sorting, searching, and applications."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / "Lab02-Sorting-Searching"
sys.path.insert(0, str(UNIT))
sys.path.insert(0, str(UNIT / "Application-Student-Record-Manager"))
sys.path.insert(0, str(UNIT / "Application-Search-Engine-Simulator"))

from sorting_algorithms import SORTS, binary_search, bubble_sort, insertion_sort, merge_sort, radix_sort
from student_record_manager import Student, search_students, sort_students
from search_engine_simulator import ChainingHashTable, DictionarySearchEngine, LinearProbingHashTable


class TestSortingAlgorithms(unittest.TestCase):
    def test_all_sorts_cover_edge_cases(self):
        cases = [[], [1], [3, 1, 2], [5, -1, 0, -9, 5], [2, 2, 2], list(range(30, -1, -1))]
        for name, algorithm in SORTS.items():
            for case in cases:
                with self.subTest(algorithm=name, case=case):
                    original = case[:]
                    self.assertEqual(algorithm(case), sorted(case))
                    self.assertEqual(case, original)

    def test_stable_sorts(self):
        records = [("x", 1), ("y", 1), ("z", 0)]
        for algorithm in (bubble_sort, insertion_sort, merge_sort):
            self.assertEqual(algorithm(records, key=lambda item: item[1]),
                             [("z", 0), ("x", 1), ("y", 1)])

    def test_radix_validation(self):
        with self.assertRaises(TypeError): radix_sort([1, 2.5, 3])

    def test_binary_search_boundaries(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 5, 8], 2), 1)
        self.assertEqual(binary_search([1, 2, 5], 7), -1)
        self.assertEqual(binary_search([], 1), -1)


class TestStudentRecords(unittest.TestCase):
    def setUp(self):
        self.records = [
            Student("R03", "Aarav Shah", 78),
            Student("R01", "Diya Patel", 91),
            Student("R02", "Aarav Shah", 91),
        ]

    def test_sort_each_field_including_radix_marks(self):
        self.assertEqual([s.roll_no for s in sort_students(self.records, "roll_no")],
                         ["R01", "R02", "R03"])
        self.assertEqual([s.name for s in sort_students(self.records, "name")],
                         ["Aarav Shah", "Aarav Shah", "Diya Patel"])
        self.assertEqual([s.marks for s in sort_students(self.records, "marks", "radix")],
                         [78, 91, 91])

    def test_search_duplicates_and_missing(self):
        self.assertEqual(len(search_students(self.records, "name", "aarav shah")), 2)
        self.assertEqual(len(search_students(self.records, "marks", 91, "linear")), 2)
        self.assertEqual(search_students(self.records, "roll_no", "R99"), [])

    def test_invalid_records_and_radix_fields(self):
        with self.assertRaises(ValueError): Student("", "Name", 50)
        with self.assertRaises(ValueError): Student("R1", "Name", 120)
        with self.assertRaises(ValueError): sort_students(self.records, "age")
        with self.assertRaises(ValueError): sort_students(self.records, "name", "radix")
        decimal = [Student("R4", "Name", 75.5)]
        with self.assertRaises(ValueError): sort_students(decimal, "marks", "radix")


class TestSearchEngine(unittest.TestCase):
    def test_all_lookup_strategies_and_update(self):
        engine = DictionarySearchEngine([("Tree", "hierarchy"), ("Graph", "network")])
        for strategy in ("binary", "chaining", "linear-probing"):
            self.assertEqual(engine.lookup("TREE", strategy), "hierarchy")
            self.assertIsNone(engine.lookup("missing", strategy))
        engine.add("tree", "updated")
        for strategy in ("binary", "chaining", "linear-probing"):
            self.assertEqual(engine.lookup("tree", strategy), "updated")

    def test_chaining_collision_and_delete(self):
        table = ChainingHashTable(5)
        table.add("a", "first"); table.add("f", "second")
        self.assertGreater(table.collision_count, 0)
        self.assertEqual(table.get("f"), "second")
        self.assertTrue(table.remove("a"))
        self.assertEqual(table.get("f"), "second")

    def test_linear_probing_collision_and_tombstone(self):
        table = LinearProbingHashTable(5)
        table.add("a", "first"); table.add("f", "second")
        self.assertGreater(table.collision_count, 0)
        self.assertEqual(table.get("f"), "second")
        self.assertTrue(table.remove("a"))
        self.assertEqual(table.get("f"), "second")
        table.add("k", "third")
        self.assertEqual(table.get("k"), "third")

    def test_hash_resizing(self):
        chain, linear = ChainingHashTable(5), LinearProbingHashTable(5)
        for i in range(20):
            chain.add(f"word{i}", str(i)); linear.add(f"word{i}", str(i))
        for i in range(20):
            self.assertEqual(chain.get(f"word{i}"), str(i))
            self.assertEqual(linear.get(f"word{i}"), str(i))


if __name__ == "__main__":
    unittest.main()
