class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # least value is 1, i need to choose "amount" of them to fill, so  2^t possible pairs
        # if amount ==0:
        #     return 0

        #bottom up:
        dp = [float('inf')]*(amount+1)
        dp[-1]=0
        
        # 
        for a in range(amount-1,-1,-1):
            # for i in range(len(coins)):
            # don't add the line to 
            for i in range(len(coins)-1,-1,-1):
                if coins[i]+ a  > amount:
                    continue
                if coins[i]+ a ==amount:
                    dp[a] = 1
                dp[a] = min(dp[a],dp[a+coins[i]]+1)
        return dp[0] if dp[0]!= float('inf') else -1 
            