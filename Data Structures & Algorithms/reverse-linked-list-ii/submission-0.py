# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i=1
        dum = ListNode()
        dum.next = head
        prev = dum
        while i<left:
            prev = head
            head = head.next
            i+=1
        l = prev # assume left =2, right = 3 q : now at 2
        ending = head
        aft = None
        while i<=right:
            save = head.next
            head.next = aft
            aft = head
            head = save
            i+=1
        ending.next = head
        l.next = aft
        return dum.next 
        