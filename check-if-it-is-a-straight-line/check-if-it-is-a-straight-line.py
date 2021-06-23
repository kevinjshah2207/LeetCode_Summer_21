class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1 = coordinates[1][0]
        y1 = coordinates[1][1]
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        # slope = ((coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0]))
        for i in range(len(coordinates)):
            # m = ((coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0]))
            x = coordinates[i][0]
            y = coordinates[i][1]
            if (dx * (y-y1) != dy * (x-x1)):
                return False
        return True