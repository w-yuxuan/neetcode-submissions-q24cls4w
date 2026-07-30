# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head 
        while f and f.next:
            s = s.next
            f = f.next.next

        if not head or not head.next:
            return

        prev = None
        cur = s
        # test when there are only <2 nodes
        while cur:
            store = cur.next
            cur.next = prev
            prev = cur
            cur = store
        # now mid is at prev
        cur = head
        while prev.next:
            save =cur.next
            save2=prev.next
            cur.next=prev
            prev.next= save
            prev=save2
            cur =save
        return 
           
        



