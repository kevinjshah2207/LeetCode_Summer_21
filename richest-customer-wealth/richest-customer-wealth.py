class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in range(0,len(accounts)):
            s = sum(accounts[i])
            rich = max(rich, s)
        return rich