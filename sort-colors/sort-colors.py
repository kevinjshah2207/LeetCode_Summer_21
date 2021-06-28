class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # d = {0:0, 1:0, 2:0}
        # for num in nums:
        #     if num in d:
        #         d[num] += 1
        # for i in range(len(nums)):
        #     if d[0] > 0:
        #         nums[i] = 0
        #         d[0] -= 1
        #     elif d[1] > 0:
        #         nums[i] = 1
        #         d[1] -= 1
        #     else:
        #         nums[i] = 2
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1