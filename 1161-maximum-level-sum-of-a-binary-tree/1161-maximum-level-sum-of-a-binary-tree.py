# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_list = []
        
        def dfs(node, depth):
            if depth > len(sum_list):
                sum_list.append(node.val)
            else:
                sum_list[depth - 1] += node.val
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
           
        dfs(root, 1)
        
        return sum_list.index(max(sum_list)) + 1
            
        