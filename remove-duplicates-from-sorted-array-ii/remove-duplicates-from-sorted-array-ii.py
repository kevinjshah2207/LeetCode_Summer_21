class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        while x < len(nums):
            if x+2 < len(nums) and nums[x] == nums[x+1] == nums[x+2]:
                del(nums[x+2])
            else:
                x += 1
        return len(nums)