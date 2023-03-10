# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.l = []
        while head:
            self.l.append(head.val)
            head = head.next
        self.length = len(self.l)

    def getRandom(self) -> int:
        return self.l[random.randint(0, self.length - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()