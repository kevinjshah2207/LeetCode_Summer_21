class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = list(str(n))
        i = len(a) - 1
        while i > 0 and a[i] <= a[i-1]:
            i -= 1
        if i == 0:
            return -1
        j = i
        while j+1 < len(a) and a[j+1] > a[i-1]:
            j += 1
        a[j], a[i-1] = a[i-1], a[j]
        a[i:] = a[i:][::-1]
        ans = int("".join(a))
        if ans > ((2**31)-1):
            return -1
        return ans