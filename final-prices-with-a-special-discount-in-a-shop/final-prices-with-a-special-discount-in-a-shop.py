class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i in range(n - 1):
            j = i+1
            while j < n:
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
                else:
                    j += 1
        return prices