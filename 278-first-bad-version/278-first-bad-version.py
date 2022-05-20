# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid - 1