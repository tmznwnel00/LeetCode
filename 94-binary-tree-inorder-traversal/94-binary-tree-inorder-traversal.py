# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        answer = []
        return self.order(root, answer)
        
    
    def order(self, root, answer):
        if root == None:
            return []
        if root.left != None:
            temp = root
            root = root.left
            self.order(root, answer)
            root = temp
        answer.append(root.val)
        if root.right != None:
            temp = root
            root = root.right
            self.order(root, answer)
            root = temp
        return answer