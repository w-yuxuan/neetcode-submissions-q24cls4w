class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        cur = []
        res = []
        n = len(nums)
        def dfs(i,tot):
            
            if target == tot:
                res.append(cur.copy())
                return

            if i > n-1 or tot > target :
                return
            
            cur.append(nums[i])
            dfs(i+1,tot+nums[i])
            cur.pop()

            while i+1 <= n-1 and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1,tot)
            
        dfs(0,0)
        return  res