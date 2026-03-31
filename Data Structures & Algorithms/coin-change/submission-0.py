class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        total = 0 
        ncoins = 0 #min num coins
        if amount == 0 :return 0

#cache stores ncoins min needed to get to this point? no you can totally not include any previous coins
        def dfs(cache,i,total):

            if total == amount:
                return 0

            if total > amount or i == len(coins) :  #any branch below will not work, other routes might
                return float('inf')

            if (i,total) in cache:
                return cache[(i,total)]

            cache[(i,total)] = min(dfs(cache,i+1,total),dfs(cache,i,total+coins[i])+1)

            return cache[(i,total)]
        if dfs(cache,0,0) == float('inf'):
            return -1
        else: return dfs(cache,0,0)
            

