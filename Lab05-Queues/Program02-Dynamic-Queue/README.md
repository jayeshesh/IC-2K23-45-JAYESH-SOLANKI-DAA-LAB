# Dynamic Queue (Linked-List Based)

**Language:** Python 3.10+  
**Run:** `python Lab05-Queues/Program02-Dynamic-Queue/dynamic_queue.py`

## 1. Problem statement
Implement an unbounded dynamic queue using singly linked nodes with `front_node` and `rear_node` pointers, guaranteeing worst-case $O(1)$ enqueue and dequeue operations without capacity restrictions.

## 2. Approach
`enqueue` appends to `rear_node` in $O(1)$ time; `dequeue` detaches `front_node` in $O(1)$ time.

## 3. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary Space |
|---|---:|---:|---:|---:|
| Enqueue | O(1) | O(1) | O(1) | O(1) |
| Dequeue | O(1) | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) | O(1) |

## 4. Sample I/O
```text
Queue: ['Task1', 'Task2', 'Task3']
Dequeued: Task1
Peek: Task2
```

## 5. Real-life application
Asynchronous task queues (e.g., Celery, RabbitMQ workers) and operating system message-passing queues.
