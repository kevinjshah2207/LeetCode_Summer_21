class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        start, end = 0, 0
        for word in words:
            l = len(word)
            for i, letter in enumerate(text):
                if text[i:i+l] == word:
                    ans.append([i,i+l-1])
        ans = sorted(ans, key = lambda x:(x[0], x[1]))
        return ans