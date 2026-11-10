# Quick Sort

**Language:** Python 3.10+  
**Run:** `python Lab02-Sorting-Searching/Program05-QuickSort/quick_sort.py`  
**Shared implementation:** [sorting_algorithms.py](../sorting_algorithms.py)

## Problem statement
Implement Quick Sort as required by Unit 2 and demonstrate it with sample data.

## Approach
The reusable implementation is in `sorting_algorithms.py`. The program in this folder imports and demonstrates the corresponding function. Sorting functions return a new list and do not mutate the source list.

## Algorithm
Partition values around a pivot into less-than, equal-to, and greater-than groups; sort the outer groups.

## Pseudocode
```text
QUICK SORT(A)
  create a working copy of A
  perform the steps described above
  return the sorted working copy
```

## Dry run
[5, 1, 4, 2], pivot 4 → [1,2] | [4] | [5] → [1,2,4,5].

## Complexity analysis
| Case | Time complexity |
|---|---|
| Best | O(n log n) expected |
| Average | O(n log n) expected |
| Worst | O(n²) |

Auxiliary space: **O(log n) typical pending ranges; O(n) worst**. The returned list is a separate copy and occupies O(n) memory.

## Sample input/output
```text
Input: [34, -2, 7, 7, 19, 0, 12]
Output: [-2, 0, 7, 7, 12, 19, 34]
```

## Real-life application
Three-way partition handles duplicates. Not stable; runtime depends on pivot behaviour.

## Learning outcomes
Complete after executing the program and reflecting on the result.

## Tests and screenshots
See [test_unit2.py](../../../tests/test_unit2.py). Capture a real terminal screenshot after running this program.
