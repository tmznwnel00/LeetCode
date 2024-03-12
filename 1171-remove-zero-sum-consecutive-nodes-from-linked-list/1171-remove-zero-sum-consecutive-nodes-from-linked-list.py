# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        h = []
        while head:
            if head.val == 0:
                if h:
                    h[-1].next = None
            elif head.val * -1 in l:
                index = l.index(head.val * -1)
                l = l[:index]
                l = [i + head.val for i in l]
                h = h[:index]
                if h:
                    h[-1].next = None
            else:
                l = [i + head.val for i in l]
                l.append(head.val)
                if h:
                    h[-1].next = head
                h.append(head)
            head = head.next
        return h[0] if h else None
                
        