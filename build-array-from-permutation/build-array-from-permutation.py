#https://helloml.org/build-array-from-permutation-solution-to-leetcode-problem/


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] + (n*(nums[nums[i]]%n)) #Modulo operator is the answer to this problem
            
        for i in range(len(nums)):
            nums[i] = nums[i] // n
        return nums