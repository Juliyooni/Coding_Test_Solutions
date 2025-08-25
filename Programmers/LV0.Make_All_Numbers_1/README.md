# Make All Numbers 1

## 📌 Problem Description  
Given a list of integers `num_list`, you can perform the following operation until each element becomes `1`:  
- If the number is **even**, divide it by 2.  
- If the number is **odd**, subtract 1 first, then divide by 2.  

Count the total number of operations required to turn **all elements** in `num_list` into 1, and return this value.  

---

### **Constraints**  
- 3 ≤ length of `num_list` ≤ 15  
- 1 ≤ num_list[i] ≤ 30  

---

### **Example**  

| num_list            | result |
|---------------------|--------|
| [12, 4, 15, 1, 14]  | 11     |

---

### **Example Explanation**  
- For 12: 12 → 6 → 3 → 1 (**3 operations**)  
- For 4: 4 → 2 → 1 (**2 operations**)  
- For 15: 15 → 7 → 3 → 1 (**3 operations**)  
- For 1: already 1 (**0 operations**)  
- For 14: 14 → 7 → 3 → 1 (**3 operations**)  

Total operations = 3 + 2 + 3 + 0 + 3 = **11**.  
