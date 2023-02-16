# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        answer = 0
        answer_list = []
        def go(node, answer):
            answer += 1
            answer_list.append(answer)
            if node.left:
                go(node.left, answer)
            if node.right:
                go(node.right, answer)
        go(root, answer)
        return max(answer_list)