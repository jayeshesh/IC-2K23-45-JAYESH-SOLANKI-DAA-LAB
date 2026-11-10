# Heap Sort

**Language:** Python 3.10+  
**Run:** `python Lab02-Sorting-Searching/Program06-HeapSort/heap_sort.py`  
**Shared implementation:** [sorting_algorithms.py](../sorting_algorithms.py)

## Problem statement
Implement Heap Sort as required by Unit 2 and demonstrate it with sample data.

## Approach
The reusable implementation is in `sorting_algorithms.py`. The program in this folder imports and demonstrates the corresponding function. Sorting functions return a new list and do not mutate the source list.

## Algorithm
Build a max heap, repeatedly swap its root with the last unsorted item, and restore the heap property.

## Pseudocode
```text
HEAP SORT(A)
  create a working copy of A
  perform the steps described above
  return the sorted working copy
```

## Dry run
[5, 1, 4, 2] → max heap → extract 5, 4, 2, 1 → [1,2,4,5].

## Complexity analysis
| Case | Time complexity |
|---|---|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

Auxiliary space: **O(1) auxiliary besides returned copy**. The returned list is a separate copy and occupies O(n) memory.

## Sample input/output
```text
Input: [34, -2, 7, 7, 19, 0, 12]
Output: [-2, 0, 7, 7, 12, 19, 34]
```

## Real-life application
Not stable; useful when worst-case O(n log n) time is desired.

## Learning outcomes
Complete after executing the program and reflecting on the result.

## Tests and screenshots
See [test_unit2.py](../../../tests/test_unit2.py). Capture a real terminal screenshot after running this program.


## Visual Execution Output
![Program Execution Screenshot](screenshots/screenshot.png)
