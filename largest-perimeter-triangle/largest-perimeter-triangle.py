class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i <= len(nums)-3:
            c = nums[i]
            b = nums[i+1]
            a = nums[i+2]
            if a + b > c:
                return a+b+c
            i += 1
        return 0