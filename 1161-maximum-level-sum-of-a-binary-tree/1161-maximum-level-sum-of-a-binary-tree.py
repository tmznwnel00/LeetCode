# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_list = []
        
        def bfs(node, depth):
            if depth > len(sum_list):
                sum_list.append(node.val)
            else:
                sum_list[depth - 1] += node.val
            if node.left:
                bfs(node.left, depth+1)
            if node.right:
                bfs(node.right, depth+1)
           
        bfs(root, 1)
        
        return sum_list.index(max(sum_list)) + 1
            
        