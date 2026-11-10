"""Sparse matrices stored in triple format for IC-307D Unit 1.

Format: [(row_count, column_count, nonzero_count), (row, column, value), ...]
Coordinates are zero-based and entries are stored in row-major order.
"""


def to_triples(matrix: list[list]) -> list[tuple[int, int, object]]:
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of rows")
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    if any(len(row) != cols for row in matrix):
        raise ValueError("matrix must be rectangular")
    entries = [
        (r, c, value)
        for r, row in enumerate(matrix)
        for c, value in enumerate(row)
        if value != 0
    ]
    return [(rows, cols, len(entries)), *entries]


def from_triples(triples: list[tuple]) -> list[list]:
    if not triples or len(triples[0]) != 3:
        raise ValueError("triple format must start with (rows, cols, nonzero_count)")
    rows, cols, count = triples[0]
    if not all(isinstance(n, int) and n >= 0 for n in (rows, cols, count)):
        raise ValueError("matrix dimensions and entry count must be non-negative integers")
    if len(triples) - 1 != count:
        raise ValueError("declared nonzero count does not match supplied entries")
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    seen = set()
    for entry in triples[1:]:
        if len(entry) != 3:
            raise ValueError("each matrix entry must be (row, column, value)")
        r, c, value = entry
        if not isinstance(r, int) or not isinstance(c, int) or not (0 <= r < rows and 0 <= c < cols):
            raise ValueError("triple coordinate is outside the matrix")
        if value == 0:
            raise ValueError("triple format must not store zero values")
        if (r, c) in seen:
            raise ValueError("duplicate coordinate in triple format")
        seen.add((r, c))
        matrix[r][c] = value
    return matrix


def transpose(triples: list[tuple]) -> list[tuple]:
    rows, cols, count = triples[0]
    entries = sorted(
        ((c, r, value) for r, c, value in triples[1:]),
        key=lambda item: (item[0], item[1]),
    )
    return [(cols, rows, count), *entries]


def add(first: list[tuple], second: list[tuple]) -> list[tuple]:
    rows_a, cols_a, _ = first[0]
    rows_b, cols_b, _ = second[0]
    if (rows_a, cols_a) != (rows_b, cols_b):
        raise ValueError("sparse matrices must have identical dimensions for addition")
    values = {}
    for r, c, value in first[1:]:
        values[(r, c)] = values.get((r, c), 0) + value
    for r, c, value in second[1:]:
        values[(r, c)] = values.get((r, c), 0) + value
    entries = [(r, c, v) for (r, c), v in sorted(values.items()) if v != 0]
    return [(rows_a, cols_a, len(entries)), *entries]


def multiply(first: list[tuple], second: list[tuple]) -> list[tuple]:
    rows_a, cols_a, _ = first[0]
    rows_b, cols_b, _ = second[0]
    if cols_a != rows_b:
        raise ValueError("matrix dimensions are incompatible for multiplication")
    a_rows = {}
    b_rows = {}
    for r, c, value in first[1:]:
        a_rows.setdefault(r, []).append((c, value))
    for r, c, value in second[1:]:
        b_rows.setdefault(r, []).append((c, value))
    result = {}
    for r, a_entries in a_rows.items():
        for k, a_value in a_entries:
            for c, b_value in b_rows.get(k, []):
                result[(r, c)] = result.get((r, c), 0) + a_value * b_value
    entries = [(r, c, v) for (r, c), v in sorted(result.items()) if v != 0]
    return [(rows_a, cols_b, len(entries)), *entries]


def storage_counts(triples: list[tuple]) -> dict[str, int | float]:
    """Compare stored scalar values in dense and triple representations."""
    rows, cols, nonzero = triples[0]
    dense = rows * cols
    sparse = 3 * nonzero + 3  # include the (rows, cols, count) header
    return {
        "dense_values": dense,
        "triple_values_including_header": sparse,
        "savings_ratio": (1 - sparse / dense) if dense else 0.0,
    }


def main() -> None:
    matrix = [[0, 0, 5], [0, 0, 0], [2, 0, 0]]
    triples = to_triples(matrix)
    print("Triple representation:", triples)
    print("Reconstructed matrix:", from_triples(triples))
    print("Transpose:", transpose(triples))
    print("Storage comparison:", storage_counts(triples))


if __name__ == "__main__":
    main()
