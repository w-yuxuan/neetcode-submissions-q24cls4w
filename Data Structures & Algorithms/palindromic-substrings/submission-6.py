class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            #odd case
            r,l = i,i
            while 0 <=l <=r <= len(s)-1 and  s[r]==s[l]:
                r+=1
                l-=1
                res+=1

            r,l = i+1,i
            while 0 <=l < r <= len(s)-1 and  s[r]==s[l]:
                r+=1
                l-=1
                res+=1
        return res






