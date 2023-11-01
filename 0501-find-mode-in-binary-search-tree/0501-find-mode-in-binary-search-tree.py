# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        
        def dfs(node):
            if node.left:
                dfs(node.left)
            d[node.val] += 1
            if node.right:
                dfs(node.right)
        
        dfs(root)
        heap = []
        for key, value in d.items():
            heappush(heap, (-value, key))
            
        max_val = 0
        answer = []
        while heap:
            value, key = heappop(heap)
            value *= -1
            
            if value >= max_val:
                max_val = value
                answer.append(key)
            else:
                break
        
        return answer
        
            