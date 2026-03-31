#need to improve
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i): # how many steps left from prev jump is not useful, once we land there is nothing "left"
            if i >= len(nums)-1:
                return True
            res = False
            for stp in range(1,nums[i]+1):
                if dfs(i+stp):
                    res= True
            return res
        return dfs(0)