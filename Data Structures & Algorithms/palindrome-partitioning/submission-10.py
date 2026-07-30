class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # decision at every letter is to include it in the current set of palindrome or to start a new palindrome 
        n = len(s)
        # if len(s)==1:return s
        res, part = [],[]

        def dfs(j):# iter over starting posi
            if j>n-1:
                res.append(part.copy())
                return

            for i in range(j,n):
                #if we found a palindrome
                if palin(s[j:i+1]):
                    part.append(s[j:i+1])
                    dfs(i+1)
                    part.pop()
            # dfs(j+1)    

  
        def palin(s):
            n = len(s)
            if len(s)==1:
                return True
            l,r = 0,n-1
            while l<r:
                if s[l]!=s[r]:
                    return False

                l+=1
                r-=1
            return True

        dfs(0)
        return res

        
        