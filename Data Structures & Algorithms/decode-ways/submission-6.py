class Solution:
    def numDecodings(self, s: str) -> int:
        ways = 0
        def dfs(i):

            if i >= len(s):
                return 1

            if s[i] == '0': return 0
            #if int(s[i] ) > 0: # can be a single value, checked last line already
            if int(s[i] ) <3 and i+1<=len(s)-1 and int(s[i:i+2])<=26: # can form a double 
                return dfs(i+2)+dfs(i+1)
            else:
                return dfs(i+1) # don't write else, always check 
             

        return dfs(0)
