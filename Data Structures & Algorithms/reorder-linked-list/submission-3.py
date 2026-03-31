# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointer won't give you all the second half elements
        # i can't go prev, else it will be easy send one pointer to reach the end and the other pointer to start at front
        
        #after hint: consider even/odd len?
        s = f = head

        while f and f.next :
            f = f.next.next
            s = s.next
        #if odd len= 7 like ex 1: i stops at 3, j at 6, 
        # if even: i also stop at 3,but now it's not the middle point that separates the 2 lists
        #A: just flip and match with the first one, odd ones will have one extra element, you can tag it onto final res
        if not s.next :
            return  # if only 1/ 2 elemnts, slow will be at second node, we don't need to flip 
        prev = None # must ok
        cur = s
        

        while cur:
            store = cur.next 
            cur.next = prev
            prev = cur
            cur = store

        # check only 1 or 2 nodes case
        # dum = ListNode(0)
        # res = dum
        cur = head # so we keep head pointer and not shift it along

        while prev.next:  #don't use: #and cur!=s to guard "if only one node". can cause error if cur and s should be ==
            save = cur.next
            save2 = prev.next

            cur.next = prev
            prev.next = save
            cur = save
            prev = save2

        # if prev:
        #     cur = prev
        return 




        




        


        
