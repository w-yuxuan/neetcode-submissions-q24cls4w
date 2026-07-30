class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == len(nums2) ==0:
            return 0
        res = []
        # if len(nums1) == 0:
        #     res = nums2
        # if len(nums2) == 0:
        #     res = nums1
        
        n1 = n2 = 0
        while n1 <= len(nums1)-1 and n2 <= len(nums2)-1:
            d1, d2 = nums1[n1], nums2[n2]
            if d1<d2:
                res.append(d1)
                n1+=1
            else:
                res.append(d2)
                n2+=1
        res.extend(nums1[n1:])
        res.extend(nums2[n2:])

        if len(res)%2 == 0:
            mid = len(res)//2
            return sum(res[mid-1:mid+1])/2
        else: 
            mid = len(res)//2
            return res[mid]

        