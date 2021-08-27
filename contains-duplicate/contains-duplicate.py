class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # flag = False
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                return True
        return False