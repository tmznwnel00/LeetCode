# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def reverse(node):
            node.left, node.right = node.right, node.left
            if node.left:
                reverse(node.left)
            if node.right:
                reverse(node.right)
        if not root.right and not root.left:
            return True
        if not root.right or not root.left:
            return False
        reverse(root.right)

        if str(root.left) == str(root.right):
            return True
        else:
            return False