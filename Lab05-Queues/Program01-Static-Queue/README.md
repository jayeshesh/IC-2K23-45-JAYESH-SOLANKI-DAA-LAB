# Static Queue (Array-Based)

**Language:** Python 3.10+  
**Run:** `python Lab05-Queues/Program01-Static-Queue/static_queue.py`

## 1. Problem statement
Implement a fixed-capacity static queue backed by a pre-allocated array supporting FIFO `enqueue`, `dequeue`, and `peek` with explicit overflow/underflow handling.

## 2. Approach
A fixed-capacity array holds items. `_front` and `_rear` indices track boundaries. `enqueue` increments `_rear` in $O(1)$; `dequeue` increments `_front` in $O(1)$.

## 3. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary Space |
|---|---:|---:|---:|---:|
| Enqueue | O(1) | O(1) | O(1) | O(1) |
| Dequeue | O(1) | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
Static Queue: [1, 2, 3]
Dequeued: 1
Front: 2
```

## 5. Real-life application
Fixed hardware buffering in embedded communication peripherals (UART, SPI buffers).
