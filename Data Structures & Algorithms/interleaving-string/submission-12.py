class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1) , len(s2), len(s3)
    
        if l1+l2 != l3:
            return False

        dp = [[False]*(l2+1) for _ in range(l1+1)]
        dp[0][0]=True

        for i in range(1,l1+1):
            if s1[i-1] == s3[i-1] and dp[i-1][0]:
                dp[i][0] = True

        for j in range(1,l2+1):
            if s2[j-1] == s3[j-1] and dp[0][j-1]:
                dp[0][j] = True

        for i in range(1,l1+1): # dp 's indes i and j are one step ahead of the actual str index                
            for j in range(1,l2+1):
                k = i+j-1 # The character in s3 we are trying to match right now is at 0-based index: k = i + j - 1: when I j both 1,both use 1 number,  k check 1
                # use str index 0 and 0 as an ex, dp indicees are 1 and 1, 
                if s1[i-1] == s3[k] and dp[i-1][j] : # advance i
                    dp[i][j] = True 

                if s2[j-1] ==s3[k] and dp[i][j-1]:# imagine i'm trying to fill dp[1][1], i look one box up at dp[1][0], and check if the first element s2[j-1] is the same as k 
                    dp[i][j] = True 
        
        return dp[l1][l2]




       

            
                
