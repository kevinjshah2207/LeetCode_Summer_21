# Sort the array. As the sum of 3 numbers is 0, take one number and multiply it by -1.
# which becomes the target
# As nums[i] + nums[j] + nums[k] = 0, nums[i] + nums[j] = -nums[k]. Now we just have to
# find 2 numbers after the target whose sum is equal to the negative of the target. 
# During each iteration, we also get rid of duplicates by continuing numbers until
# nums[s] == nums[s-1]. This gives rise to a O(n^2) algorithm for the 3 Sum problem.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return None
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s, e = i+1, N-1
            while s < e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return result