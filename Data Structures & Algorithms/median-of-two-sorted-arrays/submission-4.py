class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:       
        n1,n2 = nums1,nums2
        if len(n1)>len(n2):
            n1,n2 = nums2,nums1
        res = 0
        l,r = 0,len(n1)-1
        #initialize m1 m2
        # m1 = (l+r)//2
        # m2 = len(nums1+nums2)//2-m1-2 # pick up the rest of the value to make a sum ototal of half of (m+n)
        
        # check if they work, if it doesn't, do
        while True:
            m1 = (l+r)//2
            m2 = len(nums1+nums2)//2-m1-2

            left1 = n1[m1] if m1>=0 else float('-infinity')
            left2 = n2[m2] if m2>=0 else float('-infinity')
            right1 = n1[m1+1] if m1+1<=len(n1)-1 else float('infinity')
            right2 = n2[m2+1] if m2+1<=len(n2)-1 else float('infinity')

            if max(left1,left2) <= min(right1,right2):
                # claculate the median given even/odd:
                if len(nums1+nums2)%2==0:
                    res = (max(left1,left2) + min(right1,right2))/2
                else:
                    res = min(right1,right2)
                return res
            elif left1 > right2:
                r = m1-1
            else: l=m1+1








