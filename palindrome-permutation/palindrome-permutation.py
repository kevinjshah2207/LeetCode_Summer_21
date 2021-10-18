class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        unpaired = set()
        for i in s:
            if i not in unpaired:
                unpaired.add(i)
            else:
                unpaired.remove(i)
        
        return len(unpaired) <= 1