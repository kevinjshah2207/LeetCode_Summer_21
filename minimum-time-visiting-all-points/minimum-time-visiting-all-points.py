class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[i+1][0]
            y2 = points[i+1][1]
            x = abs(x1 - x2)
            y = abs(y1 - y2)
            time += max(x,y)
        return time