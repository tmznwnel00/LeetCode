# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = ListNode()
        a = answer
        if not lists:
            return None
        while answer:
            temp = []
        
            for l in lists:
                if l == None:
                    temp.append(10**4 + 1)
                else:
                    temp.append(l.val)
            if len(temp) == 0:
                break
            min_val = min(temp)
            if min_val == 10**4 + 1:
                break
            index = temp.index(min_val)
            replace, lists[index] = lists[index], lists[index].next
            replace.next = None
            answer.next = replace
            answer = answer.next
            if lists[index] == None:
                del lists[index]
        
        return a.next