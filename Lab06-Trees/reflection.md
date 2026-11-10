# Unit 6 Reflection – Trees

**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Course:** IC-307D | Data Structures and Algorithms Lab

## 1. What was learned
- Implementing recursive and stack-based iterative depth-first traversals across binary trees.
- Mastering tree restructuring and self-balancing through single and double AVL rotations.
- Exploring tree-structured application domains: file hierarchies, expression evaluation ASTs, compiler symbol tables, and prefix autocompletion Tries.

## 2. Difficulties encountered
- Managing height recalculation and multi-parent pointer re-wiring during double rotations (LR and RL).
- In-place successor replacement during BST deletion of two-child nodes.

## 3. Optimizations applied
- Used iterative stack simulation to guarantee safety against Python recursion limits on deep trees.
- Leveraged single-threaded pointers to achieve $O(1)$ auxiliary space during tree iteration without call stacks.
