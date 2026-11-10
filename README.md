# IC-2K23-45-JAYESH-SOLANKI-DAA-LAB

**Course:** IC-307D | Data Structures and Algorithms Lab  
**Student:** Jayesh Solanki  
**Roll number:** IC-2K23-45  
**Institution:** International Institute of Professional Studies (IIPS), Devi Ahilya Vishwavidyalaya (DAVV), Indore  
**Implementation language:** Python 3.10+

[![Python Tests](https://github.com/jayeshesh/IC-2K23-45-JAYESH-SOLANKI-DAA-LAB/actions/workflows/python-tests.yml/badge.svg)](https://github.com/jayeshesh/IC-2K23-45-JAYESH-SOLANKI-DAA-LAB/actions/workflows/python-tests.yml)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

This repository implements the complete **IC-307D Data Structures & Algorithms Lab** syllabus curriculum, covering 7 core academic units, 4 end-semester capstone projects, automated unit testing suites, and academic report deliverables.

---

## Environment & Testing
- Python 3.10 or newer
- Standard library used for all core data structure implementations
- Matplotlib for Unit 2 empirical sorting benchmark graphs: `pip install -r requirements.txt`

Run the full automated test suite (54 unit tests) from repository root:
```bash
python -m unittest discover -s tests -v
```

---

## Laboratory Units Overview & Roadmap

| Unit | Topic | CO | Deliverables & Implementations | Status |
|---|---|---|---|:---:|
| [**Unit 1**](./Lab01-Introduction-Arrays/README.md) | **Introduction to Data Structures & Arrays** | CO1 | 1D & 2D Array Operations, Sparse Matrix Triple Format, Matrix Calculator | Completed |
| [**Unit 2**](./Lab02-Sorting-Searching/README.md) | **Sorting & Searching Algorithms** | CO2 | 8 Sorting Algorithms, Binary Search, Empirical Benchmarks, Student Records, Search Engine | Completed |
| [**Unit 3**](./Lab03-Linked-Lists/README.md) | **Linked Lists** | CO1 | Singly, Doubly, & Circular Linked Lists, Polynomial Addition, Text Editor Buffer, Playlist Manager | Completed |
| [**Unit 4**](./Lab04-Stacks/README.md) | **Stacks** | CO1 | Static & Dynamic Stacks, Infix to Postfix/Prefix (Shunting-Yard), Expression Evaluator, Undo/Redo | Completed |
| [**Unit 5**](./Lab05-Queues/README.md) | **Queues** | CO1 | Static, Dynamic, & Circular Queue (Ring Buffer), Deque, Priority Queues (Array & Min-Heap), Round-Robin CPU Scheduler | Completed |
| [**Unit 6**](./Lab06-Trees/README.md) | **Trees** | CO3 | Binary Tree Traversals, BST, AVL Rotations, Threaded BST, File System Simulator, Expression Tree, Symbol Table, Trie | Completed |
| [**Unit 7**](./Lab07-Graphs/README.md) | **Graphs** | CO3 | Adjacency Matrix & List, BFS & DFS Traversals, Dijkstra Shortest Path, Social Network Graph, Maze Solver, Topological Sort | Completed |

---

## End-Semester Capstone Projects

Located in [`Capstone-Projects/`](./Capstone-Projects/README.md):
1. **[Project 01: Mini Database Engine](./Capstone-Projects/Project01-Mini-Database-Engine/README.md)**: Tabular CRUD records engine combining hash primary indexing $O(1)$ and secondary BST range indexing $O(\log n)$.
2. **[Project 02: Hospital Management System](./Capstone-Projects/Project02-Hospital-Management/README.md)**: Clinical operations simulator with emergency triage min-heap, doctor consultation stack, department tree, and epidemic contact tracing graph.
3. **[Project 03: E-Commerce Backend Simulator](./Capstone-Projects/Project03-ECommerce-Backend-Simulator/README.md)**: Production e-commerce engine with BST product catalog, shopping cart undo stack, FIFO order queue, and co-purchase recommendation graph.
4. **[Project 04: Pathfinding Visualizer](./Capstone-Projects/Project04-Pathfinding-Visualizer/README.md)**: Grid pathfinding engine comparing BFS, DFS, and Dijkstra on 2D obstacle mazes with step-by-step ASCII visual rendering.

---

## Documentation Deliverables

Located in [`docs/`](./docs/README.md):
- **[Algorithm Complexity Report (PDF)](./docs/complexity-analysis.pdf)**: Complete mathematical and empirical best/average/worst asymptotic matrix across all implemented structures.
- **[Final Laboratory Academic Report (PDF)](./docs/final-report.pdf)**: Complete academic documentation covering aims, algorithms, complexities, test evidence, and learning outcomes.
- **[Presentation Slides (PDF)](./docs/presentation.pdf)**: Slide deck highlighting algorithmic paradigms and capstone architectures.
- **[Diagrams & Algorithm Flowcharts](./docs/algorithm-flowcharts/README.md)**: Flowcharts and architectural block diagrams.

---

## Academic References
1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
2. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley Professional.
3. Devi Ahilya Vishwavidyalaya (DAVV). *Master of Computer Applications (MCA) Data Structures & Algorithms Lab Syllabus (IC-307D)*.
