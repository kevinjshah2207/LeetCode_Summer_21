# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # DFS Solution: Use Stack to traverse through the Binary tree
        stack = [root]
        out = 0
        while stack:
            node = stack.pop()
            if node:
                if node.val <= high and node.val >= low:
                    out += node.val
                stack.extend([node.right, node.left])
        return out