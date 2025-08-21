# Memory Score

**Problem Link**
https://school.programmers.co.kr/learn/courses/30/lessons/176963

## 📌 Problem Description  
Lu wants to calculate a **memory score** for each photo.  
- Each person has a **yearning score**.  
- The memory score of a photo is the **sum of the yearning scores** of all people appearing in the photo.  
- If a person in the photo does not have a yearning score, they contribute 0.  

Write a function `solution(name, yearning, photo)` that returns an array of memory scores, in the same order as the given `photo` list.  

---

### **Constraints**  
- 3 ≤ `len(name)` = `len(yearning)` ≤ 100  
- 3 ≤ length of each `name[i]` ≤ 7  
- Each `name[i]` consists of lowercase English letters.  
- `name` contains no duplicates.  
- 1 ≤ `yearning[i]` ≤ 100  
- 3 ≤ `len(photo)` ≤ 100  
- 1 ≤ `len(photo[i])` ≤ 100  
- 3 ≤ length of each `photo[i][j]` ≤ 7  
- Each `photo[i][j]` consists of lowercase English letters.  
- Each `photo[i]` contains no duplicate names.  

---

### **Example**  

| name                           | yearning         | photo                                                                 | result      |
|--------------------------------|------------------|----------------------------------------------------------------------|-------------|
| ["may", "kein", "kain", "radi"] | [5, 10, 1, 3]    | [["may","kein","kain","radi"],["may","kein","brin","deny"],["kon","kain","may","coni"]] | [19, 15, 6] |
| ["kali","mari","don"]          | [11, 1, 55]      | [["kali","mari","don"],["pony","tom","teddy"],["con","mona","don"]]  | [67, 0, 55] |
| ["may","kein","kain","radi"]   | [5, 10, 1, 3]    | [["may"],["kein","deny","may"],["kon","coni"]]                       | [5, 15, 0]  |

---

### **Example Explanation**  

- **Example 1**  
  - Photo 1: may(5) + kein(10) + kain(1) + radi(3) = 19  
  - Photo 2: may(5) + kein(10) = 15  
  - Photo 3: kain(1) + may(5) = 6  
  → `[19, 15, 6]`  

- **Example 2**  
  - Photo 1: kali(11) + mari(1) + don(55) = 67  
  - Photo 2: no matching names → 0  
  - Photo 3: don(55) → 55  
  → `[67, 0, 55]`  

- **Example 3**  
  - Photo 1: may(5) = 5  
  - Photo 2: kein(10) + may(5) = 15  
  - Photo 3: no matching names → 0  
  → `[5, 15, 0]`  