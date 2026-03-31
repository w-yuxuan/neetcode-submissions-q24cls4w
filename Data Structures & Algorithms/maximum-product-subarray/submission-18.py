class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur = 1
        maxv= maxb = nums[0]
        for i in range(len(nums)):
            if nums[i] == 0:
                cur = 1
                maxv = max (maxv,0)
            else:    
                cur *= nums[i]
                maxv = max(maxv,cur)
            
        cur = 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                cur = 1
                maxb = max (maxb,0)
            else:
                cur *= nums[i]
                maxb = max(maxb,cur)

        return max(maxv,maxb)
