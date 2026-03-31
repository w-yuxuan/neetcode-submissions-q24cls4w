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
            return lists

        def merge(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

        i=1
        res = lists[0]
        while i <= len(lists)-1:
            node = merge(res,lists[i])
            res = node
            i+=1
        return res
            
       


    # realize that after you merge sort the first the first position in each of the k list, you can't just add the next position's result at the end with extend, 
    # log k means I in total need to split k times and not n times  
    # 1. taking the first two list to do merge sort, but the number behind log 
    #comes from how many levels you need to split beneeath you, not how many list you need to run that process
    # so although you need to run this program k times, the depth is not k, but the log(longest), n

    # you can split each of the k lists into two, but then a k-pointer instead of 2pointer is much costly
     
#code the n*k: you keep comparing 2


            
        
