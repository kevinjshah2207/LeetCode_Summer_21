class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        i = 0
        n = len(s)
        while(k>0 and i<n):
            if s[i] == " ":
                k -= 1
                i += 1
            else:
                i += 1
        if i >= n:
            return s
        else:
            return s[:i-1]
            