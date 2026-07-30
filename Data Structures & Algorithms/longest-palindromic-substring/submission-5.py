class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd case:
        length = 0
        curlen=0
        res = []

        if len(s)==1:
            return s
        # if len(s)%2 != 0:
        for i in range(len(s)):
            l = r = i
            while 0<=l<=r<=len(s)-1 and s[l] == s[r]:
                curlen = r-l+1
                if curlen>length:                
                    length = max(curlen,length)
                    res = s[l:r+1]          

                l-=1
                r+=1


        #even case 
        # if len(s)%2 == 0:
            l=i
            r=1+i
            curlen = 0
            while 0<=l<=r<=len(s)-1 and s[l] == s[r]:
                curlen = r-l+1
                if curlen>length:                
                    length = max(curlen,length)
                    res = s[l:r+1]                    
                l-=1
                r+=1
        return res


