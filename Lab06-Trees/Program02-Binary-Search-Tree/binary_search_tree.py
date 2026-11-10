"""Binary Search Tree (BST) Implementation.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3)
"""

from typing import Any, List, Optional


class BSTNode:
    def __init__(self, key: Any, left: Optional["BSTNode"] = None, right: Optional["BSTNode"] = None) -> None:
        self.key: Any = key
        self.left: Optional["BSTNode"] = left
        self.right: Optional["BSTNode"] = right


class BinarySearchTree:
    """Binary Search Tree supporting insert, search, delete, min/max, and BST validation."""

    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None

    def insert(self, key: Any) -> None:
        self.root = self._insert_node(self.root, key)

    def _insert_node(self, node: Optional[BSTNode], key: Any) -> BSTNode:
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert_node(node.left, key)
        elif key > node.key:
            node.right = self._insert_node(node.right, key)
        return node

    def search(self, key: Any) -> bool:
        curr = self.root
        while curr:
            if key == curr.key:
                return True
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def find_min(self) -> Any:
        if not self.root:
            raise ValueError("BST is empty.")
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.key

    def find_max(self) -> Any:
        if not self.root:
            raise ValueError("BST is empty.")
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.key

    def delete(self, key: Any) -> None:
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node: Optional[BSTNode], key: Any) -> Optional[BSTNode]:
        if not node:
            return None
        if key < node.key:
            node.left = self._delete_node(node.left, key)
        elif key > node.key:
            node.right = self._delete_node(node.right, key)
        else:
            # Case 1 & 2: 0 or 1 child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Case 3: 2 children - find inorder successor (min in right subtree)
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete_node(node.right, succ.key)
        return node

    def inorder(self) -> List[Any]:
        res: List[Any] = []
        def _in(n: Optional[BSTNode]):
            if n:
                _in(n.left)
                res.append(n.key)
                _in(n.right)
        _in(self.root)
        return res

    def is_valid_bst(self) -> bool:
        """Validate if the tree strictly satisfies BST ordering property."""
        def _validate(node: Optional[BSTNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.key < high):
                return False
            return _validate(node.left, low, node.key) and _validate(node.right, node.key, high)
        return _validate(self.root, float("-inf"), float("inf"))


def demo() -> None:
    bst = BinarySearchTree()
    for k in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(k)
    print("Inorder (Sorted):", bst.inorder())
    print("Search 40:", bst.search(40))
    print("Search 99:", bst.search(99))
    print("Min:", bst.find_min(), "| Max:", bst.find_max())
    print("Is Valid BST?", bst.is_valid_bst())
    bst.delete(30)
    print("After deleting 30:", bst.inorder())


if __name__ == "__main__":
    demo()
