class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        d = {}
        for i, val in enumerate(nums):
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
        d = dict(sorted(d.items(), key=lambda item: -item[0]))
        for i in d:
            if d[i] == 1:
                return i
        return -1