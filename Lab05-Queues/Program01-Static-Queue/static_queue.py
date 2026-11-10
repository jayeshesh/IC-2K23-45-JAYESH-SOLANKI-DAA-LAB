"""Static Queue (Fixed-capacity array based).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1)
"""

from typing import Any, List, Optional


class QueueOverflowError(Exception):
    pass


class QueueUnderflowError(Exception):
    pass


class StaticQueue:
    """Fixed-capacity linear queue with two pointers."""

    def __init__(self, capacity: int = 100) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity: int = capacity
        self._data: List[Optional[Any]] = [None] * capacity
        self._front: int = 0
        self._rear: int = -1
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self.capacity

    def enqueue(self, item: Any) -> None:
        if self.is_full():
            raise QueueOverflowError("Queue is full.")
        self._rear += 1
        self._data[self._rear] = item
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise QueueUnderflowError("Queue is empty.")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        self._size -= 1
        return val

    def peek(self) -> Any:
        if self.is_empty():
            raise QueueUnderflowError("Queue is empty.")
        return self._data[self._front]

    def to_list(self) -> List[Any]:
        return [self._data[i] for i in range(self._front, self._rear + 1) if self._data[i] is not None]


def demo() -> None:
    sq = StaticQueue(capacity=3)
    sq.enqueue(1)
    sq.enqueue(2)
    sq.enqueue(3)
    print("Static Queue:", sq.to_list())
    print("Dequeued:", sq.dequeue())
    print("Front:", sq.peek())


if __name__ == "__main__":
    demo()
