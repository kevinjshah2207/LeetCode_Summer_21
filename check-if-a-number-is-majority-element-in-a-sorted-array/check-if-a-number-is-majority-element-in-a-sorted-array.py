class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def search(a,x):
            l, r = 0, len(a)
            while l < r:
                mid = (l+r)//2
                if a[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l
        n = len(nums)
        if nums[n//2] != target:
            return False
        a1 = search(nums, target)
        a2 = search(nums, target+1)
        return a2-a1 > n//2