# AVL Tree (Self-Balancing BST)

**Language:** Python 3.10+  
**Run:** `python Lab06-Trees/Program03-AVL-Tree/avl_tree.py`

## 1. Problem statement
Implement an AVL Tree that maintains a strict balance factor condition ($\text{Balance} \in \{-1, 0, +1\}$) for every node, automatically executing single (LL, RR) or double (LR, RL) rotations during insertion to guarantee $O(\log n)$ height.

## 2. Approach
After standard recursive BST insertion, the call stack updates heights and calculates $\text{balance} = \text{height(left)} - \text{height(right)}$. If $|\text{balance}| > 1$, the appropriate rotation (LL, RR, LR, RL) rebalances the subtree in $O(1)$ pointer adjustments.

## 3. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary Space |
|---|---:|---:|---:|---:|
| Search | O(log n) | O(log n) | O(log n) | O(1) |
| Insert | O(log n) | O(log n) | O(log n) | O(log n) |
| Rotations | O(1) | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
AVL Inorder: [10, 20, 25, 30, 40, 50]
AVL Root: 30
AVL Root Height: 3
```

## 5. Real-life application
High-frequency database search trees, router IP routing lookup tables, and in-memory key-value indexes.
