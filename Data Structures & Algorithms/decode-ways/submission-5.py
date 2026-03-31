class Solution:
    def numDecodings(self, s: str) -> int:
        ways = 0
        def dfs(i):
            nonlocal ways

            if i >= len(s):
                ways +=1
                return

            if s[i] == '0': return 
            #if int(s[i] ) > 0: # can be a single value, checked last line already
            if int(s[i] ) <3 and i+1<=len(s)-1 and int(s[i:i+2])<=26: # can form a double 
                dfs(i+2)
            dfs(i+1) # don't write else, always check 

        dfs(0)
        return ways
