class Solution:
    def reverse(self, x: int) -> int:
        # Check if the number is negative and put a flag on it. Convert the int to str and 
        # then reverse the string and convert it back to int. Also check if the reversed number
        # is less than pow(2,31) and greater than pow(-2,31)
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
        