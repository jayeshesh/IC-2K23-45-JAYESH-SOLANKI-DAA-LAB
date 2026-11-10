# Infix Expression Evaluator with Operator Precedence and Parentheses

**Language:** Python 3.10+  
**Run:** `python Lab04-Stacks/Application-Expression-Evaluator/expression_evaluator.py`

## 1. Problem statement
Build a complete arithmetic expression evaluator supporting multi-digit numbers, floating point operands, standard operators (`+`, `-`, `*`, `/`, `^`), arbitrary nested parentheses, and operator precedence and right-associativity.

## 2. Approach
Two stacks (`values` and `operators`) evaluate the expression in a single pass. When closing parenthesis `)` or lower-precedence operator is encountered, pending sub-expressions are popped and evaluated immediately.

## 3. Complexity analysis
| Metric | Value |
|---|---:|
| Time Complexity | O(n) |
| Auxiliary Space | O(n) |

## 4. Sample I/O
```text
3 + 5 * (2 - 8) = -27.0
2 ^ 3 ^ 2 = 512.0
((10 + 20) * 3) / (2 + 4) = 15.0
```

## 5. Real-life application
Spreadsheet formula calculation engines (e.g. Microsoft Excel, Google Sheets) and programming language expression parsers.
