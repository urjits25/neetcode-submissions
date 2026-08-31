# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        reverse linked list from halfway through
        start joining 0 -> n-1 -> 1 -> n-2, splicing one by one
        
        1. find the middle of the LL using slow-fast ptrs
        2. reverse slow -> end
        3. head -> end -> head.next -> end.next ...
        '''
        if not head or not head.next:
            return 

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # reverse the 2nd half of the LL
        prev, cur = mid, mid.next
        prev.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        first = head
        second = prev

        while second:
            nf = first.next
            ns = second.next
            first.next = second
            second.next = nf
            first = nf
            second = ns
        