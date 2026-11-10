# Expression Tree (Build from Postfix and Evaluate)

**Language:** Python 3.10+  
**Run:** `python Lab06-Trees/Application-Expression-Tree/expression_tree.py`

## 1. Problem statement
Construct a binary Expression Tree from a stream of postfix tokens using an operand node stack, and evaluate its result recursively using postorder tree traversal.

## 2. Approach
Operands become leaf nodes. When an operator is read, pop two subtrees, assign them as left and right children of a new operator node, and push back. Evaluation recursively evaluates subtrees and applies the node's operator.

## 3. Complexity analysis
| Operation | Time | Auxiliary Space |
|---|---:|---:|
| Build Expression Tree | O(n) | O(n) |
| Evaluate Expression Tree | O(n) | O(h) |

## 4. Sample I/O
```text
Inorder Infix from Tree: ((5 + 3) * 2)
Evaluated Value: 16.0
```

## 5. Real-life application
Compiler intermediate representation (IR), symbolic differentiation engines, SQL query parse trees.
