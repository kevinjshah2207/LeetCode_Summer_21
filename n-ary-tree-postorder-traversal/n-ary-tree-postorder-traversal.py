"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)
        recursion(root, res)
        return res