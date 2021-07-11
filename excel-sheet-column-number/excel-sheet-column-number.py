class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        ans = 0
        s = n-1
        for i in range(n):
            letter = ord(columnTitle[i]) - 64
            ans += ((26**s)*letter)
            s -= 1
        return ans