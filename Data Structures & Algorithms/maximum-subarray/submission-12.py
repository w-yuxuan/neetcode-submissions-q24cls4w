class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        curmax= 0
        globmax = nums[0]
        for i,n in enumerate(nums):
            if curmax <0:
                curmax = 0
            curmax += n
            globmax = max(globmax,curmax)
        return globmax
