class Solution:
    def minOperations(self, nums: List[int]) -> int:
        out = 0
        if len(nums) == 1:
            return out
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                out += (nums[i-1] - nums[i] + 1)
                nums[i] = nums[i-1] + 1
            elif nums[i] == nums[i-1]:
                out += 1
                nums[i] += 1
        return out