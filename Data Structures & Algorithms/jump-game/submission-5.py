class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxdist = 0
        for i in range(len(nums)):
            if i > 0 and maxdist == 0:
                return False
            maxdist = max(maxdist-1,nums[i])
            if i+maxdist >= len(nums)-1:
                return True
        return False