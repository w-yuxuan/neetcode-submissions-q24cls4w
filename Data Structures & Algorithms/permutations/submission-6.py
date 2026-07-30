class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i,nums):
            if i == len(nums):
                return [[]]
            perms = dfs(i+1,nums)
            res = []

            for p in perms:
                
                for j in range(len(p)+1):
                    new = p.copy()
                    new.insert(j,nums[i])
                    res.append(new)
            return res
        return dfs(0,nums)