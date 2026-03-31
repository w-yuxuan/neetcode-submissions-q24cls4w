class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(cache,i,total):
            if amount == total:
                return 0
            if i > len(coins)-1 or total > amount:
                return float('inf') #this only gets added more 1s up the chain, and it can only stay as inf
#one big issue is I thought with the wrong order last time: I thought about how the numbers change as I walk from top down
#same dir as my code, but when it executes the recur causes the bottom layer to be aclculated first. That causes me to think a 
# top node breaking the total>amount rule ruins all nodes after it, but it's the reverse
            
            if (i,total) in cache:
                return cache[(i,total)]

            #don't include 
            cache[(i,total)] = min(dfs(cache,i,total+coins[i])+1,dfs(cache,i+1,total))
            return cache[(i,total)]
        if dfs(cache,0,0) == float('inf'): return -1
        else: return dfs(cache,0,0)