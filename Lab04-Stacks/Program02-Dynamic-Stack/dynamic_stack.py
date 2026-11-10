"""Dynamic (Linked-List Based) Stack.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 4: Stacks (CO1)
"""

from typing import Any, List, Optional


class StackUnderflowError(Exception):
    """Raised when popping/peeking an empty stack."""
    pass


class StackNode:
    def __init__(self, data: Any, next_node: Optional["StackNode"] = None) -> None:
        self.data: Any = data
        self.next: Optional["StackNode"] = next_node


class DynamicStack:
    """Dynamic unbounded stack backed by a singly linked list."""

    def __init__(self) -> None:
        self.top_node: Optional[StackNode] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.top_node is None

    def push(self, item: Any) -> None:
        new_node = StackNode(item, next_node=self.top_node)
        self.top_node = new_node
        self._size += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise StackUnderflowError("Cannot pop: stack is empty.")
        val = self.top_node.data  # type: ignore
        self.top_node = self.top_node.next  # type: ignore
        self._size -= 1
        return val

    def peek(self) -> Any:
        if self.is_empty():
            raise StackUnderflowError("Cannot peek: stack is empty.")
        return self.top_node.data  # type: ignore

    def to_list(self) -> List[Any]:
        elements = []
        curr = self.top_node
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements[::-1]  # Bottom to top


def demo() -> None:
    ds = DynamicStack()
    ds.push("A")
    ds.push("B")
    ds.push("C")
    print("Stack bottom to top:", ds.to_list())
    print("Peek top:", ds.peek())
    print("Popped:", ds.pop())
    print("After pop:", ds.to_list())


if __name__ == "__main__":
    demo()
