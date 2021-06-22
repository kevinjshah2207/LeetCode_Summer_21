class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            val = start + (2*i)
            nums.append(val)
            if i == 0:
                ans = val
                continue
            ans ^= val
        return ans
                
        