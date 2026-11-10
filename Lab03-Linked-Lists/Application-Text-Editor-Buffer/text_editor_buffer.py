"""Text Editor Buffer using Doubly Linked List.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 3: Linked Lists (CO1) Application
"""

from typing import List, Optional


class LineNode:
    """Node representing a single text line in the editor buffer."""

    def __init__(
        self,
        text: str,
        prev_line: Optional["LineNode"] = None,
        next_line: Optional["LineNode"] = None,
    ) -> None:
        self.text: str = text
        self.prev: Optional["LineNode"] = prev_line
        self.next: Optional["LineNode"] = next_line


class TextEditorBuffer:
    """Line-by-line text editor buffer implemented using a Doubly Linked List."""

    def __init__(self) -> None:
        self.head: Optional[LineNode] = None
        self.tail: Optional[LineNode] = None
        self.current_line: Optional[LineNode] = None
        self._line_count: int = 0

    def __len__(self) -> int:
        return self._line_count

    def insert_line(self, line_num: int, text: str) -> None:
        """Insert a line at 1-based line number."""
        if line_num < 1 or line_num > self._line_count + 1:
            raise IndexError(f"Line number {line_num} out of bounds (1..{self._line_count + 1})")

        new_node = LineNode(text)
        if self._line_count == 0:
            self.head = self.tail = self.current_line = new_node
        elif line_num == 1:
            new_node.next = self.head
            self.head.prev = new_node  # type: ignore
            self.head = new_node
        elif line_num == self._line_count + 1:
            new_node.prev = self.tail
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        else:
            curr = self.head
            for _ in range(line_num - 1):
                curr = curr.next  # type: ignore
            prev_node = curr.prev  # type: ignore
            new_node.prev = prev_node
            new_node.next = curr
            prev_node.next = new_node  # type: ignore
            curr.prev = new_node  # type: ignore
        self._line_count += 1

    def append_line(self, text: str) -> None:
        """Append line to the end of buffer."""
        self.insert_line(self._line_count + 1, text)

    def delete_line(self, line_num: int) -> str:
        """Delete line at 1-based line number."""
        if line_num < 1 or line_num > self._line_count:
            raise IndexError(f"Line number {line_num} out of bounds (1..{self._line_count})")

        if self._line_count == 1:
            text = self.head.text  # type: ignore
            self.head = self.tail = self.current_line = None
            self._line_count = 0
            return text

        if line_num == 1:
            text = self.head.text  # type: ignore
            self.head = self.head.next  # type: ignore
            self.head.prev = None  # type: ignore
        elif line_num == self._line_count:
            text = self.tail.text  # type: ignore
            self.tail = self.tail.prev  # type: ignore
            self.tail.next = None  # type: ignore
        else:
            curr = self.head
            for _ in range(line_num - 1):
                curr = curr.next  # type: ignore
            text = curr.text  # type: ignore
            curr.prev.next = curr.next  # type: ignore
            curr.next.prev = curr.prev  # type: ignore

        self._line_count -= 1
        return text

    def get_lines(self) -> List[str]:
        """Return all lines in buffer."""
        lines = []
        curr = self.head
        while curr:
            lines.append(curr.text)
            curr = curr.next
        return lines

    def display(self) -> str:
        """Format buffer with line numbers."""
        output = []
        curr = self.head
        idx = 1
        while curr:
            output.append(f"{idx:3d} | {curr.text}")
            curr = curr.next
            idx += 1
        return "\n".join(output) if output else "[Empty Buffer]"


def demo() -> None:
    """Demonstrate text editor buffer."""
    editor = TextEditorBuffer()
    editor.append_line("def greet(name):")
    editor.append_line("    print(f'Hello, {name}')")
    editor.append_line("greet('Jayesh')")
    print("Initial Buffer:")
    print(editor.display())

    print("\nInserting comment at line 1:")
    editor.insert_line(1, "# MCA AI/DAA Program")
    print(editor.display())

    print("\nDeleting line 3:")
    editor.delete_line(3)
    print(editor.display())


if __name__ == "__main__":
    demo()
