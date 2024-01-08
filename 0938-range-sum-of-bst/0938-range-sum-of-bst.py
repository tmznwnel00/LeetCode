# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        l = []
        l_index, r_index = -1, -1
        def bs(root):
            nonlocal l_index, r_index
            if root.left:
                bs(root.left)
            if root.val == low:
                l_index = len(l)
            elif root.val == high:
                r_index = len(l)
            l.append(root.val)
            if root.right:
                bs(root.right)
        
        
        bs(root)
        
        return sum(l[l_index:r_index+1])
        
                
                
            

        
        