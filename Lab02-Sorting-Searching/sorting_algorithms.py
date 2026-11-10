"""Sorting/searching algorithms for IC-307D Unit 2.

Sorts return a new list and accept an optional key. The input is not mutated.
"""
from collections.abc import Callable, Sequence
from typing import Any

Key = Callable[[Any], Any]


def _key_fn(key):
    return key if key is not None else (lambda value: value)


def bubble_sort(values: Sequence, key: Key | None = None) -> list:
    result, get = list(values), _key_fn(key)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if get(result[i]) > get(result[i + 1]):
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(values: Sequence, key: Key | None = None) -> list:
    result, get = list(values), _key_fn(key)
    for start in range(len(result) - 1):
        smallest = min(range(start, len(result)), key=lambda i: get(result[i]))
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result


def insertion_sort(values: Sequence, key: Key | None = None) -> list:
    result, get = list(values), _key_fn(key)
    for i in range(1, len(result)):
        item, item_key, j = result[i], get(result[i]), i - 1
        while j >= 0 and get(result[j]) > item_key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = item
    return result


def merge_sort(values: Sequence, key: Key | None = None) -> list:
    get = _key_fn(key)

    def sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left, right = sort(items[:mid]), sort(items[mid:])
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if get(left[i]) <= get(right[j]):
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        return merged + left[i:] + right[j:]

    return sort(list(values))


def quick_sort(values: Sequence, key: Key | None = None) -> list:
    """Iterative three-way Quick Sort. Not stable; worst-case O(n^2)."""
    result, get = list(values), _key_fn(key)
    stack = [(0, len(result) - 1)] if result else []
    while stack:
        low, high = stack.pop()
        while low < high:
            pivot = get(result[(low + high) // 2])
            lt = scan = low
            gt = high
            while scan <= gt:
                current = get(result[scan])
                if current < pivot:
                    result[lt], result[scan] = result[scan], result[lt]
                    lt += 1; scan += 1
                elif current > pivot:
                    result[scan], result[gt] = result[gt], result[scan]
                    gt -= 1
                else:
                    scan += 1
            left, right = (low, lt - 1), (gt + 1, high)
            left_size = left[1] - left[0] + 1
            right_size = right[1] - right[0] + 1
            # Continue with the smaller side and defer the larger side.
            if left_size < right_size:
                if right_size > 1: stack.append(right)
                low, high = left
            else:
                if left_size > 1: stack.append(left)
                low, high = right
    return result


def heap_sort(values: Sequence, key: Key | None = None) -> list:
    result, get, n = list(values), _key_fn(key), len(values)

    def sift(root, end):
        while (child := 2 * root + 1) <= end:
            greater = child
            if child + 1 <= end and get(result[child + 1]) > get(result[child]):
                greater = child + 1
            if get(result[root]) >= get(result[greater]):
                return
            result[root], result[greater] = result[greater], result[root]
            root = greater

    for root in range(n // 2 - 1, -1, -1):
        sift(root, n - 1)
    for end in range(n - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        sift(0, end - 1)
    return result


def _radix_nonnegative(values: list[int]) -> list[int]:
    result = values[:]
    if not result: return result
    exp, maximum = 1, max(result)
    while maximum // exp:
        count, output = [0] * 10, [0] * len(result)
        for value in result: count[(value // exp) % 10] += 1
        for digit in range(1, 10): count[digit] += count[digit - 1]
        for value in reversed(result):
            digit = (value // exp) % 10
            count[digit] -= 1
            output[count[digit]] = value
        result, exp = output, exp * 10
    return result


def radix_sort(values: Sequence[int]) -> list[int]:
    """Stable LSD decimal Radix Sort; supports positive, zero, and negatives."""
    if any(not isinstance(v, int) or isinstance(v, bool) for v in values):
        raise TypeError("Radix Sort accepts integers only")
    negative = [-v for v in values if v < 0]
    nonnegative = [v for v in values if v >= 0]
    return [-v for v in reversed(_radix_nonnegative(negative))] + _radix_nonnegative(nonnegative)


def binary_search(values: Sequence, target, key: Key | None = None) -> int:
    """Return the first matching index in an ascending sequence, or -1."""
    get, low, high = _key_fn(key), 0, len(values)
    while low < high:
        mid = (low + high) // 2
        if get(values[mid]) < target: low = mid + 1
        else: high = mid
    return low if low < len(values) and get(values[low]) == target else -1


SORTS = {
    "bubble": bubble_sort, "selection": selection_sort, "insertion": insertion_sort,
    "merge": merge_sort, "quick": quick_sort, "heap": heap_sort, "radix": radix_sort,
}
