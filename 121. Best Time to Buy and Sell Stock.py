class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        max_profit = 0
        lowest_price = prices[0]
        for price in prices[1:]:
            profit = price - lowest_price
            if profit > max_profit:
                max_profit = profit
            elif price < lowest_price:
                lowest_price = price
        return max_profit