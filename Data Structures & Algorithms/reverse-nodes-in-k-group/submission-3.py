# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:       
        # count num to know when to tag on the remaining < k 
        c = head
        cur=0
        while c:
            c = c.next
            cur+=1
        i=k*(cur//k) # total steps to take 
        returnHead = head # if len=2 k =3, we do this line, i=0 so below will all get skipped

        #start flipping
        two = head # init for round 1 only
        save = None #variable to save the end of last run 
        while i:
            one = None
            end = two #end of this segment after flipping
            n=k
            while n and two: # inherit two from last round
                store = two.next
                two.next=one
                one=two
                two = store
                n-=1
                i-=1
            #define global head if i did the first k steps
            if not save:
                returnHead = one
            else:
                save.next=one #connect previous end to 
            save = end
            end.next=two
        return returnHead

                

            # decide what to link back up




        
        
        
