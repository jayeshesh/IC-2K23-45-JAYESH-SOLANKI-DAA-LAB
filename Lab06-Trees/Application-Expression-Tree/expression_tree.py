"""Expression Tree (Build from Postfix and Evaluate).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 6: Trees (CO3) Application
"""

from typing import List, Optional


class ExprTreeNode:
    def __init__(
        self,
        val: str,
        left: Optional["ExprTreeNode"] = None,
        right: Optional["ExprTreeNode"] = None,
    ) -> None:
        self.val: str = val
        self.left: Optional["ExprTreeNode"] = left
        self.right: Optional["ExprTreeNode"] = right


def build_expression_tree(postfix_tokens: List[str]) -> ExprTreeNode:
    """Build an expression tree from postfix tokens using a stack."""
    stack: List[ExprTreeNode] = []
    for token in postfix_tokens:
        if token in {"+", "-", "*", "/", "^"}:
            if len(stack) < 2:
                raise ValueError("Invalid postfix token list.")
            right = stack.pop()
            left = stack.pop()
            node = ExprTreeNode(token, left=left, right=right)
            stack.append(node)
        else:
            stack.append(ExprTreeNode(token))
    if len(stack) != 1:
        raise ValueError("Invalid postfix token list.")
    return stack.pop()


def evaluate_expression_tree(root: Optional[ExprTreeNode]) -> float:
    """Recursively evaluate an expression tree."""
    if not root:
        return 0.0
    if not root.left and not root.right:
        return float(root.val)

    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)

    if root.val == "+":
        return left_val + right_val
    elif root.val == "-":
        return left_val - right_val
    elif root.val == "*":
        return left_val * right_val
    elif root.val == "/":
        if right_val == 0:
            raise ZeroDivisionError("Division by zero in expression tree.")
        return left_val / right_val
    elif root.val == "^":
        return left_val ** right_val
    raise ValueError(f"Unknown operator {root.val}")


def inorder_expr(root: Optional[ExprTreeNode]) -> str:
    """Generate infix string with parentheses from expression tree."""
    if not root:
        return ""
    if not root.left and not root.right:
        return root.val
    return f"({inorder_expr(root.left)} {root.val} {inorder_expr(root.right)})"


def demo() -> None:
    # 5 3 + 2 * => ( (5 + 3) * 2 ) = 16
    tokens = ["5", "3", "+", "2", "*"]
    tree = build_expression_tree(tokens)
    print("Inorder Infix from Tree:", inorder_expr(tree))
    print("Evaluated Value:", evaluate_expression_tree(tree))


if __name__ == "__main__":
    demo()
