# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
import collections
class Solution:
    # def __init__(self):
    #     self.visited = dict()
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        ##### Iterative DFS
        if not root:
            return None
        visited = collections.defaultdict(lambda: NodeCopy())
        visited[None] = None
        
        S = [root]
        while S:
            node = S.pop()
            visited[node].val = node.val
            visited[node].left = visited[node.left]
            visited[node].right = visited[node.right]
            visited[node].random = visited[node.random]
            for child in (node.left, node.right):
                if child:
                    S.append(child)
        return visited[root]
            
        ##### Recursive DFS
#         if not root:
#             return None
#         if root in self.visited:
#             return self.visited[root]
#         node = NodeCopy(root.val, None, None, None)
#         self.visited[root] = node
        
#         node.left = self.copyRandomBinaryTree(root.left)
#         node.right = self.copyRandomBinaryTree(root.right)
#         node.random = self.copyRandomBinaryTree(root.random)
#         return node

