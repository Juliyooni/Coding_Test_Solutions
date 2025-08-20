# Three Musketeers

**Problem Link**
https://school.programmers.co.kr/learn/courses/30/lessons/131705

## 📌 Problem Description  
In a Korean middle school, each student is assigned an integer ID number.  
If the sum of the ID numbers of any three students equals `0`, those three students are called "Three Musketeers."  

For example:  
- Given five students with IDs `[-2, 3, 0, 2, -5]`:  
  - Students with IDs `(-2, 0, 2)` sum to 0 → they form a group.  
  - Students with IDs `(3, 2, -5)` also sum to 0 → another group.  
  - Thus, there are 2 possible groups of "Three Musketeers."  

Write a function `solution(number)` that returns the number of possible "Three Musketeers" groups.  

---

### **Constraints**  
- 3 ≤ length of `number` ≤ 13  
- -1000 ≤ `number[i]` ≤ 1000  
- Different students may have the same ID number.  

---

### **Example**  

| number                     | result |
|-----------------------------|--------|
| `[-2, 3, 0, 2, -5]`        | 2      |
| `[-3, -2, -1, 0, 1, 2, 3]` | 5      |
| `[-1, 1, -1, 1]`           | 0      |

---

### **Example Explanation**  

- **Example 1**: As described above, two groups can be formed.  
- **Example 2**: Possible groups are:  
  - (-3, 0, 3), (-2, 0, 2), (-1, 0, 1), (-2, -1, 3), (-3, 1, 2) → total 5.  
- **Example 3**: No three students sum to 0, so the result is 0.  
