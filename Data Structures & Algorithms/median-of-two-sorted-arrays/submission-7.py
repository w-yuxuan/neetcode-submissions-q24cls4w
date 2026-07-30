class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = nums1 ,nums2
        tot = len(n1) + len(n2)
        mid = tot//2
        
        if tot==0:
            return 0
        if len(n1) > len(n2):
            n2, n1 = nums1 ,nums2
        l,r = 0,len(n1)-1
        # guess where mid is in n1, infer in n2
        
        
        #m1 +1 + m2+1 = mid

        while True:
            m1 = (l+r) //2
            m2 = mid-m1-2
            l1 = n1[m1] if m1>=0 else float('-inf')
            l2 = n2[m2] if m2>=0 else float('-inf')
            r1 = n1[m1+1] if m1+1<=len(n1)-1 else float('inf')
            r2 = n2[m2+1] if m2+1<=len(n2)-1 else float('inf')
            #check 

            if l1 <= r2 and l2<= r1:
        #if works, calc median  based on even /odd
                if tot %2 !=0: # odd
                    return min(r1,r2)
                else:
                    return (max(l1,l2) + min(r1,r2))/2.0
            elif l1 > r2:
                r = m1-1
            else:
                l = m1+1
         
        # adjust binary search if doesn't work