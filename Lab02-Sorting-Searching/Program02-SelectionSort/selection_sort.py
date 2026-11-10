"""Runnable Selection Sort demonstration for IC-307D Unit 2."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sorting_algorithms import selection_sort


def main():
    data = [34, -2, 7, 7, 19, 0, 12]
    print("Selection Sort")
    print("Input: ", data)
    print("Output:", selection_sort(data))
    print("Original unchanged:", data)


if __name__ == "__main__":
    main()
