# Priority Queue (Min-Heap Based)

**Language:** Python 3.10+  
**Run:** `python Lab05-Queues/Program06-Priority-Queue-Heap/priority_queue_heap.py`

## 1. Problem statement
Implement an efficient Priority Queue backed by a binary min-heap array representation with logarithmic $O(\log n)$ insertions (`sift_up`) and extractions (`sift_down`).

## 2. Approach
A binary heap tree is mapped to a contiguous array where node $i$ has children at $2i + 1$ and $2i + 2$, with parent at $\lfloor(i - 1)/2\rfloor$. The min-heap property ($A[\text{parent}] \le A[\text{child}]$) guarantees the minimum element is always at index 0.

## 3. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary Space |
|---|---:|---:|---:|---:|
| Insert | O(1) | O(log n) | O(log n) | O(1) |
| Extract-Min | O(log n) | O(log n) | O(log n) | O(1) |
| Peek-Min | O(1) | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
Peek min: Critical Alarm
Extract min: Critical Alarm
Extract next: Important Notice
```

## 5. Real-life application
Dijkstra's shortest path algorithm, Prim's minimum spanning tree, Huffman coding compression, and OS real-time thread scheduling.
