class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        s1 = 0
        a = 0
        for i, val in enumerate(weight):
            s1 += weight[i]
            if s1 > 5000:
                break
            a += 1
        return a
                