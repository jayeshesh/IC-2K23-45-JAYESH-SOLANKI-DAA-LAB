"""Postfix and Prefix Expression Evaluation.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 4: Stacks (CO1)
"""

from typing import List


def evaluate_postfix(tokens: List[str]) -> float:
    """Evaluate a postfix expression (tokens can be multi-digit numbers or operators)."""
    stack: List[float] = []

    for token in tokens:
        if token in {"+", "-", "*", "/", "^"}:
            if len(stack) < 2:
                raise ValueError("Malformed postfix expression.")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero in expression.")
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)
        else:
            stack.append(float(token))

    if len(stack) != 1:
        raise ValueError("Malformed postfix expression.")
    return stack.pop()


def evaluate_prefix(tokens: List[str]) -> float:
    """Evaluate a prefix expression scanning from right to left."""
    stack: List[float] = []

    for token in reversed(tokens):
        if token in {"+", "-", "*", "/", "^"}:
            if len(stack) < 2:
                raise ValueError("Malformed prefix expression.")
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero in expression.")
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)
        else:
            stack.append(float(token))

    if len(stack) != 1:
        raise ValueError("Malformed prefix expression.")
    return stack.pop()


def demo() -> None:
    postfix_tokens = ["10", "2", "3", "+", "*", "5", "-"]  # 10 * (2 + 3) - 5 = 45
    print("Postfix Tokens:", postfix_tokens)
    print("Evaluated Postfix:", evaluate_postfix(postfix_tokens))

    prefix_tokens = ["-", "*", "10", "+", "2", "3", "5"]
    print("Prefix Tokens:", prefix_tokens)
    print("Evaluated Prefix:", evaluate_prefix(prefix_tokens))


if __name__ == "__main__":
    demo()
