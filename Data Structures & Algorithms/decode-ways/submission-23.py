class Solution:
    def numDecodings(self, s: str) -> int:
        def check(st):
            
            if not st or int(st)>26 or st[0]=='0':
                return False 
            return True
        mem = [0]*(len(s)+2)
        mem[len(s)]=1
        # mem[-2]=1
        for i in range(len(s)-1,-1,-1):
            res = 0
            if check(s[i:i+1]):
                res += mem[i+1]

            if check(s[i:i+2]):
                res += mem[i+2]

            mem[i] = res
        return mem[0]
                 
            