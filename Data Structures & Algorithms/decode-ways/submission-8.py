class Solution:
    def numDecodings(self, s: str) -> int:
        ways = 0
        mem=[0]* (len(s)+1)

        mem[len(s)]=1
 
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0': 
                mem[i]=0 
                continue               

            if i<len(s)-1 and int(s[i:i+2])<=26:
                mem[i] += mem[i+2]
            # if i>0:
            mem[i] += mem[i+1]
        return mem[0]
