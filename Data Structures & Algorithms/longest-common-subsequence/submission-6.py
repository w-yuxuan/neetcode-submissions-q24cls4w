class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        t1,t2 = text1, text2

        dp = [[0]*(n+1) for _ in range(m+1)]
        # dp[0][0] = 1 if t1[0]==t2[0] else 0
        # dp[m-1][n-1] = 1 if t1[m-1]==t2[n-1]

        
        for i in range(m):
            for j in range(n):
                if t1[i]==t2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j],dp[i][j+1],dp[i+1][j])
        return dp[m][n]
                    