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
            cur.next=prev
            #store.next=cur #next iter will handle this, I only link curr to prev at ea level, so no need to worry if store will be None 
            prev = cur #can't be below next line 
            cur = store
        return prev