class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #log(m*n) = log m + log n
        i = j = 0
        mem = deque()
        while i<=len(nums1)-1 and j<=len(nums2)-1:
            p,q = nums1[i], nums2[j]
            if p <= q:
                mem.append(p)
                i+=1
            else:
                mem.append(q)
                j+=1
        mem.extend(nums1[i:])
        mem.extend(nums2[j:])

        if len(mem)%2 ==0:
            # res = (mem[len(mem)//2] + mem[len(mem)//2+1] )/2 # IndexError: deque index out of range if 0 elements
            res = (mem[len(mem)//2] + mem[(len(mem)//2)-1] )/2
        else:
            res = mem[len(mem)//2]
        return res

