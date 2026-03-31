# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return 

        if len(lists)==1:
            return lists[0]
            
        if len(lists)==2:
            return self.merge(lists[0],lists[1]) #return merged list
        
        mid = len(lists)//2
        return self.merge(self.mergeKLists(lists[0:mid]), self.mergeKLists(lists[mid:]))

    def merge(self,list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        cur = dum

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                # if I do = ListNode(list1.val) then i create a copy of that node instead of just pointing dum to the existing node in list 1
                
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next=list1

        if list2:
            cur.next=list2
        return dum.next
