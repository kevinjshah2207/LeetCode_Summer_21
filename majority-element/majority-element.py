class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] == nums[n//2]:
            return nums[0]
        else:
            return nums[n//2]
        # if nums[0] == nums[1]:
        #     return nums[0]
        # else:
        #     return nums[(n//2)+1]