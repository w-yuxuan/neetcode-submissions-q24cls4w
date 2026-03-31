class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # like a subset: except update a sum var, and compare to minRes if i hit the amount 
        minRes = float('inf')
        res = 0
        memo = {}
        def dfs(amt): # find the min num at that amt
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            
            res = 1e9
            for i,coin in enumerate(coins):
                if amt-coin >=0:
                    res = min(res,1+dfs(amt-coin))
            memo[amt]=res
            return res
        mincoins = dfs(amount)
        return -1 if mincoins >= 1e9 else mincoins


            
        