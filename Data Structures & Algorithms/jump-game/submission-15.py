class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curmax = 0
        for i in range(len(nums)):
            # curmax-=1
            if i > curmax:
                return False
            curmax= max(curmax,i+nums[i])
            if curmax >= len(nums)-1:
                return True
        return False