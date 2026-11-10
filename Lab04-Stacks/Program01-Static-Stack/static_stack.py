"""Static (Array-based / Fixed Capacity) Stack.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 4: Stacks (CO1)
"""

from typing import Any, List, Optional


class StackOverflowError(Exception):
    """Raised when pushing to a full static stack."""
    pass


class StackUnderflowError(Exception):
    """Raised when popping/peeking an empty stack."""
    pass


class StaticStack:
    """Fixed-capacity stack backed by pre-allocated array."""

    def __init__(self, capacity: int = 100) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity: int = capacity
        self._data: List[Optional[Any]] = [None] * capacity
        self._top: int = -1

    def __len__(self) -> int:
        return self._top + 1

    def is_empty(self) -> bool:
        return self._top == -1

    def is_full(self) -> bool:
        return self._top == self.capacity - 1

    def push(self, item: Any) -> None:
        if self.is_full():
            raise StackOverflowError("Cannot push: stack is full.")
        self._top += 1
        self._data[self._top] = item

    def pop(self) -> Any:
        if self.is_empty():
            raise StackUnderflowError("Cannot pop: stack is empty.")
        val = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return val

    def peek(self) -> Any:
        if self.is_empty():
            raise StackUnderflowError("Cannot peek: stack is empty.")
        return self._data[self._top]

    def to_list(self) -> List[Any]:
        return [self._data[i] for i in range(self._top + 1)]


def demo() -> None:
    stack = StaticStack(capacity=3)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack elements:", stack.to_list())
    print("Top element:", stack.peek())
    print("Popped:", stack.pop())
    print("After pop:", stack.to_list())


if __name__ == "__main__":
    demo()
