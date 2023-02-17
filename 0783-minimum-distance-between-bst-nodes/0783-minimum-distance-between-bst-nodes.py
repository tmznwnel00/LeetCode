# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        l = []
        def go(root, l):
            if root.left:
                go(root.left, l)
            l.append(root.val)
            if root.right:
                go(root.right, l)
        go(root, l)
        
        m = 0
        for i in range(len(l) - 1):
            if m == 0:
                m = l[i+1] - l[i]
            else:
                m = min(m, l[i+1] -  l[i])
        return m