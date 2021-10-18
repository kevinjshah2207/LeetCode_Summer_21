class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, val in enumerate(arr):
            if val > i:
                return -1
            else:
                if i == val:
                    return i
        return -1