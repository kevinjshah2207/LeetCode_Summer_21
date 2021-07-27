# We just have to find out the parity of each coin's position. As changing parity costs 1, we
# just have to find out the minimum number of changes required to make all the coins have the
# same parity.

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