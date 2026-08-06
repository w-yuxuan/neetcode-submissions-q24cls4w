class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        if len(s)==1:
            return 1

        def dfs(i):
            nonlocal res
            l=r=i
            while 0<=l<= r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                res +=1 
            l = i
            r = i+1
            while 0<=l<= r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                res +=1 
        for i in range(len(s)):
            dfs(i)
        return res

