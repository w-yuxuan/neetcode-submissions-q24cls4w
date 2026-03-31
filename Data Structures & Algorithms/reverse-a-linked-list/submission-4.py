# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            store = cur.next
            cur.next = prev
            #store.next = cur #fail if no store
            prev = cur
            cur = store
        #stops when cur is none
        return prev




