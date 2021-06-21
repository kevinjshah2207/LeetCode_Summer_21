class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in range(0,len(accounts)):
            s = 0
            for j in range(0, len(accounts[i])):
                s += accounts[i][j]
            rich = max(rich, s)
        return rich