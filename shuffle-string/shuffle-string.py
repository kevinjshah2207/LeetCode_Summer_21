class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ""
        for i in range(len(s)):
            ans += s[indices.index(i)]
        return ans