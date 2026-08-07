# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:return list2
        if list2==None:return list1
        if list1.val<=list2.val:
            curr_node = list1
            compare_node = list2
            sorted_list = list1
        else:
            curr_node = list2
            compare_node = list1
            sorted_list = list2
        while curr_node.next:
            if curr_node.next.val<=compare_node.val:
                curr_node = curr_node.next
            else:
                temp_node = curr_node.next
                curr_node.next = compare_node
                compare_node = temp_node
                curr_node = curr_node.next
        curr_node.next = compare_node
        return sorted_list
                
        