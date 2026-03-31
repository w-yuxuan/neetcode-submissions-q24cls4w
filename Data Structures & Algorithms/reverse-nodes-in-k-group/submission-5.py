# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #count total 
        curr = 0
        cur = head
        while cur:
            cur = cur.next
            curr+=1
        i = curr-curr%k
        returnHead = head 

        #reverse
        save = None
        #for the first pass
        two = head
        
        while i:
            n=k
            end = two
            one = None
            while two and n:
                n-=1
                i-=1
                store = two.next
                two.next = one
                one = two
                two = store
            if not save:
                returnHead = one
            else:
                save.next=one
            end.next=two
            save = end
        return returnHead