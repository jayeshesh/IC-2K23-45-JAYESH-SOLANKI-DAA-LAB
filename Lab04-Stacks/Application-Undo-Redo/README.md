# Undo/Redo Feature using Command Pattern and Stacks

**Language:** Python 3.10+  
**Run:** `python Lab04-Stacks/Application-Undo-Redo/undo_redo.py`

## 1. Problem statement
Implement a robust undo/redo system for document editing or graphics applications using the Gang of Four (GoF) Command Design Pattern and dual stack architectures (`undo_stack` and `redo_stack`).

## 2. Approach
Each reversible operation encapsulates execution and rollback routines in an object inheriting from `Command`. New actions are pushed onto `undo_stack` while clearing `redo_stack`. Invoking undo pops the latest command, executes its `undo()` handler, and transfers it to `redo_stack`. Redo reverses this process.

## 3. Complexity analysis
| Operation | Time | Auxiliary Space |
|---|---:|---:|
| Execute Command | O(1) | O(1) |
| Undo | O(1) | O(1) |
| Redo | O(1) | O(1) |

## 4. Sample I/O
```text
Initial document: ''
After two inserts: 'Hello World!'
After 1st undo: 'Hello '
After redo: 'Hello World!'
After 2 undos: ''
```

## 5. Real-life application
Standard desktop applications (MS Word, VS Code `Ctrl+Z` / `Ctrl+Y`, Photoshop history brush, CAD design software).
