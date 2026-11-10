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
- Use `time.perf_counter()`; timings depend on CPU, Python version, background load, and platform.

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
- `outputs/sorting_benchmark.csv`: measured rows.
- `outputs/sorting_benchmark.png`: three-panel Matplotlib comparison chart.

A measured run is preserved in [benchmark-results.md](./benchmark-results.md) and [outputs/sorting_benchmark.csv](./outputs/sorting_benchmark.csv). The chart from the same CI run is available in the [GitHub Actions artifact](https://github.com/jayeshesh/IC-2K23-45-JAYESH-SOLANKI-DAA-LAB/actions/runs/42788884457).

## Analysis
See [benchmark-results.md](./benchmark-results.md) for the measured comparison and observations. Timings are hardware-specific; use the theoretical complexity sections in the algorithm READMEs as well.
