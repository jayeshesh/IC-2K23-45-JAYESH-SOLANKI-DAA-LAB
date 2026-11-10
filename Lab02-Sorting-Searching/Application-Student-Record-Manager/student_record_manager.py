"""Student Record Manager using the Unit 2 sorting/searching algorithms."""
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sorting_algorithms import SORTS, binary_search


@dataclass(frozen=True)
class Student:
    roll_no: str
    name: str
    marks: float

    def __post_init__(self):
        if not isinstance(self.roll_no, str) or not self.roll_no.strip():
            raise ValueError("roll number cannot be empty")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("student name cannot be empty")
        if not 0 <= float(self.marks) <= 100:
            raise ValueError("marks must be between 0 and 100")


def normalize(field, value):
    if field in {"roll_no", "name"}: return str(value).strip().casefold()
    if field == "marks": return float(value)
    raise ValueError("field must be roll_no, name, or marks")


def student_key(field):
    if field not in {"roll_no", "name", "marks"}:
        raise ValueError("field must be roll_no, name, or marks")
    return lambda student: normalize(field, getattr(student, field))


def sort_students(students, field, algorithm="merge"):
    if algorithm not in SORTS: raise ValueError(f"Unknown sorting algorithm: {algorithm}")
    if algorithm == "radix":
        if field != "marks":
            raise ValueError("Radix Sort needs integer keys; use it for whole-number marks, not text fields")
        if any(not float(student.marks).is_integer() for student in students):
            raise ValueError("Radix Sort requires whole-number marks")
        buckets = defaultdict(deque)
        for student in students:
            buckets[int(student.marks)].append(student)
        ordered_marks = SORTS["radix"]([int(student.marks) for student in students])
        return [buckets[mark].popleft() for mark in ordered_marks]
    return SORTS[algorithm](students, key=student_key(field))


def search_students(students, field, value, strategy="binary"):
    target, get = normalize(field, value), student_key(field)
    if strategy == "linear":
        return [student for student in students if get(student) == target]
    if strategy != "binary":
        raise ValueError("strategy must be linear or binary")
    ordered = sort_students(students, field, "merge")
    index = binary_search(ordered, target, key=get)
    if index == -1: return []
    start = index
    while start > 0 and get(ordered[start - 1]) == target: start -= 1
    end = index + 1
    while end < len(ordered) and get(ordered[end]) == target: end += 1
    return ordered[start:end]


def demo_records():
    return [
        Student("IC045", "Aarav Shah", 86),
        Student("IC012", "Diya Patel", 91),
        Student("IC031", "Kabir Rao", 78),
        Student("IC008", "Meera Joshi", 91),
        Student("IC027", "Aarav Shah", 82),
    ]


def main():
    records = demo_records()
    fields = {"1": "roll_no", "2": "name", "3": "marks"}
    while True:
        print("\nSTUDENT RECORD MANAGER")
        print("1. Sort  2. Search  0. Exit")
        choice = input("Choice: ").strip()
        if choice == "0": return
        if choice not in {"1", "2"}:
            print("Invalid choice."); continue
        print("Field: 1. Roll number  2. Name  3. Marks")
        selected = input("Field: ").strip()
        if selected not in fields:
            print("Invalid field."); continue
        field = fields[selected]
        try:
            if choice == "1":
                print("Algorithms:", ", ".join(SORTS))
                results = sort_students(records, field, input("Algorithm: ").strip().lower())
            else:
                value = input(f"Search {field}: ").strip()
                method = input("Search method (linear/binary): ").strip().lower()
                results = search_students(records, field, value, method)
            if results:
                for record in results: print(record)
            else: print("No matching records.")
        except (ValueError, TypeError) as exc:
            print(f"Input error: {exc}")


if __name__ == "__main__":
    main()
