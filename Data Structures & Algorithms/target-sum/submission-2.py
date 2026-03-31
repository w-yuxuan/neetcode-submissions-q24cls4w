class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # each number i have 2 options: add or substract: 0-1 knapsack 
        # each case is characterized by curSum and i pointer
        ROW = len(nums)
        #COL = 2*target
        cache = {}

        def dfs(cache,i,curSum): # returns num ways 
            # if i > ROW -1: #allow for curSum over the target since it can be substracted back later
            #     cache[(i,curSum)]=0
            #     return cache[(i,curSum)]
            if i == ROW:
                if curSum == target:
                    cache[(i,curSum)]=  + 1
                else: cache[(i,curSum)] = 0
                return cache[(i,curSum)]
            if  (i,curSum) in cache:
                return cache[(i,curSum)]
            #add cur num
            cache[(i,curSum)]= dfs(cache,i+1,curSum+nums[i]) + dfs(cache,i+1,curSum-nums[i])
            return cache[(i,curSum)]
        return dfs(cache,0,0)

