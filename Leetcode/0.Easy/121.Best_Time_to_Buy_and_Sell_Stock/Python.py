# Solution 1
# Brute Force (O(n^2)) - TLE (Time Limit Exceeded)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for buy_idx, buy_price in enumerate(prices) :
            for sell_idx in range(buy_idx + 1, len(prices)) :
                if prices[sell_idx] > buy_price :
                    if prices[sell_idx] - buy_price > max_profit:
                        max_profit = prices[sell_idx] - buy_price

        return max_profit






# Solution 2
# One Pass Optimized (O(n))
# runtime : 47ms, memory : 28.52MB


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i, price in enumerate(prices) :
            if price < min_price :
                min_price = price

            if price - min_price > max_profit :
                max_profit = price - min_price

        return max_profit




