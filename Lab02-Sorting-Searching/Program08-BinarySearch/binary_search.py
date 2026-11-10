"""Runnable Binary Search demonstration for IC-307D Unit 2."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sorting_algorithms import binary_search


def main():
    data = [2, 4, 7, 7, 9, 13, 18]
    print("Sorted input:", data)
    print("First index of 7:", binary_search(data, 7))
    print("Absent target 10:", binary_search(data, 10))


if __name__ == "__main__":
    main()
