class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #build the {}
        si={}
        ti={}

        if not s or not t:
            return False
                    
        if len(s)!=len(t):
            return False

        #for i in len(s): err
        for i in range(len(s)):

            if s[i] not in si:
            #if not si[s[i]]: don't work 
                #si.update({s[i]:0})
                si[s[i]]=0
            si[s[i]] +=1

            if t[i] not in ti:
                ti.update({t[i]:0})
            ti[t[i]] +=1

        #check if all in { } has 2 counts
        for ind in si:
            if ind not in ti:
                return False
            if si[ind] != ti[ind]: return False
             

        return True