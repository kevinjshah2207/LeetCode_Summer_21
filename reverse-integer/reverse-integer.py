class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        flag = False
        if x < 0:
            flag = True
            x *= -1
        if x > (2**31)-1:
            return 0
        s += str(x)
        s = s[::-1]
        if int(s) > (2**31)-1:
            return 0
        if flag:
            return int(s)*-1
        return int(s)
        