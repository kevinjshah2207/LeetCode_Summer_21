class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        l = 0
        r = 0
        nest = 0
        if s == "" or len(s) == 1:
            return 0
        for i in s:
            if i == '(':
                l += 1
            elif i == ')':
                depth = l - r
                nest = max(nest, depth)
                r += 1
        return nest