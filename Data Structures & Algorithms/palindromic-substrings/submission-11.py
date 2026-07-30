 # basic: n + n=1 +... is n^2 substrings, each cost n to check
       # improved:n^2 by expanding from a center we pick, assuming it's even/odd
class Solution:
    def countSubstrings(self, s: str) -> int:
        res= 0
        for i in range(len(s)):
            l = r = i 
            #odd
            while 0<=l<=r<=len(s)-1:
                if s[l] == s[r]:
                    res+=1
                else:
                    break
                l-=1
                r+=1

            r =  i
            l = i-1
            while 0<=l<=r<=len(s)-1:
                if s[l] == s[r]:
                    res+=1
                else:
                    break
                l-=1
                r+=1  
        return res