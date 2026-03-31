# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=j=head
        while j and j.next :
            j = j.next.next
            i = i.next
        return i
        #if odd len= 7 like ex 1: i stops at 3, j at 6, 
        # if even: i also stop at 3,but now it's not the middle point that separates the 2 lists