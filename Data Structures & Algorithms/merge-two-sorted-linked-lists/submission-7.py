# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        n = dum
        while list1 and list2:
            if list1.val <= list2.val:
                n.next =list1
                list1 = list1.next
                
            else:
                n.next =list2
                list2 = list2.next
                
            n=n.next
        if list1:
            n.next = list1

        if list2:
            n.next = list2

        return dum.next 


