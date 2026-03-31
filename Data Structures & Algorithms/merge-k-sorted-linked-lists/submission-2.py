# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #dfs keep dividing 'lists' by two and calling itself, edge case is when len(sublist)==1
        if not lists:
            return
        if len(lists)==1:
            return lists[0]
        mid = len(lists)//2
        return self.merge(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))

        #merge 2 lists, resistant if one is []
    def merge(self,l1,l2):
        dum=ListNode()
        cur=dum
        while l1 and l2:
            if l1.val <= l2.val: #equal to preserve order
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next=l2
        return dum.next
        
        