# Expression Evaluation (Postfix and Prefix)

**Language:** Python 3.10+  
**Run:** `python Lab04-Stacks/Program04-Expression-Evaluation/expression_evaluation.py`

## 1. Problem statement
Evaluate postfix and prefix mathematical expressions containing multi-digit numbers, arithmetic operators (`+`, `-`, `*`, `/`, `^`), and division-by-zero checks using an operand stack.

## 2. Approach
- **Postfix Evaluation:** Scan tokens left-to-right. Push operands onto the stack. When an operator is encountered, pop two operands, compute $a \text{ op } b$, and push the result.
- **Prefix Evaluation:** Scan tokens right-to-left. When an operator is encountered, pop the first two operands $a$ and $b$, compute $a \text{ op } b$, and push back.

## 3. Complexity analysis
| Metric | Postfix Evaluation | Prefix Evaluation |
|---|---:|---:|
| Time Complexity | O(n) | O(n) |
| Auxiliary Space | O(n) | O(n) |

## 4. Sample I/O
```text
Postfix Tokens: ['10', '2', '3', '+', '*', '5', '-']
Evaluated Postfix: 45.0
Prefix Tokens: ['-', '*', '10', '+', '2', '3', '5']
Evaluated Prefix: 45.0
```

## 5. Real-life application
Scientific calculators (e.g. Hewlett-Packard RPN calculators), Forth programming language interpreters, and PostScript printers.
