class Solution:
    def numDecodings(self, s: str) -> int:
        def check(st):
            # if not st
            if int(st)>26 or st[0]=='0':
                return False 
            return True
        mem = {}
        def dfs(i):
            if i in mem:
                return mem[i]

            if i==len(s)-1:
                if check(s[i:i+1]):
                    mem[i] =1
                    return 1
                else: 
                    mem[i] = 0
                    return 0
            res = 0
            if i<=len(s)-1:
                if check(s[i:i+1]):
                    res += dfs(i+1)
            if i<=len(s)-2: 
                if check(s[i:i+2]):
                    res += dfs(i+2)
            else:
                mem[i] = 1
                return 1
            mem[i] = res
            return res
        return dfs(0)
                 
            