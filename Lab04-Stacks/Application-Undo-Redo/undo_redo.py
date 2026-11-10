"""Undo/Redo Feature for Text/Drawing Application using Command Pattern and Stacks.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 4: Stacks (CO1) Application
"""

from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    """Abstract base class for reversible user commands."""

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class TextDocument:
    """Document state receiver."""

    def __init__(self) -> None:
        self.text: str = ""

    def append(self, content: str) -> None:
        self.text += content

    def delete_suffix(self, length: int) -> str:
        removed = self.text[-length:]
        self.text = self.text[:-length]
        return removed


class InsertTextCommand(Command):
    """Command to insert text."""

    def __init__(self, doc: TextDocument, text_to_insert: str) -> None:
        self.doc: TextDocument = doc
        self.text_to_insert: str = text_to_insert

    def execute(self) -> None:
        self.doc.append(self.text_to_insert)

    def undo(self) -> None:
        self.doc.delete_suffix(len(self.text_to_insert))


class UndoRedoManager:
    """Manages undo and redo stacks implementing the Command Pattern."""

    def __init__(self) -> None:
        self.undo_stack: List[Command] = []
        self.redo_stack: List[Command] = []

    def execute_command(self, cmd: Command) -> None:
        cmd.execute()
        self.undo_stack.append(cmd)
        self.redo_stack.clear()  # Clear redo history on new action

    def undo(self) -> bool:
        if not self.undo_stack:
            return False
        cmd = self.undo_stack.pop()
        cmd.undo()
        self.redo_stack.append(cmd)
        return True

    def redo(self) -> bool:
        if not self.redo_stack:
            return False
        cmd = self.redo_stack.pop()
        cmd.execute()
        self.undo_stack.append(cmd)
        return True


def demo() -> None:
    doc = TextDocument()
    mgr = UndoRedoManager()

    print("Initial document:", repr(doc.text))
    mgr.execute_command(InsertTextCommand(doc, "Hello "))
    mgr.execute_command(InsertTextCommand(doc, "World!"))
    print("After two inserts:", repr(doc.text))

    mgr.undo()
    print("After 1st undo:", repr(doc.text))

    mgr.redo()
    print("After redo:", repr(doc.text))

    mgr.undo()
    mgr.undo()
    print("After 2 undos:", repr(doc.text))


if __name__ == "__main__":
    demo()
