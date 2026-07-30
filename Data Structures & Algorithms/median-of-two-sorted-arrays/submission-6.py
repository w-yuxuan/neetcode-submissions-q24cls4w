class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = nums1,nums2
        if len(nums2)< len(nums1):
            n1, n2 = nums2,nums1
        
        #find the initial center
        l,r = 0,len(n1)-1

        total = len(n1)+len(n2)


        # check if they work
        while True:
            m1 = (l+r)//2 
            m2 = total//2 - m1- 2
            
            l1 = n1[m1] if m1 >=0 else float('-infinity')
            l2 = n2[m2] if m2 >=0 else float('-infinity')
            r1 = n1[m1+1] if m1+1<= len(n1)-1 else float('infinity')
            r2 = n2[m2+1] if m2+1<= len(n2)-1 else float('infinity')

            if max(l1,l2) <= min(r1,r2):
                # even case
                if total%2 :
                   return min(r1,r2)
                else: return  (max(l1,l2)+ min(r1,r2))/2
                # ie if you have 5 total, the middle is index 2, and your two n's have there middles at 0 and 1
                # then the actual index 2 for the concatinated string is the min(n1[m1+1],n2[m2+1])
            elif l1>r2:
                r = m1-1
            else:
                l = m1+1
            

