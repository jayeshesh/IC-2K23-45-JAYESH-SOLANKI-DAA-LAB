"""Capstone Project 2: Hospital Management System.

Combines:
- Patient emergency triage queue (Priority Queue / Min-Heap)
- Doctor availability & consultation backtracking (Stack for recent visits)
- Department clinical hierarchy (Tree)
- Patient contact tracing & relationship graph (Graph)

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
"""

import heapq
from typing import Dict, List, Optional, Set, Tuple


class HospitalDepartmentTree:
    """Hierarchical department organizational tree."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.sub_departments: List["HospitalDepartmentTree"] = []

    def add_sub_dept(self, dept_name: str) -> "HospitalDepartmentTree":
        sub = HospitalDepartmentTree(dept_name)
        self.sub_departments.append(sub)
        return sub

    def get_hierarchy(self, prefix: str = "") -> List[str]:
        lines = [f"{prefix}- {self.name}"]
        for sub in self.sub_departments:
            lines.extend(sub.get_hierarchy(prefix + "  "))
        return lines


class HospitalManagementSystem:
    """Integrated clinical patient management simulator combining heap, stack, tree, and graph."""

    def __init__(self) -> None:
        # 1. Emergency Patient Triage: Min-Heap (1 = Critical emergency, 5 = Routine)
        self.triage_heap: List[Tuple[int, int, str]] = []  # (priority, counter, name)
        self._triage_counter: int = 0

        # 2. Doctor Visit Stack (LIFO recent history)
        self.doctor_visit_stack: List[str] = []

        # 3. Department Hierarchy
        self.dept_root: HospitalDepartmentTree = HospitalDepartmentTree("Chief Medical Officer")
        cardio = self.dept_root.add_sub_dept("Cardiology")
        cardio.add_sub_dept("ICU")
        cardio.add_sub_dept("Cardiac Surgery")
        neuro = self.dept_root.add_sub_dept("Neurology")
        neuro.add_sub_dept("Neuro-Trauma")

        # 4. Patient Relationship & Contact Tracing Graph
        self.contact_graph: Dict[str, Set[str]] = {}

    def admit_patient(self, name: str, triage_priority: int) -> None:
        self._triage_counter += 1
        heapq.heappush(self.triage_heap, (triage_priority, self._triage_counter, name))

    def treat_next_patient(self) -> Optional[str]:
        if not self.triage_heap:
            return None
        priority, _, name = heapq.heappop(self.triage_heap)
        self.doctor_visit_stack.append(f"{name} (Triage Priority {priority})")
        return name

    def add_contact(self, patient_a: str, patient_b: str) -> None:
        if patient_a not in self.contact_graph:
            self.contact_graph[patient_a] = set()
        if patient_b not in self.contact_graph:
            self.contact_graph[patient_b] = set()
        self.contact_graph[patient_a].add(patient_b)
        self.contact_graph[patient_b].add(patient_a)

    def trace_contacts(self, patient: str) -> Set[str]:
        """Find direct exposure contacts."""
        return self.contact_graph.get(patient, set())


def demo() -> None:
    hosp = HospitalManagementSystem()

    print("=== 1. Hospital Department Hierarchy ===")
    for line in hosp.dept_root.get_hierarchy():
        print(line)

    print("\n=== 2. Patient Triage (Priority Queue) ===")
    hosp.admit_patient("Rohan (Flu)", 4)
    hosp.admit_patient("Jayesh (Cardiac Arrest)", 1)
    hosp.admit_patient("Priya (Sprained Ankle)", 3)

    print("Next for Emergency Treatment:", hosp.treat_next_patient())
    print("Next for Emergency Treatment:", hosp.treat_next_patient())

    print("\n=== 3. Doctor Consultation History (Stack) ===")
    print("Recent visits (top of stack is last):", hosp.doctor_visit_stack)

    print("\n=== 4. Epidemic Contact Tracing (Graph) ===")
    hosp.add_contact("Rohan (Flu)", "Amit")
    hosp.add_contact("Rohan (Flu)", "Sunita")
    print("Direct contacts of Rohan:", hosp.trace_contacts("Rohan (Flu)"))


if __name__ == "__main__":
    demo()
