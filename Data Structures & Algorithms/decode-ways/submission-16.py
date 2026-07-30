class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}
        def dfs(i):
            if i in mem:
                return mem[i]
            if i>len(s)-1:
                return 1
            res = 0
            for j in range(i+1,len(s)+1):
                new = s[i:j]
                if new[0] != '0' and int(new) <=26:
                    res += dfs(j)
            mem[i]=res
            return res

        return dfs(0)
