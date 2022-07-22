# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        now = 0
        prev = None
        start = None
        answer = head
        tmp3 = None
        real_start = None
        while head:
            now += 1
            pro = head.next
            if left != 1 and now == 1:
                real_start = head
            if left == right:
                return head
            if now == left - 1:
                start = head
                tmp2 = head.next
                start.next = None
            elif now == left:
                tmp1 = head
                tmp3 = head
                tmp2 = head.next
                tmp1.next = None
            elif now > left and now < right:
                tmp1 = head
                tmp2 = head.next
                tmp1.next = prev
            elif now == right:
                tmp3.next = head.next
                tmp1 = head
                tmp2 = head.next
                tmp1.next = prev
                if left == 1:
                    start = tmp1
                else:
                    start.next = tmp1 
            else:
                tmp2 = head.next
            prev = head
            head = tmp2
        if left != 1:
            head = real_start
        else:
            head = start
        return head
        