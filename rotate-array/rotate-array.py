class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.reverse()
        k %= n
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
       