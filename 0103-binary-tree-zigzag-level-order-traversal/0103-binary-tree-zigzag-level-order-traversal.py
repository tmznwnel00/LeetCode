# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        temp = []
        answer = [[root.val]]
        while queue:
            print(queue)
            l = []
            for i in queue[:]:    
                if i.left:
                    temp.append(i.left)
                    l.append(i.left.val)
                if i.right:
                    temp.append(i.right)
                    l.append(i.right.val)
            if l != [] :
                if len(answer) % 2 == 1:
                    l = list(reversed(l))
                answer.append(l)
            queue = temp
            temp = []
        return answer