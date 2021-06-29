class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # m1 = min(len(word1),len(word2))
        # out = []
        # for i in range(m1):
        #     out.append(word1[i])
        #     out.append(word2[i])
        # if len(word1) > m1:
        #     out.append(word1[m1:])
        # if len(word2) > m1:
        #     out.append(word2[m1:])
        # return ''.join(out)
        return ''.join(a+b for a,b in zip_longest(word1,word2, fillvalue=''))