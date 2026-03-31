# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0)
        cur  = dum
        while l1 or l2:
            v1=l1.val if l1 else 0 
            v2=l2.val if l2 else 0
            add = v1 + v2
            if add >= 10:
                below = add - 10
                cur.next = ListNode(below)
                if l1 and l1.next: 
                    l1.next.val +=1
                elif l2 and l2.next:
                    l2.next.val+=1
                else: 
                    cur.next.next = ListNode(1)
                    return dum.next
            else: cur.next = ListNode(add)
            if l1 and l1.next:
                l1 = l1.next
            else : l1= None
            if l2 and l2.next:
                l2 = l2.next 
            else: l2 = None
            cur = cur.next
        return dum.next

