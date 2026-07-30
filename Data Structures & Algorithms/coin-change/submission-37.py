#somehow this works with not efficient
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # basic : try all n^total possibilities
        # trap: least is not when you always take the largest coin 

        # res = float('inf')
        mem = [float('inf')]*(amount+1)
        mem[0] = 0

        for j in range(amount+1):
            for k,c in enumerate(coins):
                if j+c>amount:
                    continue # since coins no longer sorted
                mem[j+c]=min(mem[j]+1,mem[j+c])

        return mem[-1] if mem[-1]!=float('inf') else -1
