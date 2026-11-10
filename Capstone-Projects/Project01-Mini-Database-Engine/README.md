# Capstone Project 1: Mini Database Engine

**Language:** Python 3.10+  
**Run:** `python Capstone-Projects/Project01-Mini-Database-Engine/mini_database_engine.py`

## 1. Problem statement
Design and implement an in-memory database engine combining arrays, linked lists, primary hash indexing, and secondary BST indexing to support CRUD record operations and fast range/indexed queries.

## 2. Architecture & Algorithms
- **Primary Index:** Hash map mapping integer Record IDs to tuple payload dictionaries in $O(1)$ amortized time.
- **Secondary Index:** Binary Search Tree index on continuous attributes (e.g. salary), indexing record IDs for logarithmic search and range scans.
- **Query Processing:** Supports primary key point lookups, secondary indexed scans, and sorting.

## 3. Complexity analysis
| Operation | Average | Worst | Auxiliary Space |
|---|---:|---:|---:|
| Create (Insert) | O(log n) (due to BST index) | O(n) | O(1) per record |
| Read (Primary Key) | O(1) | O(n) | O(1) |
| Read (Indexed Field) | O(log n) | O(n) | O(k) matching |
| Update Record | O(1) | O(1) | O(1) |
| Delete Record | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
All Records: [{'id': 1, 'name': 'Jayesh', 'role': 'AI Engineer', 'salary': 85000.0}, {'id': 2, 'name': 'Aarav', 'role': 'Data Analyst', 'salary': 65000.0}, {'id': 3, 'name': 'Priya', 'role': 'System Architect', 'salary': 85000.0}]

Lookup by Primary Key (ID 1): {'id': 1, 'name': 'Jayesh', 'role': 'AI Engineer', 'salary': 85000.0}
Secondary BST Index Query (Salary 85000): [{'id': 1, ...}, {'id': 3, ...}]
```

## 5. Learning outcomes
Synthesized hash tables, BST indexing, and relational records into a complete functional mini database engine.
