# mimic leet 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dum = ListNode(0,head)
        grpprev = dum #like pointer "save" in my logic

        while True:
            kth = self.findk(grpprev,k)
            if not kth:
                break
            grpnext=kth.next # like where the pointer "two" ended after it reverses a segmt in my logic
            newtail=grpprev.next
            #reverse    
            prev,cur = kth.next , grpprev.next # so the latter side is auto attached
            while cur!=grpnext:
                store = cur.next
                cur.next = prev
                prev = cur # like the pointer "one" in my logic
                cur = store # like the pointer "two" in my logic

            #reconnect front side
            #now for the just-reversed segment: kth is start and cur is end
            grpprev.next = kth
            #save new grpprev
            grpprev = newtail 
        return dum.next

    #walk forward to find kth next in og ordering
    def findk(self,lst,k):
        while lst and k>0 :
            lst = lst.next
            k-=1
        return lst