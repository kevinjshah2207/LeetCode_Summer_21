class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        occ = 0
        val = 0
        pairs = 0
        while i < len(nums):
            if val < 1:
                val = nums[0]
                occ += 1
                i += 1
                continue
            if i == len(nums)-1:
                if val == nums[i]:
                    occ += 1
                    p = int(((occ**2) - occ)/2)
                    pairs += p
                    i+=1
                    continue
            if val == nums[i]:
                occ += 1
                i += 1
            else:
                val = nums[i]
                if occ >= 2:
                    p = int(((occ**2) - occ)/2)
                    pairs += p
                occ = 1
                i += 1
        return pairs
                
                
            