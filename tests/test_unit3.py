"""Unit tests for Unit 3: Linked Lists.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "Lab03-Linked-Lists" / "Program01-Singly-Linked-List"))
sys.path.insert(0, str(REPO_ROOT / "Lab03-Linked-Lists" / "Program02-Doubly-Linked-List"))
sys.path.insert(0, str(REPO_ROOT / "Lab03-Linked-Lists" / "Program03-Circular-Linked-List"))
sys.path.insert(0, str(REPO_ROOT / "Lab03-Linked-Lists" / "Program04-Polynomial-Operations"))
sys.path.insert(0, str(REPO_ROOT / "Lab03-Linked-Lists" / "Application-Text-Editor-Buffer"))
sys.path.insert(0, str(REPO_ROOT / "Lab03-Linked-Lists" / "Application-Playlist-Manager"))

from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
from circular_linked_list import CircularLinkedList
from polynomial_operations import PolynomialLinkedList
from text_editor_buffer import TextEditorBuffer
from playlist_manager import PlaylistManager


class TestSinglyLinkedList(unittest.TestCase):
    def test_insert_and_delete(self):
        sll = SinglyLinkedList()
        sll.append(10)
        sll.append(30)
        sll.insert_at(1, 20)
        self.assertEqual(sll.to_list(), [10, 20, 30])
        self.assertEqual(sll.delete_at(1), 20)
        self.assertEqual(sll.to_list(), [10, 30])

    def test_reverse(self):
        sll = SinglyLinkedList()
        for i in [1, 2, 3, 4]:
            sll.append(i)
        sll.reverse()
        self.assertEqual(sll.to_list(), [4, 3, 2, 1])

    def test_concatenate(self):
        sll1 = SinglyLinkedList()
        sll1.append(1)
        sll2 = SinglyLinkedList()
        sll2.append(2)
        res = sll1.concatenate(sll2)
        self.assertEqual(res.to_list(), [1, 2])


class TestDoublyLinkedList(unittest.TestCase):
    def test_bidirectional(self):
        dll = DoublyLinkedList()
        dll.append("A")
        dll.append("B")
        dll.append("C")
        self.assertEqual(dll.to_list(), ["A", "B", "C"])
        self.assertEqual(dll.to_reverse_list(), ["C", "B", "A"])

    def test_delete_and_reverse(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.append(3)
        self.assertEqual(dll.delete_at(1), 2)
        dll.reverse()
        self.assertEqual(dll.to_list(), [3, 1])


class TestCircularLinkedList(unittest.TestCase):
    def test_circular_ops(self):
        cll = CircularLinkedList()
        cll.append(10)
        cll.append(20)
        cll.prepend(5)
        self.assertEqual(cll.to_list(), [5, 10, 20])
        self.assertEqual(cll.delete_at(0), 5)
        self.assertEqual(cll.to_list(), [10, 20])
        cll.reverse()
        self.assertEqual(cll.to_list(), [20, 10])


class TestPolynomialOperations(unittest.TestCase):
    def test_addition(self):
        p1 = PolynomialLinkedList()
        p1.insert_term(5, 2)
        p1.insert_term(3, 1)

        p2 = PolynomialLinkedList()
        p2.insert_term(2, 2)
        p2.insert_term(4, 0)

        sum_p = p1.add(p2)
        self.assertEqual(sum_p.to_list(), [(7, 2), (3, 1), (4, 0)])


class TestApplications(unittest.TestCase):
    def test_editor_buffer(self):
        ed = TextEditorBuffer()
        ed.append_line("Hello")
        ed.append_line("World")
        ed.insert_line(2, "Beautiful")
        self.assertEqual(ed.get_lines(), ["Hello", "Beautiful", "World"])
        self.assertEqual(ed.delete_line(2), "Beautiful")
        self.assertEqual(ed.get_lines(), ["Hello", "World"])

    def test_playlist_manager(self):
        pm = PlaylistManager()
        pm.add_song("Song A", "Artist A", 100)
        pm.add_song("Song B", "Artist B", 200)
        self.assertIn("Song A", pm.current_track() or "")
        self.assertIn("Song B", pm.next_track() or "")
        self.assertIn("Song A", pm.next_track() or "")


if __name__ == "__main__":
    unittest.main()
