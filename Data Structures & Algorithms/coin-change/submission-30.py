class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float('inf')]*(amount+1)
        res[0]=0
        # for c in coins:
        #     res[c]=1

        # i = 1
        # while i<=len(res)-1 and res[i]!=float('inf'): #replaces for and if two lines 
        for i in range(0,len(res)):
            if res[i]!=float('inf'):
                for co in coins:
                    if i+co <= len(res)-1:res[i+co]=min(res[i]+1,res[i+co])
        return -1 if res[amount]==float('inf') else res[amount]