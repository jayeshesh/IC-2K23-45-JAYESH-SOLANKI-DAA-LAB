"""One-dimensional array operations for IC-307D Unit 1.

Python lists are used to represent a dynamic array. Positions are zero-based.
"""


def insert_at(values: list, index: int, value) -> list:
    """Return a copy of values with value inserted at index."""
    if not 0 <= index <= len(values):
        raise IndexError("insert index must be between 0 and the array length")
    result = values.copy()
    result.insert(index, value)
    return result


def delete_at(values: list, index: int) -> tuple[list, object]:
    """Return (new_array, removed_value) after deleting index."""
    if not 0 <= index < len(values):
        raise IndexError("delete index is outside the array")
    result = values.copy()
    removed = result.pop(index)
    return result, removed


def search(values: list, target) -> int:
    """Return the first matching index, or -1 when target is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def rotate_right(values: list, positions: int = 1) -> list:
    """Return a copy rotated right by positions (negative values rotate left)."""
    if not values:
        return []
    shift = positions % len(values)
    if shift == 0:
        return values.copy()
    return values[-shift:] + values[:-shift]


def main() -> None:
    """Small interactive demonstration of 1D array operations."""
    data = [10, 20, 30, 40, 50]
    print("Initial array:", data)
    print("Insert 25 at index 2:", insert_at(data, 2, 25))
    changed, removed = delete_at(data, 1)
    print(f"Delete index 1 (removed {removed}):", changed)
    print("Search for 40:", search(data, 40))
    print("Rotate right by 2:", rotate_right(data, 2))


if __name__ == "__main__":
    main()
