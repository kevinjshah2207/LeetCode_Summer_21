class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fact(x: int):
            if (x==0 or x==1):
                return 1 
            else: 
                return x*fact(x-1)
        def comb(s1: int, s2: int):
            ans = fact(s1)/(fact(s2)*fact(s1-s2))
            return int(ans)
        m -= 1
        n -= 1
        return comb(m+n, m)