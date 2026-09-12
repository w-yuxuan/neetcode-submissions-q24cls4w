class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if len(nums) == 1:
            return nums
        
        
        mid = n//2
        l,r = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])
        
        # def dfs(l,r):
        res = []
        i=j=0
        while i<mid and j< n-mid:
            if l[i]<=r[j]:
                res.append(l[i])
                i+=1
            else:
                res.append(r[j])
                j+=1
        res.extend(l[i:])
        res.extend(r[j:])
        return res
