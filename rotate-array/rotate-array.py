class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
#         k = k % n
#         for i in range(k):
#             val = nums.pop()
#             nums.insert(0,val)
        nums.reverse()
        k %= n
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])