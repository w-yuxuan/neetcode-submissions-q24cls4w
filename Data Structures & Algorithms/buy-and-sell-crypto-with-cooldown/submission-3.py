class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices
        mem = {}
        def dfs(i,have):
            if (i,have) in mem:
                return mem[(i,have)]
            if i>=len(p):
                return 0
            if have: # have stock # can sell/hold
                mem[(i,have)]=max(dfs(i+1,1),dfs(i+2,0)+p[i])     
            else: # don't have stock: can buy/hold
                mem[(i,have)]=max(dfs(i+1,1)-p[i],dfs(i+1,0))
            return mem[(i,have)]
        return dfs(0,0)


            
            