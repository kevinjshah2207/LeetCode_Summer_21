class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, val in enumerate(nums):
            nums[i] *= nums[i]
        nums.sort()
        return nums