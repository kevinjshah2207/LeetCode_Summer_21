class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        out = 0
        odd_flag = False
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        odd = 0
        for i in d.values():
            if i % 2 == 0:
                out += i
            else:
                odd += (i-1)
                odd_flag = True
                
        if odd_flag:
            odd += 1
        return out + odd