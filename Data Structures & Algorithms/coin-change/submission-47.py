class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[-1] = 0

        for a in range(amount-1,-1,-1):
            for i in range(len(coins)):
                if a + coins[i] > amount:
                    continue
                # if dp[a]==float('inf'):
                #     continue
                dp[a] = min(dp[a],dp[a+coins[i]]+1)
        return dp[0] if dp[0]!=float('inf') else -1

