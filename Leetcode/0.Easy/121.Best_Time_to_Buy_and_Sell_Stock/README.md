# [LeetCode 121] Best Time to Buy and Sell Stock

## [Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

---

## Intuition & Approach

### 1. Brute Force ($O(n^2)$) - **TLE (Time Limit Exceeded)**

* Compare every possible buying day with every possible selling day.
* Calculation: $Profit = prices[j] - prices[i]$ where $j > i$.
* **Result**: Too slow for large datasets ($n = 10^5$).

### 2. One Pass Optimized ($O(n)$) - **Accepted**

* **Concept**: We only need to track the **minimum price** seen so far and calculate the **potential profit** at each step.
* **Steps**:
1. Initialize `min_price` to infinity and `max_profit` to 0.
2. Iterate through the `prices` array:
* Update `min_price` if the current price is lower.
* Calculate profit (current price - `min_price`).
* Update `max_profit` if the current profit is higher than the previous maximum.


---

## Complexity Analysis

| Complexity | Analysis |
| --- | --- |
| **Time Complexity** | $O(n)$ — We iterate through the list exactly once. |
| **Space Complexity** | $O(1)$ — Only two variables are used regardless of input size. |

---
