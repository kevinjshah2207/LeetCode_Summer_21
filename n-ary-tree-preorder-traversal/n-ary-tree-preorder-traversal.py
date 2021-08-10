"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Iterative solution
        if not root:
            return None
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.extend(node.children[::-1])
        return ans