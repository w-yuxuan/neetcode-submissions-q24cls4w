#somehow this works with not efficient
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # basic : try all n^total possibilities
        # trap: least is not when you always take the largest coin 
        coins.sort()
        # res = float('inf')
        mem = [float('inf')]*(amount+1)
        for i,c in enumerate(coins):
            if c<=amount:
                mem[c] = 1
        if amount == 0:
            return 0
        for j in range(1,amount+1):
            if mem[j]!=float('inf'):
                for k,c in enumerate(coins):
                    if j+c>amount:
                        break
                    mem[j+c]=min(mem[j]+1,mem[j+c])

        return mem[-1] if mem[-1]!=float('inf') else -1
