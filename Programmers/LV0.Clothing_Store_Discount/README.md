# Clothing Store Discount

## 📌 Problem Description  
In a clothing store, discounts are applied as follows:  
- 5% discount for purchases of **100,000 won or more**  
- 10% discount for purchases of **300,000 won or more**  
- 20% discount for purchases of **500,000 won or more**  

Given the purchase price `price`, complete the function `solution` to return the final amount to be paid after applying the discount.  

---

### **Constraints**  
- 10 ≤ price ≤ 1,000,000  
- `price` is always a multiple of 10 (the last digit is 0).  
- The result should be returned as an integer, discarding any decimal part.  

---

### **Example**  

| price   | result  |
|---------|---------|
| 150000  | 142500  |
| 580000  | 464000  |

---

### **Example Explanation**  

- **Example 1**:  
  150,000 won → 5% discount → 142,500 won  

- **Example 2**:  
  580,000 won → 20% discount → 464,000 won  
