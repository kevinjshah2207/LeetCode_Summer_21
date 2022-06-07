class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, val in enumerate(nums):
            if val not in d:
                d[val] = 1
            else:
                return True
        return False