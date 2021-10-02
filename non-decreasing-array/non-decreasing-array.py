class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                # if err or (i > 1 and i < len(N) - 1 and N[i-2] > N[i] and N[i+1] < N[i-1]):
                    # return False
                if count or ( i > 1 and i < len(nums)-1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                count = 1
        return True