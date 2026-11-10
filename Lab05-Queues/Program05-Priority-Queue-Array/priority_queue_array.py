"""Priority Queue (Unordered Array Based).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1)
"""

from typing import Any, List, Tuple


class PriorityQueueEmptyError(Exception):
    pass


class PriorityQueueArray:
    """Priority Queue backed by an array: O(1) insert, O(n) extract-min."""

    def __init__(self) -> None:
        self._items: List[Tuple[float, Any]] = []  # (priority, value)

    def __len__(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def insert(self, priority: float, value: Any) -> None:
        """Insert element with priority in O(1)."""
        self._items.append((priority, value))

    def extract_min(self) -> Any:
        """Find and remove element with lowest priority value in O(n)."""
        if self.is_empty():
            raise PriorityQueueEmptyError("Priority queue is empty.")
        min_idx = 0
        for i in range(1, len(self._items)):
            if self._items[i][0] < self._items[min_idx][0]:
                min_idx = i
        val = self._items.pop(min_idx)[1]
        return val

    def peek_min(self) -> Any:
        """Peek element with lowest priority value in O(n)."""
        if self.is_empty():
            raise PriorityQueueEmptyError("Priority queue is empty.")
        min_idx = 0
        for i in range(1, len(self._items)):
            if self._items[i][0] < self._items[min_idx][0]:
                min_idx = i
        return self._items[min_idx][1]


def demo() -> None:
    pq = PriorityQueueArray()
    pq.insert(3, "Low Priority Task")
    pq.insert(1, "Emergency Task")
    pq.insert(2, "Medium Task")
    print("Peek min:", pq.peek_min())
    print("Extract min:", pq.extract_min())
    print("Extract next min:", pq.extract_min())


if __name__ == "__main__":
    demo()
