"""Circular Linked List Implementation.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 3: Linked Lists (CO1)
"""

from typing import Any, List, Optional


class CircularNode:
    """Node in a circular linked list."""

    def __init__(self, data: Any, next_node: Optional["CircularNode"] = None) -> None:
        self.data: Any = data
        self.next: Optional["CircularNode"] = next_node


class CircularLinkedList:
    """Circular Linked List where the last node points back to the head."""

    def __init__(self) -> None:
        self.head: Optional[CircularNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        """Check if list is empty."""
        return self.head is None

    def to_list(self) -> List[Any]:
        """Convert one full cycle of the circular list to a Python list."""
        if not self.head:
            return []
        elements = []
        curr = self.head
        while True:
            elements.append(curr.data)
            curr = curr.next  # type: ignore
            if curr == self.head:
                break
        return elements

    def insert_at(self, position: int, data: Any) -> None:
        """Insert at 0-based position within circular list."""
        if position < 0 or position > self._size:
            raise IndexError(f"Index {position} out of bounds for size {self._size}")

        new_node = CircularNode(data)
        if self._size == 0:
            new_node.next = new_node
            self.head = new_node
        elif position == 0:
            # Find the last node to update its pointer to new_node
            tail = self.head
            while tail.next != self.head:  # type: ignore
                tail = tail.next  # type: ignore
            new_node.next = self.head
            tail.next = new_node  # type: ignore
            self.head = new_node
        else:
            prev = self.head
            for _ in range(position - 1):
                prev = prev.next  # type: ignore
            new_node.next = prev.next  # type: ignore
            prev.next = new_node  # type: ignore
        self._size += 1

    def append(self, data: Any) -> None:
        """Append data to the end of circular list."""
        self.insert_at(self._size, data)

    def prepend(self, data: Any) -> None:
        """Prepend data as the new head."""
        self.insert_at(0, data)

    def delete_at(self, position: int) -> Any:
        """Delete node at 0-based position."""
        if position < 0 or position >= self._size:
            raise IndexError(f"Index {position} out of bounds for size {self._size}")

        if self._size == 1:
            val = self.head.data  # type: ignore
            self.head = None
            self._size = 0
            return val

        if position == 0:
            tail = self.head
            while tail.next != self.head:  # type: ignore
                tail = tail.next  # type: ignore
            val = self.head.data  # type: ignore
            self.head = self.head.next  # type: ignore
            tail.next = self.head  # type: ignore
        else:
            prev = self.head
            for _ in range(position - 1):
                prev = prev.next  # type: ignore
            target = prev.next  # type: ignore
            val = target.data
            prev.next = target.next
        self._size -= 1
        return val

    def reverse(self) -> None:
        """Reverse circular linked list in-place."""
        if self._size <= 1:
            return
        prev = None
        curr = self.head
        tail = self.head
        while True:
            next_node = curr.next  # type: ignore
            curr.next = prev  # type: ignore
            prev = curr
            curr = next_node
            if curr == self.head:
                break
        tail.next = prev  # Old head (now tail) points to new head
        self.head = prev

    def concatenate(self, other: "CircularLinkedList") -> "CircularLinkedList":
        """Concatenate another circular linked list and return a new one."""
        result = CircularLinkedList()
        for item in self.to_list():
            result.append(item)
        for item in other.to_list():
            result.append(item)
        return result


def demo() -> None:
    """Demonstrate CircularLinkedList operations."""
    cll = CircularLinkedList()
    cll.append(100)
    cll.append(200)
    cll.append(300)
    cll.prepend(50)
    print("Initial CLL:", cll.to_list())
    removed = cll.delete_at(2)
    print(f"Removed at index 2 ({removed}):", cll.to_list())
    cll.reverse()
    print("After reverse:", cll.to_list())


if __name__ == "__main__":
    demo()
