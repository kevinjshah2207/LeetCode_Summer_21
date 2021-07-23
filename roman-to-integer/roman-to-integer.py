class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        prev = 0
        s1 = 0
        for i in s[::-1]:
            cur = d[i]
            if prev > cur:
                s1 -= cur
            else:
                s1 += cur
            prev = cur
        return s1