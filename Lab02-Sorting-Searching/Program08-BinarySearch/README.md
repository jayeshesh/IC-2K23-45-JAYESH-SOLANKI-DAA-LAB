# Binary Search

**Language:** Python 3.10+  
**Run:** `python Lab02-Sorting-Searching/Program08-BinarySearch/binary_search.py`

## Problem statement
Search for a key in an ascending sorted sequence using Binary Search.

## Approach
Maintain a half-open search interval [low, high). Compare the middle key with the target and shrink the interval. When duplicates exist, continue toward the left boundary to return the first matching index.

## Algorithm and pseudocode
```text
BINARY_SEARCH(A, target)
  low = 0; high = length(A)
  while low < high
    mid = floor((low + high) / 2)
    if A[mid] < target: low = mid + 1
    else: high = mid
  if low < length(A) and A[low] == target: return low
  return -1
```

## Dry run
For [2, 4, 7, 7, 9] and target 7, the lower-bound search terminates at index 2, the first occurrence.

## Complexity
Best O(1), average O(log n), worst O(log n); auxiliary space O(1). The input must already be sorted by the same key.

## Sample input/output
```text
Sorted input: [2, 4, 7, 7, 9, 13, 18]
First index of 7: 2
Absent target 10: -1
```

## Real-life application
Lookup in sorted dictionaries, catalogues, and index files.

## Learning outcomes
Complete after executing and reflecting on the program.

## Tests and screenshots
See [test_unit2.py](../../../tests/test_unit2.py). Capture an actual terminal screenshot after the run.
