# 1D Array Operations

**Language:** Python 3.10+  
**Run:** `python Lab01-Introduction-Arrays/Program01-ArrayOperations/array_operations.py`

## Problem statement
Implement one-dimensional array insertion, deletion, searching, and rotation.

## Approach
Represent the array using a Python list. Operations return a new list for insert/delete/rotate, preserving the caller's original list. Search returns the first matching zero-based index or -1.

## Algorithm and pseudocode
- Insert: validate position, copy list, insert value.
- Delete: validate position, copy list, remove and return the removed value.
- Search: scan from left to right and stop at the first match.
- Rotate right: reduce rotation count modulo array length, then join the suffix and prefix.

```text
ROTATE_RIGHT(A, k)
  if A is empty: return empty array
  shift = k modulo length(A)
  return A[length(A)-shift:] + A[:length(A)-shift]
```

## Dry run
Input: `[10, 20, 30, 40]`, rotate right by 2.  
Shift = 2; suffix = `[30, 40]`; prefix = `[10, 20]`; result = `[30, 40, 10, 20]`.

## Complexity
For n elements:
| Operation | Best | Average | Worst | Auxiliary space |
|---|---:|---:|---:|---:|
| Insert at index | O(1) at end | O(n) | O(n) | O(n) due to copy |
| Delete at index | O(1) at end | O(n) | O(n) | O(n) due to copy |
| Search | O(1) | O(n) | O(n) | O(1) |
| Rotate | O(n) | O(n) | O(n) | O(n) |

## Sample I/O
```text
Initial array: [10, 20, 30, 40, 50]
Insert 25 at index 2: [10, 20, 25, 30, 40, 50]
Delete index 1 (removed 20): [10, 30, 40, 50]
Search for 40: 3
Rotate right by 2: [40, 50, 10, 20, 30]
```

## Real-life application
Array-based buffers, playlists, and circular data windows.

## Learning outcomes
_To be completed after execution and reflection._

## Tests and screenshots
See `tests/test_unit1.py`. Capture an actual terminal screenshot after running the program.
