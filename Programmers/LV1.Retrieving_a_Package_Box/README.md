# Retrieving a Package Box

**Problem Link**  
[https://school.programmers.co.kr/learn/courses/30/lessons/389478]<!-- Replace with actual problem link if available -->

---

## Problem Description

There are `n` boxes in a warehouse, numbered from **1** to **n**.  
You arrange the boxes in the following pattern:

1. Start from the bottom row, placing boxes from left to right in ascending order starting from 1.
2. When you have placed `w` boxes in a row, move up one row and place boxes from right to left.
3. Repeat this zigzag pattern (left→right, then right→left) for each row until all `n` boxes are placed.
4. Each row contains exactly `w` boxes, except possibly the last row.

**Example:**  
If `w = 6` and `n = 22`, the arrangement looks like this:

![Example 1 Layout](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e06b4c0d-0ce6-4a2d-8ad4-ba20f9398145/ex1-1.png)


(Starting from the bottom row, left to right, then the next row right to left, and so on.)

When a customer requests box `num`, you can only retrieve it by first removing all boxes **on top of it**. This means you must remove the requested box and any boxes stacked above it in the same vertical position.

Given integers:
- `n` — total number of boxes
- `w` — number of boxes per row
- `num` — the number of the requested box

Return the **total number of boxes** that must be removed to retrieve box `num` (including the box itself).

---

## Constraints
- `2 ≤ n ≤ 100`
- `1 ≤ w ≤ 10`
- `1 ≤ num ≤ n`

---

## Examples

| n   | w  | num | result |
|-----|----|-----|--------|
| 22  | 6  | 8   | 3      |
| 13  | 3  | 6   | 4      |

---

### Example Explanation

**Example #1**  
With `n = 22`, `w = 6`, and `num = 8`:

![Example 1 Layout](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e06b4c0d-0ce6-4a2d-8ad4-ba20f9398145/ex1-1.png)

To get box 8:
- Remove box 20 (above it)
- Remove box 17 (above it)
- Remove box 8 itself  
→ Total = **3 boxes**

---

**Example #2**  
With `n = 13`, `w = 3`, and `num = 6`:

![Example 2 Layout](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/cb4cf30d-2313-40ff-8366-86841f603ae6/ex2-1.png)

To get box 6:
- Remove box 13
- Remove box 12
- Remove box 7
- Remove box 6 itself  
→ Total = **4 boxes**

---

## Approach
1. Map each box number to its `(row, col)` position based on the zigzag stacking order (left→right, then right→left).
2. Find the target box’s coordinates.
3. Check how many rows above (including its own row) have a box in the same column.
4. Return that count as the total boxes to remove.
