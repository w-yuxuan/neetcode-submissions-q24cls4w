class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float('inf')]*(amount+1)
        mem[0]=0
        for cur_tot in range(0,1+amount):
            for coin in coins:
                new_tot = cur_tot+coin
                if new_tot<=amount:
                    mem[new_tot]=min(mem[new_tot],mem[cur_tot]+1)
        return mem[amount] if mem[amount]!=float('inf') else -1
