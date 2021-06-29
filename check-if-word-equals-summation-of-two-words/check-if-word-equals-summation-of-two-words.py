class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
        n1 = len(firstWord) - 1
        val1 = 0
        for s in firstWord:
            val1 += (d[s]*(10**n1))
            n1 -= 1
        n2 = len(secondWord) - 1
        val2 = 0
        for s in secondWord:
            val2 += (d[s]*(10**n2))
            n2 -= 1
        n3 = len(targetWord) - 1
        val = 0
        for s in targetWord:
            val += (d[s]*(10**n3))
            n3 -= 1
        # print(val1,val2,val)
        if val1 + val2 == val:
            return True
        return False