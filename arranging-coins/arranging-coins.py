class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, c = 1,0
        while n > 0:
            if n - i >= 0:
                n -= i
                c += 1
                i += 1
            else:
                return c
        return c