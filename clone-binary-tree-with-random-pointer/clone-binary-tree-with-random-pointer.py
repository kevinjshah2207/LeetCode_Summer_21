# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def __init__(self):
        self.visited = dict()
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None
        if root in self.visited:
            return self.visited[root]
        node = NodeCopy(root.val, None, None, None)
        self.visited[root] = node
        
        node.left = self.copyRandomBinaryTree(root.left)
        node.right = self.copyRandomBinaryTree(root.right)
        node.random = self.copyRandomBinaryTree(root.random)
        return node