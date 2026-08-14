class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1) , len(s2), len(s3)
    
        if l1+l2 != l3:
            return False

        dp = [[False]*(l2+1) for _ in range(l1+1)]
        dp[0][0]=True


        for i in range(l1+1): # dp 's indes i and j are one step ahead of the actual str index                
            for j in range(l2+1):
                k = i+j-1
                if i!= 0:
                    if s1[i-1] == s3[k] and dp[i-1][j] : # advance i
                        dp[i][j] = True 
                if j!= 0:
                    if s2[j-1] ==s3[k] and dp[i][j-1]:
                        dp[i][j] = True 
        
        return dp[l1][l2]




       

            
                
