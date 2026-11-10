"""Threaded Binary Tree (Optional Advanced Topic).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3)
"""

from typing import Any, List, Optional


class ThreadedNode:
    def __init__(self, key: Any) -> None:
        self.key: Any = key
        self.left: Optional["ThreadedNode"] = None
        self.right: Optional["ThreadedNode"] = None
        self.is_threaded: bool = False  # True if right pointer is a thread to inorder successor


class ThreadedBinaryTree:
    """Single-threaded binary search tree allowing O(1) space inorder traversal without recursion or stack."""

    def __init__(self) -> None:
        self.root: Optional[ThreadedNode] = None

    def insert(self, key: Any) -> None:
        new_node = ThreadedNode(key)
        if not self.root:
            self.root = new_node
            return

        curr: Optional[ThreadedNode] = self.root
        parent: Optional[ThreadedNode] = None

        while curr:
            parent = curr
            if key < curr.key:
                if curr.left:
                    curr = curr.left
                else:
                    break
            else:
                if not curr.is_threaded and curr.right:
                    curr = curr.right
                else:
                    break

        if key < parent.key:  # type: ignore
            new_node.right = parent
            new_node.is_threaded = True
            parent.left = new_node  # type: ignore
        else:
            if parent.is_threaded:  # type: ignore
                new_node.right = parent.right  # type: ignore
                new_node.is_threaded = True
                parent.is_threaded = False  # type: ignore
            parent.right = new_node  # type: ignore

    def inorder(self) -> List[Any]:
        """Inorder traversal using threads: O(n) time and strict O(1) space."""
        res: List[Any] = []
        curr = self.root
        # Find leftmost node
        while curr and curr.left:
            curr = curr.left

        while curr:
            res.append(curr.key)
            if curr.is_threaded:
                curr = curr.right
            else:
                curr = curr.right
                while curr and curr.left:
                    curr = curr.left
        return res


def demo() -> None:
    tbt = ThreadedBinaryTree()
    for k in [20, 10, 30, 5, 15]:
        tbt.insert(k)
    print("Threaded BST Inorder (O(1) space):", tbt.inorder())


if __name__ == "__main__":
    demo()
