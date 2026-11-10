# Capstone Project 2: Hospital Management System

**Language:** Python 3.10+  
**Run:** `python Capstone-Projects/Project02-Hospital-Management/hospital_management.py`

## 1. Problem statement
Design and implement an integrated Hospital Operations System coordinating four critical algorithmic modules:
1. **Patient Emergency Queue**: Priority queue (Binary Min-Heap) triage system.
2. **Doctor Availability**: LIFO Stack for recent medical consultation history and visit undo.
3. **Department Hierarchy**: N-ary Tree organizing medical departments and specialty clinics.
4. **Patient Relationship Graph**: Undirected graph for epidemiology and contact tracing.

## 2. Complexity analysis
| Subsystem | Operation | Time Complexity | Auxiliary Space |
|---|---|---:|---:|
| Triage Queue | Admit / Treat | O(log n) | O(n) |
| Consultation History | Push / Pop | O(1) | O(1) |
| Department Tree | Add Dept / Display | O(1) / O(V) | O(height) |
| Contact Graph | Add / Trace Contact | O(1) / O(deg) | O(V + E) |

## 3. Sample I/O
```text
=== 1. Hospital Department Hierarchy ===
- Chief Medical Officer
  - Cardiology
    - ICU
    - Cardiac Surgery
  - Neurology
    - Neuro-Trauma

=== 2. Patient Triage (Priority Queue) ===
Next for Emergency Treatment: Jayesh (Cardiac Arrest)
Next for Emergency Treatment: Priya (Sprained Ankle)

=== 3. Doctor Consultation History (Stack) ===
Recent visits: ['Jayesh (Cardiac Arrest) (Triage Priority 1)', 'Priya (Sprained Ankle) (Triage Priority 3)']
```

## 4. Learning outcomes
Integrated heaps, stacks, trees, and graphs into a cohesive real-world clinical workflow.
