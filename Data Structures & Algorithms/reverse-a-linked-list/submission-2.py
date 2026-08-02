# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        previous = None
        while curr:
            next = curr.next
            newHead = curr
            newHead.next = previous
            previous = newHead
            curr = next
        return previous
        