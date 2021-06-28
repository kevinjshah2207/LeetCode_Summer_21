class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # d = {}
        # for i in nums:
        #     if i in d:
        #         return i
        #     else:
        #         d[i] = 1
        
        #Find intersection point of the two runners
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        #Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare