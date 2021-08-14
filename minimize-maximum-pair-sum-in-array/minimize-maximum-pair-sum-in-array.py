class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        max1 = 0
        while l < r:
            max1 = max(max1, nums[l] + nums[r])
            l += 1
            r -= 1
        return max1