class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        mem = [0]*(amount+1)
        mem[amount]=1
        for c in coins:
            for a in range(amount,-1,-1):
                if a-c >= 0:
                    mem[a-c]+= mem[a]
        return mem [0] 

            