# Initialize a large value as min_price and 0 as max_profit. Loop through the list given. If the value is lesser than min_price, replace it. If difference
# prices[i] and min_price is greater than max_profit, replace the value. In the end, return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        min_price = 100000
        max_profit = 0
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
        
