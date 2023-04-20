# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dict = defaultdict(int)
        min_dict = defaultdict(int)
        def bfs(node, height, index):
            max_dict[height] = max(max_dict[height], index)
            if min_dict[height] == 0:
                min_dict[height] = index
            else:
                min_dict[height] = min(min_dict[height], index)
            if node.left:
                bfs(node.left, height + 1, 2 * index - 1)
            if node.right:
                bfs(node.right, height + 1, 2 * index)
        bfs(root, 1, 1)
        answer = 0
        for x, y in zip(max_dict.values(), min_dict.values()):
            answer = max(answer, x - y)

        return answer + 1