"""Unit tests for Unit 1 array and matrix programs.

The repository folder names intentionally follow the lab guide and contain
hyphens, so each program directory is added directly to sys.path.
"""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PROGRAM_DIRS = [
    "Lab01-Introduction-Arrays/Program01-ArrayOperations",
    "Lab01-Introduction-Arrays/Program02-2DArrayOperations",
    "Lab01-Introduction-Arrays/Program03-SparseMatrix",
    "Lab01-Introduction-Arrays/Program04-MatrixCalculator",
]
for relative in PROGRAM_DIRS:
    sys.path.insert(0, str(ROOT / relative))

from array_operations import delete_at, insert_at, rotate_right, search
from array_2d_operations import (
    delete_column, delete_row, insert_column, insert_row, rotate_clockwise,
    search as search_2d,
)
from sparse_matrix import (
    add as sparse_add, from_triples, multiply as sparse_multiply,
    to_triples, transpose as sparse_transpose,
)
from matrix_calculator import add, determinant, multiply, transpose


class TestOneDimensionalArrays(unittest.TestCase):
    def test_insert_delete_search_rotate(self):
        data = [1, 2, 3]
        self.assertEqual(insert_at(data, 1, 9), [1, 9, 2, 3])
        changed, removed = delete_at(data, 1)
        self.assertEqual((changed, removed), ([1, 3], 2))
        self.assertEqual(search(data, 3), 2)
        self.assertEqual(search(data, 99), -1)
        self.assertEqual(rotate_right(data, 1), [3, 1, 2])
        self.assertEqual(rotate_right(data, -1), [2, 3, 1])
        self.assertEqual(rotate_right([], 8), [])

    def test_invalid_positions(self):
        with self.assertRaises(IndexError):
            insert_at([1], 3, 2)
        with self.assertRaises(IndexError):
            delete_at([1], 1)


class TestTwoDimensionalArrays(unittest.TestCase):
    def test_row_and_column_operations(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(insert_row(matrix, 1, [8, 9]), [[1, 2], [8, 9], [3, 4]])
        self.assertEqual(delete_row(matrix, 0), ([[3, 4]], [1, 2]))
        self.assertEqual(insert_column(matrix, 1, [5, 6]), [[1, 5, 2], [3, 6, 4]])
        self.assertEqual(delete_column(matrix, 0), ([[2], [4]], [1, 3]))

    def test_search_rotate_and_invalid_shape(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(search_2d(matrix, 5), [(1, 1)])
        self.assertEqual(rotate_clockwise(matrix), [[4, 1], [5, 2], [6, 3]])
        with self.assertRaises(ValueError):
            rotate_clockwise([[1, 2], [3]])


class TestSparseMatrices(unittest.TestCase):
    def test_conversion_transpose_add_multiply(self):
        a = to_triples([[1, 0], [0, 2]])
        b = to_triples([[3, 0], [0, 4]])
        self.assertEqual(from_triples(a), [[1, 0], [0, 2]])
        self.assertEqual(sparse_transpose(a), [(2, 2, 2), (0, 0, 1), (1, 1, 2)])
        self.assertEqual(sparse_add(a, b), to_triples([[4, 0], [0, 6]]))
        self.assertEqual(sparse_multiply(a, b), to_triples([[3, 0], [0, 8]]))

    def test_invalid_triples(self):
        with self.assertRaises(ValueError):
            from_triples([(2, 2, 1), (2, 0, 5)])


class TestMatrixCalculator(unittest.TestCase):
    def test_operations(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        self.assertEqual(add(a, b), [[6, 8], [10, 12]])
        self.assertEqual(multiply(a, b), [[19, 22], [43, 50]])
        self.assertEqual(transpose(a), [[1, 3], [2, 4]])
        self.assertEqual(determinant(a), -2)

    def test_dimension_errors(self):
        with self.assertRaises(ValueError):
            add([[1]], [[1, 2]])
        with self.assertRaises(ValueError):
            multiply([[1, 2]], [[1, 2]])
        with self.assertRaises(ValueError):
            determinant([[1, 2, 3], [4, 5, 6]])


if __name__ == "__main__":
    unittest.main()
