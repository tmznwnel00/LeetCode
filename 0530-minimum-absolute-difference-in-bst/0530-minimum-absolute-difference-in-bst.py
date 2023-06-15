# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        node_list = []
        def dfs(node):
            node_list.append(node.val)
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        node_list.sort()
        
        answer = node_list[-1] - node_list[0]
        for x, y in zip(node_list[:-1], node_list[1:]):
            answer = min(answer, y-x)
        
        return answer
            