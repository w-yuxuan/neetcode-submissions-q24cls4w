class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = [0] * (amount + 1)
        mem[amount] = 1 
        
        for c in coins:
            # Safely iterate backward. No 'if' statement needed!
            for j in range(amount - c, -1, -1):            
                mem[j] += mem[j + c]
        
        return mem[0]