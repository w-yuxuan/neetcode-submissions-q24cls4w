class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = prices
        dp = [[0]*len(p) for i in range(2)]
        dp[0][len(p)-1] = 0
        dp[1][len(p)-1] = p[len(p)-1]

        for i in range(len(p)-2,-1,-1):
            #buy or hold: list out possible paths to get here: sell from a 0 state or 1 st 
            dp[0][i]= max(dp[0][i+1],dp[1][i+1]-p[i])
            #sell or hold
            prof = dp[0][i+2] if i+2 < len(p) else 0 
            dp[1][i] = max(prof+p[i],dp[1][i+1]) 
        return dp[0][0] 