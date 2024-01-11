import copy
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
#         ancestor dictionary 만들어둬야함

        ancestor = defaultdict(set)
        
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if node.left:
                ancestor[node.left.val] = copy.deepcopy(ancestor[node.val])
                ancestor[node.left.val].add(node.val)
                queue.append(node.left) 
            if node.right:
                ancestor[node.right.val] = copy.deepcopy(ancestor[node.val])
                ancestor[node.right.val].add(node.val)
                queue.append(node.right)
                
            
        answer = 0
        for key, value in ancestor.items():
            for val in value:
                if abs(val - key) > answer:
                    answer = abs(val - key)
                    
        return answer
                
            
                
                
            