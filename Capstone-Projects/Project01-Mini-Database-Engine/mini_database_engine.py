"""Capstone Project 1: Mini Database Engine.

Combines arrays, linked lists, hash indexing, BST/AVL indexing, and sorting/searching.
Supports full CRUD on tabular records with indexing.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

from typing import Any, Dict, List, Optional


class IndexBSTNode:
    def __init__(self, key: Any, record_id: int) -> None:
        self.key: Any = key
        self.record_ids: List[int] = [record_id]
        self.left: Optional["IndexBSTNode"] = None
        self.right: Optional["IndexBSTNode"] = None


class BSTIndex:
    """Secondary index for range and ordered queries using BST."""

    def __init__(self) -> None:
        self.root: Optional[IndexBSTNode] = None

    def insert(self, key: Any, record_id: int) -> None:
        self.root = self._insert(self.root, key, record_id)

    def _insert(self, node: Optional[IndexBSTNode], key: Any, record_id: int) -> IndexBSTNode:
        if not node:
            return IndexBSTNode(key, record_id)
        if key < node.key:
            node.left = self._insert(node.left, key, record_id)
        elif key > node.key:
            node.right = self._insert(node.right, key, record_id)
        else:
            if record_id not in node.record_ids:
                node.record_ids.append(record_id)
        return node

    def delete_record(self, key: Any, record_id: int) -> None:
        """Remove record_id from the index node."""
        curr = self.root
        while curr:
            if key == curr.key:
                if record_id in curr.record_ids:
                    curr.record_ids.remove(record_id)
                return
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

    def search(self, key: Any) -> List[int]:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.record_ids
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return []


class MiniDatabaseEngine:
    """In-Memory Relational Engine supporting CRUD, primary hash indexing, and secondary BST indexing."""

    def __init__(self, table_name: str) -> None:
        self.table_name: str = table_name
        self.records: Dict[int, Dict[str, Any]] = {}  # Primary hash index (ID -> Record)
        self.salary_index: BSTIndex = BSTIndex()     # Secondary ordered index
        self._next_id: int = 1

    def create(self, name: str, role: str, salary: float) -> int:
        """Create (Insert) a new record with auto-increment ID."""
        rec_id = self._next_id
        self._next_id += 1
        record = {"id": rec_id, "name": name, "role": role, "salary": salary}
        self.records[rec_id] = record
        self.salary_index.insert(salary, rec_id)
        return rec_id

    def read(self, record_id: int) -> Optional[Dict[str, Any]]:
        """Read (Select by Primary Key) in O(1) time."""
        return self.records.get(record_id)

    def update(self, record_id: int, **kwargs) -> bool:
        """Update existing record attributes and refresh secondary index."""
        if record_id not in self.records:
            return False
        rec = self.records[record_id]
        if "salary" in kwargs and kwargs["salary"] != rec["salary"]:
            old_sal = rec["salary"]
            new_sal = kwargs["salary"]
            self.salary_index.delete_record(old_sal, record_id)
            self.salary_index.insert(new_sal, record_id)
        for key, val in kwargs.items():
            rec[key] = val
        return True

    def delete(self, record_id: int) -> bool:
        """Delete record by ID."""
        if record_id not in self.records:
            return False
        sal = self.records[record_id]["salary"]
        self.salary_index.delete_record(sal, record_id)
        del self.records[record_id]
        return True

    def query_by_salary(self, salary: float) -> List[Dict[str, Any]]:
        """Query records via secondary BST index in O(log n)."""
        ids = self.salary_index.search(salary)
        return [self.records[rid] for rid in ids if rid in self.records]

    def scan_all(self, sort_by: str = "id") -> List[Dict[str, Any]]:
        """Full table scan with sorting."""
        all_recs = list(self.records.values())
        return sorted(all_recs, key=lambda r: r.get(sort_by, 0))


def demo() -> None:
    db = MiniDatabaseEngine("Employees")
    id1 = db.create("Jayesh", "AI Engineer", 85000.0)
    id2 = db.create("Aarav", "Data Analyst", 65000.0)
    id3 = db.create("Priya", "System Architect", 85000.0)

    print("All Records:", db.scan_all())
    print("\nLookup by Primary Key (ID 1):", db.read(id1))
    print("Secondary BST Index Query (Salary 85000):", db.query_by_salary(85000.0))

    db.update(id2, salary=70000.0)
    print("\nAfter Salary Update for Aarav:", db.read(id2))

    db.delete(id3)
    print("After Deleting Priya:", db.scan_all())


if __name__ == "__main__":
    demo()
