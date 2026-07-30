class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = {}
        def dfs(a,i):
            if (a,i) in mem:
                return mem[(a,i)]
            if a == amount:
                return 1
            if a > amount or i > len(coins)-1:
                return 0 
            
            res = 0
            res += dfs(a+coins[i],i)
            res += dfs(a,i+1)
            mem[(a,i)] = res
            return res

        return dfs(0,0) 