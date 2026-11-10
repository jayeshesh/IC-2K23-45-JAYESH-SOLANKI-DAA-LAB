# Course Prerequisite Tracker (Topological Sort Bonus)

**Language:** Python 3.10+  
**Run:** `python Lab07-Graphs/Application-Course-Prerequisite-Tracker-Bonus/course_prerequisite_tracker.py`

## 1. Problem statement
Given an academic curriculum of courses and required prerequisites, determine a valid linear course sequence using Directed Acyclic Graph (DAG) Topological Sorting, detecting circular dependency deadlocks.

## 2. Approach
Kahn's algorithm tracks in-degrees (number of incoming prerequisites) for each course. Courses with in-degree 0 are queued. Dequeuing a course decrements the in-degrees of its dependent courses. If the final ordered list length differs from the course count, a cycle exists.

## 3. Complexity analysis
| Metric | Value |
|---|---:|
| Time Complexity | O(V + E) |
| Auxiliary Space | O(V + E) |

## 4. Sample I/O
```text
Valid Semester Course Sequence:
CS101 -> CS102 -> DS201 -> ALGO301 -> AI401
```

## 5. Real-life application
Build dependency resolvers (Makefiles, CMake, npm package dependency graphs) and university degree audit degree planning systems.
