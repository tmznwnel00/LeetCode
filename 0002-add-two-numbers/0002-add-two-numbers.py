# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ''
        number2 = ''
        while l1:
            number1 = str(l1.val) + number1
            l1 = l1.next
        while l2:
            number2 = str(l2.val) + number2
            l2 = l2.next
        value = str(int(number1) + int(number2))
        answer = ListNode()
        last = None
        for i in value:
            now = ListNode()
            now.val = int(i)
            if last != None:
                now.next = last
            last = now

        return last