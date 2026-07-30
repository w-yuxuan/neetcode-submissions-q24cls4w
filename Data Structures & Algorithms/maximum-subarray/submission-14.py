class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmax = 0
        globmax = nums[0]

        for i in range(len(nums)) :
            curmax = max(0,curmax)
            curmax += nums[i]
            globmax=max(globmax,curmax)
        
        return globmax