"""Circular Queue (Ring Buffer Implementation).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1)
"""

from typing import Any, List, Optional


class QueueOverflowError(Exception):
    pass


class QueueUnderflowError(Exception):
    pass


class CircularQueue:
    """Fixed-capacity circular queue (ring buffer) reusing empty slots modulo capacity."""

    def __init__(self, capacity: int = 100) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity: int = capacity
        self._data: List[Optional[Any]] = [None] * capacity
        self._front: int = 0
        self._rear: int = 0
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self.capacity

    def enqueue(self, item: Any) -> None:
        if self.is_full():
            raise QueueOverflowError("Circular queue is full.")
        self._data[self._rear] = item
        self._rear = (self._rear + 1) % self.capacity
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise QueueUnderflowError("Circular queue is empty.")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1
        return val

    def peek(self) -> Any:
        if self.is_empty():
            raise QueueUnderflowError("Circular queue is empty.")
        return self._data[self._front]

    def to_list(self) -> List[Any]:
        items = []
        for i in range(self._size):
            idx = (self._front + i) % self.capacity
            items.append(self._data[idx])
        return items


def demo() -> None:
    cq = CircularQueue(capacity=3)
    cq.enqueue("A")
    cq.enqueue("B")
    cq.enqueue("C")
    print("Initial CQ:", cq.to_list())
    print("Dequeued:", cq.dequeue())
    cq.enqueue("D")  # Reuses slot 0 modulo capacity
    print("After wrapping enqueue D:", cq.to_list())


if __name__ == "__main__":
    demo()
