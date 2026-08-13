class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i=j=k=0
        if len(s2)+len(s1) != len(s3):
            return False
        # if not (s1 and s2 and s3):
        #     return True
        mem = {}

        def dfs(i,j):
            if (i,j) in mem:
                return mem[(i,j)]

            k = i+j
            if k == len(s3):
                mem[(i,j)] = True
                return True
            
            if i<len(s1) and s3[k]==s1[i]:
                if dfs(i+1,j):
                    mem[(i,j)]=True                    
                    return True
                
            if j<len(s2) and s3[k]==s2[j]:
                if dfs(i,j+1):
                    mem[(i,j)]=True
                    return True
                    
            mem[(i,j)]=False
            return False                

        return dfs(0,0)