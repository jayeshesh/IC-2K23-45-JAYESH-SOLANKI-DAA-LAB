# Sorting Benchmark Analysis

**Run from repository root:** `python Lab02-Sorting-Searching/Analysis-Sorting-Benchmarks/benchmark_sorting.py --sizes 100 500 1000 --repeats 3`

## Problem statement
Compare Bubble, Selection, Insertion, Merge, Quick, Heap, and Radix Sort empirically across sizes and random, sorted, and reverse-sorted inputs.

## Methodology
- Input types: random, sorted, reverse-sorted.
- Default sizes: 100, 500, 1000.
- Three repetitions per algorithm/input pair; report the median time.
- Fixed random seed (42) for repeatable datasets.
- Validate each output against Python's built-in `sorted` before recording the observation.
- Use `time.perf_counter()`. Timings depend on CPU, Python version, background load, and platform.

## Algorithm and pseudocode
```text
FOR each input size
  FOR each input type (random, sorted, reverse-sorted)
    generate source data and expected sorted output
    FOR each sorting algorithm
      repeat and measure elapsed time
      verify output
      record median elapsed time
WRITE CSV
PLOT median time against input size for each input type
```

## Complexity
There are A algorithms, D data types, S sizes, and R repeats. The benchmark runs A×D×S×R sort operations. Each run has the corresponding algorithm's own time complexity.

## Outputs
The script generates:
- `outputs/sorting_benchmark.csv`: measurements, input type, size, algorithm, median seconds, and repeat count.
- `outputs/sorting_benchmark.png`: three-panel Matplotlib comparison chart.

No timing values are pre-filled. Run the benchmark on the machine used for the lab and report those actual results.

## Analysis and reflection
Compare quadratic sorts with n log n sorts as n grows, note the effect of already sorted input, and compare Radix Sort's behaviour for integer data. Record actual observations and add a genuine screenshot of the generated chart.
