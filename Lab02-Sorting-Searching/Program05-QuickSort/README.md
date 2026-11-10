# Quick Sort

**Run:** `python Lab02-Sorting-Searching/Program05-QuickSort/quick_sort.py`  
**Shared implementation:** [sorting_algorithms.py](../sorting_algorithms.py)

## Problem statement
Sort values in ascending order using Quick Sort.

## Approach and algorithm
The iterative implementation uses a middle element as pivot and three-way partitioning into less-than, equal-to, and greater-than sections. It processes the smaller partition immediately and defers the larger one on an explicit stack.

## Pseudocode
```text
QUICK_SORT(A)
  push full range on explicit stack
  while a range remains:
    choose middle pivot
    partition into < pivot, = pivot, > pivot
    defer larger partition; process smaller partition next
  return sorted copy
```

## Dry run
[5, 1, 4, 2], pivot 4 → [1, 2] | [4] | [5] → [1, 2, 4, 5].

## Complexity analysis
Best O(n log n), expected average O(n log n), worst O(n²). Processing the smaller partition first bounds the pending range stack to O(log n). The returned copy occupies O(n) memory. Quick Sort is not stable.

## Sample input/output
```text
Input: [34, -2, 7, 7, 19, 0, 12]
Output: [-2, 0, 7, 7, 12, 19, 34]
```

## Real-life application
Quick in-memory sorting; runtime depends on pivot and input arrangement.

## Learning outcomes
Complete after execution.

## Tests and screenshots
See [test_unit2.py](../../../tests/test_unit2.py). Capture a real terminal screenshot.
