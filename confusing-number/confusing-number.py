class Solution:
    def confusingNumber(self, n: int) -> bool:
        d = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        a = str(n)
        b = ''
        for i in a:
            if i not in d:
                return False
            else:
                b += d[i]
        b = b[::-1]
        if a == b:
            return False
        return True