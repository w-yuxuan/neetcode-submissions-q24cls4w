class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxv = nums[0]
        # clear add floor 
        for i,val in enumerate(nums):
            if cur < 0:
                cur = 0
            cur += val
            maxv = max(maxv,cur)
        return maxv