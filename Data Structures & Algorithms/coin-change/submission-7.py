class Solution:
    def coinChange(self, coins: List[inf], amount: inf) -> inf:
        tot = 0
        count = 0
        mem = {}
        # mini = float('inf')
        def dfs(i,tot):
            if i>len(coins)-1:
                return float('inf')
            if (i,tot) in mem:
                return mem[(i,tot)]
            if tot>amount:
                mem[(i,tot)]=float('inf')
                return mem[(i,tot)]
            if tot==amount:
                mem[(i,tot)]=0
                return 0
            mem[(i,tot)] = min(dfs(i,tot+coins[i])+1,dfs(i+1,tot))
            return mem[(i,tot)]
        return -1 if dfs(0,0)==float('inf') else dfs(0,0)

            
            