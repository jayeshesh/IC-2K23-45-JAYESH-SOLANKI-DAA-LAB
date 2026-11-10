"""Binary Tree Traversals (Recursive and Iterative).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3)
"""

from typing import Any, List, Optional


class TreeNode:
    def __init__(
        self,
        val: Any,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val: Any = val
        self.left: Optional["TreeNode"] = left
        self.right: Optional["TreeNode"] = right


def inorder_recursive(root: Optional[TreeNode]) -> List[Any]:
    res: List[Any] = []
    if root:
        res.extend(inorder_recursive(root.left))
        res.append(root.val)
        res.extend(inorder_recursive(root.right))
    return res


def inorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    res: List[Any] = []
    stack: List[TreeNode] = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def preorder_recursive(root: Optional[TreeNode]) -> List[Any]:
    res: List[Any] = []
    if root:
        res.append(root.val)
        res.extend(preorder_recursive(root.left))
        res.extend(preorder_recursive(root.right))
    return res


def preorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    res: List[Any] = []
    stack: List[TreeNode] = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def postorder_recursive(root: Optional[TreeNode]) -> List[Any]:
    res: List[Any] = []
    if root:
        res.extend(postorder_recursive(root.left))
        res.extend(postorder_recursive(root.right))
        res.append(root.val)
    return res


def postorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    res: List[Any] = []
    stack1: List[TreeNode] = [root]
    stack2: List[TreeNode] = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        res.append(stack2.pop().val)
    return res


def demo() -> None:
    # Build tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Inorder (Rec):", inorder_recursive(root))
    print("Inorder (Iter):", inorder_iterative(root))
    print("Preorder (Rec):", preorder_recursive(root))
    print("Preorder (Iter):", preorder_iterative(root))
    print("Postorder (Rec):", postorder_recursive(root))
    print("Postorder (Iter):", postorder_iterative(root))


if __name__ == "__main__":
    demo()
