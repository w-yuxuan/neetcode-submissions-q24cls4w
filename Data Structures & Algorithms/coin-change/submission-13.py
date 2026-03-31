class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:return 0
        mem = {}
        def dfs(tot):# return num coins needed
            if tot<0:
                return float('inf')
            if tot in mem:
                return mem[tot]
            if tot==0:
                return 0
            #havent seen this before, calc it
            # def res so that we can find the min amount at each for loop level
            # ie ea level is one added coin, the loop loops over ea coin
            #ie if i need to sum to 3, i want 1,2 not 1,1,1

            res = float('inf')
            for i,coin in enumerate(coins):
                res = min(dfs(tot-coin)+1,res)
            mem[tot]=res
            return mem[tot]
        output=dfs(amount)
        return -1 if output  == float('inf') else output
