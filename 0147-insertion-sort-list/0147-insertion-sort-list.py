# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = [head]
        head = head.next
        while head:
            temp = head.next
            check = 0 
            for i in range(len(l)):
                if head.val < l[i].val and i == 0:
                    head.next = l[i]
                    l.insert(i, head)
                    check = 1
                    break
                elif head.val < l[i].val:
                    l[i - 1].next = head
                    head.next = l[i]
                    l.insert(i, head)
                    check = 1
                    break
            if check == 0:
                l[-1].next = head
                l.append(head)
            head = temp
        l[-1].next = None
        # print(l)
        # for i in range(len(l)-1):
        #     l[i].next = l[i + 1]
        # l[-1].next = None
        return l[0]