class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = {}
        for i, val in enumerate(arr):
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
        count = 0
        for i in d:
            if i+1 in d:
                count += d[i]
        return count