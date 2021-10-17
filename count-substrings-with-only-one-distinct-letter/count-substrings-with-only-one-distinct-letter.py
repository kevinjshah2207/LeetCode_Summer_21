class Solution:
    def countLetters(self, s: str) -> int:
        total = left = 0
        for right in range(len(s)+1):
            if right == len(s) or s[left] != s[right]:
                l_s = right - left
                total += (1 + l_s) * l_s // 2
                left = right
        return total