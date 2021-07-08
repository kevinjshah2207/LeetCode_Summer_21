
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_rows = [False]*m
        odd_cols = [False]*n
        for r,c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        return (n - sum(odd_cols)) * sum(odd_rows) + (m - sum(odd_rows))* sum(odd_cols)