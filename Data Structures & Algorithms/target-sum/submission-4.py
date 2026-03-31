class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        #stores nways as output, use i and curSum as labels
        def dfs(cache,i,curSum):
            #oo bounds
            if i > len(nums)-1:
                if curSum == target:
                    return 1
                else: return 0

            if (i,curSum) in cache:
                return cache[(i,curSum)]

            cache[(i,curSum)] = cache.get((i,curSum),0)+ dfs(cache,i+1,curSum+nums[i]) + dfs(cache,i+1,curSum-nums[i])
            return cache[(i,curSum)]

        return dfs(cache,0,0)


