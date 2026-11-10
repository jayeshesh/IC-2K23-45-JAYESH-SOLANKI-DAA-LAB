# Capstone Project 3: E-Commerce Backend Simulator

**Language:** Python 3.10+  
**Run:** `python Capstone-Projects/Project03-ECommerce-Backend-Simulator/ecommerce_backend.py`

## 1. Problem statement
Construct an end-to-end e-commerce backend simulator combining:
1. **Product Catalog**: Binary Search Tree (BST) for fast $O(\log n)$ SKU lookups.
2. **Shopping Cart**: Stack for LIFO item addition with instant undo capability.
3. **Order Processing**: FIFO Queue dispatching orders sequentially to warehouses.
4. **Recommendation System**: Graph connecting co-purchased items for "Customers Who Bought This Also Bought..." recommendations.

## 2. Complexity analysis
| Subsystem | Operation | Time Complexity | Auxiliary Space |
|---|---|---:|---:|
| Catalog BST | Lookup / Insert | O(log n) | O(1) |
| Cart Stack | Add / Undo Item | O(1) | O(1) |
| Order Queue | Enqueue / Process | O(1) | O(1) |
| Rec Graph | Query Co-purchases | O(deg) | O(V + E) |

## 3. Sample I/O
```text
Undo last added item: Mechanical Keyboard
Order placed with ID: 1
Recommendations for buyers of 'Laptop': ['Wireless Mouse', 'Mechanical Keyboard']
Processing order FIFO: {'order_id': 1, 'customer': 'Jayesh Solanki', 'items': ['Laptop', 'Wireless Mouse'], 'total': 66200.0}
```

## 4. Learning outcomes
Coordinated multiple core data structures to drive a realistic distributed e-commerce workflow.
