# Unit 2: Sorting & Searching Algorithms

**Course:** IC-307D | Data Structures and Algorithms Lab  
**Course Outcome:** CO2

## Basic requirements
Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Radix Sort, Binary Search.

## Application / analysis requirements
Compare all sorting algorithms by empirical timing across input sizes and random, sorted, and reverse-sorted data. Generate graphs using Matplotlib via Python or export data. Student Record Manager: sort/search by roll number, name, and marks. Search Engine Simulator: dictionary using binary search + hashing; handle collisions using Separate Chaining + Linear Probing.

## Programs
- [Bubble Sort](./Program01-BubbleSort/README.md)
- [Selection Sort](./Program02-SelectionSort/README.md)
- [Insertion Sort](./Program03-InsertionSort/README.md)
- [Merge Sort](./Program04-MergeSort/README.md)
- [Quick Sort](./Program05-QuickSort/README.md)
- [Heap Sort](./Program06-HeapSort/README.md)
- [Radix Sort](./Program07-RadixSort/README.md)
- [Binary Search](./Program08-BinarySearch/README.md)
- [Sorting Benchmark Analysis](./Analysis-Sorting-Benchmarks/README.md)
- [Student Record Manager](./Application-Student-Record-Manager/README.md)
- [Search Engine Simulator](./Application-Search-Engine-Simulator/README.md)

## Validation
- [x] Implementations added
- [x] Full test suite passing in GitHub Actions on Python 3.10, 3.11, 3.12, and 3.13
- [ ] Benchmark CSV/graph reviewed and observations written
- [ ] Genuine execution screenshots added
- [ ] Unit reflection completed

The benchmark workflow generates a CSV and a three-panel graph as a downloadable GitHub Actions artifact. Timings are machine-specific. See [Sorting Benchmark Analysis](./Analysis-Sorting-Benchmarks/README.md).

See [reflection.md](./reflection.md).
