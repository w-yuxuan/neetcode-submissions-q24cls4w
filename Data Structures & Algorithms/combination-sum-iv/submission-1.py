class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = {}
        def dfs(tot): # how many so far
            res = 0

            if tot > target:
                return 0

            if tot == target:
                mem[tot]=1
                return 1
            
            if tot in mem:
                return mem[tot]

            for j in range(n):
                new = tot+nums[j]
                res += dfs(new)
            mem[tot] = res
            return res
        return dfs(0)
            



