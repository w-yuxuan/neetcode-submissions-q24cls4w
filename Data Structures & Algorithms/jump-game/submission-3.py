#need to improve
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        def dfs(i): # how many steps left from prev jump is not useful, once we land there is nothing "left"
            if i >= len(nums)-1:
                mem[i]=True
            if i in mem:
                return mem[i]
            mem[i] = False
            for stp in range(1,nums[i]+1):
                if dfs(i+stp):
                    mem[i] = True
            return mem[i]
        return dfs(0)