class Solution:
    def numDecodings(self, s: str) -> int:
        ways = 0
        def dfs(i):
            nonlocal ways

            if i >= len(s):
                ways +=1
                return

            if s[i] == '0': return 

            for j in range(i+1,len(s)+1):
                cur =  s[i:j]
                if int(cur) <= 26:
                    dfs(j)
                else:
                    break
        
        dfs(0)
        return ways
