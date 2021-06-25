class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        l_sum = 0
        r_sum = 0
        l = 0
        r = len(nums) - 1
        # n = len(nums) - 1
        lsum = sum(nums)
        rsum = 0
        while lsum > rsum:
            lsum -= nums[r]
            rsum += nums[r]
            r -= 1
        return nums[:r+2]