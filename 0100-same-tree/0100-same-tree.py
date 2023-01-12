# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def node2list(n: Optional[TreeNode], l: Optional[int]) -> Optional[int]:
            l.append(n.val)
            if n.left is not None:
                node2list(n.left, l)
            else:
                l.append(None)
            if n.right is not None:
                node2list(n.right, l)
            else:
                l.append(None)
        p_list = []
        q_list = []
        if p is not None:
            node2list(p, p_list)
        if q is not None:
            node2list(q, q_list)

        if p_list == q_list:
            return True
        else:
            return False