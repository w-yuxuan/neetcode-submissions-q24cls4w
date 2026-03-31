class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        #edge cases
        if total%2 != 0: return False
        COL = total//2
        ROW = len(nums)
        cache = [[None]*(COL+1) for i in range(ROW)]
        def dfs(cache,i,curSum):
            #base cases
            if i>ROW-1 or i<0 or curSum>COL or curSum <0:
                return False
            if curSum == COL: return True
            if cache[i][curSum] is not None:
                return cache[i][curSum]
            #calc and write result to cache
            #don't include i
            cache[i][curSum] = dfs(cache,i+1,curSum) or dfs(cache,i+1,curSum+nums[i])
            return cache[i][curSum]
        return dfs(cache,0,0)






