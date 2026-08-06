class Solution:
    def numDecodings(self, s: str) -> int:
        def check(st):
            
            if not st or int(st)>26 or st[0]=='0':
                return False 
            return True
        mem = {}
        def dfs(i):
            if i in mem:
                return mem[i]
            if i==len(s):
                mem[i] =1
                return 1

            res = 0
            if check(s[i:i+1]):
                res += dfs(i+1)

            if check(s[i:i+2]):
                res += dfs(i+2)

            mem[i] = res
            return res
        return dfs(0)
                 
            