class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = 0
        cache = {}
        def find(i,total): # return the fewest num coins needed to get to amount
            if total == amount:
                return 0
            if i>len(coins)-1 or total > amount:
                return 2*10**31-1
            if (i,total) in cache:
                return cache[(i,total)]
            
            #include coin i
            cache[(i,total)]= min(find(i,total+coins[i])+1,find(i+1,total))
            return cache[(i,total)]
        
        return find(0,0) if find(0,0)!=2*10**31-1 else -1