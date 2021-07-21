class Solution:
    def reverseWords(self, s: str) -> str:
        # First we split the string into different words using the delimiter " ". Then we simply
        # reverse each word using [::-1] and then join it back again to give us the answer
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return " ".join(s)