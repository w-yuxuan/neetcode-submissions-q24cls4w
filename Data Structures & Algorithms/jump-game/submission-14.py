class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # similar to target sum total: coin change
        stop = 0 
        for i in range(len(nums)):
            stop = max(nums[i],stop-1)
            if stop==0 and i<len(nums)-1:
                return False
        return True

