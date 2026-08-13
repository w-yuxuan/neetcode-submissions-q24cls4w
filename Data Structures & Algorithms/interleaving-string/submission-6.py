class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        m,n = len(s1), len(s2)
        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        # dp[m+1][n+1]=1

        dp[0][0]=True

        for i in range(1,m+1):
            k = i-1
            if dp[i-1][0] and s1[i-1]==s3[k]: 
                dp[i][0]=True
            
        for j in range(1,n+1):
            k = j-1
            if dp[0][j-1] and s2[j-1]==s3[k]:
                dp[0][j]=True            

        for i in range(1,m+1):
            for j in range(1,n+1):
                k = i+j-1
                if dp[i][j-1] and s2[j-1]==s3[k]:
                    dp[i][j]=True

                if dp[i-1][j] and s1[i-1] == s3[k]:
                    dp[i][j]=True

        return dp[m][n]
            




        