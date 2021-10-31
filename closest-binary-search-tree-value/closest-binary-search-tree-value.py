# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack = [root]
        dif1 = 10000000000
        val = root.val
        while stack:
            node = stack.pop()
            if node:
                dif2 = abs(node.val - target)
                if dif2 < dif1:
                    val = node.val
                    dif1 = dif2
                stack.extend([node.right, node.left])
        return val