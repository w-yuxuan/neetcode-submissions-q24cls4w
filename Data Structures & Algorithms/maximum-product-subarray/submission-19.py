class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur = 1
        maxv= maxb = nums[0]
        for i in range(len(nums)):
            cur *= nums[i]
            maxv = max(maxv,cur)
            if nums[i] == 0:
                cur = 1
        
        cur = 1
        for i in range(len(nums)-1,-1,-1):

            cur *= nums[i]
            maxb = max(maxb,cur)
            if nums[i] == 0:
                cur = 1

        return max(maxv,maxb)
