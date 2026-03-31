# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.reverse()
        dum = ListNode()
        cur = dum
        for i, val in enumerate(res):
            cur.next = ListNode(val)
            cur = cur.next
        return dum.next
