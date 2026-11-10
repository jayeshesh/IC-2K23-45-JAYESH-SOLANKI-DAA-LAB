"""Singly Linked List Implementation.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 3: Linked Lists (CO1)
"""

from typing import Any, List, Optional


class Node:
    """Node in a singly linked list."""

    def __init__(self, data: Any, next_node: Optional["Node"] = None) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = next_node


class SinglyLinkedList:
    """Singly Linked List supporting insertion, deletion, reversal, and concatenation."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        """Check if the list contains zero elements."""
        return self.head is None

    def to_list(self) -> List[Any]:
        """Convert linked list elements to a standard Python list."""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

    def insert_at(self, position: int, data: Any) -> None:
        """Insert data at a 0-based position.
        
        Raises:
            IndexError: If position is negative or exceeds list size.
        """
        if position < 0 or position > self._size:
            raise IndexError(f"Index {position} out of bounds for size {self._size}")

        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.head
            for _ in range(position - 1):
                prev = prev.next  # type: ignore
            new_node.next = prev.next  # type: ignore
            prev.next = new_node  # type: ignore
        self._size += 1

    def append(self, data: Any) -> None:
        """Append data to the end of the list."""
        self.insert_at(self._size, data)

    def prepend(self, data: Any) -> None:
        """Prepend data to the start of the list."""
        self.insert_at(0, data)

    def delete_at(self, position: int) -> Any:
        """Delete and return data at a 0-based position.
        
        Raises:
            IndexError: If list is empty or position is out of bounds.
        """
        if position < 0 or position >= self._size:
            raise IndexError(f"Index {position} out of bounds for size {self._size}")

        if position == 0:
            deleted_data = self.head.data  # type: ignore
            self.head = self.head.next  # type: ignore
        else:
            prev = self.head
            for _ in range(position - 1):
                prev = prev.next  # type: ignore
            target = prev.next  # type: ignore
            deleted_data = target.data
            prev.next = target.next
        self._size -= 1
        return deleted_data

    def reverse(self) -> None:
        """Reverse the singly linked list in-place in O(n) time and O(1) space."""
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def concatenate(self, other: "SinglyLinkedList") -> "SinglyLinkedList":
        """Return a new SinglyLinkedList combining this list followed by other."""
        result = SinglyLinkedList()
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
    """Interactive demo of SinglyLinkedList operations."""
    sll = SinglyLinkedList()
    print("Initial SLL:", sll.to_list())
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print("After appending 10, 20, 30:", sll.to_list())
    sll.insert_at(1, 15)
    print("After inserting 15 at index 1:", sll.to_list())
    removed = sll.delete_at(2)
    print(f"After deleting at index 2 (removed {removed}):", sll.to_list())
    sll.reverse()
    print("After in-place reverse:", sll.to_list())

    other = SinglyLinkedList()
    other.append(99)
    other.append(100)
    concat = sll.concatenate(other)
    print("Concatenated with [99, 100]:", concat.to_list())


if __name__ == "__main__":
    demo()
