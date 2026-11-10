"""Menu-driven matrix calculator for IC-307D Unit 1."""

from typing import Sequence


def _shape(matrix: Sequence[Sequence[float]]) -> tuple[int, int]:
    if not matrix:
        return 0, 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular")
    return len(matrix), width


def add(first: list[list[float]], second: list[list[float]]) -> list[list[float]]:
    shape_a, shape_b = _shape(first), _shape(second)
    if shape_a != shape_b:
        raise ValueError("matrix addition requires equal dimensions")
    return [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(first, second)]


def multiply(first: list[list[float]], second: list[list[float]]) -> list[list[float]]:
    rows_a, cols_a = _shape(first)
    rows_b, cols_b = _shape(second)
    if cols_a != rows_b:
        raise ValueError("matrix multiplication requires columns(A) == rows(B)")
    return [
        [sum(first[i][k] * second[k][j] for k in range(cols_a)) for j in range(cols_b)]
        for i in range(rows_a)
    ]


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    _shape(matrix)
    return [list(row) for row in zip(*matrix)] if matrix else []


def determinant(matrix: list[list[float]]) -> float:
    """Compute determinant recursively; intended for small square matrices."""
    rows, cols = _shape(matrix)
    if rows != cols or rows == 0:
        raise ValueError("determinant requires a non-empty square matrix")
    if rows == 1:
        return matrix[0][0]
    if rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    total = 0
    for column, value in enumerate(matrix[0]):
        minor = [
            [matrix[r][c] for c in range(cols) if c != column]
            for r in range(1, rows)
        ]
        total += ((-1) ** column) * value * determinant(minor)
    return total


def _read_matrix(input_fn=input, output_fn=print) -> list[list[float]]:
    while True:
        try:
            rows = int(input_fn("Number of rows: "))
            cols = int(input_fn("Number of columns: "))
            if rows <= 0 or cols <= 0:
                raise ValueError("dimensions must be positive")
            matrix = []
            for index in range(rows):
                values = [float(x) for x in input_fn(
                    f"Enter {cols} values for row {index + 1}, separated by spaces: "
                ).split()]
                if len(values) != cols:
                    raise ValueError(f"row must contain exactly {cols} values")
                matrix.append(values)
            return matrix
        except ValueError as exc:
            output_fn(f"Invalid matrix input: {exc}. Please try again.")


def main() -> None:
    """Run the menu-driven calculator until the user chooses Exit."""
    operations = {
        "1": "Addition",
        "2": "Multiplication",
        "3": "Transpose",
        "4": "Determinant",
    }
    while True:
        print("\nMATRIX CALCULATOR")
        print("1. Addition\n2. Multiplication\n3. Transpose\n4. Determinant\n0. Exit")
        choice = input("Choose an operation: ").strip()
        if choice == "0":
            print("Exiting matrix calculator.")
            return
        if choice not in operations:
            print("Invalid choice. Select 0, 1, 2, 3, or 4.")
            continue
        try:
            first = _read_matrix()
            if choice in {"1", "2"}:
                second = _read_matrix()
                result = add(first, second) if choice == "1" else multiply(first, second)
            elif choice == "3":
                result = transpose(first)
            else:
                result = determinant(first)
            print(f"{operations[choice]} result:")
            print(result)
        except (ValueError, TypeError) as exc:
            print(f"Cannot perform operation: {exc}")


if __name__ == "__main__":
    main()
