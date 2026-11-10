# Dynamic Stack (Linked List Based)

**Language:** Python 3.10+  
**Run:** `python Lab04-Stacks/Program02-Dynamic-Stack/dynamic_stack.py`

## 1. Problem statement
Implement an unbounded dynamic stack using a linked list structure where memory grows and shrinks dynamically per push/pop operation with no artificial maximum size limit.

## 2. Approach
Nodes (`StackNode`) link downward. `push` prepends a new node as `top_node` in $O(1)$ time; `pop` detaches `top_node` and advances to `top_node.next` in $O(1)$ time.

## 3. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary space |
|---|---:|---:|---:|---:|
| Push | O(1) | O(1) | O(1) | O(1) |
| Pop | O(1) | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
Stack bottom to top: ['A', 'B', 'C']
Peek top: C
Popped: C
After pop: ['A', 'B']
```

## 5. Real-life application
Programming language execution call stacks, JVM operand stack, and unlimited backtracking history.
