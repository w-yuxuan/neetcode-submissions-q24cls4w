class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # c = coins
        cur,res = [],[]
        mem = [float('inf')]*(amount+1) 
        mem[0]=0

        for a in range(amount+1):
            for c in coins:
                if a+c<=amount:
                    mem[a+c]=min(mem[a]+1,mem[a+c])
        return -1 if mem[amount]==float('inf') else mem[amount]

            
            



