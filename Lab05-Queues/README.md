# Lab 05 – Queues

**Course:** IC-307D | Data Structures and Algorithms Lab  
**Unit:** Unit 5: Queues (CO1)  
**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Language:** Python 3.10+

---

## 1. Unit Overview
Unit 5 implements FIFO queues, double-ended queues, and priority structures:
- **Program 01:** Static Queue (array-based linear queue)
- **Program 02:** Dynamic Queue (linked-list based unbounded queue)
- **Program 03:** Circular Queue (ring buffer with modular indexing)
- **Program 04:** Deque (double-ended queue with $O(1)$ operations at both ends)
- **Program 05:** Priority Queue using Unsorted Array ($O(1)$ insert, $O(n)$ extract)
- **Program 06:** Priority Queue using Binary Min-Heap ($O(\log n)$ insert and extract)
- **Application 01:** Customer Service Desk simulation
- **Application 02:** OS Process Scheduling (Round-Robin CPU scheduler)

---

## 2. Directory Structure
```text
Lab05-Queues/
├── Program01-Static-Queue/
│   ├── static_queue.py
│   └── README.md
├── Program02-Dynamic-Queue/
│   ├── dynamic_queue.py
│   └── README.md
├── Program03-Circular-Queue/
│   ├── circular_queue.py
│   └── README.md
├── Program04-Deque/
│   ├── deque.py
│   └── README.md
├── Program05-Priority-Queue-Array/
│   ├── priority_queue_array.py
│   └── README.md
├── Program06-Priority-Queue-Heap/
│   ├── priority_queue_heap.py
│   └── README.md
├── Application-Customer-Service-Queue/
│   ├── customer_service_queue.py
│   └── README.md
├── Application-Process-Scheduling/
│   ├── process_scheduling.py
│   └── README.md
├── Application-Expression-Evaluator/
│   └── README.md
├── Application-Undo-Redo/
│   └── README.md
├── reflection.md
└── README.md
```

---

## 3. Execution Instructions
Run from repository root:
```bash
python Lab05-Queues/Program01-Static-Queue/static_queue.py
python Lab05-Queues/Program02-Dynamic-Queue/dynamic_queue.py
python Lab05-Queues/Program03-Circular-Queue/circular_queue.py
python Lab05-Queues/Program04-Deque/deque.py
python Lab05-Queues/Program05-Priority-Queue-Array/priority_queue_array.py
python Lab05-Queues/Program06-Priority-Queue-Heap/priority_queue_heap.py
python Lab05-Queues/Application-Customer-Service-Queue/customer_service_queue.py
python Lab05-Queues/Application-Process-Scheduling/process_scheduling.py
```

Run test suite:
```bash
python -m unittest tests/test_unit5.py
```
