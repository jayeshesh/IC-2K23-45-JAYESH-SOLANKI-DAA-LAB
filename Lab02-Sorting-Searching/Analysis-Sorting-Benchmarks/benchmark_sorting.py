"""Empirical sorting benchmark for IC-307D Unit 2.

Measures seven sorts on random, sorted, and reverse-sorted arrays. Writes CSV
and a Matplotlib graph. Run from the repository root.
"""
import argparse
import csv
from pathlib import Path
import random
import statistics
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sorting_algorithms import SORTS


def make_dataset(kind, size, rng):
    data = [rng.randint(-10000, 10000) for _ in range(size)]
    if kind == "sorted": return sorted(data)
    if kind == "reverse-sorted": return sorted(data, reverse=True)
    if kind == "random": return data
    raise ValueError(f"Unknown dataset: {kind}")


def benchmark(sizes=(100,  500, 1000), repeats=3, seed=42):
    if repeats < 1 or any(size < 0 for size in sizes):
        raise ValueError("repeats must be positive and sizes non-negative")
    rng, rows = random.Random(seed), []
    for size in sizes:
        for kind in ("random", "sorted", "reverse-sorted"):
            source = make_dataset(kind, size, rng)
            expected = sorted(source)
            for name, algorithm in SORTS.items():
                times = []
                for _ in range(repeats):
                    start = time.perf_counter()
                    result = algorithm(source)
                    times.append(time.perf_counter() - start)
                    if result != expected:
                        raise AssertionError(f"{name} returned an incorrect ordering")
                rows.append({
                    "input_type": kind, "size": size, "algorithm": name,
                    "median_seconds": statistics.median(times), "repeats": repeats,
                })
    return rows


def save_results(rows, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "sorting_benchmark.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "input_type", "size", "algorithm", "median_seconds", "repeats"
        ])
        writer.writeheader()
        writer.writerows(rows)
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise RuntimeError("Install Matplotlib with: pip install matplotlib") from exc
    graph_path = output_dir / "sorting_benchmark.png"
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    for axis, kind in zip(axes, ("random", "sorted", "reverse-sorted")):
        for name in SORTS:
            data = sorted(
                (row for row in rows if row["input_type"] == kind and row["algorithm"] == name),
                key=lambda row: row["size"],
            )
            axis.plot([r["size"] for r in data], [r["median_seconds"] for r in data],
                      marker="o", label=name)
        axis.set_title(kind.replace("-", " ").title())
        axis.set_xlabel("Input size (n)")
        axis.set_ylabel("Median time (seconds)")
        axis.grid(True, alpha=0.3)
    axes[-1].legend(fontsize=8)
    fig.suptitle("Sorting algorithm benchmark")
    fig.tight_layout()
    fig.savefig(graph_path, dpi=160)
    plt.close(fig)
    return csv_path, graph_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=[100, 500, 1000])
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--output", type=Path, default=Path(
        "Lab02-Sorting-Searching/Analysis-Sorting-Benchmarks/outputs"
    ))
    args = parser.parse_args()
    rows = benchmark(args.sizes, args.repeats)
    csv_path, graph_path = save_results(rows, args.output)
    print(f"Completed {len(rows)} verified measurements.")
    print(f"CSV: {csv_path}")
    print(f"Graph: {graph_path}")
    print("Timings depend on the machine and system load.")


if __name__ == "__main__":
    main()
