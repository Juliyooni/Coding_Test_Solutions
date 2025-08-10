# Pizza Slices Problem (3)

## Problem Description

At Meoseuk’s Pizza Shop, pizzas can be cut into any number of slices from **2 to 10**.  
Given:  
- `slice`: the number of slices a single pizza is cut into  
- `n`: the number of people eating the pizza  

Write a function `solution(slice, n)` that returns the **minimum number of whole pizzas** needed so that each of the `n` people can have **at least one slice**.

---

## Constraints
- 2 ≤ slice ≤ 10  
- 1 ≤ n ≤ 100

---

## Example

| slice | n  | result |
|-------|----|--------|
| 7     | 10 | 2      |
| 4     | 12 | 3      |

---

### Example Explanation

**Example #1**  
If each pizza has 7 slices and there are 10 people, at least **2 pizzas** are needed so that everyone gets at least one slice.

**Example #2**  
If each pizza has 4 slices and there are 12 people, at least **3 pizzas** are needed so that everyone gets at least one slice.

## Solution Idea

1. **Multiplication & Comparison Approach**  
    - To ensure that everyone gets **at least one slice**, the **total number of pizza slices** must be **greater than or equal to** the number of people.  

2. **Division & Ceiling Approach**  
   - Divide the number of people by the number of slices per pizza: `n / slice`.  
     This gives the **exact number of pizzas needed** as a floating-point value.