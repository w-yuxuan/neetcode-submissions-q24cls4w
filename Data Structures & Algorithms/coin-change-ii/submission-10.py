class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # sort(coins) no need,bc no repeat 
        # a = amount
        n=len(coins)
        mem = defaultdict(int)
        mem[amount]=1 # num ways to get to end 
        for c in coins:
            for a in range(amount,-1,-1):
                if a-c>=0:
                    mem[a-c] += mem[a] 
        return mem[0] 


        
            

