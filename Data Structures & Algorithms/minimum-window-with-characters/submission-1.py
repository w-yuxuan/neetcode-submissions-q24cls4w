#line by line fix 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""  # FIXED: added basic edge case check

        ss = {}
        tt = {} 

        # Setup target dictionary
        for lett in t:
            tt[lett] = tt.get(lett, 0) + 1
        
        have = 0 
        need = len(tt)
        res = [float('inf'),0,0] #(r-l-1,r,l)
            
        l = 0
        for r, lett in enumerate(s):

            ss[lett] = ss.get(lett, 0) + 1
            if lett in tt and ss[lett] == tt[lett]:
                have +=1 

            while have == need:
                # start moving l
                if r-l-1 < res[0]:
                    res = [r-l-1,l,r]

                ss[s[l]]-=1

                if s[l] in tt and ss[s[l]] < tt[s[l]]:
                    have -=1
                l+=1
        return "" if res[0]==float('inf') else s[res[1]:res[2]+1]
        
