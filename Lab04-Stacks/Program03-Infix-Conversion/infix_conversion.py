"""Infix to Postfix and Prefix Conversion.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 4: Stacks (CO1)
"""

from typing import List


PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
RIGHT_ASSOCIATIVE = {"^"}


def infix_to_postfix(expression: str) -> str:
    """Convert an infix algebraic expression to postfix (Reverse Polish Notation)."""
    output: List[str] = []
    stack: List[str] = []

    tokens = expression.replace(" ", "")
    for char in tokens:
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
        elif char in PRECEDENCE:
            while (
                stack
                and stack[-1] in PRECEDENCE
                and (
                    PRECEDENCE[stack[-1]] > PRECEDENCE[char]
                    or (
                        PRECEDENCE[stack[-1]] == PRECEDENCE[char]
                        and char not in RIGHT_ASSOCIATIVE
                    )
                )
            ):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return "".join(output)


def infix_to_prefix(expression: str) -> str:
    """Convert infix to prefix by reversing, transforming parentheses, and converting to postfix."""
    # 1. Reverse tokens and invert parentheses
    tokens = list(expression.replace(" ", "")[::-1])
    for i, ch in enumerate(tokens):
        if ch == "(":
            tokens[i] = ")"
        elif ch == ")":
            tokens[i] = "("

    # 2. Convert to postfix with adapted right/left associativity
    output: List[str] = []
    stack: List[str] = []

    for char in tokens:
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
        elif char in PRECEDENCE:
            while (
                stack
                and stack[-1] in PRECEDENCE
                and (
                    PRECEDENCE[stack[-1]] > PRECEDENCE[char]
                    or (
                        PRECEDENCE[stack[-1]] == PRECEDENCE[char]
                        and char in RIGHT_ASSOCIATIVE
                    )
                )
            ):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    # 3. Reverse output to get prefix
    return "".join(output[::-1])


def demo() -> None:
    expr = "A+B*(C^D-E)^(F+G*H)-I"
    print(f"Infix:   {expr}")
    print(f"Postfix: {infix_to_postfix(expr)}")
    print(f"Prefix:  {infix_to_prefix(expr)}")


if __name__ == "__main__":
    demo()
