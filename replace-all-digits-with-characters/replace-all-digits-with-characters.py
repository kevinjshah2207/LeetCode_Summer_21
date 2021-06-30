class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int) -> str:
            # print(c,x)
            i = int(ord(c))
            i += x
            return chr(i)
        i = 1
        # out = ''
        while i < len(s):
            # print(type(s[i]))
            # c = int(ord(s[i]))
            x = int(s[i])
            c = shift(s[i-1], x)
            s = s.replace(s[i], c, 1)
            i += 2
        return s
            