# Initialize 2 pointers l = 0 and r = len(s). As the output array is a list of [0,r], we just
# place l if we encounter I and r if we encounter D. We also increment l when I and decrement
# r when D occurs. In the end we just append the last r to complete the array with the 
# missing number in the range [0,len(s)]

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, r = 0, len(s)
        out = []
        for i in range(len(s)):
            out.append(l if s[i] == "I" else r)
            if s[i] == "I":
                l += 1
            else:
                r -= 1
        out.append(r)
        return out