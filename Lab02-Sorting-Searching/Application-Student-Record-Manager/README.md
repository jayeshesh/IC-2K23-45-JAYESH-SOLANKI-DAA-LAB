# Student Record Manager

**Run:** `python Lab02-Sorting-Searching/Application-Student-Record-Manager/student_record_manager.py`

## Problem statement
Sort and search student records by roll number, name, and marks using Unit 2 algorithms.

## Approach
A Student record stores roll number, name, and marks. Sorting supports all seven algorithms. Radix Sort requires integer keys, so it is supported for whole-number marks only; names and alphanumeric roll numbers use comparison sorts. Searching supports linear scan or binary search after sorting. Both strategies return all matching records, including duplicates.

## Algorithm and pseudocode
```text
SORT(records, field, algorithm)
  choose field key
  if Radix: require whole-number marks and sort integer marks
  otherwise: run selected sort with the field key
  return sorted records

SEARCH(records, field, value, method)
  if linear: scan and collect matches
  otherwise: merge-sort by field, binary-search first match,
             collect adjacent records with equal keys
```

## Dry run
Marks [78, 91, 91] sorted with Radix Sort remain [78, 91, 91]. Searching for 91 returns both matching records.

## Complexity
For n records, sorting time depends on the selected algorithm (see algorithm READMEs). Linear search is O(1) best and O(n) average/worst. Binary search including pre-sorting is O(n log n) overall; the search phase alone is O(log n).

## Sample I/O
The demonstration data contains duplicate names and marks. Try Radix Sort for marks and Merge Sort for names. Record actual output from execution.

## Real-life application
Student information systems, examination offices, and academic result portals.

## Learning outcomes
Complete after testing the application.

## Tests and screenshots
Tests cover field sorting, Radix on whole-number marks, duplicate matches, missing values, and invalid input. Capture genuine terminal screenshots.
