# Static Stack (Array-Based)

**Language:** Python 3.10+  
**Run:** `python Lab04-Stacks/Program01-Static-Stack/static_stack.py`

## 1. Problem statement
Implement a fixed-capacity static stack backed by a fixed array, supporting standard LIFO operations: `push`, `pop`, `peek`, `is_empty`, and `is_full` with explicit overflow/underflow exception handling.

## 2. Approach
A pre-allocated fixed-size list stores elements. A `_top` index tracking the top-of-stack advances upon push and recedes upon pop. When `_top == capacity - 1`, push triggers `StackOverflowError`.

## 3. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary space |
|---|---:|---:|---:|---:|
| Push | O(1) | O(1) | O(1) | O(1) |
| Pop | O(1) | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
Stack elements: [10, 20, 30]
Top element: 30
Popped: 30
After pop: [10, 20]
```

## 5. Real-life application
Embedded firmware call stacks, fixed-size interrupt buffers, and hardware CPU registers.
