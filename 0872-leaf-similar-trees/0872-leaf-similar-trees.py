# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leaf1 = []
        leaf2 = []
        
        def bfs(root, l):
            if root.left:
                bfs(root.left, l)
            if root.left is None and root.right is None:
                l.append(root.val)
            if root.right:
                bfs(root.right, l)
        
        bfs(root1, leaf1)
        bfs(root2, leaf2)
        
        return leaf1==leaf2