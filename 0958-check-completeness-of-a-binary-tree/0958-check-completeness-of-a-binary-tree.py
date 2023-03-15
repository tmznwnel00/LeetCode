# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        
        check = 0
        while True:

            if len(queue) == 0:
                break
            q = queue.popleft()
            if q is None:
                check = 1
                
            else:
                if check == 1:
                    return False
                queue.append(q.left)
                queue.append(q.right)
        return True