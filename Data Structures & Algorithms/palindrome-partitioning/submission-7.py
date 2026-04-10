class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # decision at every letter is to include it in the current set of palindrome or to start a new palindrome 
        n = len(s)
        # if len(s)==1:return s
        res, part = [],[]

        def dfs(i):
            if i > n-1: # what if we have a string in the middle that is not a palindrome?
                res.append(part.copy())
                return
            for j in range(i,n): # this is the keep trying to create the larges palindrome option. don't need to add to result as it will be done when we reach the end, base case
                if palin(s[i:j+1]):
                    part.append(s[i:j+1]) # this is the create new palindrome option: add 'a' alone and then find palindromes in the rest of s
                    dfs(j+1)
                    part.pop()
                # if false then we don't do the prev 3 lines and don't open a new search branch
                                           
  
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

        
        