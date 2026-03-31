class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ss = {}
        tt= {}
        for lett in t:
            tt[lett] = tt.get(lett,0)+1
        need = len(tt)   

        res = [float('inf'),0,0] #[r-l+1,l,r]
        have = 0  

        l=0
        for r,char in enumerate(s):
            ss[char] = ss.get(char,0)+1
            
            if char in tt and ss[char] == tt[char]: # not >= to avoid repeated adding
                have +=1

            while have == need: # try to pair down
                if r-l+1<res[0]:
                    res = [r-l+1,l,r]
                l+=1
                ss[s[l-1]] -= 1

                if s[l-1] in tt and ss[s[l-1]] < tt[s[l-1]]:
                    have -=1


        return "" if res[0]==float('inf') else s[res[1]:res[2]+1]
                



