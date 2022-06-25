# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        answer = 0
        l = []
        while 1:
            l.append(head.val)
            if head.next is None:
                break
            else:
                head = head.next
        length = len(l)
        if length % 2 == 1:
            del l[length/2]
        length = len(l)
        if length == 0:
            answer = True
        else:
            l1 = []
            for i in range(length/2):
                if l[i] != l[length - 1 - i]:
                    answer = False
                    break
                answer = True
                
        return answer