class Solution:
    def dist(self, x1: int, y1: int, x2: int, y2: int) -> float:
        x = pow(x2-x1, 2)
        y = pow(y2-y1, 2)
        return pow(x+y, 0.5)
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            count = 0
            for point in points:
                d = self.dist(query[0], query[1], point[0], point[1])
                count += (d <= query[2])
            answer.append(count)
        return answer