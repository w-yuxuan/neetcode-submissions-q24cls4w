class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float('inf')]*(amount+1)
        mem[0] = 0

        for i,m in enumerate(mem):
            if m == float('inf'):
                continue
            for c in coins:
                if i+c <= amount:
                    mem[i+c] = min(mem[i+c],mem[i]+1)
        return mem[-1] if mem[-1]!=float('inf') else -1