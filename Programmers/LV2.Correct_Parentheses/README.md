# Correct Parentheses

### **Problem Link**  
[Programmers - Correct Parentheses](https://school.programmers.co.kr/learn/courses/30/lessons/12909)  


## 📌 Problem Description  
A string of parentheses is considered **valid** if:  
- Every opening parenthesis `'('` has a corresponding closing parenthesis `')'`.  
- The pairs are correctly nested.  

Examples:  
- `"()()"` or `"(())()"` → valid  
- `")()("` or `"(()("` → invalid  

Given a string `s` consisting only of `'('` and `')'`, write a function `solution(s)` that returns:  
- `true` if the string is a valid parentheses string,  
- `false` otherwise.  

---

### **Constraints**  
- 1 ≤ length of `s` ≤ 100,000  
- `s` contains only `'('` and `')'`.  

---

### **Example**  

| s       | answer |
|---------|--------|
| `"()()"`  | true   |
| `"(())()"` | true   |
| `")()("`   | false  |
| `"(()("`   | false  |

---
