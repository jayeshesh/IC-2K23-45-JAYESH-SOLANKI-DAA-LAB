# Doubly Linked List

**Language:** Python 3.10+  
**Run:** `python Lab03-Linked-Lists/Program02-Doubly-Linked-List/doubly_linked_list.py`

## 1. Problem statement
Implement a doubly linked list with bidirectional node linkage (`prev` and `next`), providing $O(1)$ operations at both ends (`head` and `tail`), arbitrary insertion and deletion, in-place reversal, and concatenation.

## 2. Approach
Each node holds `data`, `prev`, and `next` references. The list maintains both `head` and `tail` pointers. Deletion and insertion at extremities are strictly $O(1)$. In-place reversal is achieved efficiently by swapping the `prev` and `next` pointers of each node while traversing from head to tail and swapping the head and tail references.

## 3. Algorithm and Pseudocode
```text
REVERSE_DLL(head, tail):
  curr = head
  swap(head, tail)
  while curr != null:
    temp = curr.prev
    curr.prev = curr.next
    curr.next = temp
    curr = curr.prev // move using original next pointer
```

## 4. Complexity analysis
| Operation | Best | Average | Worst | Auxiliary space |
|---|---:|---:|---:|---:|
| Prepend / Append | O(1) | O(1) | O(1) | O(1) |
| Insert at position $k$ | O(1) | O(k) | O(n) | O(1) |
| Delete head / tail | O(1) | O(1) | O(1) | O(1) |
| Delete at position $k$ | O(1) | O(k) | O(n) | O(1) |
| Reverse | O(n) | O(n) | O(n) | O(1) |
| Concatenate | O(m + n) | O(m + n) | O(m + n) | O(m + n) |

## 5. Sample I/O
```text
Forward: ['Alpha', 'Beta', 'Gamma', 'Delta']
Backward: ['Delta', 'Gamma', 'Beta', 'Alpha']
Removed at index 1 (Beta): ['Alpha', 'Gamma', 'Delta']
After reverse: ['Delta', 'Gamma', 'Alpha']
```

## 6. Real-life application
Web browser backward/forward navigation history, LRU Cache internal structures, and text editor buffer line manipulation.

## 7. Learning outcomes
- Implemented bidirectional linked structures with synchronized two-way pointers.
- Verified constant-time operations at both ends using explicit tail pointers.
