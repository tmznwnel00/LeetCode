# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        list1 = []
        list2 = []
        while head:
            if head.val >= x:
                tmp = head
                head = head.next
                tmp.next = None
                list2.append(tmp)
            else:
                tmp = head
                head = head.next
                tmp.next = None
                list1.append(tmp)
        answer = None
        if len(list1) == 0 and len(list2) == 0:
            return None
        elif len(list1) == 0:
            start = list2[0]
            del list2[0]
        else:
            start = list1[0]
            del list1[0]
        answer = start
        while list1:
            start.next = list1[0]
            del list1[0]
            start = start.next
        while list2:
            start.next = list2[0]
            del list2[0]
            start = start.next
        return answer