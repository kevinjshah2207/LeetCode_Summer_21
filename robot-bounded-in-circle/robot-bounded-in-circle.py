class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in range(len(instructions)):
            if instructions[i] == 'G':
                x, y = x + dx, y + dy
            if instructions[i] == 'L':
                dx, dy = -dy, dx
            if instructions[i] == 'R':
                dx, dy = dy, -dx
        return (x, y) == (0, 0) or (dx, dy) != (0,1)