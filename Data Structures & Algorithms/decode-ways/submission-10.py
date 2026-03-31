class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0]*(len(s)+1)
        res[len(s)]=1 # how many ways until this digit

        # def dfs(i):

            
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0': #start with 0
                res[i]=0 
                continue
            # if i see a 0 while moving forward, i should document num ways i can arrange the digits
            #i passed behind me, and see if the next digit is a 1 or 2 in next condition to add one to "ways"
            # else i need to return 0 as there's no way to decode

            res[i] = res[i+1]
            if i<=len(s)-2 and int(s[i])<3 and int(s[i:i+2])<27:
                res[i]+=res[i+2]
            
            # for i in range(j:len(s)+1):
        # dfs[0]
        return res[0]

