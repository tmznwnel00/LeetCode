import heapq
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        vertex = set([])
        edge = defaultdict(list)
        
        def bfs(node):
            vertex.add(node.val)
            if node.left:
                edge[node.val].append(node.left.val)
                edge[node.left.val].append(node.val)
                bfs(node.left)
            if node.right:
                edge[node.val].append(node.right.val)
                edge[node.right.val].append(node.val)
                bfs(node.right)
                
        bfs(root)
        
        queue = deque([start])
        visited = set([start])
        answer = 0

        while queue:
            for i in range(len(queue)):
                val = queue.popleft()
                for j in edge[val]:
                    if j not in visited:
                        queue.append(j)
                        visited.add(j)
                
            answer += 1
                
        return answer - 1