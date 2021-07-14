class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # i = 1
        # if len(nums) == 1:
        #     return 0
        # for i in range(1,len(nums)-1):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i
        # if nums[0] > nums[1]:
        #     return 0
        # else:
        #     return len(nums) - 1
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        return low