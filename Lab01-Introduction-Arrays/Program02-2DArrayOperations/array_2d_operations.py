"""Two-dimensional array operations for IC-307D Unit 1.

Matrices are represented as lists of rows. Ragged matrices are rejected so
that row/column operations have predictable behaviour.
"""


def _validate(matrix: list[list]) -> tuple[int, int]:
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of rows")
    if not matrix:
        return 0, 0
    if any(not isinstance(row, list) for row in matrix):
        raise TypeError("each matrix row must be a list")
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular (no ragged rows)")
    return len(matrix), width


def insert_row(matrix: list[list], index: int, row: list) -> list[list]:
    rows, cols = _validate(matrix)
    if not 0 <= index <= rows:
        raise IndexError("row insertion index is out of range")
    if rows and len(row) != cols:
        raise ValueError("inserted row must have the same number of columns")
    if not rows and not isinstance(row, list):
        raise TypeError("row must be a list")
    result = [r.copy() for r in matrix]
    result.insert(index, row.copy())
    return result


def delete_row(matrix: list[list], index: int) -> tuple[list[list], list]:
    rows, _ = _validate(matrix)
    if not 0 <= index < rows:
        raise IndexError("row deletion index is out of range")
    result = [r.copy() for r in matrix]
    removed = result.pop(index)
    return result, removed


def insert_column(matrix: list[list], index: int, values: list) -> list[list]:
    rows, cols = _validate(matrix)
    if not 0 <= index <= cols:
        raise IndexError("column insertion index is out of range")
    if len(values) != rows:
        raise ValueError("one inserted value is required for each row")
    result = [r.copy() for r in matrix]
    for row, value in zip(result, values):
        row.insert(index, value)
    return result


def delete_column(matrix: list[list], index: int) -> tuple[list[list], list]:
    rows, cols = _validate(matrix)
    if not 0 <= index < cols:
        raise IndexError("column deletion index is out of range")
    result = [r.copy() for r in matrix]
    removed = [row.pop(index) for row in result]
    return result, removed


def search(matrix: list[list], target) -> list[tuple[int, int]]:
    """Return all (row, column) positions containing target."""
    _validate(matrix)
    return [
        (r, c)
        for r, row in enumerate(matrix)
        for c, value in enumerate(row)
        if value == target
    ]


def rotate_clockwise(matrix: list[list]) -> list[list]:
    """Rotate a rectangular matrix 90 degrees clockwise."""
    _validate(matrix)
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix[::-1])]


def main() -> None:
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("Initial matrix:", matrix)
    print("Insert row at index 1:", insert_row(matrix, 1, [7, 8, 9]))
    print("Delete column 1:", delete_column(matrix, 1)[0])
    print("Search for 6:", search(matrix, 6))
    print("Rotate clockwise:", rotate_clockwise(matrix))


if __name__ == "__main__":
    main()
