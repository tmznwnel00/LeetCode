# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        ln = []
        if not head:
            return None
        while head:
            ln.append(head.val)
            head = head.next
        def bs(l, r):
            m = (l + r) // 2
            t = TreeNode()
            t.val = ln[m]
        
            if m > l:
                t.left = bs(l, m- 1)
            if m < r:
                t.right = bs(m + 1, r)
            return t
        
        l = 0
        r = len(ln) - 1
        return bs(l, r)