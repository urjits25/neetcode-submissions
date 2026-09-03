# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l3 = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                l3.next = list1
                list1 = list1.next
            else:
                l3.next = list2
                list2 = list2.next
            l3 = l3.next
        
        if list1:
            l3.next = list1
        
        if list2:
            l3.next = list2

        return dummy.next