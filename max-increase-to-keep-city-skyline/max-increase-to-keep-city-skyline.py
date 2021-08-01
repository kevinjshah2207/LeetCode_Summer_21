class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row, col, out = [], [], 0
        for i in range(len(grid)):
            row.append(max(grid[i]))
        for i in range(len(grid)):
            max_col = 0
            for j in range(len(grid[0])):
                max_col = max(max_col, grid[j][i])
            col.append(max_col)
        # print(col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                out += (min(row[i], col[j]) - grid[i][j])
        return out