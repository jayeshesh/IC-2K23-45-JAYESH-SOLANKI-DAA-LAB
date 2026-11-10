# Bubble Sort

**Language:** Python 3.10+  
**Run:** `python Lab02-Sorting-Searching/Program01-BubbleSort/bubble_sort.py`  
**Shared implementation:** [sorting_algorithms.py](../sorting_algorithms.py)

## Problem statement
Implement Bubble Sort as required by Unit 2 and demonstrate it with sample data.

## Approach
The reusable implementation is in `sorting_algorithms.py`. The program in this folder imports and demonstrates the corresponding function. Sorting functions return a new list and do not mutate the source list.

## Algorithm
Compare adjacent values and swap inverted neighbours. Stop early when a full pass makes no swaps.

## Pseudocode
```text
BUBBLE SORT(A)
  create a working copy of A
  perform the steps described above
  return the sorted working copy
```

## Dry run
[5, 1, 4, 2] → [1, 4, 2, 5] → [1, 2, 4, 5].

## Complexity analysis
| Case | Time complexity |
|---|---|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |

Auxiliary space: **O(1) auxiliary**. The returned list is a separate copy and occupies O(n) memory.

## Sample input/output
```text
Input: [34, -2, 7, 7, 19, 0, 12]
Output: [-2, 0, 7, 7, 12, 19, 34]
```

## Real-life application
Stable; useful for teaching and very small datasets.

## Learning outcomes
Complete after executing the program and reflecting on the result.

## Tests and screenshots
See [test_unit2.py](../../../tests/test_unit2.py). Capture a real terminal screenshot after running this program.
