"""Unit tests for Unit 5: Queues.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Program01-Static-Queue"))
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Program02-Dynamic-Queue"))
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Program03-Circular-Queue"))
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Program04-Deque"))
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Program05-Priority-Queue-Array"))
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Program06-Priority-Queue-Heap"))
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Application-Customer-Service-Queue"))
sys.path.insert(0, str(REPO_ROOT / "Lab05-Queues" / "Application-Process-Scheduling"))

from static_queue import StaticQueue, QueueOverflowError, QueueUnderflowError
from dynamic_queue import DynamicQueue
from circular_queue import CircularQueue
from deque import Deque
from priority_queue_array import PriorityQueueArray
from priority_queue_heap import PriorityQueueHeap
from customer_service_queue import CustomerServiceQueue, Customer
from process_scheduling import Process, simulate_round_robin


class TestQueues(unittest.TestCase):
    def test_static_queue(self):
        sq = StaticQueue(capacity=2)
        sq.enqueue(1)
        sq.enqueue(2)
        self.assertTrue(sq.is_full())
        with self.assertRaises(QueueOverflowError):
            sq.enqueue(3)
        self.assertEqual(sq.dequeue(), 1)
        self.assertEqual(sq.peek(), 2)

    def test_dynamic_queue(self):
        dq = DynamicQueue()
        dq.enqueue("A")
        dq.enqueue("B")
        self.assertEqual(dq.dequeue(), "A")
        self.assertEqual(dq.peek(), "B")

    def test_circular_queue(self):
        cq = CircularQueue(capacity=2)
        cq.enqueue(10)
        cq.enqueue(20)
        self.assertEqual(cq.dequeue(), 10)
        cq.enqueue(30)
        self.assertEqual(cq.to_list(), [20, 30])

    def test_deque(self):
        d = Deque()
        d.append_rear(10)
        d.append_front(5)
        d.append_rear(20)
        self.assertEqual(d.to_list(), [5, 10, 20])
        self.assertEqual(d.pop_front(), 5)
        self.assertEqual(d.pop_rear(), 20)
        self.assertEqual(d.to_list(), [10])

    def test_priority_queues(self):
        pqa = PriorityQueueArray()
        pqh = PriorityQueueHeap()
        for p, v in [(3, "C"), (1, "A"), (2, "B")]:
            pqa.insert(p, v)
            pqh.insert(p, v)
        self.assertEqual(pqa.extract_min(), "A")
        self.assertEqual(pqh.extract_min(), "A")
        self.assertEqual(pqa.extract_min(), "B")
        self.assertEqual(pqh.extract_min(), "B")

    def test_simulations(self):
        csq = CustomerServiceQueue()
        csq.enqueue_customer(Customer(1, "Test", 4))
        self.assertEqual(csq.total_estimated_wait_time(), 4)

        procs = [Process("P1", 2), Process("P2", 1)]
        timeline = simulate_round_robin(procs, quantum=1)
        self.assertEqual(len(timeline), 3)


if __name__ == "__main__":
    unittest.main()
