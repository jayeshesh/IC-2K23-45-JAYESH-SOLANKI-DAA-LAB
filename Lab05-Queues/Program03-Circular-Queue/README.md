# Circular Queue (Ring Buffer)

**Language:** Python 3.10+  
**Run:** `python Lab05-Queues/Program03-Circular-Queue/circular_queue.py`

## 1. Problem statement
Implement a fixed-capacity circular queue (ring buffer) where `front` and `rear` pointers advance using modular arithmetic (`(index + 1) % capacity`), eliminating the linear queue false-overflow problem.

## 2. Approach
An array of size $N$ stores elements. When elements are dequeued from the front, subsequent enqueues wrap around to index 0 modulo $N$, allowing 100% capacity reuse.

## 3. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary Space |
|---|---:|---:|---:|---:|
| Enqueue | O(1) | O(1) | O(1) | O(1) |
| Dequeue | O(1) | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
Initial CQ: ['A', 'B', 'C']
Dequeued: A
After wrapping enqueue D: ['B', 'C', 'D']
```

## 5. Real-life application
Circular audio/video streaming buffers, keyboard input interrupt buffers, and network packet circular queues.
