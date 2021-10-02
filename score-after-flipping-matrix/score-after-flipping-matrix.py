class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        res = (1 << N - 1) * M
        for j in range(1, N):
            cur = 0
            for i in range(M):
                if A[i][j] == A[i][0]:
                    cur += 1
                # print(A[i], j, i)
                # print(A[i][j], A[i][0], cur)
            # cur = sum(A[i][j] == A[i][0] for i in range(M))
            res += max(cur, M - cur) * (1 << N - 1 - j)
            print(cur, M-cur, (1 << N-1-j))
        return res