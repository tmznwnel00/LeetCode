# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        l = []
        def dfs(root, string):
            string += str(root.val)
            if not root.left and not root.right:
                l.append(string)
                # print(string)
            if root.left:
                dfs(root.left, string)
            if root.right:
                dfs(root.right, string)
        dfs(root, '')
        
    
        return sum(map(int, l))