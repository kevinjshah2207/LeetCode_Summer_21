# Sliding Window Approach: We create a dictionary that stores the index of occurrence of
# the character. We keep calculating the length of the substring in each iteration.
# If the character is already in the dict, we check if its occurrence is after our 
# sliding window's start position (l) or not. If it is not present in the current window
# then we just normally calculate the length, else, we slide the window start position to
# the right of where the repeated character was first seen.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {}
        l = 0
        count = 0
        for r in range(len(s)):
            if s[r] not in seen:
                count = max(count, r-l+1)
            else:
                if seen[s[r]] < l:
                    count = max(count, r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return count