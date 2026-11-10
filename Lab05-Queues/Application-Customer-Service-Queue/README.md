# Customer Service Queue Simulation

**Language:** Python 3.10+  
**Run:** `python Lab05-Queues/Application-Customer-Service-Queue/customer_service_queue.py`

## 1. Problem statement
Simulate a real-time bank counter or customer service helpdesk queue where incoming customers are queued FIFO and served sequentially, tracking total estimated waiting times.

## 2. Approach
A FIFO customer queue processes arriving requests. Each customer carries an estimated service duration. Wait times and service dispatching are managed in $O(1)$ operations.

## 3. Complexity analysis
| Operation | Time | Auxiliary Space |
|---|---:|---:|
| Enqueue Customer | O(1) | O(1) |
| Serve Customer | O(1) | O(1) |
| Total Wait Time | O(n) | O(1) |

## 4. Sample I/O
```text
Waiting Customers: 3
Total Wait Time: 15 minutes
Served: Customer #101 (Alice)
Remaining Wait Time: 10 minutes
```

## 5. Real-life application
Hospital triage ticketing systems, bank teller lines, airline boarding queues, and call center IVR routing.
