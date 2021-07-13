class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        # horizontalCuts.insert(0,0)
        # verticalCuts.insert(0,0)
        # horizontalCuts.append(h)
        # verticalCuts.append(w)
        height = 0
        length = 0
        # mod = 10000007
        for i in range(len(horizontalCuts)-1):
            height = max(height, horizontalCuts[i+1]-horizontalCuts[i])
        for i in range(len(verticalCuts)-1):
            length = max(length, verticalCuts[i+1]-verticalCuts[i])
        return (height*length)%((10**9)+7)