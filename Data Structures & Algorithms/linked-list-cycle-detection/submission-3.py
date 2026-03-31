# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        one = head
        if not head: return False
        if head.next == None: return False
        
        two = head.next 
        while one and two:
            if one.val == two.val:
                return True
            one = one.next
            if two.next:
                two = two.next.next
            else:break
        return False

