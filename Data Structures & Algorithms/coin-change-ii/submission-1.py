class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        def dfs(i,total):#compute the number of unique ways 
            if total == amount:
                return 1
            if i > len(coins)-1 or total > amount:
                return 0
            if (i,total) in cache:
                return cache[(i,total)]
            #keep including  the current
            res1 = dfs(i,total+coins[i])
            #not current, jumpt to next
            while i <= len(coins)-1 and coins[i]==coins[i-1]:
                i+=1
            res2=dfs(i+1,total)
            cache[(i,total)] = res1+res2
            return cache[(i,total)]
        return dfs(0,0)
