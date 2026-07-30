class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # sort(coins) no need,bc no repeat 
        a = amount
        n=len(coins)
        mem = defaultdict(int)
        # mem[amount]=1
        def dfs(i,tot): #num ways to sum to amt from this state
            if i>n-1:
                return 0
            if tot>a:
                return 0
            if tot==a:
                return 1
            if (i,tot) in mem:
                return mem[(i,tot)]

            
            mem[(i,tot)]+= dfs(i+1,tot)+dfs(i,tot+coins[i])
            return mem[(i,tot)]
        return dfs(0,0)
        
            

