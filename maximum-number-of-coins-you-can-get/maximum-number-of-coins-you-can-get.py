class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        n = int(n - n/3)
        s = 0
        for i in range(1, n, 2):
            s += piles[i]
        return s