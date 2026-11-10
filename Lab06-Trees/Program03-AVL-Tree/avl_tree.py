"""AVL Tree (Self-Balancing Binary Search Tree).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3)
"""

from typing import Any, List, Optional


class AVLNode:
    def __init__(self, key: Any) -> None:
        self.key: Any = key
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height: int = 1


class AVLTree:
    """Self-balancing BST with strict O(log n) height invariant via tree rotations."""

    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def balance_factor(self, node: Optional[AVLNode]) -> int:
        return self.height(node.left) - self.height(node.right) if node else 0

    def right_rotate(self, y: AVLNode) -> AVLNode:
        x = y.left
        assert x is not None
        t2 = x.right

        # Perform rotation
        x.right = y
        y.left = t2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x: AVLNode) -> AVLNode:
        y = x.right
        assert y is not None
        t2 = y.left

        # Perform rotation
        y.left = x
        x.right = t2

        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, key: Any) -> None:
        self.root = self._insert_node(self.root, key)

    def _insert_node(self, node: Optional[AVLNode], key: Any) -> AVLNode:
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert_node(node.left, key)
        elif key > node.key:
            node.right = self._insert_node(node.right, key)
        else:
            return node  # Duplicate keys not inserted

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        # 4 Rotation Cases:
        # Case 1: Left-Left (LL)
        if balance > 1 and key < node.left.key:  # type: ignore
            return self.right_rotate(node)

        # Case 2: Right-Right (RR)
        if balance < -1 and key > node.right.key:  # type: ignore
            return self.left_rotate(node)

        # Case 3: Left-Right (LR)
        if balance > 1 and key > node.left.key:  # type: ignore
            node.left = self.left_rotate(node.left)  # type: ignore
            return self.right_rotate(node)

        # Case 4: Right-Left (RL)
        if balance < -1 and key < node.right.key:  # type: ignore
            node.right = self.right_rotate(node.right)  # type: ignore
            return self.left_rotate(node)

        return node

    def inorder(self) -> List[Any]:
        res: List[Any] = []
        def _in(n: Optional[AVLNode]):
            if n:
                _in(n.left)
                res.append(n.key)
                _in(n.right)
        _in(self.root)
        return res


def demo() -> None:
    avl = AVLTree()
    # Insert sequentially increasing numbers (would skew a normal BST to O(n))
    for k in [10, 20, 30, 40, 50, 25]:
        avl.insert(k)
    print("AVL Inorder:", avl.inorder())
    print("AVL Root:", avl.root.key if avl.root else None)
    print("AVL Root Height:", avl.height(avl.root))


if __name__ == "__main__":
    demo()
