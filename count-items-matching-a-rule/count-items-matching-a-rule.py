class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            r = 0
        elif ruleKey == "color":
            r = 1
        else:
            r = 2
        count = 0
        # print(r)
        for i in range(len(items)):
            # print(ruleValue, items[i][r])
            if items[i][r] == ruleValue:
                count += 1
        return count