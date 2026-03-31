class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0: return 0
        mem = [-1]*(amount+1)
        mem[0]=0
        def bfs(tot): #return min coins to a sum == tot
            if tot<0:
                return float('inf')                
            # if tot == 0:
            #     return 0
            if mem[tot]!=-1:
                return mem[tot]
            
            mem[tot] = float('inf')  
            for j,n in enumerate(coins):
                # nonlocal tot
                mem[tot] = min(mem[tot],bfs(tot-n)+1)
            return mem[tot]
        res = bfs(amount)            
        return -1 if res==float('inf') else res