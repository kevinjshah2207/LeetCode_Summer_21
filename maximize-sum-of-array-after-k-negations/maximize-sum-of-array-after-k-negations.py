class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and k > 0:
            if nums[i] < 0:
                nums[i] *= -1
                k -= 1
                i += 1
            elif nums[i] == 0:
                break
            else:
                if k % 2 == 0:
                    break
                else:
                    if nums[i] < nums[i-1]:
                        nums[i] *= -1
                    else:
                        nums[i-1] *= -1
                    break
        return sum(nums)