# Unit 2: Sorting Benchmark Results

**Course:** IC-307D | Data Structures and Algorithms Lab  
**Environment:** GitHub Actions `ubuntu-latest`, Python 3.12  
**Run:** [Successful benchmark and test workflow](https://github.com/jayeshesh/IC-2K23-45-JAYESH-SOLANKI-DAA-LAB/actions/runs/42788884457)  
**Data file:** [sorting_benchmark.csv](./outputs/sorting_benchmark.csv)

## Method

Seven algorithms (Bubble, Selection, Insertion, Merge, Quick, Heap, and Radix Sort) were compared on random, sorted, and reverse-sorted integer inputs at sizes 100, 500, and 1,000. Each timing is the median of three runs. The random data generator uses seed 42. Each output was checked against Python's built-in `sorted` before its measurement was recorded.

The recorded time is measured with `time.perf_counter()`. Values below are milliseconds, converted from the stored seconds in the CSV.

## Fastest and slowest at each size

| Input type | n | Fastest | Time (ms) | Slowest | Time (ms) |
|---|---:|---|---:|---|---:|
| Random | 100 | Radix | 0.0687 | Selection | 0.3568 |
| Random | 500 | Radix | 0.3138 | Bubble | 10.3691 |
| Random | 1,000 | Radix | 0.6976 | Bubble | 46.7333 |
| Sorted | 100 | Bubble | 0.0060 | Selection | 0.3490 |
| Sorted | 500 | Bubble | 0.0339 | Selection | 9.1601 |
| Sorted | 1,000 | Bubble | 0.0731 | Selection | 37.8462 |
| Reverse-sorted | 100 | Quick | 0.0578 | Bubble | 0.4215 |
| Reverse-sorted | 500 | Radix | 0.2830 | Bubble | 11.4572 |
| Reverse-sorted | 1,000 | Radix | 0.6352 | Bubble | 53.5745 |

## All algorithms at n = 1,000

| Algorithm | Random (ms) | Sorted (ms) | Reverse-sorted (ms) |
|---|---:|---:|---:|
| Bubble | 46.7333 | 0.0731 | 53.5745 |
| Selection | 37.3140 | 37.8462 | 37.5222 |
| Insertion | 17.2924 | 0.1057 | 31.0235 |
| Merge | 1.5924 | 1.1173 | 1.1838 |
| Quick | 1.2537 | 0.9915 | 0.9900 |
| Heap | 1.6854 | 1.7617 | 1.5082 |
| Radix | 0.6976 | 0.6412 | 0.6352 |

## Observations

1. The simple quadratic sorts become much slower as input size grows on random and reverse-sorted datasets. At n=1,000, Bubble Sort took about 46.7 ms on random data and 53.6 ms on reverse-sorted data, while Merge, Quick, and Heap stayed around 1–2 ms in this run.
2. Bubble Sort's early-exit optimization is visible on already sorted input: it took about 0.073 ms at n=1,000. Insertion Sort also performed well on sorted input at about 0.106 ms.
3. Selection Sort remained around 37–38 ms for all three n=1,000 input types, consistent with its quadratic comparison count.
4. Radix Sort was the fastest on random and reverse-sorted arrays in this run. This is an integer-only algorithm and its measured performance depends on the decimal digit range as well as n.
5. Quick Sort was also consistently fast in this run, but its general worst-case complexity remains O(n²); the timing result does not remove that theoretical case.

## Limitations

These timings are one benchmark run on a GitHub-hosted runner, not universal hardware-independent rankings. Small sub-millisecond measurements are especially sensitive to machine load, interpreter build, and timing noise. The results should be interpreted alongside the theoretical best/average/worst-case analysis in each program README.

The CI run also executed the Python unit tests on versions 3.10, 3.11, 3.12, and 3.13; all passed. The benchmark generated a three-panel Matplotlib graph, which is available with the CSV as an artifact in the linked workflow run.
