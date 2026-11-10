# Search Engine Simulator

**Run:** `python Lab02-Sorting-Searching/Application-Search-Engine-Simulator/search_engine_simulator.py`

## Problem statement
Implement a dictionary with Binary Search and hashing. Handle hash collisions with Separate Chaining and Linear Probing.

## Approach
Keep three synchronized representations: sorted key/value pairs, a chaining hash table, and a linear-probing hash table. Keys are case-folded. Both hash tables resize above their selected load-factor thresholds. Linear Probing uses a tombstone marker so deletion does not break a later probe sequence.

## Algorithm and pseudocode
```text
LOOKUP(word, strategy)
  normalize word
  if binary: binary-search sorted entries
  if chaining: hash to bucket and scan bucket
  if linear probing: scan from hash slot until key, empty slot, or full cycle
  return meaning or NOT FOUND
```

## Dry run
At capacity 5, keys "a" and "f" have the same polynomial-hash initial bucket. Separate Chaining stores both in one bucket; Linear Probing puts the second at the next free slot.

## Complexity
Let n be number of terms, m table capacity, and k bucket length:
| Operation | Binary search index | Separate Chaining | Linear Probing |
|---|---:|---:|---:|
| Lookup average | O(log n) | O(1) expected | O(1) expected |
| Lookup worst | O(log n) | O(n) | O(n) |
| Insert average | O(n) due to sorted-list reordering | O(1) expected | O(1) expected |
| Insert worst | O(n) | O(n) | O(n) |
| Delete average | O(n) | O(1) expected | O(1) expected |
| Storage | O(n) | O(n+m) | O(m) |

Expected hash lookup depends on hash distribution and controlled load factor. Resizing is O(n).

## Sample I/O
The default dictionary contains array, graph, queue, stack, and tree. Look up "tree" using binary, chaining, and linear-probing strategies; each should return the same meaning.

## Real-life application
Glossaries, small search indexes, symbol lookup, and autocomplete dictionaries.

## Learning outcomes
Complete after running and reflecting on the three lookup strategies.

## Tests and screenshots
Tests cover lookup, updates, collisions, deletion, tombstones, and resizing. Capture a genuine CLI screenshot.
