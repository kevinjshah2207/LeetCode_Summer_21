class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max1 = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            max1 = max(max1, curr)
        return max1
                