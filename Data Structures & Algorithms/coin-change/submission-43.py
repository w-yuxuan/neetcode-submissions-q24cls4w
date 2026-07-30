class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        mem = [float('inf')]*(amount+1)
        
        # while True:
            # for i in range(len(coins)):
        for c in coins:
            if c <= amount:
                mem[c]=1
        for c in coins:
            for a in range(amount+1):
                if a+c <= amount and mem[a] != float('inf'):
                # if a+c <= amount:
                    mem[a+c] = min(1+mem[a],mem[a+c])
    
        return mem[-1] if mem[-1] != float('inf') else -1


