# Average of Array Elements

**Problem Link**
https://school.programmers.co.kr/learn/courses/30/lessons/120817

## Problem Description

You are given an integer array `numbers`.  
Write a function `solution(numbers)` that returns the **average value** of the elements in `numbers`.

---

## Constraints
- `0 ≤ numbers[i] ≤ 1000`
- `1 ≤ numbers.length ≤ 100`
- The decimal part of the answer will always be either `.0` or `.5`.

---

## Example

| numbers | result |
|---------|--------|
| [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | 5.5 |
| [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] | 94.0 |

---

### Example Explanation

**Example #1**  
The average of the elements in `numbers` is:  
(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10) / 10 = 55 / 10 = 5.5

**Example #2**  
The average of the elements in `numbers` is:  
(89 + 90 + 91 + 92 + 93 + 94 + 95 + 96 + 97 + 98 + 99) / 11 = 1034 / 11 = 94.0

---

## Solution Idea

