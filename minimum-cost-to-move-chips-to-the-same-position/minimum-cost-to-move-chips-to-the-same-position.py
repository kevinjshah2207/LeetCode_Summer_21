class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        eve = 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                eve += 1
            else:
                odd += 1
        return min(odd, eve)