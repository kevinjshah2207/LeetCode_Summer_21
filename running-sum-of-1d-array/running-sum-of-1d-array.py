class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n, i = len(nums), 0
        s = 0
        while i < n:
            s += nums[i]
            nums[i] = s
            i += 1
        return nums
        