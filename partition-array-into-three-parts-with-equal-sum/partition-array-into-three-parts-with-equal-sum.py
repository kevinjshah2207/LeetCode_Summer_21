class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        l, r, s = 1, len(arr) - 2, sum(arr)
        l_sum, r_sum, avg_sum = arr[0], arr[-1], s//3
        if s % 3 != 0:
            return False
        while l <= r:
            if l_sum != avg_sum and l < r:
                l_sum += arr[l]
                l += 1
            if r_sum != avg_sum and l < r:
                r_sum += arr[r]
                r -= 1
            if l_sum == avg_sum == r_sum:
                return True
            if l == r:
                break
        return False