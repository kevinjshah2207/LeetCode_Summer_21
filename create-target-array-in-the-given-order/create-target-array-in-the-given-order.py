class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            ind = index[i]
            target.insert(ind, nums[i])
        return target