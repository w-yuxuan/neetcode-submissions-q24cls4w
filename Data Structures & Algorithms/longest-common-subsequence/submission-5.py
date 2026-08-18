class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dumb: compare all possib: 2^n+2^m to generate, another (2^n*2^m) to compare
        # at each point if they don't agree i can move either pointer forward by 1 step
        m,n = len(text1),len(text2)
        t1,t2 = text1, text2
        mem = {}
        def dfs(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i > m-1:
                return 0
            if j > n-1:
                return 0
            res= 0
            if t1[i]==t2[j]:
                mem[(i,j)] = dfs(i+1,j+1)+1
                return dfs(i+1,j+1)+1
            mem[(i,j)]=max(res,dfs(i+1,j),dfs(i,j+1))
            return max(res,dfs(i+1,j),dfs(i,j+1))
            
        return dfs(0,0)
         
            
            

        

