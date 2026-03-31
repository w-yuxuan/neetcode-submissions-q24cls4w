class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curmax = 0
        globmax = nums[0]
        for i in range(len(nums)):
            # clear add floor
            curmax = max(0,curmax)
            curmax += nums[i]
            globmax = max(curmax,globmax)
        return globmax
