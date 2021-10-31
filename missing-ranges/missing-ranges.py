class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if not nums:
            if lower == upper:
                ans.append(str(lower))
            else:
                st = str(lower) + '->' + str(upper)
                ans.append(st)
            return ans
        if lower != nums[0]:
            l = lower
            r = nums[0] - 1
            if l == r:
                ans.append(str(l))
            else:
                st = str(l) + '->' + str(r)
                ans.append(st)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                continue
            else:
                l = nums[i] + 1
                r = nums[i+1] - 1
                if l == r:
                    ans.append(str(l))
                else:
                    st = str(l) + '->' + str(r)
                    ans.append(st)
        if nums[-1] != upper:
            l = nums[-1] + 1
            r = upper
            if l == r:
                ans.append(str(l))
            else:
                st = str(l) + '->' + str(r)
                ans.append(st)
        return ans