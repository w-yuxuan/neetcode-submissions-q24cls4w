class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        c = coins
        mem = [[float('inf')]*(n+1) for _ in range(amount+1)]
        mem[-1] = [0]*(n+1) #0 to n-1
        for i in range(n-1,-1,-1):
            for tot in range(amount-1,-1,-1):
                mem[tot][i] = min(mem[tot][i],mem[tot][i+1])
                if tot+c[i]<=amount:
                    mem[tot][i] = min(mem[tot][i],mem[tot+c[i]][i]+1,mem[tot+c[i]][i+1]+1)
        return -1 if mem[0][0]==float('inf') else mem[0][0] 

