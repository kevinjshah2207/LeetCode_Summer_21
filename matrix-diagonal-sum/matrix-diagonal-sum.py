class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        n = len(mat)
        for i in range(n):
            if n % 2 == 0:
                s += mat[i][i] + mat[i][n-i-1]
            else:
                s += mat[i][i] + mat[i][n-i-1]
        if n % 2 != 0:
            s -= mat[n//2][n//2]
        return s