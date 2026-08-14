# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        a -> b -> c -> d ... -> None
        ^ <- ^    ^
        i    j    k
            i     j    k
                  i     j  k
        '''
        if not head or not head.next:
            return head

        i, j = head, head.next
        i.next = None
        while j:
            k = j.next
            j.next = i
            i, j = j, k
        return i
            