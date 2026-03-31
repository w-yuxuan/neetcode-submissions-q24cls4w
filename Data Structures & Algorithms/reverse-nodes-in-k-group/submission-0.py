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

        def rev(head):
            nonlocal i
            one = None
            two = head
            end = head

            n=k
            while n and two:
                store = two.next
                two.next = one
                one = two
                two = store
                n-=1
                i-=1
            if i:
                end.next = rev(two)
            else: 
                end.next = two
            return one

        return rev(head)
                


    

