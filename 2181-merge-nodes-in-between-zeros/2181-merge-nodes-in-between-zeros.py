# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.answer = ListNode()
        self.answer2 = ListNode()
        self.answer2 = self.answer
        merge = 0
        head = head.next
        while head:
            if head.val == 0:
                self.answer.next = ListNode()
                self.answer = self.answer.next
                self.answer.val = merge
                merge = 0
            merge += head.val
            head = head.next
        return self.answer2.next