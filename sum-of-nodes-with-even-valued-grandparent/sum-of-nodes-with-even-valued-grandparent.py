# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        out = 0
        if not root:
            return 0
        if (root.val & 1) == 0:
            if root.left and root.left.left:
                out += root.left.left.val
            if root.left and root.left.right:
                out += root.left.right.val
            if root.right and root.right.left:
                out += root.right.left.val
            if root.right and root.right.right:
                out += root.right.right.val
        return out + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)