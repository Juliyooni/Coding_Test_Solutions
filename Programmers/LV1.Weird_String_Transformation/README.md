# Weird String Transformation

## 📌 Problem Description  
You are given a string `s` consisting of one or more words.  
Each word is separated by one or more spaces.  
Transform the string so that in each word:  
- Characters at **even indices** (0-based within the word) are converted to uppercase.  
- Characters at **odd indices** are converted to lowercase.  

Return the transformed string.  

---

### **Constraints**  
- Transformation is applied **per word**, not across the entire string.  
- The first character of each word is considered index 0 (even).  

---

### **Example**  

| s                  | return             |
|--------------------|--------------------|
| `"try hello world"` | `"TrY HeLlO WoRlD"` |

---

### **Example Explanation**  
The string `"try hello world"` consists of three words:  
- `"try"` → `"TrY"`  
- `"hello"` → `"HeLlO"`  
- `"world"` → `"WoRlD"`  

Joining them back with spaces gives:  
```
"TrY HeLlO WoRlD"
```
