class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        stop = len(nums) - 1

        res=False
        for i in range(len(nums) - 2, -1, -1):
            n = nums[i]
            if n + i >= stop:
                res=True
                stop=i
            else:
                res=False
        return res