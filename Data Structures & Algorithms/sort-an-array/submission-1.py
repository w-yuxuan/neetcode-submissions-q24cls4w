class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<=1:
            return nums
        
        mid = n//2 
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        
        def two(a,b):
            res = []
            l,r = 0,0
            while l<len(a) and r<len(b):
                if a[l]> b[r]:
                    res.append(b[r])
                    r+=1
                else: #nums[l] <= nums[r]:
                    res.append(a[l])
                    l+=1
            res.extend(a[l:])
            res.extend(b[r:])
            return res

        return two(left,right)


        