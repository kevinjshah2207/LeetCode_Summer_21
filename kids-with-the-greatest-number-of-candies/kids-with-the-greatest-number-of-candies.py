class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        ans = []
        for i in range(len(candies)):
            if ((candies[i]+extraCandies) >= m):
                print(candies[i]+extraCandies)
                ans.append(True)
            else:
                ans.append(False)
        return ans