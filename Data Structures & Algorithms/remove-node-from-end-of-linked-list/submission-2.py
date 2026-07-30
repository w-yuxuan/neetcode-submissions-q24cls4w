# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        cur = head
        while cur:
            cur = cur.next
            length +=1
        
        target = length-n # steps to the node to be removed . if the last one, then it is the length'th node
        cur = head
        if target == 0: # if remove the 1st element
            if cur:
                return cur.next
            else: return [] # case when there was only one node

        # only lenth >= 2 makes it to here, so ok to check 'if cur.next.next' as we start checking from the 1st node 
        while cur: # if removed element is not 1st
            if target == 1: #the one to remove is the next node
                if cur.next.next: # not at the end after removal
                    cur.next = cur.next.next
                    return head
                else:
                    cur.next = None 
                    return head # at the end: 
            else:
                cur = cur.next
                target -=1 # track num steps to the target
        return head

