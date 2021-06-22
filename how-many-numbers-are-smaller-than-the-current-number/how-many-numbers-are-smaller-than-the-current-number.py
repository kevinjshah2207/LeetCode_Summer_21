class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums = nums.copy()
        snums.sort()
        # print(nums)
        ans = []
        for i in nums:
            ans.append(snums.index(i))
        return ans
        