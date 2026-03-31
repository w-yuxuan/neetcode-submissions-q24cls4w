class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr,res = [], []
        total =0
        nums.sort()
        #as long as one index don't repeatedly appear, you good 
        def dfs(i,curr,total):
            if total == target:
                res.append(curr.copy())
                return
            if i > len(nums)-1 or total > target:
                return

            for j in range(i,len(nums)):
                # if nums[j]!= nums[j-1]:
                    curr.append(nums[j])
                    dfs(j,curr,total+nums[j])
                    curr.pop()
            #i+=1
            #dfs(i+1,curr,total)
 
        dfs(0,curr,total)
        return res
