class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat = [[0]*len(colSum) for i in range(len(rowSum))]
        # mat1 = [[1]*len(colSum) for i in range(len(rowSum))]
        m, n = len(rowSum), len(colSum)
        for i in range(m):
            for j in range(n):
                mat[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= mat[i][j]
                colSum[j] -= mat[i][j]
        return mat