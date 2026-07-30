class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums=candidates
        nums.sort()
        res = []
        cur = []

        def dfs(i,tot):
            if tot == target:
                res.append(cur.copy())
                return
            if tot > target or i>len(nums)-1:
                return
            

            cur.append(nums[i])
            dfs(i+1,tot+nums[i])
            cur.pop()

            while i+1 <= len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1,tot)

        dfs(0,0)
        return res    