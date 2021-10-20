class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # for i, val in enumerate(arr):
        #     if val > i:
        #         return -1
        #     else:
        #         if i == val:
        #             return i
        # return -1
        l, r = 0, len(arr)-1
        while l < r:
            mid = (l+r)//2
            if arr[mid] - mid < 0:
                l = mid+1
            else:
                r = mid
        return l if arr[l] == l else -1