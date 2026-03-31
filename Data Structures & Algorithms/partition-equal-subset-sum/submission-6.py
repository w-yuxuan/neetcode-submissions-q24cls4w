class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False
        COL = total//2
        ROW = (len(nums))
        cache = [[None]*(COL+1) for i in range(ROW)]
        # how to determine cache content: it depends on the pointers you use to identify individual branches: their characteristics 
        def dfs(cache,i,total):
            # don't write base case: when you do cache always write the base case in the cache matrix
            # but in the cases below that would be out of boudns of the cache matrix so we need to write it out 

            if total > COL or total < 0 or i > ROW-1: return False

            if total == COL: return True 

            if cache[i][total] != None:
                return cache[i][total] 
            # don't include
            #cache[i+1][total] = 

            #include
            #cache[i+1][total] = dfs(cache,i+1,total+nums[i])

            #combined cases
            cache[i][total] = dfs(cache,i+1,total+nums[i]) or dfs(cache,i+1,total)
            #return cache
            return cache[i][total]
        return dfs(cache,0,0)
        
            
            
