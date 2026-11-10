# Student Record Manager

**Run:** `python Lab02-Sorting-Searching/Application-Student-Record-Manager/student_record_manager.py`

## Problem statement
Sort and search student records by roll number, name, and marks using different Unit 2 algorithms and provide a comparative performance report.

## Approach
A Student record contains roll number, name, and marks. Sorting accepts any of the seven implemented sorting algorithms and a field-specific key. Search supports linear scan or binary search after sorting. Both strategies return all records for duplicate names or marks.

## Algorithm and pseudocode
```text
SORT(records, field, algorithm)
  choose key extractor for field
  return selected algorithm(records, key)

SEARCH(records, field, value, method)
  normalize value
  if method is linear: scan and collect every matching record
  otherwise: merge-sort by field; binary-search first matching key;
             collect adjacent records with equal key
  return matches
```

## Dry run
Marks [78, 91, 91] sorted ascending remain [78, 91, 91]. Searching for 91 returns both records with those marks.

## Complexity
For n records, sorting cost depends on the selected algorithm (see algorithm READMEs). Linear search is O(1) best and O(n) average/worst. Binary search including the required pre-sort is O(n log n) overall; the binary-search phase alone is O(log n). Returned result storage is O(k) for k matches; merge-sort workspace is O(n).

## Sample I/O
The demonstration dataset includes duplicate names and marks. Run the CLI, select a field, and try both linear and binary search. Record the actual output used in the lab report.

## Real-life application
Student information systems, examination offices, and academic result portals.

## Learning outcomes
Complete after testing the app.

## Tests and screenshots
Tests cover all three sort fields, duplicate matches, missing values, and invalid records. Capture actual terminal screenshots.
