class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []
        tot=0

        def dfs(i,tot):
            if tot==target:
                res.append(cur.copy())
                return 
            if i>len(nums)-1 or tot>target:
                return
            
            cur.append(nums[i])
            dfs(i,tot+nums[i])
            cur.pop()

            dfs(i+1,tot)

        dfs(0,0)
        return res
                