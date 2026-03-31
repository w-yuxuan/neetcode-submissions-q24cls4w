class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr,res = [], []
        total =0
        #as long as one index don't repeatedly appear, you good 
        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i > len(nums)-1:
                return

            curr.append(nums[i])            
            dfs(i,curr,total+nums[i]) # keep choosing me 
            curr.pop()

            dfs(i+1,curr,total) # move to next if the prev num can't work
        dfs(0,curr,total)
        return res