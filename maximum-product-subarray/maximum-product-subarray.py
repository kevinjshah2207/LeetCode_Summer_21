class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, max1, min1 = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            max2 = max(nums[i], min1*nums[i], max1*nums[i])
            min1 = min(nums[i], min1*nums[i], max1*nums[i])
            max1 = max2
            ans = max(max1, ans)
        return ans
        