# Lab 04 – Stacks

**Course:** IC-307D | Data Structures and Algorithms Lab  
**Unit:** Unit 4: Stacks (CO1)  
**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Language:** Python 3.10+

---

## 1. Unit Overview
Unit 4 implements LIFO abstract data types and fundamental stack parsing and execution engines:
- **Program 01:** Static Stack (fixed array capacity, overflow/underflow handling)
- **Program 02:** Dynamic Stack (unbounded linked list implementation)
- **Program 03:** Infix to Postfix/Prefix (Shunting-Yard conversion algorithm)
- **Program 04:** Postfix and Prefix Evaluation (multi-digit evaluation engine)
- **Application 01:** Full Expression Evaluator (operator precedence, associativity, parentheses)
- **Application 02:** Undo/Redo Engine (GoF Command Pattern with dual history stacks)

---

## 2. Directory Structure
```text
Lab04-Stacks/
├── Program01-Static-Stack/
│   ├── static_stack.py
│   └── README.md
├── Program02-Dynamic-Stack/
│   ├── dynamic_stack.py
│   └── README.md
├── Program03-Infix-Conversion/
│   ├── infix_conversion.py
│   └── README.md
├── Program04-Expression-Evaluation/
│   ├── expression_evaluation.py
│   └── README.md
├── Application-Expression-Evaluator/
│   ├── expression_evaluator.py
│   └── README.md
├── Application-Undo-Redo/
│   ├── undo_redo.py
│   └── README.md
├── reflection.md
└── README.md
```

---

## 3. Execution Instructions
Run from repository root:
```bash
python Lab04-Stacks/Program01-Static-Stack/static_stack.py
python Lab04-Stacks/Program02-Dynamic-Stack/dynamic_stack.py
python Lab04-Stacks/Program03-Infix-Conversion/infix_conversion.py
python Lab04-Stacks/Program04-Expression-Evaluation/expression_evaluation.py
python Lab04-Stacks/Application-Expression-Evaluator/expression_evaluator.py
python Lab04-Stacks/Application-Undo-Redo/undo_redo.py
```

Run test suite:
```bash
python -m unittest tests/test_unit4.py
```
