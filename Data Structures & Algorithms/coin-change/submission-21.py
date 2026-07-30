class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        mem = [[float('inf')]*(amount+1) for _ in range(n+1)]
        # Create a 2D grid: (amount + 1) rows, (n + 1) columns
        for i in range (n+1):
            mem[i][amount]=0
        # i=n
        # tot=amount-1
        c =coins
        for i in range(n-1,-1,-1):
            for tot in range(amount-1,-1,-1):
        # while i>=0 and tot >= 0:
                mem[i][tot] = min(mem[i][tot],mem[i+1][tot])
                if tot+c[i]<=amount:
                    mem[i][tot]= min(mem[i][tot],mem[i][tot+c[i]]+1,mem[i+1][tot+c[i]]+1)
        return -1 if mem[0][0]==float('inf') else mem[0][0]
