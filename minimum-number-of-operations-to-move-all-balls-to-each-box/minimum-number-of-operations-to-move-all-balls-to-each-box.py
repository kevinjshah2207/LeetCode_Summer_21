class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        s = list(boxes)
        for i in range(len(s)):
            count = 0
            for j in range(len(s)):
                if s[j] == "1":
                    count += abs(i-j)
            ans.append(count)
        return ans