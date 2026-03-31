# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 

        count = 0
        cur = head
        while cur:
            cur = cur.next
            count +=1
        i = count-count%k # number of nodes to run the algo ( reverse or just connecting) 
        if i==count:returnHead = head
# for the first run
        one = None
        two = head
        save = None # save the end of last segment to connect to the first node aft doing reversal 

        while i:
            n=k
            pt = two
            while n: # find start of next series
                pt = pt.next
                n-=1

            end = two
            one = None
            n=k
            #flip a section
            while n and two:
                store = two.next
                two.next = one
                one = two
                two = store
                n-=1
                i-=1
            
            #connect to next section/ ending
            if save is None: # first revesral group
                returnHead = one
            else:
                save.next = one
            #else: 
            end.next = two #already done in the while loop
                #i should return the end of the first revesred node, or if i never reversed any segments, i return head
            save = end # save the end of last segment to connect to the first node aft doing reversal 

        return returnHead 

                


    

