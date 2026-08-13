class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1) , len(s2), len(s3)
        if not (s1 or s2 or s3):
            return True       
        if l1+l2 != l3:
            return False 
        mem = {}

        def dfs(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            k = i+j
            if k == l3:
                mem[(i,j)] = True 
                return True 
            
            if i < l1 and s1[i] == s3[k]:
                if dfs(i+1,j):
                    mem[(i,j)] = True
                    return True

            if j < l2 and s2[j] == s3[k]:
                if dfs(i,j+1):
                    mem[(i,j)] = True
                    return True
            mem[(i,j)] = False
            return False
        return dfs(0,0)

            
                
