# Unit 4 Reflection – Stacks

**Student:** Jayesh Solanki (Roll No: IC-2K23-45)  
**Course:** IC-307D | Data Structures and Algorithms Lab

## 1. What was learned
- Designing static versus dynamic memory layouts for LIFO abstractions.
- Applying Dijkstra's Shunting-Yard algorithm to enforce operator precedence, associativity rules, and parentheses scoping.
- Structuring reversible software actions via the GoF Command Pattern using dual stacks.

## 2. Difficulties encountered
- Managing right-associative exponentiation (`^`) correctly in both infix-to-postfix and infix-to-prefix conversions.
- Distinguishing prefix vs postfix operand evaluation ordering when popping $a$ and $b$ from operand stacks.

## 3. Optimizations applied
- Handled all operator lookups and precedence comparisons via $O(1)$ dictionary lookups.
- Pre-allocated array memory in static stack to avoid dynamic array resizing amortized costs.
