# Unit 3 Reflection – Linked Lists

**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Course:** IC-307D | Data Structures and Algorithms Lab

## 1. What was learned
- Designing and manipulating node-based structures where memory allocation is dynamic and non-contiguous.
- Managing one-way, two-way, and cyclic pointer relationships without leaking or losing reference handles.
- Applying two-pointer merge techniques to polynomial arithmetic in $O(m + n)$ time.

## 2. Difficulties encountered
- Ensuring edge cases (empty list, single element list, operating at index 0 or tail) do not raise `AttributeError: 'NoneType' object has no attribute 'next'`.
- Maintaining the circular loop invariant in circular lists across in-place reversals.

## 3. Optimizations applied
- Maintained a dedicated `tail` pointer in `DoublyLinkedList` for instant $O(1)$ append and reverse operations.
- Avoided full array copies or linear shifts in the text editor buffer by leveraging pointer mutations.
