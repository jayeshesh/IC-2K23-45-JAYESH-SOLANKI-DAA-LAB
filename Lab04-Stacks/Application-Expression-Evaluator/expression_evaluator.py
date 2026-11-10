"""Full Expression Evaluator with Operator Precedence and Parentheses.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 4: Stacks (CO1) Application
"""

import re
from typing import List


PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
RIGHT_ASSOCIATIVE = {"^"}


def tokenize(expression: str) -> List[str]:
    """Tokenize mathematical expression supporting multi-digit numbers, floats, and operators."""
    token_pattern = r"\d+(?:\.\d+)?|[+\-*/^()]"
    tokens = re.findall(token_pattern, expression)
    return tokens


def evaluate_infix(expression: str) -> float:
    """Evaluate raw infix expression handling parentheses, precedence, and associativity in O(n)."""
    tokens = tokenize(expression)
    values: List[float] = []
    operators: List[str] = []

    def apply_op() -> None:
        if not operators or len(values) < 2:
            raise ValueError("Malformed expression.")
        op = operators.pop()
        b = values.pop()
        a = values.pop()
        if op == "+":
            values.append(a + b)
        elif op == "-":
            values.append(a - b)
        elif op == "*":
            values.append(a * b)
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero in expression.")
            values.append(a / b)
        elif op == "^":
            values.append(a ** b)

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.replace(".", "", 1).isdigit():
            values.append(float(token))
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                apply_op()
            if not operators or operators[-1] != "(":
                raise ValueError("Mismatched parentheses.")
            operators.pop()  # pop '('
        elif token in PRECEDENCE:
            while (
                operators
                and operators[-1] in PRECEDENCE
                and (
                    PRECEDENCE[operators[-1]] > PRECEDENCE[token]
                    or (
                        PRECEDENCE[operators[-1]] == PRECEDENCE[token]
                        and token not in RIGHT_ASSOCIATIVE
                    )
                )
            ):
                apply_op()
            operators.append(token)
        i += 1

    while operators:
        if operators[-1] == "(":
            raise ValueError("Mismatched parentheses.")
        apply_op()

    if len(values) != 1:
        raise ValueError("Malformed expression.")
    return values[0]


def demo() -> None:
    expressions = [
        "3 + 5 * (2 - 8)",
        "2 ^ 3 ^ 2",  # 2^(3^2) = 2^9 = 512
        "((10 + 20) * 3) / (2 + 4)",
    ]
    for expr in expressions:
        print(f"{expr} = {evaluate_infix(expr)}")


if __name__ == "__main__":
    demo()
