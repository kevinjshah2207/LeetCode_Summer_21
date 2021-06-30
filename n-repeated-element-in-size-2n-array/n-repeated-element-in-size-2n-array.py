class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return nums[i]
            else:
                d[nums[i]] = 1
        