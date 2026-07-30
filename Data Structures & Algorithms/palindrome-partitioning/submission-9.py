class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # decision at every letter is to include it in the current set of palindrome or to start a new palindrome 
        n = len(s)
        # if len(s)==1:return s
        res, part = [],[]

        def dfs(j,i):
            # base case 
            if i>n-1:
                if i==j:
                    res.append(part.copy())
                return 
            # record prev palindrome to start a new one for hte next letter: only if we have palindrome now 
            if palin(s[j:i+1]):
                part.append(s[j:i+1])
                dfs(i+1,i+1)# next function call will move the right side by1
                part.pop()
            # we can always try to inlucde one more letter 
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

        
        