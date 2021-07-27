class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # left = right = 0
        # res = [0]
        # for i in S:
        #     if i == "I":
        #         right += 1
        #         res.append(right)
        #     else:
        #         left -= 1
        #         res.append(left)
        # return [i - left for i in res]
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