# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def order(node, preorder, inorder):
            node.val = preorder[0]
            index = inorder.index(node.val)
            l_size = index
            r_size = len(inorder) - index - 1
            if l_size > 0:
                left_node = TreeNode()
                node.left = order(left_node, preorder[1:1+l_size], inorder[:index])
            if r_size > 0:
                right_node = TreeNode()
                node.right = order(right_node, preorder[1+l_size:], inorder[index + 1 :])
            return node
        
        answer = order(TreeNode(), preorder, inorder)
        
        return answer