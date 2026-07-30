class Solution:    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # basic : try all n^total possibilities
        # trap: least is not when you always take the largest coin 
        if amount == 0: return 0
        coins.sort()
        # res = float('inf')
        mem = [float('inf')]*(amount+1)
        for c in coins:
            if c <= amount: mem[c] = 1
        
        for j in range(1, amount + 1):
            if mem[j] != float('inf'):
                for c in coins:
                    if j + c > amount:
                        break
                    mem[j + c] = min(mem[j + c], mem[j] + 1)

        return mem[amount] if mem[amount] != float('inf') else -1