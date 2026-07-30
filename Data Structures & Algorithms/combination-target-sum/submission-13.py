class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def dfs(i,tot):
            if tot > target or i>len(nums)-1:
                return
            
            if tot == target:
                res.append(cur.copy())
                return
             
            cur.append(nums[i])
            dfs(i,tot+nums[i])
            cur.pop()

            dfs(i+1,tot)
        dfs(0,0)
        return res        