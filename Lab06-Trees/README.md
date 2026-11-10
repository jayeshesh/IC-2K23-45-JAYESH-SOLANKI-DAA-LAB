# Lab 06 – Trees

**Course:** IC-307D | Data Structures and Algorithms Lab  
**Unit:** Unit 6: Trees (CO3)  
**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Language:** Python 3.10+

---

## 1. Unit Overview
Unit 6 implements hierarchical non-linear tree data structures, self-balancing rotations, and practical tree applications:
- **Program 01:** Binary Tree Traversals (Recursive + Stack Iterative Inorder, Preorder, Postorder)
- **Program 02:** Binary Search Tree (Insert, Delete with successor replacement, Search, Min/Max, Validation)
- **Program 03:** AVL Tree (Self-balancing with LL, RR, LR, RL single and double rotations)
- **Program 04:** Threaded Binary Tree (Optional advanced topic with $O(1)$ space traversal)
- **Application 01:** File System Simulator (Hierarchical tree structure with `cd`, `mkdir`, `touch`, `tree`)
- **Application 02:** Expression Tree (Build from postfix and recursively evaluate)
- **Application 03:** Symbol Table for a Mini-Compiler (Fast identifier resolution using BST)
- **Application 04:** Directory Manager / Autocomplete Dictionary (Prefix Trie)

---

## 2. Directory Structure
```text
Lab06-Trees/
├── Program01-Binary-Tree-Traversals/
│   ├── binary_tree_traversals.py
│   └── README.md
├── Program02-Binary-Search-Tree/
│   ├── binary_search_tree.py
│   └── README.md
├── Program03-AVL-Tree/
│   ├── avl_tree.py
│   └── README.md
├── Program04-Threaded-Binary-Tree-Optional/
│   ├── threaded_binary_tree.py
│   └── README.md
├── Application-File-System-Simulator/
│   ├── file_system_simulator.py
│   └── README.md
├── Application-Expression-Tree/
│   ├── expression_tree.py
│   └── README.md
├── Application-Symbol-Table/
│   ├── symbol_table.py
│   └── README.md
├── Application-Directory-Manager/
│   ├── directory_manager_trie.py
│   └── README.md
├── reflection.md
└── README.md
```

---

## 3. Execution Instructions
Run from repository root:
```bash
python Lab06-Trees/Program01-Binary-Tree-Traversals/binary_tree_traversals.py
python Lab06-Trees/Program02-Binary-Search-Tree/binary_search_tree.py
python Lab06-Trees/Program03-AVL-Tree/avl_tree.py
python Lab06-Trees/Program04-Threaded-Binary-Tree-Optional/threaded_binary_tree.py
python Lab06-Trees/Application-File-System-Simulator/file_system_simulator.py
python Lab06-Trees/Application-Expression-Tree/expression_tree.py
python Lab06-Trees/Application-Symbol-Table/symbol_table.py
python Lab06-Trees/Application-Directory-Manager/directory_manager_trie.py
```

Run test suite:
```bash
python -m unittest tests/test_unit6.py
```
