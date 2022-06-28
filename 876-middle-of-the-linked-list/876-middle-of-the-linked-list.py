# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        l = []
        cnt = 0
        while True:
            cnt += 1
            l.append(head)
            if head.next == None:
                break
            else:
                head = head.next


        return l[len(l)//2]
                

        