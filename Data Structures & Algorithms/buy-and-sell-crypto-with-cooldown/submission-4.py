class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        p = prices
        if len(p)<2:
            return 0
        dp = [[0]*len(p) for i in range(2)]
        dp[0][len(p)-1] = 0
        dp[1][len(p)-1] = -p[0]

        dp[0][1] = max(p[1]-p[0],0) # i sold day 1 purchase or didn't buy again
        dp[1][1] = max(-p[0],-p[1]) # i held the day 1 purchase or just bought

        for i in range(2,len(p)):
            #sold or hold: list out possible paths to get here: sell from a 0 state or 1 st 
            dp[0][i]= max(dp[0][i-1],dp[1][i-1]+p[i])
            #bought or hold
            dp[1][i] = max(dp[0][i-2]-p[i],dp[1][i-1])
        
        return dp[0][len(p)-1]
        # return max(dp[0][i] for i in range(2))
        

