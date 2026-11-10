"""Priority Queue (Binary Min-Heap Based).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1)
"""

from typing import Any, List, Tuple


class PriorityQueueEmptyError(Exception):
    pass


class PriorityQueueHeap:
    """Priority Queue backed by a binary min-heap: O(log n) insert and extract-min."""

    def __init__(self) -> None:
        self._heap: List[Tuple[float, Any]] = []

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def insert(self, priority: float, value: Any) -> None:
        """Insert element and bubble up in O(log n)."""
        self._heap.append((priority, value))
        self._sift_up(len(self._heap) - 1)

    def extract_min(self) -> Any:
        """Extract root element and bubble down in O(log n)."""
        if self.is_empty():
            raise PriorityQueueEmptyError("Priority queue is empty.")
        if len(self._heap) == 1:
            return self._heap.pop()[1]

        min_val = self._heap[0][1]
        self._heap[0] = self._heap.pop()
        self._sift_down(0)
        return min_val

    def peek_min(self) -> Any:
        """Peek minimum priority element in O(1)."""
        if self.is_empty():
            raise PriorityQueueEmptyError("Priority queue is empty.")
        return self._heap[0][1]

    def _sift_up(self, idx: int) -> None:
        parent = (idx - 1) // 2
        while idx > 0 and self._heap[idx][0] < self._heap[parent][0]:
            self._heap[idx], self._heap[parent] = self._heap[parent], self._heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx: int) -> None:
        n = len(self._heap)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self._heap[left][0] < self._heap[smallest][0]:
                smallest = left
            if right < n and self._heap[right][0] < self._heap[smallest][0]:
                smallest = right
            if smallest != idx:
                self._heap[idx], self._heap[smallest] = self._heap[smallest], self._heap[idx]
                idx = smallest
            else:
                break


def demo() -> None:
    pq = PriorityQueueHeap()
    pq.insert(5, "Routine Task")
    pq.insert(1, "Critical Alarm")
    pq.insert(3, "Important Notice")
    print("Peek min:", pq.peek_min())
    print("Extract min:", pq.extract_min())
    print("Extract next:", pq.extract_min())


if __name__ == "__main__":
    demo()
