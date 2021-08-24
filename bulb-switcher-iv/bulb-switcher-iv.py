class Solution:
    def minFlips(self, target: str) -> int:
        flag = "0"
        count = 0
        for bulb in target:
            if bulb != flag:
                count += 1
                flag = bulb
        return count