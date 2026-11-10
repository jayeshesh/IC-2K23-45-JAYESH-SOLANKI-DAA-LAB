# Unit 5 Reflection – Queues

**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Course:** IC-307D | Data Structures and Algorithms Lab

## 1. What was learned
- Designing FIFO data structures and resolving false queue overflow through circular ring-buffer modulo pointer arithmetic.
- Comparing priority queue implementations: Unsorted Array ($O(1)$ insert, $O(n)$ extract) vs. Binary Min-Heap ($O(\log n)$ insert and extract).
- Implementing Round-Robin CPU scheduling using circular queue execution cycles.

## 2. Difficulties encountered
- Managing the heap array indexing formula ($2i+1$ and $2i+2$) while maintaining the min-heap shape invariant during deletions.
- Distinguishing queue full versus empty states in circular queues by tracking an explicit size variable.

## 3. Optimizations applied
- Used binary min-heap for logarithmic priority operations instead of costly linear array scans.
- Implemented Deque using doubly linked lists with tail pointers for strict $O(1)$ front and rear operations.
