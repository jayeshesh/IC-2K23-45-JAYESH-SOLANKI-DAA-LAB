"""Course Prerequisite Tracker (Topological Sort / DAG Dependency Resolution).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 7: Graphs (CO3) Application / Bonus
"""

from typing import Dict, List, Set


def topological_sort_kahn(courses: List[str], prerequisites: List[tuple[str, str]]) -> List[str]:
    """Resolve valid academic course scheduling order using Kahn's in-degree algorithm."""
    adj: Dict[str, List[str]] = {c: [] for c in courses}
    in_degree: Dict[str, int] = {c: 0 for c in courses}

    for prereq, course in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    queue: List[str] = [c for c in courses if in_degree[c] == 0]
    order: List[str] = []

    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != len(courses):
        raise ValueError("Cycle detected in course prerequisites! Topological sort impossible.")

    return order


def demo() -> None:
    courses = ["CS101", "CS102", "DS201", "ALGO301", "AI401"]
    prereqs = [
        ("CS101", "CS102"),
        ("CS102", "DS201"),
        ("DS201", "ALGO301"),
        ("ALGO301", "AI401"),
    ]
    schedule = topological_sort_kahn(courses, prereqs)
    print("Valid Semester Course Sequence:")
    print(" -> ".join(schedule))


if __name__ == "__main__":
    demo()
