# Matrix Calculator

**Language:** Python 3.10+  
**Run:** `python Lab01-Introduction-Arrays/Program04-MatrixCalculator/matrix_calculator.py`

## Problem statement
Build a menu-driven calculator for matrix addition, multiplication, transpose, and determinant for small matrices.

## Approach
Represent matrices as rectangular lists of numeric rows. Validate dimensions before addition and multiplication. Compute determinant recursively by cofactor expansion, with direct base cases for 1×1 and 2×2 matrices. This determinant implementation is intended for small matrices, as requested in the guide.

## Algorithm and pseudocode
```text
DETERMINANT(M)
  if M is 1x1: return its only value
  if M is 2x2: return ad - bc
  result = 0
  for each column j in first row:
    minor = matrix excluding first row and column j
    result += (-1)^j * M[0][j] * DETERMINANT(minor)
  return result
```

## Dry run
For `[[1,2],[3,4]]`, determinant = (1×4) − (2×3) = −2.

## Complexity
For r×c matrices:
| Operation | Time | Auxiliary space |
|---|---:|---:|
| Addition | O(rc) | O(rc) for result |
| Multiplication (r×k by k×c) | O(rkc) | O(rc) for result |
| Transpose | O(rc) | O(rc) for result |
| Determinant (n×n, cofactor expansion) | O(n!) | O(n²) recursion/minor storage at a time (implementation-dependent) |

## Sample I/O
```text
Choose 4. Determinant
Enter matrix: [[1, 2], [3, 4]]
Result: -2
```
The interactive program prompts for dimensions and matrix rows; the snippet above illustrates the corresponding operation.

## Real-life application
Small-scale scientific, graphics, and engineering calculations.

## Learning outcomes
_To be completed after execution and reflection._

## Tests and screenshots
See `tests/test_unit1.py`. Run the menu program and capture an actual terminal screenshot.
