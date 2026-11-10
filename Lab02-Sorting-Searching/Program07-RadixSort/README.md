# Radix Sort

**Language:** Python 3.10+  
**Run:** `python Lab02-Sorting-Searching/Program07-RadixSort/radix_sort.py`  
**Shared implementation:** [sorting_algorithms.py](../sorting_algorithms.py)

## Problem statement
Implement Radix Sort as required by Unit 2 and demonstrate it with sample data.

## Approach
The reusable implementation is in `sorting_algorithms.py`. The program in this folder imports and demonstrates the corresponding function. Sorting functions return a new list and do not mutate the source list.

## Algorithm
Use stable least-significant-digit decimal passes. Sort negative magnitudes separately and reverse their order.

## Pseudocode
```text
RADIX SORT(A)
  create a working copy of A
  perform the steps described above
  return the sorted working copy
```

## Dry run
[170, 45, 75, -90] → digit passes → [-90, 45, 75, 170].

## Complexity analysis
| Case | Time complexity |
|---|---|
| Best | O(d(n+10)) |
| Average | O(d(n+10)) |
| Worst | O(d(n+10)) |

Auxiliary space: **O(n+10) auxiliary**. The returned list is a separate copy and occupies O(n) memory.

## Sample input/output
```text
Input: [34, -2, 7, 7, 19, 0, 12]
Output: [-2, 0, 7, 7, 12, 19, 34]
```

## Real-life application
Stable LSD sort for integers; d is number of decimal digits and base is 10.

## Learning outcomes
Complete after executing the program and reflecting on the result.

## Tests and screenshots
See [test_unit2.py](../../../tests/test_unit2.py). Capture a real terminal screenshot after running this program.
