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
            l.append(head.val)
            if head.next == None:
                break
            else:
                head = head.next
        temp = l[cnt//2:]
        answer = ListNode(temp[0])
        head = answer
        cursor = answer.next
        for i in range(1,len(temp)):
            newNode = ListNode(temp[i])
            answer.next = newNode
            answer = answer.next
        return head
                

        