class Solution:
    def numDecodings(self, s: str) -> int:
        # looks like a  palindrome partiion q
        # every time i hit the last one i add one 
        mem = [0]*(len(s)+1)
        mem[-1] = 1

        for i in range(len(s)-1,-1,-1):
            res = 0
            for j in range(i+1,min(i+3,len(s)+1)):
                cut = s[i:j]
                if cut[0]!='0' and int(cut)<=26:
                    res+=mem[j]
            mem[i]=res
        return mem[0]