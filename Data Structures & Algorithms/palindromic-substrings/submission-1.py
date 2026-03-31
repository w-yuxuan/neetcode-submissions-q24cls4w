class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) ==1:
            return 1
        res = 0
        for i in range(len(s)):
            #odd len
            l=r=i
            res1=0
            while s[l]==s[r]:
                l-=1
                r+=1
                res1+=1
                if l<0 or r>len(s)-1:
                    break

            #even len
            l=i
            r=l+1
            while r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                res1+=1
                if l<0 or r>len(s)-1:
                    break
            res += res1
        return res
            
            