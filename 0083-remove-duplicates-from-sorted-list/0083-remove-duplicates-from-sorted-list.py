# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set([])
        point = None
        answer = head
        while head:
            if head.val in s:
                point.next = head.next
            else:
                s.add(head.val)
                point = head
            head = head.next

            
        return answer