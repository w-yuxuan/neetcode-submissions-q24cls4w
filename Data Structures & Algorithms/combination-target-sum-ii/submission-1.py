class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        curr,res = [], []
        total =0
        nums.sort()
        #as long as one index don't repeatedly appear, you good 
        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i > len(nums)-1:
                return


            curr.append(nums[i])            
            dfs(i+1,curr,total+nums[i])
            curr.pop()
            while i < len(nums)-1 and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1,curr,total)
        dfs(0,curr,total)
        return res