"""Customer Service Queue Simulation.

Course: IC-307D Data Structures & Algorithms LAB
Student: Jayesh Solanki | Roll No: IC-2K23-45
Unit 5: Queues (CO1) Application
"""

from typing import List, Optional


class Customer:
    def __init__(self, customer_id: int, name: str, service_time: int) -> None:
        self.customer_id: int = customer_id
        self.name: str = name
        self.service_time: int = service_time


class CustomerServiceQueue:
    """Simulates a multi-counter or single-counter bank/teller customer service queue."""

    def __init__(self) -> None:
        self._queue: List[Customer] = []

    def enqueue_customer(self, customer: Customer) -> None:
        self._queue.append(customer)

    def serve_next_customer(self) -> Optional[Customer]:
        if not self._queue:
            return None
        return self._queue.pop(0)

    def waiting_count(self) -> int:
        return len(self._queue)

    def total_estimated_wait_time(self) -> int:
        return sum(c.service_time for c in self._queue)


def demo() -> None:
    csq = CustomerServiceQueue()
    csq.enqueue_customer(Customer(101, "Alice", 5))
    csq.enqueue_customer(Customer(102, "Bob", 3))
    csq.enqueue_customer(Customer(103, "Charlie", 7))

    print(f"Waiting Customers: {csq.waiting_count()}")
    print(f"Total Wait Time: {csq.total_estimated_wait_time()} minutes")

    served = csq.serve_next_customer()
    print(f"Served: Customer #{served.customer_id} ({served.name})")  # type: ignore
    print(f"Remaining Wait Time: {csq.total_estimated_wait_time()} minutes")


if __name__ == "__main__":
    demo()
