# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def node2list(n: Optional[TreeNode], l: [int]) -> [int]:
            l.append(n.val)
            if n.left is not None:
                node2list(n.left, l)
            if n.right is not None:
                node2list(n.right, l)
        if root:
            node2list(root, answer)
            return answer
        else:
            return answer