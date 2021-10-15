class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key = {}
        for i, val in enumerate(keyboard):
            key[keyboard[i]] = i
        ans = 0
        for i, val in enumerate(word):
            if i == 0:
                ans += abs(0 - key[val])
                continue
            ans += abs(key[word[i-1]] - key[val])
        return ans