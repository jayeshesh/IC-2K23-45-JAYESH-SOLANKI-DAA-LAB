"""Unit tests for Unit 4: Stacks.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "Lab04-Stacks" / "Program01-Static-Stack"))
sys.path.insert(0, str(REPO_ROOT / "Lab04-Stacks" / "Program02-Dynamic-Stack"))
sys.path.insert(0, str(REPO_ROOT / "Lab04-Stacks" / "Program03-Infix-Conversion"))
sys.path.insert(0, str(REPO_ROOT / "Lab04-Stacks" / "Program04-Expression-Evaluation"))
sys.path.insert(0, str(REPO_ROOT / "Lab04-Stacks" / "Application-Expression-Evaluator"))
sys.path.insert(0, str(REPO_ROOT / "Lab04-Stacks" / "Application-Undo-Redo"))

from static_stack import StaticStack, StackOverflowError, StackUnderflowError
from dynamic_stack import DynamicStack
from infix_conversion import infix_to_postfix, infix_to_prefix
from expression_evaluation import evaluate_postfix, evaluate_prefix
from expression_evaluator import evaluate_infix
from undo_redo import TextDocument, UndoRedoManager, InsertTextCommand


class TestStaticAndDynamicStacks(unittest.TestCase):
    def test_static_stack(self):
        s = StaticStack(capacity=2)
        s.push(10)
        s.push(20)
        self.assertTrue(s.is_full())
        with self.assertRaises(StackOverflowError):
            s.push(30)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.peek(), 10)
        s.pop()
        self.assertTrue(s.is_empty())
        with self.assertRaises(StackUnderflowError):
            s.pop()

    def test_dynamic_stack(self):
        ds = DynamicStack()
        ds.push("A")
        ds.push("B")
        self.assertEqual(ds.peek(), "B")
        self.assertEqual(ds.pop(), "B")
        self.assertEqual(ds.pop(), "A")
        self.assertTrue(ds.is_empty())


class TestConversionsAndEvaluations(unittest.TestCase):
    def test_infix_to_postfix(self):
        expr = "A+B*C"
        self.assertEqual(infix_to_postfix(expr), "ABC*+")

    def test_infix_to_prefix(self):
        expr = "A+B*C"
        self.assertEqual(infix_to_prefix(expr), "+A*BC")

    def test_eval_postfix_and_prefix(self):
        # 3 4 + 2 * = 14
        self.assertEqual(evaluate_postfix(["3", "4", "+", "2", "*"]), 14.0)
        # * + 3 4 2 = 14
        self.assertEqual(evaluate_prefix(["*", "+", "3", "4", "2"]), 14.0)

    def test_eval_infix(self):
        self.assertEqual(evaluate_infix("2 + 3 * 4"), 14.0)
        self.assertEqual(evaluate_infix("(2 + 3) * 4"), 20.0)
        self.assertEqual(evaluate_infix("2 ^ 3 ^ 2"), 512.0)


class TestUndoRedo(unittest.TestCase):
    def test_undo_redo_manager(self):
        doc = TextDocument()
        mgr = UndoRedoManager()
        mgr.execute_command(InsertTextCommand(doc, "Part 1; "))
        mgr.execute_command(InsertTextCommand(doc, "Part 2"))
        self.assertEqual(doc.text, "Part 1; Part 2")
        mgr.undo()
        self.assertEqual(doc.text, "Part 1; ")
        mgr.redo()
        self.assertEqual(doc.text, "Part 1; Part 2")


if __name__ == "__main__":
    unittest.main()
