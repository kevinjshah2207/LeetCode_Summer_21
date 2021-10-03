class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)//2
        types = 0
        d = {}
        for i, c in enumerate(candyType):
            if c not in d:
                types += 1
                d[c] = 1
        return min(n, types)