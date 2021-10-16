class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = n
        l = len(str(n))
        ans = 0
        while s > 0:
            s, r = divmod(s, 10)
            ans += r**l
        return ans == n
            
        