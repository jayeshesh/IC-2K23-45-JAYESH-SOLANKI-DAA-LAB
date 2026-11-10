"""Doubly Linked List Implementation.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 3: Linked Lists (CO1)
"""

from typing import Any, List, Optional


class DoublyNode:
    """Node in a doubly linked list."""

    def __init__(
        self,
        data: Any,
        prev_node: Optional["DoublyNode"] = None,
        next_node: Optional["DoublyNode"] = None,
    ) -> None:
        self.data: Any = data
        self.prev: Optional["DoublyNode"] = prev_node
        self.next: Optional["DoublyNode"] = next_node


class DoublyLinkedList:
    """Doubly Linked List supporting bidirectional traversal, insert, delete, reverse, and concat."""

    def __init__(self) -> None:
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        """Check if list is empty."""
        return self.head is None

    def to_list(self) -> List[Any]:
        """Convert list forward to standard Python list."""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

    def to_reverse_list(self) -> List[Any]:
        """Convert list backward from tail to standard Python list."""
        elements = []
        curr = self.tail
        while curr:
            elements.append(curr.data)
            curr = curr.prev
        return elements

    def insert_at(self, position: int, data: Any) -> None:
        """Insert data at 0-based position."""
        if position < 0 or position > self._size:
            raise IndexError(f"Index {position} out of bounds for size {self._size}")

        new_node = DoublyNode(data)
        if self._size == 0:
            self.head = self.tail = new_node
        elif position == 0:
            new_node.next = self.head
            self.head.prev = new_node  # type: ignore
            self.head = new_node
        elif position == self._size:
            new_node.prev = self.tail
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        else:
            curr = self.head
            for _ in range(position):
                curr = curr.next  # type: ignore
            prev_node = curr.prev  # type: ignore
            new_node.prev = prev_node
            new_node.next = curr
            prev_node.next = new_node  # type: ignore
            curr.prev = new_node  # type: ignore
        self._size += 1

    def append(self, data: Any) -> None:
        """Append data to the end."""
        self.insert_at(self._size, data)

    def prepend(self, data: Any) -> None:
        """Prepend data to the beginning."""
        self.insert_at(0, data)

    def delete_at(self, position: int) -> Any:
        """Delete and return data at 0-based position."""
        if position < 0 or position >= self._size:
            raise IndexError(f"Index {position} out of bounds for size {self._size}")

        if self._size == 1:
            val = self.head.data  # type: ignore
            self.head = self.tail = None
            self._size = 0
            return val

        if position == 0:
            val = self.head.data  # type: ignore
            self.head = self.head.next  # type: ignore
            self.head.prev = None  # type: ignore
        elif position == self._size - 1:
            val = self.tail.data  # type: ignore
            self.tail = self.tail.prev  # type: ignore
            self.tail.next = None  # type: ignore
        else:
            curr = self.head
            for _ in range(position):
                curr = curr.next  # type: ignore
            val = curr.data  # type: ignore
            curr.prev.next = curr.next  # type: ignore
            curr.next.prev = curr.prev  # type: ignore

        self._size -= 1
        return val

    def reverse(self) -> None:
        """Reverse the doubly linked list in-place by swapping next and prev pointers."""
        curr = self.head
        self.head, self.tail = self.tail, self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev  # Move using original next pointer (now prev)

    def concatenate(self, other: "DoublyLinkedList") -> "DoublyLinkedList":
        """Return a new DoublyLinkedList containing this list followed by other."""
        result = DoublyLinkedList()
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        curr_other = other.head
        while curr_other:
            result.append(curr_other.data)
            curr_other = curr_other.next
        return result


def demo() -> None:
    """Demonstrate DoublyLinkedList functionality."""
    dll = DoublyLinkedList()
    dll.append("Alpha")
    dll.append("Beta")
    dll.append("Delta")
    dll.insert_at(2, "Gamma")
    print("Forward:", dll.to_list())
    print("Backward:", dll.to_reverse_list())
    removed = dll.delete_at(1)
    print(f"Removed at index 1 ({removed}):", dll.to_list())
    dll.reverse()
    print("After reverse:", dll.to_list())


if __name__ == "__main__":
    demo()
