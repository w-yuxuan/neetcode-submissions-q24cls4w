# Definition for singly-linked list.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            #if l1 or l2 1 or less 
            dum = ListNode()
            cur = dum 
            while l2 and l1:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l2:
                cur.next = l2
            if l1:
                cur.next = l1
                
            return dum.next

        if len(lists)==0:
            return 
        if len(lists) ==1:
            return lists[0]

        mid = len(lists)//2 # right lean

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        res = merge(left,right)

        return res

            
