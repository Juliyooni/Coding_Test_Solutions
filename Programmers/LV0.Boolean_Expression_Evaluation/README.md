# Boolean Expression Evaluation

**Problem Link**
https://school.programmers.co.kr/learn/courses/30/lessons/181917

## 📌 Problem Description  
You are given four boolean variables: `x1`, `x2`, `x3`, `x4`.  
Write a function `solution(x1, x2, x3, x4)` that returns the boolean result of the following expression:

```
(x1 ∨ x2) ∧ (x3 ∨ x4)
```

Here:  
- `∨` denotes **logical OR**  
- `∧` denotes **logical AND**

---

### **Input / Output Example**

| x1    | x2    | x3    | x4    | result |
|-------|-------|-------|-------|--------|
| false | true  | true  | true  | true   |
| true  | false | false | false | false  |

---

### **Example Explanation**

- **Example 1**  
  ```
  (x1 ∨ x2) ∧ (x3 ∨ x4)
  = (F ∨ T) ∧ (T ∨ T)
  = T ∧ T
  = T
  ```
  → return `true`

- **Example 2**  
  ```
  (x1 ∨ x2) ∧ (x3 ∨ x4)
  = (T ∨ F) ∧ (F ∨ F)
  = T ∧ F
  = F
  ```
  → return `false`

---

### **Truth Tables**

**OR (∨)**  
| x | y | x ∨ y |
|---|---|-------|
| T | T | T     |
| T | F | T     |
| F | T | T     |
| F | F | F     |

**AND (∧)**  
| x | y | x ∧ y |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |
