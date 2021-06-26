class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == "L":
                l += 1
            else:
                r += 1
            if l == r and l > 0:
                count += 1
                l, r = 0, 0
        return count