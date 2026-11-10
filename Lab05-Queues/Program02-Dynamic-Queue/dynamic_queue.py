"""Dynamic (Linked-List Based) Queue.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1)
"""

from typing import Any, List, Optional


class QueueUnderflowError(Exception):
    pass


class QueueNode:
    def __init__(self, data: Any, next_node: Optional["QueueNode"] = None) -> None:
        self.data: Any = data
        self.next: Optional["QueueNode"] = next_node


class DynamicQueue:
    """Unbounded dynamic queue backed by singly linked nodes with head and tail pointers."""

    def __init__(self) -> None:
        self.front_node: Optional[QueueNode] = None
        self.rear_node: Optional[QueueNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.front_node is None

    def enqueue(self, item: Any) -> None:
        new_node = QueueNode(item)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node  # type: ignore
            self.rear_node = new_node
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise QueueUnderflowError("Queue is empty.")
        val = self.front_node.data  # type: ignore
        self.front_node = self.front_node.next  # type: ignore
        if self.front_node is None:
            self.rear_node = None
        self._size -= 1
        return val

    def peek(self) -> Any:
        if self.is_empty():
            raise QueueUnderflowError("Queue is empty.")
        return self.front_node.data  # type: ignore

    def to_list(self) -> List[Any]:
        items = []
        curr = self.front_node
        while curr:
            items.append(curr.data)
            curr = curr.next
        return items


def demo() -> None:
    dq = DynamicQueue()
    dq.enqueue("Task1")
    dq.enqueue("Task2")
    dq.enqueue("Task3")
    print("Queue:", dq.to_list())
    print("Dequeued:", dq.dequeue())
    print("Peek:", dq.peek())


if __name__ == "__main__":
    demo()
