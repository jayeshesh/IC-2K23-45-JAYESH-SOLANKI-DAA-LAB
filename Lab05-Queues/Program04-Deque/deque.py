"""Double-Ended Queue (Deque).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1)
"""

from typing import Any, List, Optional


class DequeEmptyError(Exception):
    pass


class DequeNode:
    def __init__(
        self,
        data: Any,
        prev_node: Optional["DequeNode"] = None,
        next_node: Optional["DequeNode"] = None,
    ) -> None:
        self.data: Any = data
        self.prev: Optional["DequeNode"] = prev_node
        self.next: Optional["DequeNode"] = next_node


class Deque:
    """Double-Ended Queue supporting O(1) insertions and deletions at both extremities."""

    def __init__(self) -> None:
        self.head: Optional[DequeNode] = None
        self.tail: Optional[DequeNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def append_front(self, item: Any) -> None:
        new_node = DequeNode(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node  # type: ignore
            self.head = new_node
        self._size += 1

    def append_rear(self, item: Any) -> None:
        new_node = DequeNode(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        self._size += 1

    def pop_front(self) -> Any:
        if self.is_empty():
            raise DequeEmptyError("Deque is empty.")
        val = self.head.data  # type: ignore
        self.head = self.head.next  # type: ignore
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._size -= 1
        return val

    def pop_rear(self) -> Any:
        if self.is_empty():
            raise DequeEmptyError("Deque is empty.")
        val = self.tail.data  # type: ignore
        self.tail = self.tail.prev  # type: ignore
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self._size -= 1
        return val

    def peek_front(self) -> Any:
        if self.is_empty():
            raise DequeEmptyError("Deque is empty.")
        return self.head.data  # type: ignore

    def peek_rear(self) -> Any:
        if self.is_empty():
            raise DequeEmptyError("Deque is empty.")
        return self.tail.data  # type: ignore

    def to_list(self) -> List[Any]:
        items = []
        curr = self.head
        while curr:
            items.append(curr.data)
            curr = curr.next
        return items


def demo() -> None:
    dq = Deque()
    dq.append_rear(10)
    dq.append_rear(20)
    dq.append_front(5)
    print("Deque elements:", dq.to_list())
    print("Pop front:", dq.pop_front())
    print("Pop rear:", dq.pop_rear())
    print("Remaining:", dq.to_list())


if __name__ == "__main__":
    demo()
