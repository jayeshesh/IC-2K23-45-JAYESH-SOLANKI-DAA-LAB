"""OS Process Scheduling Simulation (Round Robin & Priority).

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1) Application
"""

from typing import List, Tuple


class Process:
    def __init__(self, pid: str, burst_time: int, priority: int = 1) -> None:
        self.pid: str = pid
        self.burst_time: int = burst_time
        self.remaining_time: int = burst_time
        self.priority: int = priority


def simulate_round_robin(processes: List[Process], quantum: int = 2) -> List[Tuple[str, int, int]]:
    """Simulate Round-Robin CPU scheduling with given time quantum using a circular queue discipline."""
    queue = [p for p in processes]
    timeline = []  # (pid, start_time, end_time)
    current_time = 0

    while queue:
        p = queue.pop(0)
        time_slice = min(quantum, p.remaining_time)
        start = current_time
        current_time += time_slice
        p.remaining_time -= time_slice
        timeline.append((p.pid, start, current_time))
        if p.remaining_time > 0:
            queue.append(p)

    return timeline


def demo() -> None:
    procs = [
        Process("P1", burst_time=5),
        Process("P2", burst_time=3),
        Process("P3", burst_time=1),
    ]
    print("Round Robin Simulation (Quantum = 2):")
    timeline = simulate_round_robin(procs, quantum=2)
    for pid, start, end in timeline:
        print(f"Time {start:2d} -> {end:2d} : Executing {pid}")


if __name__ == "__main__":
    demo()
