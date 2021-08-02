# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        while q:
            pre = q
            cur = []
            for p in q:
                for child in [p.left, p.right]:
                    if child:
                        cur.append(child)
            q = cur
        return sum(node.val for node in pre)