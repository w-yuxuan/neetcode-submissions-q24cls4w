class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        mem = {}
        def dfs(i,tot): #coins needed from now 
            if i>n-1 or tot>amount:
                return float('inf')
            if tot==amount:
                return 0
            if (i,tot) in mem:
                return mem[i,tot]
            mem[i,tot]=min(dfs(i+1,tot+coins[i])+1,dfs(i+1,tot),dfs(i,tot+coins[i])+1)
            return mem[i,tot]
        return -1 if dfs(0,0)==float('inf') else dfs(0,0)
