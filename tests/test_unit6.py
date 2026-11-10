"""Unit tests for Unit 6: Trees.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Program01-Binary-Tree-Traversals"))
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Program02-Binary-Search-Tree"))
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Program03-AVL-Tree"))
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Program04-Threaded-Binary-Tree-Optional"))
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Application-File-System-Simulator"))
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Application-Expression-Tree"))
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Application-Symbol-Table"))
sys.path.insert(0, str(REPO_ROOT / "Lab06-Trees" / "Application-Directory-Manager"))

from binary_tree_traversals import (
    TreeNode,
    inorder_recursive,
    inorder_iterative,
    preorder_recursive,
    preorder_iterative,
    postorder_recursive,
    postorder_iterative,
)
from binary_search_tree import BinarySearchTree
from avl_tree import AVLTree
from threaded_binary_tree import ThreadedBinaryTree
from file_system_simulator import FileSystemSimulator
from expression_tree import build_expression_tree, evaluate_expression_tree
from symbol_table import SymbolTableBST
from directory_manager_trie import AutocompleteTrie


class TestTrees(unittest.TestCase):
    def test_traversals(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(inorder_recursive(root), [2, 1, 3])
        self.assertEqual(inorder_iterative(root), [2, 1, 3])
        self.assertEqual(preorder_recursive(root), [1, 2, 3])
        self.assertEqual(preorder_iterative(root), [1, 2, 3])
        self.assertEqual(postorder_recursive(root), [2, 3, 1])
        self.assertEqual(postorder_iterative(root), [2, 3, 1])

    def test_bst_and_validation(self):
        bst = BinarySearchTree()
        for k in [40, 20, 60, 10, 30, 50, 70]:
            bst.insert(k)
        self.assertTrue(bst.is_valid_bst())
        self.assertTrue(bst.search(50))
        self.assertFalse(bst.search(999))
        self.assertEqual(bst.find_min(), 10)
        self.assertEqual(bst.find_max(), 70)
        bst.delete(20)
        self.assertFalse(bst.search(20))
        self.assertTrue(bst.is_valid_bst())

    def test_avl_tree(self):
        avl = AVLTree()
        for k in [10, 20, 30, 40, 50, 25]:
            avl.insert(k)
        self.assertEqual(avl.inorder(), [10, 20, 25, 30, 40, 50])
        self.assertEqual(avl.root.key, 30)  # Balanced root

    def test_threaded_tree(self):
        tbt = ThreadedBinaryTree()
        for k in [20, 10, 30, 5, 15]:
            tbt.insert(k)
        self.assertEqual(tbt.inorder(), [5, 10, 15, 20, 30])

    def test_applications(self):
        # File System
        fs = FileSystemSimulator()
        fs.mkdir("docs")
        fs.touch("readme.txt")
        self.assertEqual(fs.list_dir(), ["docs", "readme.txt"])

        # Expression Tree: (4 + 6) * 2 = 20
        expr_tree = build_expression_tree(["4", "6", "+", "2", "*"])
        self.assertEqual(evaluate_expression_tree(expr_tree), 20.0)

        # Symbol Table
        st = SymbolTableBST()
        st.insert("x", "int", 0, 42)
        self.assertEqual(st.lookup("x").value, 42)

        # Autocomplete Trie
        trie = AutocompleteTrie()
        trie.insert("cat")
        trie.insert("caterpillar")
        self.assertEqual(trie.autocomplete("cat"), ["cat", "caterpillar"])


if __name__ == "__main__":
    unittest.main()
