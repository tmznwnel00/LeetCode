# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
from collections import Counter, deque
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        answer = 0
        queue = deque()
        dp = []
        queue.append((root, set([])))
        while queue:
            now, history = queue.popleft()
            new_history = copy.deepcopy(history)
            
            if now.val in new_history:
                new_history.remove(now.val)
            else:
                new_history.add(now.val)
 
            if now.left:
                queue.append((now.left, new_history))
            if now.right:
                queue.append((now.right, new_history))
            if now.left is None and now.right is None:
                if len(new_history) < 2:
                    answer += 1

        return answer
            
            
            
            