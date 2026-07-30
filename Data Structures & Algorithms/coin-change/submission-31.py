class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # basic : try all n^total possibilities
        # trap: least is not when you always take the largest coin 

        # res = float('inf')
        mem = {}

        def dfs(total): # amount of coins needed to reach this total  
               
            if total==0:
                return 0
            if total < 0:
                return float('inf')
            if total in mem:
                return mem[total]
            res = float('inf')
            for i,c in enumerate(coins):
                res = min(res,1+dfs(total-c))
            mem[total] = res
            return mem[total]

        return dfs(amount) if dfs(amount)!= float('inf') else -1

