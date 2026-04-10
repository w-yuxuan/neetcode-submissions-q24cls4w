class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # decision at every letter is to include it in the current set of palindrome or to start a new palindrome 
        n = len(s)
        # if len(s)==1:return s
        res, part = [],[]

        def dfs(j,i):
            # base case- if we are done traversing s
            if i > n-1:
                if i==j:
                    res.append(part.copy())
                return
            #case 1: start a new branch only when we find a palindrome
            if palin(s[j:i+1]):
                part.append(s[j:i+1])
                dfs(i+1,i+1)
                part.pop()
            #case 2: we can always keep on adding letters to the current
            dfs(j,i+1)
  
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

        dfs(0,0)
        return res

        
        