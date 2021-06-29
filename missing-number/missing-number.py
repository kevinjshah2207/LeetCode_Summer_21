class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = (n+1)*(n)//2
        return sum1 - sum(nums)