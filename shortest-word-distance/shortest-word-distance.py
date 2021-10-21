class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        dist = len(wordsDict)
        for i, val in enumerate(wordsDict):
            if val == word1:
                i1 = i
            elif val == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                dist = min(dist, abs(i1-i2))
        return dist